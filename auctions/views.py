from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, Listing, Bid, Comment

def index(request):
    activeListings = Listing.objects.filter(isActive=True)
    return render(request, "auctions/index.html",{
        "listings": activeListings
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def createListing(request):
    if request.method == "GET":
        listofCategories = Category.objects.all()
        return render(request, "auctions/create.html",{
            "categories": listofCategories
        })
    else:
        currentUser = request.user
        itemTitle = request.POST["title"]
        itemDescription = request.POST["description"]
        itemImageurl = request.POST["imageurl"]
        itemPrice = request.POST["price"]
        itemCategory = request.POST["category"]

        bid = Bid(bid=float(itemPrice), user=currentUser)
        bid.save()
        
        catergoryContent = Category.objects.get(categoryName=itemCategory)

        newListing = Listing(
            title=itemTitle,
            description=itemDescription,
            imageUrl=itemImageurl,
            price=bid,
            owner=currentUser,
            category=catergoryContent
        )
        newListing.save()
        return HttpResponseRedirect(reverse("index"))

def categories(request):
    listofCategories = Category.objects.all()
    return render(request, "auctions/categories.html",{
        "categories": listofCategories
    })

def filterbyCategories(request, selectedCategory):
    category = Category.objects.get(categoryName=selectedCategory)
    activeListings = Listing.objects.filter(isActive=True, category=category)
    listofCategories = Category.objects.all()
    return render(request, "auctions/index.html",{
        "listings": activeListings,
        "categories": listofCategories
    })

def listings(request, id):
    listData = Listing.objects.get(pk=id)
    currentUser = request.user
    isWatching = currentUser in listData.watchlist.all()
    comments = Comment.objects.filter(listing=listData)
    if not listData.isActive and currentUser.id == listData.price.user.id:
        message = "Congratulations, You Won the Auction!"
    else:
        message = False

    return render(request, "auctions/listings.html",{
        "listing": listData,
        "isWatching": isWatching,
        "message": message,
        "comments": comments
    })

def addWatchlist(request, id):
    listData = Listing.objects.get(pk=id)
    currentUser = request.user
    listData.watchlist.add(currentUser)
    return HttpResponseRedirect(reverse(listings, args=(id, )))
 
def removeWatchlist(request, id):
    listData = Listing.objects.get(pk=id)
    currentUser = request.user
    listData.watchlist.remove(currentUser)
    return HttpResponseRedirect(reverse(listings, args=(id, )))

def showWatchlist(request):
    currentUser = request.user
    userWatchlist = currentUser.watchlist.all()
    return render(request, "auctions/watchlist.html",{
        "userWatchlist": userWatchlist
    })

def addBid(request, id):
    newBid = float(request.POST['newBid'])
    listing = Listing.objects.get(pk=id)
    if newBid > listing.price.bid:
        updateBid = Bid(user=request.user, bid=newBid)
        updateBid.save()
        listing.price = updateBid
        listing.save()
        message = "Accepted Bid"    
    else:
        message = "Bid rejected"
    
    return render(request, "auctions/listings.html", {
        "listing": listing,
        "message": message
    })

def closeAuction(request, id):
    listData = Listing.objects.get(pk=id)
    listData.isActive = False
    listData.save()
    message = "Congratulations Your auction has ended."
    return render(request, "auctions/listings.html", {
        "listing": listData,
        "message": message
    })

def addComments(request, id):
    listData = Listing.objects.get(pk=id)
    currentUser = request.user
    commentText = request.POST['newComment']
    newComment = Comment(
        user = currentUser,
        listing = listData,
        comment = commentText
    )
    newComment.save()
    return HttpResponseRedirect(reverse(listings, args=(id, )))
# Project: Commerce

**Objective**
>_Design an eBay-like e-commerce auction site._   

<br>
  
**Specification**
>- _Models: Your application should have at least three models in addition to the User model: one for auction listings, one for bids, and one for comments made on auction listings. It’s up to you to decide what fields each model should have, and what the types of those fields should be. You may have additional models if you would like._
>- _Create Listing: Users should be able to visit a page to create a new listing. They should be able to specify a title for the listing, a text-based description, and what the starting bid should be. Users should also optionally be able to provide a URL for an image for the listing and/or a category (e.g. Fashion, Toys, Electronics, Home, etc.)._
>- _Active Listings Page: The default route of your web application should let users view all of the currently active auction listings. For each active listing, this page should display (at minimum) the title, description, current price, and photo (if one exists for the listing)._   
>- _Listing Page: Clicking on a listing should take users to a page specific to that listing. On that page, users should be able to view all details about the listing, including the current price for the listing._
>   - _If the user is signed in, the user should be able to add the item to their “Watchlist.” If the item is already on the watchlist, the user should be able to remove it_
>   - _If the user is signed in, the user should be able to bid on the item. The bid must be at least as large as the starting bid, and must be greater than any other bids that have been placed (if any). If the bid doesn’t meet those criteria, the user should be presented with an error._
>   -_If the user is signed in and is the one who created the listing, the user should have the ability to “close” the auction from this page, which makes the highest bidder the winner of the auction and makes the listing no longer active._
>   -_If a user is signed in on a closed listing page, and the user has won that auction, the page should say so._
>   -_Users who are signed in should be able to add comments to the listing page. The listing page should display all comments that have been made on the listing._
>- _Watchlist: Users who are signed in should be able to visit a Watchlist page, which should display all of the listings that a user has added to their watchlist. Clicking on any of those listings should take the user to that listing’s page._
>- _Categories: Users should be able to visit a page that displays a list of all listing categories. Clicking on the name of any category should take the user to a page that displays all of the active listings in that category._
>- _Django Admin Interface: Via the Django admin interface, a site administrator should be able to view, add, edit, and delete any listings, comments, and bids made on the site._

<br>
   
**Documentation**   
_[Model field reference](https://docs.djangoproject.com/en/4.0/ref/models/fields/)_   
_[Forms Bootstrap](https://getbootstrap.com/docs/4.0/components/forms/)_   
_[HTML option tag](https://www.w3schools.com/tags/tag_option.asp)_   
_[Cards Bootstrap](https://getbootstrap.com/docs/4.0/components/card/)_   
_[Django Built-in template tags and filters](https://docs.djangoproject.com/en/4.0/ref/templates/builtins)_   
_[List group Bootstrap](https://getbootstrap.com/docs/4.0/components/list-group/)_   

<br>

**Progress**   
![](https://geps.dev/progress/100)   
  
<br>
<br>

_According to HarvardX - Web Programming with Python and JavaScript Course_

<br>

![screenshot](img/preview.png?raw=true "screenshot")

<br>

<a href="https://youtu.be/i17qzrVg2Vc" target="_blank"><img border="0" width="3%" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/YouTube_full-color_icon_%282017%29.svg/2560px-YouTube_full-color_icon_%282017%29.svg.png" alt="Watch it on youtube"/> _Watch it on youtube_</a>
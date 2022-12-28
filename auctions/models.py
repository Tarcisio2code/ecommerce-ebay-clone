from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    categoryName = models.CharField(max_length=50)
    imageUrl = models.CharField(max_length=1000, default=None, blank=True, null=True)

    def __str__(self):
        return self.categoryName

class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    imageUrl = models.CharField(max_length=1000)
    price = models.FloatField(default=0)
    isActive = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name="watchlist")

    def __str__(self):
        return self.title

class Bid(models.Model):
    bid = models.FloatField(default=0)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="bidListing")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="userBid")

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="commentUser")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="commentListing")
    comment = models.CharField(max_length=300)
    postDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.user} comment on {self.listing}"

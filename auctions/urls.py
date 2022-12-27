from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/<int:id>", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.createListing, name="create"),
    path("categories", views.categories, name="categories"),
    path("filterbyCategories/<str:selectedCategory>", views.filterbyCategories, name="filterbyCategories"),
    path("listings/<int:id>", views.listings, name="listings"),
    path("addWatchlist/<int:id>", views.addWatchlist, name="addWatchlist"),
    path("removeWatchlist/<int:id>", views.removeWatchlist, name="removeWatchlist"),
    path("showWatchlist", views.showWatchlist, name="showWatchlist"),
    path("addBid/<int:id>", views.addBid, name="addBid"),
    path("closeAuction/<int:id>", views.closeAuction, name="closeAuction"),
    path("addComments/<int:id>", views.addComments, name="addComments")
]

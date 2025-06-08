from django.urls import path, include


urlpatterns = [
    path("account/", include("api.account.urls")),
    path("book/", include("api.book.urls")),

]

from django.urls import path, include

urlpatterns = [
    # ... admin, etc.
    path("api/", include("listings.urls")),
]

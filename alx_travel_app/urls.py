from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_schema_view(
    openapi.Info(
        title="Travel App API",
        default_version='v1',
        description="API for Listings and Bookings",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    # ... admin, etc.
    path("api/", include("listings.urls")),
    path('admin/', admin.site.urls),
    path('', include('listings.urls')),  # inclure nos endpoints
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('api-auth/', include('rest_framework.urls')),  # Auth DRF pour la Browsable API

]

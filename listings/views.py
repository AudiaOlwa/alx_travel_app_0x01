#!/usr/bin/env python3
"""Views (ViewSets) for the listings app."""

from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ListingViewSet(viewsets.ModelViewSet):
    """CRUD for listings."""
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class BookingViewSet(viewsets.ModelViewSet):
    """CRUD for bookings."""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

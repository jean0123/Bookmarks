from rest_framework.routers import DefaultRouter
from .views import *

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'bookmarks', BookmarkViewset, '')
router.register(r'bookmarks_public', BookmarkPublicViewset)

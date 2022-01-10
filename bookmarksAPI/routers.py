from django.urls import path, include
from bookmark.urls import router as bookmark

# The API URLs are now determined automatically by the router.
drf_urls = [
    path('usr/', include(bookmark.urls)),
]

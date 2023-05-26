from django.urls import path, include
from .views import UserProfileView

app_name = 'accounts'
urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('signup/', include('dj_rest_auth.registration.urls')),
    path('profile/', UserProfileView.as_view(), name='profile'),
]

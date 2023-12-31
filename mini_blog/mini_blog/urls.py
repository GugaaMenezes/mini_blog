from django.contrib import admin
from django.urls import path, include

from miniblog.views import generate_token


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('miniblog.urls')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),    
    path('', generate_token, name='generate_token'),
]

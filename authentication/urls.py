from django.urls import path
from rest_framework_simplejwt import views


urlpatterns = [
    path('authentication/token/', views.TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('authentication/token/refresh/', views.TokenRefreshView.as_view(), name='token-refresh'),
    path('authentication/token/verify/', views.TokenVerifyView.as_view(), name='token-verify'),

]

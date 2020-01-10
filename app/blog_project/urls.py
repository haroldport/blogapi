from django.contrib import admin
from django.urls import include, path

from rest_auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/password/reset/confirm/<uidb64>/<token>/',
         views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
]

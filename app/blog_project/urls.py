from django.contrib import admin
from django.urls import include, path

from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_auth import views

API_TITLE = 'Blog API'
API_DESCRIPTION = 'A Web API for creating and editing blog posts.'
schema_view = get_schema_view(
    openapi.Info(
        title=API_TITLE,
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/password/reset/confirm/<uidb64>/<token>/',
         views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title=API_TITLE,
                                    description=API_DESCRIPTION)),
    path('swagger-docs/', schema_view.with_ui('swagger', cache_timeout=0)),
]

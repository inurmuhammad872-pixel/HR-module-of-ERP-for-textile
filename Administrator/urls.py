from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# 🔹 Swagger schema
schema_view = get_schema_view(
    openapi.Info(
        title="HR API",
        default_version='v1',
        description="Adminapp uchun API hujjatlari",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # 🔹 Django admin
    path('admin/', admin.site.urls),

    # 🔹 Adminapp API (router)
    path('api/', include('Adminapp.urls')),

    # 🔹 dj-rest-auth
    path('dj-rest-auth/', include('dj_rest_auth.urls')),

    # 🔹 JWT
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # 🔹 Swagger
    re_path(
        r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    re_path(
        r'^redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]

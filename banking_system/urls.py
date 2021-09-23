from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

API_TITLE = 'Currency API'
API_DESCRIPTION = 'A web API for creating and editing blog posts.'
schema_view = get_schema_view(title="Blog API")

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # Apps
    path('auth/', include('auth_app.urls')),
    path('transaction/', include('transaction_app.urls')),
    path('account/', include('accounts_app_account.urls')),
    path('employee/', include('employee_app.urls')),
    # path('auth/', include('django.contrib.auth.urls')),
    path('chat/', include('chat.urls')),
    # API
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # Task queues
    path('celery-progress/', include('celery_progress.urls')),
    #MFA
    path('settings/', include('django_mfa.urls')),
    # Documentation
    path('documentation/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
]

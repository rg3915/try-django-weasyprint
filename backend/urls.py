from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('backend.core.urls', namespace='core')),
    path('accounts/', include('backend.accounts.urls')),  # without namespace
    path('crm/', include('backend.crm.urls', namespace='crm')),
    path('expense/', include('backend.expense.urls', namespace='expense')),
    path('admin/', admin.site.urls),
]

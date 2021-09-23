from django.contrib import admin

# Register your models here.

from api.models import Currency
from api.models import Rate

admin.site.register(Currency)
admin.site.register(Rate)
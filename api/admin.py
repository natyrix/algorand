from django.contrib import admin
from api.models import Account, Assets

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    pass

class AssetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Account)
admin.site.register(Assets)
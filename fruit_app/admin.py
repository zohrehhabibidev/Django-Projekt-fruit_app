from django.contrib import admin

from fruit_app.models import Fruit, Customer, OrderItem, Order
# Register your models here.


class FruitAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_available']
    search_fields = ['name', 'color']
    list_filter = ['price']
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = [
        (
            None,
            {
                "fields": ["name", "weight", "price", "is_available"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["color", "description", "origin_country", "slug"],
            },
        ),
    ]


class customerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name', 'email']
    list_filter = ['created_at']
    readonly_fields = ['created_at']


admin.site.register(Fruit, FruitAdmin)
admin.site.register(Customer, customerAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)

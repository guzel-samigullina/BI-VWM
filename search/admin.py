from django.contrib import admin
from .models import Item
from .models import Word
from .models import Dictionary


admin.site.register(Item)
admin.site.register(Word)
admin.site.register(Dictionary)



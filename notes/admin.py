from django.contrib import admin
from .models import StickyNote, Author

# Register your models here.
admin.site.register(StickyNote)
admin.site.register(Author)
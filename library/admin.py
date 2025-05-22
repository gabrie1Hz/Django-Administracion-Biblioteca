from django.contrib import admin
from .models import author, category, books, issuedbooks, reservedbooks, issuebookhistory, searchedcontent

# Register your models here.

admin.site.register(author)
admin.site.register(category)
admin.site.register(books)
admin.site.register(issuedbooks)
admin.site.register(reservedbooks)
admin.site.register(issuebookhistory)
admin.site.register(searchedcontent)

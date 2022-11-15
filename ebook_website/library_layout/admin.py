from django.contrib import admin
from library_layout.models import UserProfileInfo, author, ebook, loan, review

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(author)
admin.site.register(ebook)
admin.site.register(loan)
admin.site.register(review)
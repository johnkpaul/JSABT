from photocopy.models import Photocopy
from django.contrib import admin

class PhotocopyAdmin(admin.ModelAdmin):
    # We exclude these fields because they are populated
    # automatically on save()
    exclude = ('article_content','fetch_date',)

admin.site.register(Photocopy, PhotocopyAdmin)


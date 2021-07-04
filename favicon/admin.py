from django.contrib import admin
from favicon.models import Favicon, FaviconImg


class FaviconAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_favicon')


class FaviconImgAdmin(admin.ModelAdmin):
    list_display = ('faviconFK', 'rel', 'size', 'faviconImage')

    def queryset(self, request):
        qs = super(FaviconImgAdmin, self).queryset(request)
        is_favicon = Favicon.objects.filter(is_favicon=True)
        if not len(is_favicon) == 1:
            for n in Favicon.objects.all():
                n.is_favicon = False
            return qs
        is_favicon = is_favicon[0]
        return qs.filter(faviconFK=is_favicon)


admin.site.register(Favicon, FaviconAdmin)
admin.site.register(FaviconImg, FaviconImgAdmin)

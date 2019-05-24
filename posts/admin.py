from django.contrib import admin
from django.utils.safestring import mark_safe

from posts.models import Post

#admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_select_related = ['owner']
    list_per_page = 5
    list_display = ['get_img', 'title', 'get_owner_name', 'modification_date']
    list_filter = ['categories']
    search_fields = ['owner__first_name', 'short_description', 'owner__last_name', 'title', 'publish_Date']
    readonly_fields = ['get_img', 'get_owner_name', 'creation_date', 'modification_date']

    fieldsets = [
        [None, {
            'fields': ['title', 'short_description', 'content', 'categories']
        }],
        ['Multimedia', {
            'fields': ['get_img', 'image', 'video'],
            'classes': ['collapse']
        }],
        ['Metadata', {
            'fields': ['publish_Date', 'creation_date', 'modification_date', 'owner'],
            'classes': ['collapse']
        }]
    ]

    def get_owner_name(self, obj):
        return '{0} {1}'.format(obj.owner.first_name, obj.owner.last_name)

    def get_img(self, obj):
        return mark_safe('<img src="{0}" height="50">'.format(obj.image))

    get_owner_name.short_description = 'Owner'
    get_img.short_description = 'Image'
    get_owner_name.admin_order_field = 'owner__first_name'
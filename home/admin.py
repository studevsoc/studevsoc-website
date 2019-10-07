from django.contrib import admin

from .models import Jumbotron, Project, ProjectCategory
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'

class JumbotronAdmin(admin.ModelAdmin):
    list_display = ('introtitle', 'status', 'updated_on')
    list_filter = ('status',)
    search_fields = ['introtitle', 'introcontent']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'progress', 'updated_on','category')
    list_filter = ('progress','category')
    search_fields = ['name', 'description']

class ProjectCategoryAdmin(admin.ModelAdmin):
    fields = ['name']

admin.site.register(Jumbotron, JumbotronAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(Contact, ContactAdmin)

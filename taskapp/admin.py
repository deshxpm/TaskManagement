from django.contrib import admin
from .models import UserProfile, Task, Expert, Allocation

class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('email', 'is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    readonly_fields = ('created_at', 'updated_at')

class ExpertAdmin(admin.ModelAdmin):
    list_display = ('name', 'expertise', 'user')
    search_fields = ('name', 'expertise', 'user__email')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'user')
    search_fields = ('title', 'description', 'user__email')

class AllocationAdmin(admin.ModelAdmin):
    list_display = ('task', 'expert', 'allocated_at')
    list_filter = ('task', 'expert')
    search_fields = ('task__title', 'expert__name')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Expert, ExpertAdmin)
admin.site.register(Allocation, AllocationAdmin)

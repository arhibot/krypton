from django.contrib import admin
from .models import (SSHKey,
                     UserProfile,
                     Project,
                     Team,
                     ToolType,
                     Tool,)

admin.site.register(SSHKey)
admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Team)
admin.site.register(ToolType)
admin.site.register(Tool)

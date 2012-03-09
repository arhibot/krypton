from django.contrib.auth.models import User
from django.db.models.signals import post_save

from orgprj.models import Project, UserProfile, Team, TeamMember


def create_user_env(sender, instance, created, **kwargs):
    if not created:
        return
    user = instance
    profile, _new = UserProfile.objects.get_or_create(user=user)
    project, _new = Project.objects.get_or_create(parent=None,
                                                  descr=user.username,
                                                  name=user.username)
    team, _new = Team.objects.get_or_create(name="",
                                            project=project,
                                            perm='owner')
    tm, _new = TeamMember.objects.get_or_create(member=user,
                                                team=team)
    print profile
    print project
    print team.members.all()

post_save.connect(create_user_env, sender=User)

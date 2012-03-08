import os

from django.db import models
from django.conf import settings
from django.utils.functional import SimpleLazyObject
from django.contrib.auth.models import User


PERMS_CHOICES = dict(
    ro='read-only',
    rw='read-write',
    owner='owner',
)


class SSHKey(models.Model):
    title = models.CharField(max_length=255)
    ssh_key = models.TextField(max_length=4048)

    owner = models.ForeignKey(User)


    def __unicode__(self):
        return u'%s:%s' % (self.owner,
                           self.title,)


class UserProfile(models.Model):
    user = models.OneToOneField(User)


class Project(models.Model):
    class Meta:
        unique_together = (('name', 'parent',),)

    name = models.CharField('Project name', max_length=255)
    descr = models.CharField('Description', max_length=255, blank=True)
    parent = models.ForeignKey('self', null=True)

    path = models.CharField('URL path',
                            max_length=1024,
                            blank=True)

    def save(self, *args, **kwargs):
        parent_path = self.parent.path if self.parent else ''
        self.path = '%s%s/' % (parent_path, self.name)
        return super(Project, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Team(models.Model):
    '''
    project team
    '''
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project)
    members = models.ManyToManyField(User, through='TeamMember')
    perm = models.CharField(max_length=255, choices=PERMS_CHOICES.items())

    def __unicode__(self):
        return u'%s(%s):%s' % (self.name,
                               ','.join(map(unicode,self.members.all())),
                               self.perm)


class TeamMember(models.Model):
    '''
    Team member
    '''

    class Meta:
        unique_together = ('member', 'team',)

    member = models.ForeignKey(User)
    team = models.ForeignKey(Team)

    def __unicode__(self):
        return u':'.join(map(unicode,
                             (self.team, self.member,)))


class ToolType(models.Model):
    tool_type = models.CharField(max_length=255,
                                 choices=settings.ORGPRJ_TOOLS_TYPES.items(),
                                 unique=True)

    def __unicode__(self):
        return self.tool_type


class Tool(models.Model):
    class Meta:
        unique_together = (('project', 'tool_type',))

    project = models.ForeignKey(Project)
    tool_type = models.ForeignKey(ToolType)

    def __unicode__(self):
        return u'%s:%s' % (self.project,
                           self.tool_type)


from . import handlers

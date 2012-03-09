import os

from django.db.models.signals import post_save
from django.conf import settings

from dulwich import repo

from gittool.models import GitTool


def create_gittool_env(sender, instance, created, **kwargs):
    if not created:
        return
    t = instance
    try:
        repo_path = os.path.join(settings.GITTOOL_REPOS_PATH,
                                 os.path.normpath(t.project.path) + '.git')
        os.makedirs(repo_path)
        repo.Repo.init_bare(repo_path)
    except OSError:
        pass
    try:
        _r = repo.Repo(repo_path)
    except repo.NotGitRepository:
        print "OOPS"

post_save.connect(create_gittool_env, sender=GitTool)


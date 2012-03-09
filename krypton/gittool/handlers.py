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
        repo_path = t.path_to_repo()
        repo.Repo.init_bare(repo_path)
    except OSError:
        pass
    try:
        _r = repo.Repo(repo_path)
    except repo.NotGitRepository:
        print "OOPS"

post_save.connect(create_gittool_env, sender=GitTool)


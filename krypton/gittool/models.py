import os
from django.conf import settings
from django.utils.functional import SimpleLazyObject

from orgprj.models import Tool

from .vcs import GitVCS


class GitTool(Tool):
    def __init__(self, *args, **kwargs):
        super(GitTool, self).__init__(*args, **kwargs)
        self.vcs = SimpleLazyObject(lambda: GitVCS(self.path_to_repo()))

    def path_to_repo(self):
        return os.path.join(settings.GITTOOL_REPOS_PATH,
                            os.path.normpath(self.project.path) + '.git')

    def branches(self):
        return self.vcs.branches()

    def get_object(self, sha1):
        return self.vcs.get_object(sha1)

    def get_object_by_path(self, ref, path):
        return self.vcs.get_object_by_path(ref, path)


from . import handlers

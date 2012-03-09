import os

from dulwich.repo import Repo
from dulwich.objects import Tree


class GitVCS(object):
    def __init__(self, path):
        self.repo = Repo(path)

    def branches(self):
        return dict(((k.replace('refs/heads/', ''), v) for k, v in self.repo.get_refs().items()
                     if k.startswith('refs/heads/')))

    def get_branch_ref(self, branch):
        branches = self.branches()
        if not branch in branches:
            return None
        return branches[branch]

    def get_object(self, sha1):
        try:
            return self.repo.get_object(sha1)
        except AssertionError:
            return None

    def get_object_by_path(self, ref, path):
        c = self.get_object(self.get_branch_ref(ref) or ref)
        if not c:
            return None
        paths = path.split(os.sep)
        count = len(paths)
        obj = self.get_object(c.tree)
        for i, x in enumerate(paths):
            if not x:
                return obj
            try:
                _mode, sha1 = obj[x]
            except KeyError:
                obj = None
                break
            obj = self.get_object(sha1)
            if i < count - 1 and not isinstance(obj, Tree):
                obj = None
                break

        if not obj:
            raise ValueError("Bad path")

        print "Result: ", type(obj), obj
        return obj

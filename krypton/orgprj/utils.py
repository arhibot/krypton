import os

from orgprj.models import Project, Tool

def endslash(path):
    return os.path.normpath(path) + '/'


def fix_prj_path(fn):
    def wrapper(request, prj_path, *args, **kwargs):
        return fn(request, endslash(prj_path), *args, **kwargs)
    return wrapper


def project_exists(fn):
    def wrapper(request, prj_path, *args, **kwargs):
        Project.objects.get(path=prj_path)
        return fn(request, prj_path, *args, **kwargs)
    return wrapper


def tool_exists(toolname):
    def deco(fn):
        def wrapper(request, prj_path, *args, **kwargs):
            Tool.objects.get(project__path=prj_path,
                             tool_type__tool_type=toolname)
            return fn(request, prj_path, *args, **kwargs)
        return wrapper
    return deco

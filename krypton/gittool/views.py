import os

from orgprj.models import Tool
from orgprj.utils import fix_prj_path, project_exists, tool_exists

import settings

@fix_prj_path
@project_exists
@tool_exists(settings.GITTOOL_NAME)
def show_obj(request, prj_path, otype, ref, fpath):
    tool = Tool.objects.get(project__path=prj_path,
                            tool_type__tool_type=settings.GITTOOL_NAME).gittool
    if not ref:
        ref = tool.get_default_ref()
    print tool.get_object_by_path(ref, os.path.normpath(fpath) if fpath else '')
    print 'Project: ', prj_path
    print "Object type: ", otype
    print "Ref: ", ref
    print "File path: '%s'" % fpath
    1/0

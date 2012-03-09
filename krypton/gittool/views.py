from orgprj.models import Tool
from orgprj.utils import fix_prj_path, project_exists, tool_exists

import settings

@fix_prj_path
@project_exists
@tool_exists(settings.GITTOOL_NAME)
def show_obj(request, prj_path, otype, ref, fpath):
    tool = Tool.objects.get(project__path=prj_path,
                            tool_type__tool_type=settings.GITTOOL_NAME).gittool
    print 'Project: ', prj_path
    print "Object type: ", otype
    print "Ref: ", ref
    print "File path: ", fpath
    1/0

from orgprj.utils import fix_prj_path, project_exists


@fix_prj_path
@project_exists
def project_page(request, prj_path):
    print 1/0

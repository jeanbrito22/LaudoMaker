#Just for win executable
from cx_Freeze import setup, Executable
import os, sys
include_files = [ './templates',
                  './static',
                  os.path.join(sys.base_prefix, 'DLLs', 'sqlite3.dll'),
                  'models.py']

include = ['jinja2', 'jinja2.ext',]
flaskapp = (Executable('main.py',
                       targetName = 'lmk.exe',
                       ))
setup(
    name='lmk',
    version='1.2',
    author='Jean',
    description="Sistema para criacao de laudos entomologicos",
    options={
        'build_exe': {
            'include_files': include_files,
            'includes': include,
            'build_exe': "build"
            }
        },
    executables=[flaskapp]
)

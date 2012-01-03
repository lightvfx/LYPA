from distutils.core import setup
import sys
sys.path.append('C:/Program Files (x86)/Microsoft Visual Studio 9.0/VC/redist/amd64/Microsoft.VC90.CRT')
from sqlalchemy.dialects.postgresql.base import dialect
import py2exe
setup(console=['LYPA_001_beta.py'],options={"py2exe" : {"includes": ["sip", "PyQt4.QtSql","psycopg2","ctypes", "logging"],"excludes": ["OpenGL"],"packages": ["sqlalchemy.dialects.postgres"]}})

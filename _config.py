import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = '\x83\x00r\xbc\x1a\xd6\xf6\xcd>S\xa9\x80\xc5\xf0\xbdt4\xf7\xd9\xfak}\xb6E'
WTF_CSRF_ENABLED = True
DATABASE_PATH = os.path.join(basedir,DATABASE)



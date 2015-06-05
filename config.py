import os
basedir = os.path.abspath(os.path.dirname(__file__))
 
SQLALCHEMY_DATABASE_URI = 'mysql://yaas:naima88712@192.168.1.160:3306/yaas'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
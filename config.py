__author__ = 'maddalena'

import os

basedir = os.path.abspath(os.path.dirname(__file__))

# -----------------------------------------------------------------------
# SQLALCHEMY paths (dialect+driver://username:password@host:port/database)
# -----------------------------------------------------------------------
#SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")    # SQLite
SQLALCHEMY_DATABASE_URI = "mysql://testuser:test@localhost/alchemytest"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, "db_repository")            # migrate data file

# ---------------------
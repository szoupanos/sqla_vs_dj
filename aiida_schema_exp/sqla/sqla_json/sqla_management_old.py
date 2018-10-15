import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


# def recreate_after_fork(engine):
#     """
#     :param engine: the engine that will be used by the sessionmaker
#
#     Callback called after a fork. Not only disposes the engine, but also recreates a new scoped session
#     to use independent sessions in the forked process.
#     """
#     sqlalchemy.engine.dispose()
#     sqlalchemy.scopedsessionclass = scoped_session(sessionmaker(bind=sqlalchemy.engine, expire_on_commit=True))


# def reset_session(config):
#     """
#     :param config: the configuration of the profile from the
#        configuration file
#
#     Resets (global) engine and sessionmaker classes, to create a new one
#     (or creates a new one from scratch if not already available)
#     """
#     from multiprocessing.util import register_after_fork
#
#     engine_url = (
#         "postgresql://{AIIDADB_USER}:{AIIDADB_PASS}@"
#         "{AIIDADB_HOST}:{AIIDADB_PORT}/{AIIDADB_NAME}"
#     ).format(**config)
#
#     sqlalchemy.engine = create_engine(engine_url, json_serializer=dumps_json,
#                               json_deserializer=loads_json)
#     sqlalchemy.scopedsessionclass = scoped_session(sessionmaker(bind=sqlalchemy.engine,
#                                                         expire_on_commit=True))
#     register_after_fork(sqlalchemy.engine, recreate_after_fork)


print sqlalchemy.__version__

# engine = create_engine('sqlite:///:memory:', echo=True)
from sqlalchemy import create_engine
engine = create_engine('postgresql://aiida:qaq4Sz6B4Q7BjdLDZUji@localhost:5432/aiidadb_sqla_jsonb', echo=True)

from models.authinfo import DbAuthInfo
from models.comment import DbComment
from models.computer import DbComputer
from models.group import DbGroup
from models.lock import DbLock
from models.log import DbLog
from models.node import DbNode
from models.node import DbCalcState
from models.node import DbLink
from models.settings import DbSetting
from models.user import DbUser
from models.workflow import DbWorkflow
from models.workflow import DbWorkflowData
from models.workflow import DbWorkflowStep

from models.base import Base
Base.metadata.create_all(engine)

print "=====>", Base.metadata.tables.keys()

import sys
sys.exit(0)
########## UNTIL HERE

print "User created"


print "Creating user ed"
ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')

print "Ed username ", ed_user.name
print "ED user id", str(ed_user.id)

Session = sessionmaker(bind=engine)
session = Session()

session.add(ed_user)

our_user = session.query(User).filter_by(name='ed').first()
print "Query result ", our_user

print ed_user.id
print our_user.id


session.commit()

print "Session commited"

print ed_user.id
print our_user.id
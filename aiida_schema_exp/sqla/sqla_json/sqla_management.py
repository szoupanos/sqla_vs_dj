import sqlalchemy
from sqlalchemy import create_engine
import logging

# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)

print sqlalchemy.__version__
# engine = create_engine('postgresql://aiida:qaq4Sz6B4Q7BjdLDZUji'
#                        '@localhost:5432/aiidadb_sqla_jsonb', echo=True)
engine = create_engine('postgresql://aiida:qaq4Sz6B4Q7BjdLDZUji'
                       '@localhost:5432/aiidadb_sqla_jsonb', echo=False)

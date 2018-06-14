from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.schema import Column, Table, UniqueConstraint
from sqlalchemy.types import Integer, String, Boolean, DateTime, Text
from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://aiida:qaq4Sz6B4Q7BjdLDZUji@localhost:5432/aiidadb_sqla_flask_test"
db = SQLAlchemy(app)

table_groups_nodes = Table(
    'dbgroup_dbnodes',
    db.Model.metadata,
    Column('id', Integer, primary_key=True),
    Column('dbnode_id', Integer, ForeignKey('dbnode.id', deferrable=True, initially="DEFERRED")),
    Column('dbgroup_id', Integer, ForeignKey('dbgroup.id', deferrable=True, initially="DEFERRED"))
)

class DbNode(db.Model):
    __tablename__ = "dbnode"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    def __repr__(self):
        return '<Post %r>' % self.title


class DbGroup(db.Model):
    __tablename__ = "dbgroup"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    dbnodes = relationship('DbNode', secondary=table_groups_nodes,
                           backref="dbgroups", lazy='dynamic')


    def __repr__(self):
        return '<Category %r>' % self.name



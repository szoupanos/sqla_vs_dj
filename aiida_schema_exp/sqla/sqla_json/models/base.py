# -*- coding: utf-8 -*-
###########################################################################
# Copyright (c), The AiiDA team. All rights reserved.                     #
# This file is part of the AiiDA code.                                    #
#                                                                         #
# The code is hosted on GitHub at https://github.com/aiidateam/aiida_core #
# For further information on the license, see the LICENSE.txt file        #
# For further information please visit http://www.aiida.net               #
###########################################################################
from __future__ import absolute_import

from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import UnmappedClassError
from sqla_json.aiida_exceptions import InvalidOperation

scopedsessionclass = None


class _QueryProperty(object):

    def __init__(self, query_class=orm.Query):
        self.query_class = query_class

    def __get__(self, obj, _type):
        try:
            mapper = orm.class_mapper(_type)
            if mapper:
                return self.query_class(
                    mapper, session=get_scoped_session())
        except UnmappedClassError:
            return None


class _SessionProperty(object):
    def __get__(self, obj, _type):
        if not get_scoped_session():
            raise InvalidOperation("You need to call load_dbenv before "
                                   "accessing the session of SQLALchemy.")
        return get_scoped_session()


class _AiidaQuery(orm.Query):

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super(_AiidaQuery, self).__init__(*args, **kwargs)

    def __iter__(self):
        iterator = super(_AiidaQuery, self).__iter__()
        for r in iterator:
            # Allow the use of with_entities
            if issubclass(type(r), Model):
                yield r.get_aiida_class()
            else:
                yield r


# from aiida.backends.sqlalchemy import get_scoped_session

def get_scoped_session():
    """
    Return a scoped session (according to SQLAlchemy docs,
    this returns always the same object within a thread, and
    a different object in a different thread.
    Moreover, since we update the scopedsessionclass upon
    forking, also forks have different session objects.
    """
    if scopedsessionclass is None:
        s = None
    else:
        s = scopedsessionclass()

    return s


class Model(object):
    query = _QueryProperty()

    session = _SessionProperty()

    def save(self, commit=True):
        sess = get_scoped_session()
        sess.add(self)
        if commit:
            sess.commit()
        return self

    def delete(self, commit=True):
        sess = get_scoped_session()
        sess.delete(self)
        if commit:
            sess.commit()


Base = declarative_base(cls=Model, name='Model')

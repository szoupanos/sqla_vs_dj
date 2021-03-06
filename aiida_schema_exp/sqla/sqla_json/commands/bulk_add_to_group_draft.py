import click


@click.command()
def cmd():
    """
    Group addition with manual SQL statement that has a template. To see
    why this is much slower than v4.
    """
    # Importing the engine
    from sqla_json.sqla_management import engine
    from sqlalchemy.orm import sessionmaker
    from sqla_json.models.node import DbNode
    from sqla_json.models.group import DbGroup
    from sqlalchemy.sql.expression import bindparam

    from sqla_json.commands import DEFAULT_GROUP_NAME

    import time
    import sys

    # Creating the needed session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Getting the one and only group with that name
    dbgroup = session.query(DbGroup).filter_by(name=DEFAULT_GROUP_NAME).first()

    if dbgroup is None:
        print "No group is found, exiting"
        sys.exit()

    # Find all nodes
    print "Getting all the nodes"
    start_time = time.time()

    ins_dict = list()
    list_node = list()
    for (dbn, ) in session.query(DbNode.id).all():
        list_node.append(dbn)
        ins_dict.append({'dbnode_id': dbn, 'dbgroup_id': dbgroup.id})

    print "Found #{} nodes".format(len(list_node))

    # Add the nodes to the group
    print "Adding the nodes to the group"
    from sqla_json.models.group import table_groups_nodes
    # from sqla_json.models.base import Base
    # my_table = Base.metadata.tables['db_dbgroup_dbnodes']
    # ins = my_table.insert()
    # ins = my_table.insert().postfix_with('ON CONFLICT DO NOTHING')
    # ins = my_table.update()
    # session.expunge_all()
    # session.execute(ins, ins_dict)
    # print ins.compile(compile_kwargs=ins_dict)

    # print "PPPPPPP =>", str(ins)
    # print "PPPPPPP =>", str(ins.compile().params)

    # from sqlalchemy.dialects import postgresql
    # print str(q.statement.compile(dialect=postgresql.dialect()))

    # for x in list_node:
    #     ins = ins.values(dbnode_id=x, dbgroup_id=dbgroup.id)
    #     session.execute(ins)

    # print "+++++++ ", str(ins)
    # print "+++++++ ", str(ins.compile().params)
    # session.execute(ins)

    insert_txt = ""
    for (nid,) in session.query(DbNode.id).all():
        insert_txt += "({}, {}), ".format(nid, dbgroup.id)
    insert_txt = insert_txt[:-2]

    statement = """INSERT INTO db_dbgroup_dbnodes(dbnode_id, dbgroup_id) values {}""".format(
        insert_txt)
    session.execute(statement)
    session.commit()

    # print "+++++", ins
    # # my_table = DbGroup.__table__
    # print "===>", my_table
    #
    # update_statement = my_table.update().where(my_table.c.id == bindparam('key')).values(dbnodes=bindparam('value'))
    # session.execute(update_statement, [
    #     {'key': dbgroup.id, 'value': list_node[0]}
    # ])


    # print "Adding the nodes to the group"
    # session.bulk_update_mappings(update_statement, {'id': dbgroup.id,
    #                                        'dbnodes': list_node})

    # session.add(dbgroup)
    # session.commit()
    end_time = time.time()

    print "Added to group"
    print "Elapsed time --- {} seconds --- ".format(end_time - start_time)


if __name__ == '__main__':
    import sys
    import os

    dir_of_curr_file = os.path.dirname(os.path.realpath(__file__))
    # project folder
    par_dir = os.path.dirname(dir_of_curr_file)
    proect_dir = os.path.dirname(par_dir)
    # adding the project folder to the path
    sys.path.append(proect_dir)

    # calling the command
    cmd()

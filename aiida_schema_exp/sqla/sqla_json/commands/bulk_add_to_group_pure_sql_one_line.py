import click


@click.command()
def cmd():
    """
    Group addition with manual SQL statement.
    One line statement with all the value pairs.
    """
    # Importing the engine
    from sqla_json.sqla_management import engine
    from sqlalchemy.orm import sessionmaker
    from sqla_json.models.node import DbNode
    from sqla_json.models.group import DbGroup

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

    # Add the nodes to the group
    print "Adding the nodes to the group"

    insert_txt = ""
    for (nid,) in session.query(DbNode.id).all():
        insert_txt += "({}, {}), ".format(nid, dbgroup.id)
    insert_txt = insert_txt[:-2]

    statement = """INSERT INTO db_dbgroup_dbnodes(dbnode_id, dbgroup_id) values {}""".format(
        insert_txt)
    session.execute(statement)
    session.commit()

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

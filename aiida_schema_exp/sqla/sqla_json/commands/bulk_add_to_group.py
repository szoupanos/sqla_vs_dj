import click


@click.command()
def cmd():
    """Creating a user"""
    # Importing the engine
    from sqla_json.sqla_management import engine
    from sqlalchemy.orm import sessionmaker
    from sqla_json.commands import NUMBER_OF_NODES_TO_CREATE, DEFAULT_USER_EMAIL
    from sqla_json.models.user import DbUser
    from sqla_json.models.node import DbNode
    from sqla_json.models.group import DbGroup

    from sqla_json.commands import DEFAULT_GROUP_NAME

    import json

    # Creating the needed session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Getting the one and only group with that name
    dbgroup = session.query(DbGroup).filter_by(name=DEFAULT_GROUP_NAME).first()

    # Find all nodes and get the pks
    print "Getting all the nodes"
    print "UUUU",  session.query(DbNode).all()
    list_node = list()
    for dbn in session.query(DbNode).all():
        list_node.append(dbn)

    print "Found #{} pks".format(len(list_node))

    # Add the nodes to the group
    print "Adding the nodes to the group"
    dbgroup.dbnodes.extend(list_node)

    # It could be added directly with a query
    # To see the performance
    # dbgroup.dbnodes.extend(session.query(DbNode))

    session.add(dbgroup)
    session.commit()

    print "Created"


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

import click


@click.command()
def cmd():
    """Creating a user"""
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

    list_node = list()
    for dbn in session.query(DbNode).all():
        list_node.append(dbn)

    print "Found #{} nodes".format(len(list_node))

    # Add the nodes to the group - Normal addition
    print "Adding the nodes to the group"
    dbgroup.dbnodes.extend(list_node)

    session.add(dbgroup)
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

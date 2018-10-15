import click


@click.command()
def cmd():
    """Creating a user"""
    # Importing the engine
    from sqla_json.sqla_management import engine
    from sqlalchemy.orm import sessionmaker
    from sqla_json.models.user import DbUser
    from sqla_json.models.node import DbNode
    from sqla_json.models.group import DbGroup

    # Creating the needed session
    Session = sessionmaker(bind=engine)
    session = Session()

    print "Deleting all nodes"
    session.query(DbNode).delete()

    print "Deleting all users"
    session.query(DbUser).delete()

    print "Deleting all groups"
    session.query(DbGroup).delete()

    session.commit()
    print "Deleted"


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

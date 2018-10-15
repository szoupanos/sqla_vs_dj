import click

@click.command()
def cmd():
    """Creating a user"""
    # Importing the engine
    from sqla_json.sqla_management import engine
    from sqla_json.sqlalchemy.orm import sessionmaker
    from sqla_json.models.user import DbUser

    print "Creating user ed"
    ed_user = DbUser('a@b.c', first_name='Ed', last_name='Jones', password='edspassword')

    print "Ed first name ", ed_user.first_name
    print "ED user id", str(ed_user.id)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(ed_user)

    our_user = session.query(DbUser).filter_by(first_name='Ed').first()
    print "Query result ", our_user

    print ed_user.id
    print our_user.id

    session.commit()

    print "Session commited"


if __name__ == '__main__':
    import sys
    import os

    dir_of_curr_file = os.path.dirname(os.path.realpath(__file__))
    # project folder
    par_dir = os.path.dirname(dir_of_curr_file)
    # adding the project folder to the path
    sys.path.append(par_dir)
    # calling the command
    cmd()

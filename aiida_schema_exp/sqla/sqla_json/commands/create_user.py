import click

@click.command()
def cmd():
    """Creating a user"""
    # Importing the engine
    from sqla_json.sqla_management import engine
    from sqlalchemy.orm import sessionmaker
    from sqla_json.models.user import DbUser

    from sqla_json.commands import DEFAULT_USER_EMAIL

    print "Creating user"

    # Creating the needed session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Checking if user exists
    usr_exists = session.query(
        session.query(DbUser).filter_by(email=DEFAULT_USER_EMAIL).exists()
    ).scalar()

    if not usr_exists:
        # Creating the user that doesn't exist
        curr_user = DbUser(DEFAULT_USER_EMAIL)
        session.add(curr_user)
        session.commit()
        print "The user with email {} was created".format(
            DEFAULT_USER_EMAIL)
    else:
        print "The user with email {} was already there".format(
            DEFAULT_USER_EMAIL)


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

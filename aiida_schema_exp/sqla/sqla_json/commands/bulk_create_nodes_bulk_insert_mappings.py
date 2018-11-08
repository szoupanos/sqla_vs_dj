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

    import json
    import time

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
        curr_user = session.query(DbUser).filter_by(
            email=DEFAULT_USER_EMAIL).first()

    print "Creating nodes & starting measuring time"
    start_time = time.time()

    print "Constructing mappings"
    node_mappings = list()
    counter = 0
    for i in range(NUMBER_OF_NODES_TO_CREATE):
        node_mappings.append({'label': 'my_node_{}'.format(i), 'user_id': curr_user.id,
                              'attributes': json.dumps(['attr', i, {'bar': ('baz', None, 1.0, 2)}]),
                              'extras': json.dumps(['extra', i, {'bar': ('baz', None, 1.0, 2)}])})
        counter += 1

    print "Committing mappings (updating nodes)"
    session.bulk_insert_mappings(DbNode, node_mappings)
    session.commit()
    end_time = time.time()

    print "{} nodes created".format(counter)
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

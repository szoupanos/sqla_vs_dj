import click


@click.command()
def cmd():
    """Creating a user"""
    # Importing the engine
    from sqla_json.sqla_management import engine
    from sqlalchemy.orm import sessionmaker
    from sqla_json.models.node import DbNode
    from sqlalchemy.orm.attributes import flag_modified
    from sqla_json import timezone
    # from sqlalchemy.dialects.postgresql import insert
    from sqlalchemy.sql.expression import update

    import json
    import time

    sec = timezone.now().second
    msec = timezone.now().microsecond

    # Creating the needed session
    Session = sessionmaker(bind=engine)
    session = Session()

    print "Finding all the nodes and updating them one by one"
    start_time = time.time()

    print "Constructing mappings"
    node_mappings = list()
    counter=0
    for nid, in session.query(DbNode.id).all():
        node_mappings.append({'id': nid,
                              'attributes': json.dumps(
                                  ['attr', msec + counter, {'bar': ('baz', 'bulk_update_json_model_sql',
                                                                    sec + counter, 2)}]),
                              'extras': json.dumps(
                                  ['extra', msec + counter, {'bar': ('baz', 'bulk_update_json_model_sql',
                                                                    sec + counter, 2)}])})
        counter += 1

    print "Committing mappings"
    session.bulk_update_mappings(DbNode, node_mappings)
    session.commit()
    end_time = time.time()

    print("Updated the json fields (attributes and extras) "
          "of {} nodes.".format(counter))

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

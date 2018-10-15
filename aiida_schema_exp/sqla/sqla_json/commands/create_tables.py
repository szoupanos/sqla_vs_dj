import click

@click.command()
def cmd():
    """Creating the needed database tables"""
    # Importing the schema
    from sqla_json.models.base import Base
    from sqla_json.models.authinfo import DbAuthInfo
    from sqla_json.models.comment import DbComment
    from sqla_json.models.computer import DbComputer
    from sqla_json.models.group import DbGroup
    from sqla_json.models.lock import DbLock
    from sqla_json.models.log import DbLog
    from sqla_json.models.node import DbNode
    from sqla_json.models.node import DbCalcState
    from sqla_json.models.node import DbLink
    from sqla_json.models.settings import DbSetting
    from sqla_json.models.user import DbUser
    from sqla_json.models.workflow import DbWorkflow
    from sqla_json.models.workflow import DbWorkflowData
    from sqla_json.models.workflow import DbWorkflowStep

    # Importing the engine
    from sqla_json.sqla_management import engine

    click.echo('Creating tables')
    Base.metadata.create_all(engine)
    click.echo('Tables created')


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

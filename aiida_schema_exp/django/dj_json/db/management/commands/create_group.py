from django.core.management.base import BaseCommand
from db.management.commands import DEFAULT_USER_EMAIL, DEFAULT_GROUP_NAME


class Command(BaseCommand):

    def clean(self):
        pass

    def handle(self, *args, **kwargs):
        from db.models import DbGroup
        from db.models import DbUser

        usr, usr_res = DbUser.objects.get_or_create(email=DEFAULT_USER_EMAIL)
        if usr_res:
            print "The user with email {} was created".format(
                DEFAULT_USER_EMAIL)
        else:
            print "The user with email {} was already there".format(
                DEFAULT_USER_EMAIL)

        print "Creating group for user {}".format(DEFAULT_USER_EMAIL)
        _, group_res = DbGroup.objects.get_or_create(name=DEFAULT_GROUP_NAME,
                                                     user=usr)

        if group_res:
            print "Created the group {}".format(DEFAULT_GROUP_NAME)
        else:
            print "The group {} already exists".format(DEFAULT_GROUP_NAME)

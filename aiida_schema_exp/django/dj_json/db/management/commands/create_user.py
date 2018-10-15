from django.core.management.base import BaseCommand
from db.management.commands import DEFAULT_USER_EMAIL


class Command(BaseCommand):

    def clean(self):
        pass

    def handle(self, *args, **kwargs):
        from db.models import DbUser
        print "Creating user"

        usr, usr_res = DbUser.objects.get_or_create(email=DEFAULT_USER_EMAIL)
        if usr_res:
            print "The user with email {} was created".format(
                DEFAULT_USER_EMAIL)
        else:
            print "The user with email {} was already there".format(
                DEFAULT_USER_EMAIL)


import os, sys


if __name__ == '__main__':
    # Setup environ
    sys.path.append(os.getcwd())
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

    # Setup django
    import django
    django.setup()

    from mymodels.mymodels import Article, Reporter
    print "Hello world"

from django.core.management.base import BaseCommand
from django.db import transaction
from sqla_comp.models import Post, Category

import time

class Command(BaseCommand):

    def clean(self):
        Post.objects.all().delete()

    def handle(self, *args, **kwargs):
        # from dj_experiments.try2.mysite.sqla_comp.models import Post, Category

        py = Category(name='Python')
        py.save()

        Post(title='Hello Python!', body='Python is pretty cool')

        posts = list()
        for i in range(1, 10000):
            p = Post(title='Snakes {}'.format(i), body='Ssssssss {}'.format(i))
            p.save()
            posts.append(p)

        print "Adding posts one by one to the category and to the session in general"
        with transaction.atomic():
            start = time.time()
            count = 0
            prev_end = start
            for p in posts:
                py.posts.add(p)
                count = count + 1
                if count % 100 == 0:
                    curr_end = time.time()
                    print "Counter: {}, Time elapsed in sec: {}, Throughput (time per 1000 nodes): {}".format(
                        count, str(curr_end - start), str(curr_end - prev_end))
                    prev_end = curr_end
        print "Time elapsed in sec", str(time.time() - start)

        print "Data added"

        print "Category ====> ", Category.objects.all()
        print "Post ====> ", Post.objects.count()

        print "Cleaning tables"
        Category.objects.all().delete()
        Post.objects.all().delete()
        print "Tables cleaned"

        print "Category ====> ", Category.objects.all()
        print "Post ====> ", Post.objects.count()


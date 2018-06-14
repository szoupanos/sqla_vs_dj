# Adding objects and committing in the end

from mymodels.flaskmodel_3 import db
from mymodels.flaskmodel_3 import Category, Post
import time

OBJECT_NO = 100000

if __name__ == "__main__":
    print "Creating tables"
    db.create_all()
    print "Tables created"

    print "Adding data"
    py = Category(name='Python')
    # Post(title='Hello Python!', body='Python is pretty cool')

    # posts = list()
    # for i in range(1, OBJECT_NO):
    #     p = Post(title='Snakes {}'.format(i), body='Ssssssss {}'.format(i))
    #     posts.append(p)

    start_total = time.time()

    print "Adding category to the session"
    start_sa = time.time()
    db.session.add(py)
    db.session.commit()
    print "Time elapsed in sec (session add)", str(time.time() - start_sa)

    print "Adding posts to the database"
    start = time.time()
    for chunk in range(1, OBJECT_NO, 1000):
        db.session.bulk_insert_mappings(Post,
                               [dict(id=i, title='Snakes {}'.format(i), body='Ssssssss {}'.format(i)) for i in xrange(chunk, min(chunk + 1000, OBJECT_NO))]
                               )

    # count = 0
    # prev_end = start
    # for p in posts:
    #     # py.posts.append(p)
    #     db.session.add(p)
    #     count = count + 1
    #     if count % 100 == 0:
    #         curr_end = time.time()
    #         print "Counter: {}, Time elapsed in sec: {}, Throughput (time per 1000 nodes): {}".format(
    #             count, str(curr_end - start), str(curr_end - prev_end))
    #         prev_end = curr_end
    print "Time elapsed in sec", str(time.time() - start)


    # print "Committing"
    # start_co = time.time()
    # db.session.commit()
    # print "Time elapsed in sec (commit)", str(time.time() - start_co)
    #
    # print "Time elapsed in sec (total loading procedure)", str(
    #     time.time() - start_total)

    print "Data added"

    print "Category ====> ", Category.query.all()
    print "Post ====> ", Post.query.count()
    # db.session.flush()

    # print "Adding posts one by one to the group and to the session"
    # start = time.time()
    # count = 0
    # prev_end = start
    # for p in posts:
    #     py.posts.append(p)
    #     # db.session.add(p)
    #     count = count + 1
    #     if count % 100 == 0:
    #         curr_end = time.time()
    #         print "Counter: {}, Time elapsed in sec: {}, Throughput (time per 1000 nodes): {}".format(
    #             count, str(curr_end - start), str(curr_end - prev_end))
    #         prev_end = curr_end
    # print "Time elapsed in sec", str(time.time() - start)

    # db.session.bulk_update_mappings(Post,
    #                        [dict(id=i, category_id=1) for i in range(1, 10000)]
    #                        )

    # db.session.bulk_update_mappings(Post,
    #                        [dict(id=1, category_id=1)]
    #                        )

    print "Bulk update - adding posts to the right category"
    start_co = time.time()
    for chunk in range(1, OBJECT_NO, 1000):
        db.session.bulk_update_mappings(Post,
                               [dict(id=i, category_id=py.id) for i in xrange(chunk, min(chunk + 1000, OBJECT_NO))]
                               )
    print "Time elapsed in sec (bulk update)", str(time.time() - start_co)

    print "Lalalala", Post.query.filter_by(category=py).count()
    # print "Post ====> ", Post.query.all()

    print "py.posts", len(py.posts)

    db.session.close()

    print "Droping tables"
    db.drop_all()
    print "Tables dropped"

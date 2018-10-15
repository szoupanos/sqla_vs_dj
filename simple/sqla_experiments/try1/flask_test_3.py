from mymodels.flaskmodel_2 import db
from mymodels.flaskmodel_2 import Category, Post
import time

if __name__ == "__main__":
    print "Creating tables"
    db.create_all()
    print "Tables created"

    print "Adding data"
    py = Category(name='Python')
    Post(title='Hello Python!', body='Python is pretty cool', category=py)

    posts = list()
    for i in range(1, 100000):
        p = Post(title='Snakes {}'.format(i), body='Ssssssss {}'.format(i))
        posts.append(p)

    print "Adding posts one by one"
    start = time.time()
    count = 0
    prev_end = start
    for p in posts:
        py.posts.append(p)
        count = count + 1
        if count % 100 == 0:
            curr_end = time.time()
            print "Counter: {}, Time elapsed in ms: {}, Throughput (time per 100 nodes): {}".format(
                count, str(curr_end - start), str(curr_end - prev_end))
            prev_end = curr_end
    print "Time elapsed in sec", str(time.time() - start)

    print "Adding category to the session - This will also add all the posts"
    start_sa = time.time()
    db.session.add(py)
    print "Time elapsed in sec (session add)", str(time.time() - start_sa)

    print "Committing"
    start_co = time.time()
    db.session.commit()
    print "Time elapsed in sec (commit)", str(time.time() - start_co)

    print "Data added"

    print "Category ====> ", Category.query.all()
    print "Post ====> ", Post.query.count()
    # db.session.flush()
    db.session.close()

    print "Droping tables"
    db.drop_all()
    print "Tables dropped"

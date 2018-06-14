# Adding objects and committing one by one


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
    for i in range(1, 10000):
        p = Post(title='Snakes {}'.format(i), body='Ssssssss {}'.format(i))
        posts.append(p)


    print "Adding category to the session"
    start_sa = time.time()
    db.session.add(py)
    print "Time elapsed in sec (session add)", str(time.time() - start_sa)

    print "Adding posts one by one to the category and to the session in general"
    start = time.time()
    count = 0
    prev_end = start
    for p in posts:
        py.posts.append(p)
        db.session.add(p)
        db.session.commit()
        count = count + 1
        if count % 100 == 0:
            curr_end = time.time()
            print "Counter: {}, Time elapsed in ms: {}, Throughput (time per 100 nodes): {}".format(
                count, str(curr_end - start), str(curr_end - prev_end))
            prev_end = curr_end
    print "Time elapsed in sec", str(time.time() - start)


    # print "Committing"
    # start_co = time.time()
    # db.session.commit()
    # print "Time elapsed in sec (commit)", str(time.time() - start_co)

    print "Data added"

    print "Category ====> ", Category.query.all()
    print "Post ====> ", Post.query.count()
    # db.session.flush()
    db.session.close()

    print "Droping tables"
    db.drop_all()
    print "Tables dropped"

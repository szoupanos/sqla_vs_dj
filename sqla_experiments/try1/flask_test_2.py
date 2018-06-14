from mymodels.flaskmodel_2 import db
from mymodels.flaskmodel_2 import Category, Post

if __name__ == "__main__":
    print "Creating tables"
    db.create_all()
    print "Tables created"

    py = Category(name='Python')
    Post(title='Hello Python!', body='Python is pretty cool', category=py)
    p = Post(title='Snakes', body='Ssssssss')

    print "Adding data"
    py.posts.append(p)
    db.session.add(py)
    db.session.commit()
    print "Data added"

    print "Category ====> ", Category.query.all()
    print "Post ====> ", Post.query.all()
    # db.session.flush()
    db.session.close()

    print "Droping tables"
    db.drop_all()
    print "Tables dropped"

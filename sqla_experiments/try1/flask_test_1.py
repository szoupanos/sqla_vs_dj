from mymodels.flaskmodel_1 import db
from mymodels.flaskmodel_1 import User

if __name__ == "__main__":
    print "Creating tables"
    db.create_all()
    print "Tables created"

    admin = User(username='admin', email='admin@example.com')
    guest = User(username='guest', email='guest@example.com')

    print "Adding data"
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
    print "Data added"

    print "====> ", User.query.all()
    # db.session.flush()
    db.session.close()

    print "Droping tables"
    db.drop_all()
    print "Tables dropped"




# Adding objects and committing
# Then adding to the group and commiting


from mymodels.flaskmodel import db
from mymodels.flaskmodel import DbGroup, DbNode

import time

OBJECT_NO = 10000

if __name__ == "__main__":
    print "Creating tables"
    db.create_all()
    print "Tables created"

    print "Adding data"
    start_total = time.time()

    print "Creating the group and committing it"
    start_gr = time.time()
    gr = DbGroup(name='Python')
    db.session.add(gr)
    db.session.commit()
    print "Time elapsed in sec (group creation and commit)", str(time.time() - start_gr)

    print "Creating the nodes and committing them"
    start_n = time.time()
    nodes = list()
    for i in range(1, OBJECT_NO):
        n = DbNode(title='Snakes {}'.format(i), body='Ssssssss {}'.format(i))
        nodes.append(n)
        db.session.add(n)
    db.session.commit()
    print "Time elapsed in sec (node creation and commit)", str(
        time.time() - start_n)

    # db.session.expunge_all()

    print "Adding nodes one by one to the group and to the session"
    start = time.time()
    count = 0
    prev_end = start
    for n in nodes:
        gr.dbnodes.append(n)
        db.session.add(n)
        count = count + 1
        if count % 100 == 0:
            curr_end = time.time()
            print "Counter: {}, Time elapsed in sec: {}, Throughput (time per 1000 nodes): {}".format(
                count, str(curr_end - start), str(curr_end - prev_end))
            prev_end = curr_end
    print "Time elapsed in sec", str(time.time() - start)

    print "Committing"
    start_co = time.time()
    db.session.commit()
    print "Time elapsed in sec (commit)", str(time.time() - start_co)

    print "Time elapsed in sec (total loading procedure)", str(
        time.time() - start_total)

    print "Data added"

    print "DbGroup ====> ", DbGroup.query.all()
    print "DbNode ====> ", DbNode.query.count()
    # db.session.flush()
    db.session.close()

    print "Droping tables"
    db.drop_all()
    print "Tables dropped"

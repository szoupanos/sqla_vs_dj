# Adding objects and committing in the end

from mymodels.flaskmodel import db
from mymodels.flaskmodel import DbGroup, DbNode, table_groups_nodes
import time

OBJECT_NO = 1000

if __name__ == "__main__":
    print "Creating tables"
    db.create_all()
    print "Tables created"

    print "Adding data"
    gr = DbGroup(name='Python')
    start_total = time.time()

    print "Adding category to the session"
    start_sa = time.time()
    db.session.add(gr)
    db.session.commit()
    print "Time elapsed in sec (session add)", str(time.time() - start_sa)

    print "Adding posts to the database"
    start = time.time()
    for chunk in range(1, OBJECT_NO, 1000):
        db.session.bulk_insert_mappings(DbNode,
                                        [dict(id=i, title='Snakes {}'.format(i), body='Ssssssss {}'.format(i)) for i in xrange(chunk, min(chunk + 1000, OBJECT_NO))]
                                        )
    print "Time elapsed in sec", str(time.time() - start)


    print "Data added"

    print "Group ====> ", DbGroup.query.all()
    print "Nodes ====> ", DbNode.query.count()

    print "Bulk update - adding posts to the right category"
    start_co = time.time()
    # for chunk in range(1, OBJECT_NO, 1000):
    #     db.session.bulk_update_mappings(DbNode,
    #                                     [dict(id=i, group_id=gr.id) for i in xrange(chunk, min(chunk + 1000, OBJECT_NO))]
    #                                     )

    for chunk in range(1, OBJECT_NO, 1000):
        db.session.bulk_update_mappings(DbGroup,
                                        [dict(dbnode_id=i, dbgroup_id=gr.id) for i in xrange(chunk, min(chunk + 1000, OBJECT_NO))]
                                        )

    print "Time elapsed in sec (bulk update)", str(time.time() - start_co)

    # print "Lalalala", DbNode.query.filter_by(db_group=gr).count()

    print "gr.dbnodes", len(gr.dbnodes.all())

    db.session.close()
    #
    # print "Droping tables"
    # db.drop_all()
    # print "Tables dropped"

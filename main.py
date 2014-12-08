#!env/bin/python

__author__ = 'maddalena'

from config import SQLALCHEMY_DATABASE_URI
from app import Session, logger
from app.models import User

session = Session()


def main(args):
    print '------------------------------'
    print "sql alchemy test: "
    print "(database: %s)" % SQLALCHEMY_DATABASE_URI
    print '------------------------------'

    logger.debug('Insert three users')
    print "Insert three users:"
    add_user("Hanna", "hanna@test.com")
    add_user("John Smith", "j.smith@test.com")
    add_user("r.connors", "r.connors@test.com")

    users = session.query(User).all()
    show_users(users)

    logger.debug('Update users[1]')
    print "\n"
    print "Update users[1]"
    u = users[1]
    u.name = "******"
    session.add(u)
    session.commit()

    users = session.query(User).all()
    show_users(users)

    print "\n"
    print "Query by name == Hanna"
    u = session.query(User).filter(User.name == "Hanna").all()
    print u

    logger.debug('Delete all users')
    print "\n"
    print "Delete all users"
    session.query(User).delete()
    #session.flush()
    session.commit()

    users = session.query(User).all()
    show_users(users)

    session.close()


def show_users(userlist):

    if len(userlist) == 0:
        print "no user found"
    else:
        for u in userlist:
            print "%s %s %s" % (u.id, u.name, u.email)


def add_user(name, email):
    u = User(name, email)
    session.add(u)
    session.commit()


if __name__ == "__main__":
    import sys
    main(sys.argv)
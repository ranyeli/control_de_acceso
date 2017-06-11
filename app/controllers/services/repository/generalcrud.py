from session import session, DBSession


def insertdb(entity):
    session.add(entity)
    try:
        session.commit()
        DBSession.remove()
    except:
        session.rollback()

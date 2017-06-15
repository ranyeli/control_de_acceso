from session import session, DBSession


def insertdb(entity):
    session.add(entity)
    try:
        session.commit()
    except:
        DBSession.rollback()
    finally:
        DBSession.remove()

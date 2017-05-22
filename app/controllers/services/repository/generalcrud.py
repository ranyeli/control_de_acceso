from session import session


def insertdb(entity):
    session.add(entity)
    session.commit()

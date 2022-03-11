try:
    from userbot.modules.sql_helper import SESSION, BASE
except ImportError:
    raise AttributeError

from sqlalchemy import Column, String, UnicodeText


class GLOBELMute(BASE):
    __tablename__ = "globelmute"
    sender = Column(String(14), primary_key=True)

    def __init__(self, sender):
        self.sender = str(sender)


GLOBELMute.__table__.create(checkfirst=True)


def is_globelmuted(sender_id):
    try:
        return SESSION.query(GLOBELMute).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def globelmute(sender):
    adder = GLOBELMute(str(sender))
    SESSION.add(adder)
    SESSION.commit()


def unglobelmute(sender):
    if rem := SESSION.query(GLOBELMute).get((str(sender))):
        SESSION.delete(rem)
        SESSION.commit()

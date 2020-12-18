def check_tips(session):
    if session.get("tip") is None:
        tip = dict()
        tip["content"] = ""
        tip["level"] = "info"
        return tip
    else:
        tip = session.get("tip")
        session["tip"] = None
        return tip


def pass_tips(session, level, message):
    tip = dict()
    tip["content"] = message
    tip["level"] = level
    session["tip"] = tip


def modify_tips(level, message):
    tip = dict()
    tip["content"] = message
    tip["level"] = level
    return tip

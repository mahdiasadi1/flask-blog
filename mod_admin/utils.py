from flask import session,abort
from functools import wraps
def protected_view(func):
    @wraps(func)
    def innter_func(*args,**kwarg):
        print(session)
        if session.get('user_id') is None:
            abort(401)
        if session.get('role') is None or session.get('role')==0:
            abort(403)
        return func(*args,**kwarg)
    return innter_func    


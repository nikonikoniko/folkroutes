from threading import local

_user = local()

class CurrentUserMiddleware(object):
    def process_request(self, request):
        _user.value = request.user

def get_current_user():
    return _user.value

def get_current_user_id():
    return _user.value.id

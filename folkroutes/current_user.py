from threading import local

_user = local()

class CurrentUserMiddleware(object):
    def process_request(self, request):
        _user.value = request.user

def get_current_user():
    if hasattr(_user, "value"):
      return _user.value
    else:
      return 1

def get_current_user_id():
    return _user.value.id

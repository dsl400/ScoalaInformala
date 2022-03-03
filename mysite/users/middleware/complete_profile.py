


from django.shortcuts import redirect


class CompleteProfile():
    def __init__(self, get_response):
            self.get_response = get_response
    def __call__(self, request):
        if not request.user.is_anonymous:
            is_complete = True
            if not request.user.username:
                is_complete = False
            if not request.user.first_name:
                is_complete = False
            if not request.user.last_name:
                is_complete = False
            if not is_complete and request.path not in ['/users/profile', '/users/logout', '/users/profile_update'] :
                return redirect('/users/profile')
        return self.get_response(request)


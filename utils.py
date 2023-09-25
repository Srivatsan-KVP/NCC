def isLogged(req):
    return req.COOKIES.get('logged_in', False)
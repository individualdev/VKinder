class Search:

    def __init__(self):
        self.user = ""

    def SearchVKTop(self, api, user):
        return {"user": user, "api": api}

    def top(self, user, api):
        self.user = user
        return self.SearchVKTop(api, user)

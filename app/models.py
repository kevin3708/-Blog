class Blog:
    def __init__(self,title,post):
        self.title = title
        self.post = post




class Comment:
    all_comments = []
    
    def __init__(self,title,comment):
        self.title = title
        self.comment = comment

    def save_comment():
        Comment.all_comments.append

    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()
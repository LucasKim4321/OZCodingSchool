from flask_login import UserMixin

users = {
    'admin' : {'password':'pw123'}
}


class User(UserMixin):
    def __init__(self, username):
        self.id = username
    
    @staticmethod
    def get(user_id):
        if user_id in users:
            return User(user_id)  # user_id에 해당하는 User객체를 넘겨줌
        
        return None
    
    
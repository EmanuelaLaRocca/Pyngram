from user import User
from datetime import datetime


class Recipient(User):
    def __init__(self, name, surname, username, password, city, age, profile_privacy="public",is_premium=False):
        super().__init__(self, name, surname, username, password, city, age, profile_privacy="public",is_premium=False)

    def message_receive(self,sender,message):
        self.inbox.append({
     'sender':self.username,
     'date':datetime.now().strftime("%Y-%m-%d-%H:%M:%S"),
     'content': message})
        print(f"Messaggio ricevuto da {sender}")

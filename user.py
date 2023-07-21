from datetime import datetime
import ctypes
#import Recipient


class User:
    
    all_user = {}

    # Creo una variabile di classe dizionario che associa allo username la relativa password

    # Costruttore della classe
    def __init__(self, name, surname, username, password, city, age, profile_privacy="public",is_premium=False):  # profile_privacy, home
        self.name = name
        self.surname = surname
        self.username = username
        self.age = age
        self.city = city
        self.password = password
        self.profile_privacy = profile_privacy
        self.friend_list = []
        self.friend_list_request = []
        self.inbox = []
        self.is_premium = is_premium
        self.notice=[]
        self.homepage = []
        self.inbox= []
        self.dashboard = []

    # creo un metodo di classe per modificare l' attributo di classe: all_user
    @classmethod  # metodo di classe
    def sign_in(cls, name, surname, username, password, city, age):
        # aggiunge l'utente al "database"
        cls.all_user.append([username, password, name, surname, city, age])

    # creo un setter per assegnare l'attributo
    def setter__profile_privacy(self, privacy_level):
        self.__profile_privacy = privacy_level

    # creo un getter per "controllare" lla privacy delk'user
    def getter__profile_privacy(self):
        print(f"Il tuo livello di privacy è {self.__profile_privacy}")
        return self.__profile_privacy

    # mostra le notifiche dell'utente
    def show_notice(self):
        print("Notifiche: \n", self.notice)


    def show_homepage(self):
        print("Homepage: \n", self.homepage)


    # aggiunge notifiche al pannello notifiche
    def add_notice(self, new_notice):
        self.notice = self.notice.append(new_notice)

    def add_to_homepage(self, text):
     self.homepage= self.homepage.append(text)

    def add_to_dashboard(self, text): 
        self.dashboard= self.dashboard.append(text)

    # mostra le richieste di amicizia
    def show_friend_request_list(self):
        print(self.friend_request_list)

    # accetta le richieste di amicizia
    def accept_request(self, sender):
        if sender in self.friend_request_list:
            self.friend_list.append(sender)
            self.friend_request_list.remove(sender)
            self.add_notice(f"{sender} è stato aggiunto agli amici")

    def add_friend_request(self, sender):
        self.friend_list_request.append(sender)

    def send_message(self, recipient, message):
        print("nnnnnnnnnnnn")
      #  self.inbox.append({
       #     'sender':self.username,\
            #'date':datetime.now().strftime("%Y-%m-%d-%H:%M:%S"),
        #    'content': message})
        #Recipient.inbox.append({
         #   'sender': self.username,
          #  'date': datetime.now().strftime("%Y-%m-%d-%H:%M:%S"),
           # 'content': message})

        #print(f"Messagio inviato a {recipient}")
       # print(self.inbox)
       # else:
        #    print("Utente destinatario non trovato.")

    def upgrade_to_premium(self):
        while True:
            # Chiedi all'utente di inserire il codice di pagamento manualmente
            while True:
                credit_card = input("Inserisci il numero della carta di credito per l'upgrade a premium (16 cifre): ")
                if len(credit_card) == 16 and credit_card.isdigit():
                    break
                else:
                    print(f"Il numero di cifre da inserire è 16 \nIl numero di cifre inserite: {len(credit_card)}")

            holder = input("Inserisci il titolare della carta di credito: ")
            expiry_date = input("Inserisci data di scadenza della carta di credito: ")
            while True:
                cvc = input("Inserisci cvc (3 cifre): ")
                if len(cvc) == 3 and cvc.isdigit():
                    break
                else:
                    print("CVC non valido. Inserisci un CVC numerico di 3 cifre.")
            break

        self.is_premium = True
        print(
            f"Complimenti {self.username}, il tuo profilo è stato aggiornato a premium! \nOra il tuo account è contrassegnato da un spunta blu")





Default= User("Giulio", "Rossi", "GiuRos", "123Abc12@", "Firenze", 33)
User.all_user["GiuRos"]= "123Abc12@"
giulio_pointer = id(Default)
casted_object = ctypes.cast(giulio_pointer,ctypes.py_object).value
#Default.add_friend_request("Gabriele97")
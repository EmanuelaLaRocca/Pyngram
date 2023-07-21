#funzioni
from user import User
import user
import post
import ctypes
all_username_pointers = {}
all_username_pointers["GiuRos"] = user.giulio_pointer


def welcome_message():
        print("Benvenuto su Pyngram!\n Ti trovi sulla nuova piattaforma Social totalmente made in Italy\n")

def message_error():
        print("ERRORE\n azione non eseguibile")

def  add_friend(current_user,receiver):
    #friend_username= input("Inserire l'username del contatto a cui mandare la richiesta di amicizia")
    for i in current_user.friendlist:
        if receiver.username == current_user.friendlist[i]:#for per controllare l'amicizia
            receiver.add_notice(f"nuova richiesta di amicizia da {current_user.username}")
            receiver.add_friend_request(current_user)
            print("Richiesta inviata")
        break
    print("Contatto non trovato")


def check_password(password):
    special_sym=["$","@","#","%"]
    psw_accepted=True
    if len(password)<8:
        print("La password deve contenere almeno 8 caratteri")
        psw_accepted=False
    if not any(char.isdigit() for char in password):
        print("La password deve contenere almeno un numero")
        psw_accepted=False
    if not any(char.isupper() for char in password):
        print("La password deve contenere almeno un lettera maiuscola")
        psw_accepted=False
    if not any(char.islower() for char in password):
        print("La password deve contenere almeno una lettera minuscola")
        psw_accepted=False
    if not any(char in special_sym for char in password):
        print(f"La password deve contenere almeno un carattere speciale {special_sym}")
        psw_accepted=False

    return psw_accepted

#def  send_messageg(User1, User2,all_user):
    #friend_username= input("Inserire l'username del contatto a cui mandare un messaggio")
 #   message = input("Inserire il messaggio da inivare")
  #  if User2.username in all_user:
   #     User2.add_notice(f"nuova messaggio da {User1.username}")
    #    User2.add_message(User1.username, message)
     #   print("Messaggio inviato")
    #else:
     #   print("Contatto non trovato")


def check_username(username):
    if username==" " or username =="":
        print("Inserire username")
        return False

    for used_username in User.all_user:
        if username == used_username :
            print("username già in uso")
            return False
            break
        else:
            return True


#Funzione per controllare se l'utente è maggiorenne
def check_age(age):
    if age < 18:
        print("Hai meno di 18 anni")
        return False
    else:
        return True

'''
#funzione per controllare la validità della password
def check_password(password):
    special_sym=["$","@","#","%"]

    val=True
    #almeno 8 caratteri
    if len(password)<8:
        print("La password deve contenere almeno 8 caratteri")
        val=False

    #almeno 1 numeor
    if not any(char.isdigit() for char in password):
        print("La password deve contenere almeno un numero")
        val=False

    #almeno una lettera maiuscola
    if not any(char.isupper() for char in password):
        print("La password deve contenere almeno un lettera maiuscola")
        val=False

    #almeno una lettera minuscola
    if not any(char.islower() for char in password):
        print("La password deve contenere almeno una lettera minuscola")
        val=False

    #almeno un carattere speciale
    if not any(char in special_sym for char in password):
        print(f"La password deve contenere almeno un carattere speciale {special_sym}")
        val=False

    return val
'''

#funzione per controllare se la password e lo username sono corretti e accettati
def check_log_in(username,password):
  #prende in input username e password, restitusce vero se esiste e combaciano all'interno del dizionario User.all_us
   if password!= User.all_user[username]:
    print("Password errata")
    return False
   else:
    return True

 #return user e username in coppia gia aggiunti a un dizionario
#procedura sign_in
def sign_in():
    username=" "
    password=" "

    name=input("Inserisci il tuo nome: \n")
    surname=input("Inserisci il tuo cognome: \n")
    age=int(input("Inserisci la tua età: \n"))
    city=input("Inserisci la tua città: \n")


    while check_username(username) is False:
        username=input("Inserisci il tuo username: \n")

    while check_password(password) is False:
        password=input("Inserisci una password: \n")


    User.all_user[username]= password
    User1= User(name,surname,username,age,city,password)

    user_pointer = id(User1)
    User.all_username_pointers[username] = user_pointer

    return True

def name_object(username):
    pointer =all_username_pointers[username]
    casted_object = ctypes.cast(pointer,ctypes.py_object).value
    return casted_object

#def add_to_homepage(Current_User, Post):
#    Current_User.homepage= Current_User.homepage.append(Post)



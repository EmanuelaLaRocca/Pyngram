import user
import funzioni
from post import Post
import post
import ctypes
import Recipient 

entry=False


username=" "
password=" "

funzioni.welcome_message() #stampa un messaggio di benvenuto "Benvenuto su InstaFace!"
first_choice = input("Hai già un account? [si] [no]\n").lower()
if first_choice != "si" and first_choice !="sì":
    #creo il primo account
    print("Creiamo un account!")
    funzioni.sign_in()
    print("Account registrato con successo!\n")
    other_account = input("Vuoi creare un altro account?").lower()
    while other_account == "si" or other_account == "sì":
        funzioni.sign_in()
        print("Account registrato con successo!\n")
        other_account = input("Vuoi creare un altro account?").lower()


#Fase di login
while entry is False:
  print("Log in\n")
  username=input("Inserisci il tuo username: \n")
  password=input("Inserisci una password: \n")
  result_log_in= funzioni.check_log_in(username,password)
  if result_log_in:
    print("Login avvenuto con successo!")
    Current_User = funzioni.name_object(username)
    entry= True
  else:
    print("utente o password errati")

#INIZIO CORE DEL PROGRAMMA
id_choice = False
while id_choice is False:
  menu_choice = input("""Scegli un'azione dal menu\nMenu: \n\
                1- Visualizza le notifiche\n\
                2- Crea un nuovo post\n\
                3- Visualizza Homepage\n\
                4- Visualizza Dashboard\n\
                5- Manda una richiesta di amicizia\n\
                6- Accetta una richiesta di amicizia\n\
                7- Apri una chat\n\
                8- Fai un upgrade a premium\n\
                9- Gestisci la tua privacy\n\
               Digita logout per uscire da InstaFace\n\
               """)

  #MOSTRA NOTIFICHE
  if menu_choice=="1":
    Current_User.show_notice()

  #AGGIUNGI POST
  if menu_choice=="2":
    text_post = input("Scrivi un post: ")
    while True:
        pubblication_choice = input("""Premi 1 se vuoi pubblicare il post,\n
        2 per riscrivere il post,\n
        premi 3 per ritornare al menù principale: """)
        if pubblication_choice == "1":
            print("Il post è stato pubblicato con successo!")
            post1 = Post(text_post, Current_User)
            post1.add_post()
            Current_User.add_to_homepage(post1.text)
            Current_User.add_to_dashboard(post1.text)
            print("Il post è stato pubblicato con successo!")
            break
        elif pubblication_choice == "2":
            text_post = input("Riscrivi il post: ")
        else:
            print("ciao")
            break
   

      #VISUALIZZA HOMEPAGE
  elif menu_choice=="3":
     Current_User.show_homepage()


   #VISUALIZZA DASHBOARD
  elif menu_choice=="4":
     print(post.all_post_tot)
  # manda una richiesta di amicizia
  elif menu_choice =="5":
      us_friend = input("Inserisci username per mandare una richiesta di amicizia?")
      funzioni.add_friend(Current_User, funzioni.name_object(us_friend))
      print("Richiesta di amicizia inviata a", us_friend)

  # accetta richiesta di amicizia
  elif menu_choice == "6":
      pass

  #manda un messaggio a un tuo amicone
  elif menu_choice =="7":
      recipient = input("A chi vuoi scrivere?")
      message = input("Che vuoi scrivere?")
      Current_User.send_message(recipient,message)
     # Receiver = Recipient("Giulio", "Rossi", "GiuRos", "123Abc12@", "Firenze", 33)
      #Receiver.message_receive(Current_User,message)


    #fai upgrade a premium
  elif menu_choice =="8":
      Current_User.upgrade_to_premium()

  #IMPOSTA PRIVACY
  elif menu_choice=="9":
      Current_User.getter__profile_privacy()
      level_privacy=input("Scegli 0 per profilo privato, 1 per profilo pubblico, 2 per lasciare il profilo inalterato: ")
      if level_privacy=="1":
          Current_User.setter__profile_privacy("Public")
          print("Livello privacy modificato con successo")
      if level_privacy=="0":
          Current_User.setter__profile_privacy("Private")
          print("Livello privacy modificato con successo")

  elif menu_choice=="logout":
    print("A presto!")
    break
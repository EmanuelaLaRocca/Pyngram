# Pyngram
Programma che simula un social. 
  
Per prima cosa abbiamo realizzato un diagramma ER per rappresentare graficamente entità, relazioni e attributi del nostro sistema.  
  
  
  
Ecco il link al diagramma ER: 
  
https://www.canva.com/design/DAFo-Sd3AZ4/Cd7FTsBDW4F0WsWU3yNlBQ/edit  
  
  
  
Abbiamo deciso di creare un blocco di codice principale (main.py) contenente le funzioni che l’utente può effettuare su Pyngram. 
  
In questo blocco di codice principale sono richiamati dei moduli tramite l’istruzione import. Una volta importati i moduli, è stato possibile accedere alle sue definizioni utilizzando il nome del modulo seguito da un punto. 
  
I moduli da noi importati sono: user.py, funzioni.py e post.py. 
  
Inoltre, abbiamo importato una libreria ctypes per estrarre un oggetto. 
  
  
  
La prima cosa che si può fare nel main è iscriversi a Pyngram. 
  
La prima domanda che ci viene fornita lanciando il codice è se abbiamo già un account o meno. 
  
Se la risposta è no, ci fa procedere all’iscrizione. 
  
Per iscriversi è necessario inserire nome, cognome, età, città, username e password (sono presenti alcune condizioni che se non rispettate in fase di iscrizione, non ci permettono di procedere e ci “buttano” indietro). 
  
  
  
Nel main.py è presente il core del nostro programma: sono presenti tutte le azioni principali che può svolgere un utente registrato al social. 
  
Attraverso un ciclo while è possibile scegliere le attività che si desiderano svolgere: 
  
•	Visualizzare notifiche
•	Creare un nuovo post
•	Visualizzare la homepage
•	Manda una richiesta di amicizia
•	Accetta una richiesta di amicizia
•	Scrivere un messaggio ad un altro utente
•	Fare un upgrade a premium
•	Gestire la privacy
  
  
Nel modulo post.py è presente la classe Post che contiene text e user come attributi e alcuni metodi relativi a questa classe: aggiunta di un post. 
  
  
  
Nel modulo user.py è presente la classe User che contiene name, surname, password, city, age, profile_privacy, is_premium come attributi e alcuni metodi relativi a questa classe: sign_in, modifca_pricacy, mostra_notifiche, invia_richieste_amicizia, invia_messaggi, passaggio_premium. 
  
Inoltre, è stato inserire un utente di default “GiuRos” per permettere di visualizzare le interazioni con il current_user. 



ROADMAP 
  
Potremmo aggiungere: 
  
- modifiche successive dei post 
  
- suggerimento amicizie 
  
- implementazione database csv esterno che contiene tutte le info (salvando le informazioni relative agli utenti iscritti, ai loro post e alle interazioni con gli altri utenti). 
  
  

  
  
  
Nel modulo funzioni.py sono presenti tutte le funzioni che richiamiamo nel main. 
  
  
  

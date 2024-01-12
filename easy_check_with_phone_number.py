from exchangelib import Credentials, Account, DELEGATE
from pushbullet import PushBullet
import schedule
import time
import requests

resp = requests.post('https://textbelt.com/text',

{
 'phone': '', 
 'message': 'NOUVEAU MESSAGE OUTLOOK',
 'key': 'textbelt',

 })

credentials = Credentials("", "")
account = Account('', credentials=credentials, autodiscover=True, access_type=DELEGATE)

def get_last_message_id():
    return "AQAAATtTPEYBAAAC2S1xTwAAAAA="
    

last_message_id = get_last_message_id()
new_messages = account.inbox.filter(datetime_received__gt=last_message_id) #le double tiret du bas "__" avant gt veut dire plus grand que donc dans ce cas tout les message suivant le précédent message donc "last message" autrement dit le message le plus récent

pb = PushBullet('o.Ze66vPBQQB6Icm7vt6K8lieFYg4kO4ci')
push = pb.push_note("Nouveau message Outlook", "Nouveau message reçu M. ...")

def verif():
    # Vérifiez les nouveaux messages et envoyez la notification
    if get_last_message_id != "AQAAATtTPEYBAAAC2S1xTwAAAAA=":
        print(push) 
        print(resp.json()) # envoie la notif a votre numéro de tel
        

#Planifier la tâche pour s'exécuter toutes les deux secondes
schedule.every(2).minutes.do(verif)

# Boucle infini 
while True:
    schedule.run_pending() # Exécute la tache planifier donc execute la ligne suivante "schedule.every(2).minutes.do(verif)"
    time.sleep(1) #laisse 1 seconde de repos pour éviter surcharge




        
        
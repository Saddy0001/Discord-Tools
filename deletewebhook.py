from discord_webhook import DiscordWebhook
import requests
from colorama import Fore , Style
webzn = input("Url da webhook que você irá queimar : ")
msg = input("Insira uma mensagem para floodar antes da webhook ser deletada : ")
username = input("Insira o nome da webhook : ")
webhook = DiscordWebhook(url=webzn, content=msg ,username = username, avatar_url="https://cdn.discordapp.com/embed/avatars/0.png")
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()
response = webhook.execute()

print("Webhook caiu deletando...")
response = webhook.execute()
requests.delete(webzn)
print(f"\n{Fore.LIGHTBLUE_EX}Webhook deletada em nome de :\n mensagem enviada :{msg}\nusername : {username}\n{Fore.LIGHTBLACK_EX}")


    # -- coding: utf-8 --
from os import name, system
from time import sleep
from colorama import Fore, init

init()
banniere = """            dddddddd                                                                                                     
            d::::::d                                         BBBBBBBBBBBBBBBBB                             tttt          
            d::::::d                                         B::::::::::::::::B                         ttt:::t          
            d::::::d                                         B::::::BBBBBB:::::B                        t:::::t          
            d:::::d                                          BB:::::B     B:::::B                       t:::::t          
    ddddddddd:::::d    mmmmmmm    mmmmmmm                      B::::B     B:::::B   ooooooooooo   ttttttt:::::ttttttt    
  dd::::::::::::::d  mm:::::::m  m:::::::mm                    B::::B     B:::::B oo:::::::::::oo t:::::::::::::::::t    
 d::::::::::::::::d m::::::::::mm::::::::::m                   B::::BBBBBB:::::B o:::::::::::::::ot:::::::::::::::::t    
d:::::::ddddd:::::d m::::::::::::::::::::::m ---------------   B:::::::::::::BB  o:::::ooooo:::::otttttt:::::::tttttt    
d::::::d    d:::::d m:::::mmm::::::mmm:::::m -:::::::::::::-   B::::BBBBBB:::::B o::::o     o::::o      t:::::t          
d:::::d     d:::::d m::::m   m::::m   m::::m ---------------   B::::B     B:::::Bo::::o     o::::o      t:::::t          
d:::::d     d:::::d m::::m   m::::m   m::::m                   B::::B     B:::::Bo::::o     o::::o      t:::::t          
d:::::d     d:::::d m::::m   m::::m   m::::m                   B::::B     B:::::Bo::::o     o::::o      t:::::t    tttttt
d::::::ddddd::::::ddm::::m   m::::m   m::::m                 BB:::::BBBBBB::::::Bo:::::ooooo:::::o      t::::::tttt:::::t
 d:::::::::::::::::dm::::m   m::::m   m::::m                 B:::::::::::::::::B o:::::::::::::::o      tt::::::::::::::t
  d:::::::::ddd::::dm::::m   m::::m   m::::m                 B::::::::::::::::B   oo:::::::::::oo         tt:::::::::::tt
   ddddddddd   dddddmmmmmm   mmmmmm   mmmmmm                 BBBBBBBBBBBBBBBBB      ooooooooooo             ttttttttttt  """
print(Fore.CYAN+banniere)
print("         Bot dev par Toto'#1337 pour barjo l'homosexuel")
sleep(5)
if name  == "nt":
    system("color 1")
    def clear():
        clear()
else:
    def clear():
        system("clear")

try:
    import discord
except:
    print("Les modules nécessaires ne sont pas installés.")
    sleep(1.5)
    clear()
    print("Tentative d'installation des modules...\n")
    sleep(0.5)
    try :
        system("pip install discord")
        clear()
        print("Les modules sont maintenant installés.")
        sleep(1)
        clear()
        import discord
    except :
        print("Erreur lors de la tentative d'installation des modules.")
        sleep(1.5)
        print("'pip' n'est probablement pas installé.")
        input()
        quit()

from discord.ext import commands
token = "Token de ton bot"
username = "Toto#1337"
def dmall(membre) :
    return f"""Message a dm"""

async def spam_members(guild):
    for member in guild.members:
        try:
            await member.send(dmall(member.name))
        except:
            pass


bot = commands.Bot(command_prefix='>', intents=discord.Intents.all())
     
@bot.event
async def on_ready():
    
    activity = discord.Game(name=">dmall pour dmall fils de pute", type=1)
    await bot.change_presence(status=discord.Status.idle, activity=activity)


@bot.event
async def on_message(message):
    serveur = message.guild
    if message.content == ">dmall":
        await spam_members(serveur)
  
try:
    bot.run(token)
except:
    input("Le token du bot est invalide :/")
    quit()

import urllib
import json
import requests
import discord
from discord.ext import commands
import datetime
import io
 
from urllib import parse, request
from PIL import Image, ImageDraw, ImageFont, ImageFile
import time
###
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash import SlashCommand, SlashContext



intents = discord.Intents.all()

bot = commands.Bot(command_prefix = '/', intents=intents)
bot.remove_command("help") # Borra el comando por defecto !help
slash = SlashCommand(bot, sync_commands=True)
@slash.slash(
    name="habbo", description="Escribe tu nombre.",
    options=[
                create_option(
                  name="habbonombre",
                  description="Escribe tu nombre de habbo hotel.",
                  option_type=3,
                  required=True
                ),
                 create_option(
                  name="hotel",
                  description="Elige él hotel",
                  option_type=3,
                  required=True,
                  choices=[
                      create_choice(
                          name="ES",
                          value="es"
                      ),
                      create_choice(
                          name="BR",
                          value="com.br"
                      ),
                      create_choice(
                          name="COM",
                          value="com"
                      ),
                      create_choice(
                          name="DE",
                          value="de"
                      ),
                      create_choice(
                          name="FR",
                          value="fr"
                      ),
                      create_choice(
                          name="FI",
                          value="fi"
                      ),
                      create_choice(
                          name="IT",
                          value="it"
                      ),
                      create_choice(
                          name="TR",
                          value="com.tr"
                      ),
                      create_choice(
                          name="NL",
                          value="nl"
                      )
                  ]
                
               
                  
                )
             ])
             
            
             

    


async def _habbo(ctx:SlashContext, habbonombre:str,hotel:str):
    await ctx.defer()
   
   

   
    

    
    
   
    
    url = f"https://www.habbo.{hotel}/habbo-imaging/avatarimage?user={habbonombre}&action=std&direction=2&head_direction=2&gesture=std&size=l" #url
    

   
    
    


    
    


    



    
    r = requests.get(url)
    if  r.status_code ==200:
        imagen = Image.open(io.BytesIO(requests.get(url).content))
        with io.BytesIO() as imagen_binary:
            imagen.save(imagen_binary, 'PNG')
            imagen_binary.seek(0)
            
            
            await ctx.send(file=discord.File(fp=imagen_binary, filename=f'keko.png'))
            print(f"Habbo Nombre: {habbonombre}") #Esto lo puedes quitar si quieres   

    else:
        
        print(f"Habbo Nombre: {habbonombre} no existe") #Esto lo puedes quitar si quieres   
        await ctx.send(f"{habbonombre} no existe ❌")
        

  
 
 
 
@bot.event
async def on_ready():
    print("BOT listo!")
    
 
     
bot.run('') 

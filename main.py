import discord
from discord.ext import commands
import random
import os

images = os.listdir('Çevre Botu\images')
cevre1 = ["Geri dönüşüm ve hangi malzemelerin geri dönüştürülebileceği hakkında bilgi edinin.",
        "Eski eşyaları çöpe atmak yerine geri dönüştürün", 
        "Tek kullanımlık ürünlerin kullanımını azaltmak için yeniden kullanılabilir ürünler kullanın.",
         "Hangi ürünlerin ve ambalajların geri dönüşüm için en iyi olduğunu araştırın ve satın alırken bunları seçin.",
          "Su kullanmadığınız zamanlarda musluğu açık bırakmayarak su tasarrufu yapın.",
           "Evde ampuller ve klimalar gibi enerji tasarruflu cihazlar kullanın.",
            "Ulaşım masraflarını azaltmak için yerel kaynaklardan yiyecek satın alın." ]

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def mem(ctx):
    choiceimage = random.choice(images)
    with open(f'Çevre Botu\images\{choiceimage}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def cevre(ctx):
    bilgi = random.choice(cevre1)
    await ctx.send(f'İşte bir bilgi: {bilgi}')

bot.run("Token")

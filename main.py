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

cevre2 = ["Günde yaklaşık 27,000 ağaç kesiliyor.", "İnsanlar dünya'daki suyun sadece yüzde birini kullanabiliyor.", "Bütün karıncaların ağırlıkları bütün insanların ağırlıklarından daha fazla."]

cevre3 = ["Dünya'daki suyun yüzde kaçı tatlı sudur? A) %3  B) %1,5  C) %2,5 D) %2", "Türkiye'nin yaklaşık olarak yüzde kaçı ormandır? A) %25  B) %30  C) %35  D) %40"]

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

@bot.command()
async def facts(ctx):
    fact = random.choice(facts)
    await ctx.send(f'İşte bir bilgi: {fact}')

@bot.command()
async def question(ctx):
    soru = random.choice(cevre3)
    await ctx.send(f'Soru: {soru}')

bot.run("Token")

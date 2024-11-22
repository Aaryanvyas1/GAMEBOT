import telebot
import webbrowser

Token = "8073459577:AAF42t9fgT9T7TXWw-1Ovk1AAynE6fKxqYU"

bot = telebot.TeleBot(Token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to the Gaming Bot! Enter what game you would like to download.")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, """Available commands:
/start - Greetings from the bot
/help - Help on how to use the bot
<name of the game> - Enter the name of the game you want to download.""")

@bot.message_handler(func=lambda message: True)
def custom(message):
    glinks = {
        "RDR": 'https://dodi-repacks.site/?s=rdr',
        "GTA": 'https://dodi-repacks.site/?s=gta',
        "Sekiro": 'https://dodi-repacks.site/?s=sekiro',
        "DMC": 'https://dodi-repacks.site/?s=DMC',
        "GOW": 'https://dodi-repacks.site/?s=god+of+war',
        "WWE": 'https://dodi-repacks.site/?s=WWE',
        "FIFA": 'https://dodi-repacks.site/?s=fifa'
    }

    gname = message.text.strip()  
    
    if gname in glinks:
        bot.reply_to(message, f"Here is your link: {glinks[gname]}")
    else:
        bot.reply_to(message, "Sorry, I don't have a link for that game.")

bot.polling()
import os
import telebot
import google.generativeai as genai

# Эти переменные мы настроим позже в Koyeb
BOT_TOKEN = os.getenv('BOT_TOKEN')
GEMINI_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle(message):
    try:
        res = model.generate_content(message.text)
        bot.reply_to(message, res.text)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    bot.infinity_polling()

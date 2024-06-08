import telebot
from telebot import types
import random

bot = telebot.TeleBot('6882051733:AAHk4QhZznYnbXybGoXtod1aVxcWxeo0018')

# Command handlers
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello There! I am a mini game bot. Type /help to see the list of commands")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "/ben10 to play Ben 10 game\n/rps to play Rock Paper Scissors")

# Ben 10 game
@bot.message_handler(commands=['ben10'])
def play_ben10(message):
    alien_list = ["Fourarms", "Spidermonkey", "Bigchill", "Swampfire", "Waybig", "Humagasour", "Ghostfreak", "Jetray", "Goop", "Clomastone", "Cannonbolt", "Wildmutt", "Rath", "Alien X"]
    aliens = random.sample(alien_list, 5)
    vil = bot.send_message(message.chat.id, "Now Vilgax is coming. Hurry up! Select an alien to defeat him.")
    markup = types.InlineKeyboardMarkup(row_width=1)
    buttons = [types.InlineKeyboardButton(alien, callback_data=alien) for alien in aliens]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "**YOUR OMNITRIX**", reply_markup=markup)

# Rock Paper Scissors game
@bot.message_handler(commands=['rps'])
def play_rps(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    choices = ["Rock", "Paper", "Scissors"]
    buttons = [types.InlineKeyboardButton(choice, callback_data=choice) for choice in choices]
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Choose! Rock, Paper, or Scissors", reply_markup=markup)

# Callback query handling
@bot.callback_query_handler(func=lambda call: True)
def game(call):
    if call.data in ["Rock", "Paper", "Scissors"]:
        play_rps_game(call)
    elif call.data in ["Fourarms", "Spidermonkey", "Bigchill", "Swampfire", "Waybig", "Humagasour", "Ghostfreak", "Jetray", "Goop", "Clomastone", "Cannonbolt", "Wildmutt", "Rath", "Alien X"]:
        play_ben10_game(call)

# Ben 10 game logic
def play_ben10_game(call):
    selected_alien = call.data
    killer = random.choice(["Fourarms", "Spidermonkey", "Bigchill", "Swampfire", "Waybig", "Humagasour", "Ghostfreak", "Jetray", "Goop", "Clomastone", "Cannonbolt", "Wildmutt", "Rath", "Alien X"])
    if selected_alien == killer:
        bot.send_message(call.message.chat.id, f"Congratulations! Your {selected_alien} defeated Vilgax!")
    else:
        bot.send_message(call.message.chat.id, f"Oops! Your {selected_alien} is not strong enough to defeat Vilgax.")
    bot.send_message(call.message.chat.id, "**Game Over**, to play again type /ben10")

# Rock Paper Scissors game logic
def play_rps_game(call):
    computer = random.choice(["Rock", "Paper", "Scissors"])
    if call.data == computer:
        bot.send_message(call.message.chat.id, f"It's a draw! I chose {computer}")
    elif (call.data == "Rock" and computer == "Scissors") or (call.data == "Paper" and computer == "Rock") or (call.data == "Scissors" and computer == "Paper"):
        bot.send_message(call.message.chat.id, f"You win! I chose {computer}")
    else:
        bot.send_message(call.message.chat.id, f"You lose! I chose {computer}")

# Start the bot
bot.polling()

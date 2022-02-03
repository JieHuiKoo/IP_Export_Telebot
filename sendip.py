import telebot
import os

# Depending on OS type, the / is different in the directory
if os.name == 'posix':
    slash = '/obtain_ip/' 
else:
    slash = '\\'

# # Getting the currently working directory
current_working_directory = os.getcwd()

# Open the files for ip address, token for the telebot, and the user ID
ip_file = open(current_working_directory + slash + 'ip_address.txt', 'r')
token_file = open(current_working_directory + slash + 'token.txt', 'r')
user_file = open(current_working_directory + slash + 'user.txt', 'r')

# Obtain the ip address, token for the telebot, and the user ID, then close the files
IP_address_text = ip_file.read()
token_text = token_file.read()
user_text = user_file.read()
ip_file.close()
token_file.close()
user_file.close()

# Create bot
bot = telebot.TeleBot(token=token_text)

# Send message
bot.send_message(user_text, str('The IP address of most recently turned on Rasp PI is:\n'+ IP_address_text))
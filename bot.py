import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm your bot!")

def main():
    # Set up the bot
    updater = Updater(token='5265562585:AAE1XXeQqOeT2KVg7qPpjpmQQWyJIQZucKE', use_context=True)
    dispatcher = updater.dispatcher

    # Add command handler
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

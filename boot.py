from BOT_HOSTING import keep_alive, bot

if __name__ == "__main__":
    keep_alive()
    print("Bot is running...")
    bot.infinity_polling()

import launcher
import logging

logging.basicConfig(level=logging.INFO)

# Launch the desired bot with the parameters defined in the Configuration file
bot = launcher.bot()
logging.info(bot)
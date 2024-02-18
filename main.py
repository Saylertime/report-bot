from loader import bot
import handlers
from telebot.custom_filters import StateFilter
from utils.set_bot_commands import set_default_commands
import schedule
import time
import threading
from db_maker import *

notifications_10 = Notifications.select(Notifications.user_id).where(Notifications.notification_time == 15)
user_ids_10 = [notification.user_id for notification in notifications_10]
notifications_15 = Notifications.select(Notifications.user_id).where(Notifications.notification_time == 15)
user_ids_15 = [notification.user_id for notification in notifications_15]
notifications_20 = Notifications.select(Notifications.user_id).where(Notifications.notification_time == 20)
user_ids_20 = [notification.user_id for notification in notifications_20]

def job():
    while True:
        schedule.run_pending()
        time.sleep(1)

def send_periodic_message(user_id):
    bot.send_message(user_id, "Ваше периодическое сообщение")

def set_notification_time():
    notifications_10 = datetime.datetime.now().replace(hour=10, minute=0, second=0, microsecond=0)
    notifications_15 = datetime.datetime.now().replace(hour=15, minute=0, second=0, microsecond=0)
    notifications_20 = datetime.datetime.now().replace(hour=20, minute=0, second=0, microsecond=0)

    for user_id in user_ids_10:
        schedule.every().day.at(notifications_10.strftime('%H:%M')).do(send_periodic_message, user_id)
    for user_id in user_ids_15:
        schedule.every().day.at(notifications_15.strftime('%H:%M')).do(send_periodic_message, user_id)
    for user_id in user_ids_20:
        schedule.every().day.at(notifications_20.strftime('%H:%M')).do(send_periodic_message, user_id)

if __name__ == "__main__":
    set_notification_time()
    threading.Thread(target=job).start()
    bot.add_custom_filter(StateFilter(bot))
    set_default_commands(bot)
    bot.infinity_polling()















# from loader import bot
# import handlers
# from telebot.custom_filters import StateFilter
# from utils.set_bot_commands import set_default_commands
#
# if __name__ == "__main__":
#     bot.add_custom_filter(StateFilter(bot))
#     set_default_commands(bot)
#     bot.infinity_polling()
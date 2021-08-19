from btrader import BTrader
from config.config import *
from telegram.ext import *


def help_command(update, context):
    update.message.reply_text(help_message)


def alarm(context: CallbackContext) -> None:
    job = context.job
    trader = BTrader(job.name)
    trader.run()
    text = trader.response.get_response()
    if not text and notify_when_there_is_no_signal:
        text = non
    context.bot.send_message(job.context, text=text)


def remove_job_if_exists(name: str, context: CallbackContext) -> bool:
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


def set_timer(update, context):
    chat_id = update.message.chat_id

    job_removed = remove_job_if_exists(str(chat_id), context)
    context.job_queue.run_repeating(
        alarm, telegram_hour, context=chat_id, name=str(chat_id))

    update.message.reply_text(start_message)


def unset(update, context):
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    text = stop_message if job_removed else off_message
    update.message.reply_text(text)



def error(update, context):
    print(f'Update {update} caused error {context.error}')


def main():
    updater = Updater(
        TELEGRAM_API_KEY, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler("start", set_timer))
    dp.add_handler(CommandHandler("stop", unset))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()

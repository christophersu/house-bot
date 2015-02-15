from apscheduler.schedulers.blocking import BlockingScheduler
import secrets
import requests

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon,wed,fri', hour=9)
def scheduled_job():
    requests.post("https://api.groupme.com/v3/bots/post", data={
        "text" : 'Dishwasher cycle scheduled for today.',
        "bot_id" : secrets.BOT_ID
    })

print "Starting scheduler."
sched.start()
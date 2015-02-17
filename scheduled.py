from apscheduler.schedulers.blocking import BlockingScheduler
import os
import requests

if 'GROUPME_BOT_ID' in os.environ:
    GROUPME_BOT_ID = os.environ['GROUPME_BOT_ID']
else:
    import secrets
    GROUPME_BOT_ID = secrets.GROUPME_BOT_ID

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon,wed,fri', hour=9)
def scheduled_job():
    requests.post("https://api.groupme.com/v3/bots/post", data={
        "text" : 'Dishwasher cycle scheduled for today.',
        "bot_id" : GROUPME_BOT_ID
    })

print "Starting scheduler."
sched.start()
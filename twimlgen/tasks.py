from models import Call
from lendup.celery import app
from django.conf import settings
import datetime
import time
from django.core.urlresolvers import reverse

@app.task()
def delay_call(number, delay):
	print "waiting"
	time.sleep(int(delay))
	print "calling"
	call = settings.TWILIO_CLIENT.calls.create(
            to=number,
            from_="13236202984",
            url=settings.DOMAIN + (reverse("twimlgen:enter_number"))
        )
	call_obj = Call(number = number, origin_time = datetime.datetime.now(), delay = delay)
	call_obj.save()

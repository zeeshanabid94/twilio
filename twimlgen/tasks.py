from models import Call
from lendup.celery import app
from django.conf import settings
import datetime
import time
from django.core.urlresolvers import reverse
from twilio.rest import Client

@app.task()
def delay_call(number, delay, url_number):
	print "waiting"
	time.sleep(int(delay))
	print "calling"
	TWILIO_CLIENT = Client(settings.TWILIO_ACCOUNT_ID, settings.TWILIO_TOKEN)
	call = TWILIO_CLIENT.calls.create(
            to=number,
            from_="13236202984",
            url='http://twiliodemo.hopto.org/enter_a_number/'
        )

	try:
		call_obj = Call.objects.get(number = number)
	except:
		call_obj = Call(number = number, origin_time = datetime.datetime.now(), delay = delay)
		call_obj.save()

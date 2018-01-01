# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from twilio.twiml.voice_response import Gather, VoiceResponse, Say
from django.views.generic import View, FormView
from django.conf import settings
from django.http import HttpResponse
from django.core.urlresolvers import reverse
import strings
from forms import UserInputForm
from models import Call, Game
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# from twilio.twiml.voice_response import Gather, VoiceResponse, Say
#
# response = VoiceResponse()
# gather = Gather(input='speech dtmf', timeout=3, num_digits=1)
# gather.say('Please press 1 or say sales for sales.')
# response.append(gather)

# Create your views here.

class UserInputView(FormView):
	template_name = 'welcome.html'
	form_class = UserInputForm
	success_url = 'still have to write this'

	def get_context_data(self, **kwargs):
		context = super(UserInputView, self).get_context_data()
		context["list"] = Game.objects.all()
		return context

	def form_valid(self, form):
		print "Valid form"
		# This method is called when valid form data has been POSTed.
		# It should return an HttpResponse.
		form.call_user(self.request)
		return super(FormView, self).form_valid(form)


@method_decorator(csrf_exempt, name='dispatch')
class TwimlGen(View):
	def get(self, *args, **kwargs):
		twimlresponse = VoiceResponse()

		twimlresponse.say("Enter a number followed by the pound key")
		gather = Gather(input='dtmf')

		# Can add a beep here
		twimlresponse.append(gather)

		# Debugging print statements
		print twimlresponse
		httpresponse = HttpResponse(twimlresponse, content_type="text/xml", status = 200)
		return httpresponse


	def post(self, *args, **kwargs):
		number = self.request.POST.get('Digits', 10)
		to = self.request.POST.get('To', 'number')
		try:
			call = Call.objects.get(number=to)
			game = Game(call = call, fizzbuzz = number)
			game.save()
		except:
			pass
		print number
		twimlresponse = VoiceResponse()

		for i in range(1, int(number) + 1):
			if i % 3 == 0 and i % 5 == 0:
				twimlresponse.say(strings.Fizzbuzz, voice="woman", language="en-US")
			elif i % 3 == 0:
				twimlresponse.say(strings.Fizz, voice="woman", language="en-US")
			elif i % 5 == 0:
				twimlresponse.say(strings.Buzz, voice="woman", language="en-US")
			else:
				twimlresponse.say(str(i), voice="woman", language="en-US")

		# Debugging print statements
		print twimlresponse

		httpresponse = HttpResponse(twimlresponse, content_type="application/xml", status=200)
		return httpresponse


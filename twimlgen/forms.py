from django import forms
from django.conf import settings
from django.core.urlresolvers import reverse
from background_task import background

class UserInputForm(forms.Form):
    name = forms.CharField(max_length = 256, required=True)
    number = forms.CharField(max_length=16, required=True)
    time = forms.CharField(max_length=2, required=True)

    # def clean_recipients(self):
    #     data = self.cleaned_data['recipients']
    #     if "fred@example.com" not in data:
    #         raise forms.ValidationError("You have forgotten about Fred!")
    #
    #     # Always return a value to use as the new cleaned data, even if
    #     # this method didn't change it.
    #     return data
    # def clean_number(self):
    #     data = self.cleaned_data['number']
    #
    #     if '+' not in data:
    #         raise forms.ValidationError("Enter number in the form +123456789")
    #
    #     return data

    def call_user(self, request):
        print "Calling User"

        @background(schedule=60 * int(self.cleaned_data['time']))
        def call_user_delayed(user_id):
            print "This works"
            call = settings.TWILIO_CLIENT.calls.create(
                to=self.cleaned_data["number"],
                from_="13236202984",
                url=request.build_absolute_uri(reverse("twimlgen:enter_number"))
            )


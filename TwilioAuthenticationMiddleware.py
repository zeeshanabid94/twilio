
# This is for security purposes. Verifies
# the X-Twilio-Signature.

# Can be finished in the end
class TwilioAuthenticationMiddleware(object):

    def process_request(self, request):
        urlstring = request.build_absolute_uri()

        if request.method == 'POST':
            # Sort post params first

            post_params = request.POST

            # sorted_params = sorted(post_params, key = lambda x : )
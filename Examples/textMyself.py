#! python3
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string

from twilio.rest import TwilioRestClient

# Preset values:
accountSID = 'ACf0b15a2348daa30c348062c010f4ba54'
authToken = '0dcd711b1dde2966890de12ef9a1b0bc'
myNumber = '+79148773089'
twilioNumber = '+12566458080'


def textmyself(message):
    twilioCli = TwilioRestClient(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)

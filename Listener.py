import configparser
import json
import asyncio
from datetime import date, datetime
from telethon import TelegramClient, events, sync
from twilio.rest import Client
import sys
import getopt
import os

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
    PeerChannel
)


# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
#to_whatsapp_number='whatsapp:+14132304412'

twilioSIDRegularSlotsList = ['ACc109dfc6c2bc906c9521f9c2c12eb046', 'AC3bbb75f0b55ad8896bb21e7bd6410c95']
twilioAuthTokenRegularSLotsList = ['eb4e53f7db05c516649f874533bcff46', 'a199c782336570019ee38dad4b01f2ba']
toWhatsappNumberRegularSlotsList = ['+14132304412', '+919739865109']


twilioSIDStampingSlotsList = ['ACc109dfc6c2bc906c9521f9c2c12eb046']
twilioAuthTokenStampingSlotsList = ['eb4e53f7db05c516649f874533bcff46']
toWhatsappNumberStampingSlotsList = ['+14132304412']


def startListener():

    api_id = "16901005"
    api_hash = "878bbfdc2c7d9be5a4f620be7fd83c42"

    # use full phone number including + and country code
    phone = "+14132304412"
    username = "kartik_chhapia"

    user_input_channel_regular_slots = 'https://t.me/Regular_H1B_H4_VisaSlotsChecking'
    user_input_channel_stamping_slots = 'https://t.me/H1B_H4_Visa_Dropbox_slots'




    # Create the client and connect
    client = TelegramClient(username, api_id, api_hash)

    client.start()

    @client.on(events.NewMessage(chats=user_input_channel_regular_slots))
    async def newMessageListener(event):
            messageFromEvent = event.message.message
            if not filterRegularSlots(messageFromEvent):
                print ("not sending to whatsapp")
            else:
                sendMessageRegularSlotsWhatsapp(messageFromEvent)

    @client.on(events.NewMessage(chats=user_input_channel_stamping_slots))
    async def newMessageListener(event):
            messageFromEvent = event.message.message
            if not filterStampingSlots(messageFromEvent):
                print ("not sending to whatsapp")
            else:
                sendMessageStammpingSlotsWhatsapp(messageFromEvent)

    with client:
            client.run_until_disconnected()



def filterRegularSlots(messageFromEvent):
    sendToWhatsapp = False
    if "na " in messageFromEvent.lower() or "not" in messageFromEvent.lower() or "?" in messageFromEvent.lower() \
    or "if" in messageFromEvent.lower() or "no" in messageFromEvent.lower():
        print ("ignoring sending to whatsapp1")
    elif "ofc" in messageFromEvent.lower() and "available" in messageFromEvent.lower() and not "ca" in messageFromEvent.lower():
        print ("ignoring sending to whatsapp2")

    elif "available" in messageFromEvent.lower() and "ca" in messageFromEvent.lower() :
                    sendToWhatsapp = True

    elif "just" in messageFromEvent.lower() and "booked" in messageFromEvent.lower() :
                    sendToWhatsapp = True

    elif "just" in messageFromEvent.lower() and "got" in messageFromEvent.lower() :
                    sendToWhatsapp = True

    elif "available" in messageFromEvent.lower() and "booked" in messageFromEvent.lower() :
                    sendToWhatsapp = True

    elif "available" in messageFromEvent.lower() and "slots" in messageFromEvent.lower() :
                    sendToWhatsapp = True

    elif "available" in messageFromEvent.lower() and "still" in messageFromEvent.lower() :
                    sendToWhatsapp = True


    return sendToWhatsapp


def filterStampingSlots(messageFromEvent):
    sendToWhatsapp = False
    if "na " in messageFromEvent.lower() or "not" in messageFromEvent.lower() or "?" in messageFromEvent.lower():
        print ("ignoring sending to whatsapp stamping")
    elif "ofc" in messageFromEvent.lower() and "available" in messageFromEvent.lower() and not "ca" in messageFromEvent.lower():
        print ("ignoring sending to whatsapp stamping")

    elif "available" in messageFromEvent.lower() and "ca" in messageFromEvent.lower() :
                    sendToWhatsapp = True

    elif "just" in messageFromEvent.lower() and "booked" in messageFromEvent.lower() :
                    sendToWhatsapp = True


    elif "just" in messageFromEvent.lower() and "got" in messageFromEvent.lower() :
                    sendToWhatsapp = True

    elif "available" in messageFromEvent.lower() and "booked" in messageFromEvent.lower() :
                    sendToWhatsapp = True


    elif "available" in messageFromEvent.lower() and "slots" in messageFromEvent.lower() :
                    sendToWhatsapp = True


    elif "available" in messageFromEvent.lower() and "still" in messageFromEvent.lower() :
                    sendToWhatsapp = True


    return False


def sendMessageRegularSlotsWhatsapp(messageFromEvent):
            for token, sid, to_number in zip(twilioAuthTokenRegularSLotsList, twilioSIDRegularSlotsList, toWhatsappNumberRegularSlotsList):

                os.environ["TWILIO_AUTH_TOKEN"] = token
                os.environ["TWILIO_ACCOUNT_SID"] = sid
                twilioClient = Client()
                to_whatsapp_number = 'whatsapp:' + to_number
                twilioClient.messages.create(body=messageFromEvent,
                                       from_=from_whatsapp_number,
                                       to=to_whatsapp_number)


def sendMessageStammpingSlotsWhatsapp(messageFromEvent):
            for token, sid, to_number in zip(twilioAuthTokenRegularSLotsList, twilioSIDRegularSlotsList, toWhatsappNumberRegularSlotsList):

                os.environ["TWILIO_AUTH_TOKEN"] = token
                os.environ["TWILIO_ACCOUNT_SID"] = sid
                twilioClient = Client()
                to_whatsapp_number = 'whatsapp:' + to_number
                twilioClient.messages.create(body=messageFromEvent,
                                       from_=from_whatsapp_number,
                                       to=to_whatsapp_number)

argv = sys.argv[1:]
try:

        # Start the listener
        print("Starting the listener")
        startListener()

except getopt.GetoptError:
    print(usage)
    sys.exit(1)
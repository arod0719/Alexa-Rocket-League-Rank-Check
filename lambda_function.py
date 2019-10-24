from __future__ import print_function
from RocketLeagueRanks import *
from RLdatabase import *

usid = '' #alexa user profile
session_ranks = Ranks() #creates a rank instance for every user
database = Database(str(usid)) #find individual database
database.cleanup() #remove errors in database

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

def transcribeName(string):
    string = string.replace(" ","").replace(".","").replace("underscore","_").replace("dash","-").capitalize()
    return string


# --------------- Skill request handeling  ------------------
def refresh_request():
    global database
    global session_ranks
    session_ranks = Ranks(session_ranks.user, session_ranks.name)
    database = Database(str(usid))
    speech_output = "Database and Users have been successfully updated"
    session_attributes = {}
    card_title = "refresh"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, should_end_session))

def get_session_change_request(intent, session):
    global session_ranks
    global database
    tempname = transcribeName(str(intent['slots']['name']['value']))
    users = database.get()
    if (tempname in users):
        if (tempname == session_ranks.name):
            speech_output = str(tempname) + "'s profile is already active."
        else:
            session_ranks = Ranks(users[tempname], tempname)
            speech_output = str(tempname) + "'s profile " + users[tempname] + " is now active"
    else:
        speech_output = "I don't know that person."
    session_attributes = {}
    card_title = "change"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, should_end_session))

def quick_lookup_request(intent, session):
    if (intent["confirmationStatus"]=="CONFIRMED"):
        global session_ranks
        user = transcribeName(str(intent['slots']['user']['value']))
        session_ranks = Ranks(user, "the player")
        speech_output = user + "'s profile is now active"
    else:
        speech_output = "I won't lookup that player"
    session_attributes = {}
    card_title = "quicklookup"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, should_end_session))
    

def get_userlist_response():
    userlist = database.listusers()
    speech_output = "The current names in the database are " + userlist
    session_attributes = {}
    card_title = "list"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, should_end_session))

def get_current_user():
    speech_output = "The current user is " + session_ranks.name
    session_attributes = {}
    card_title = "current"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, should_end_session))
    

def delete_user_request(intent, session):
    global database
    currentNames = database.get()
    name = transcribeName(str(intent['slots']['name']['value']))
    if (name in currentNames):
        if (intent["confirmationStatus"]=="CONFIRMED"):
            database.delete(name)
            database = Database(str(usid))
            speech_output = name + " has been successfully deleted."
        else:
            speech_output = "Okay, I wont delete " + name
    else:    
        speech_output = "I don't know that person."
    session_attributes = {}
    card_title = "delete"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, should_end_session))
    

def add_name_request(intent, session):
    global database
    users = database.get()
    database.cleanup()
    name = transcribeName(str(intent['slots']['name']['value']))
    if (name not in users):
        if (intent["confirmationStatus"]=="CONFIRMED"):
            database.add(name, 'null')
            speech_output = name + " has been added successfully, please add their username now"
            database = Database(str(usid))
        else:
            speech_output = "Okay I won't add " + name
    else:
        speech_output = name + " is already in the database. Delete them first and try again."
    session_attributes = {}
    card_title = "addname"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, should_end_session))

def add_user_request(intent, session):
    global database
    global session_ranks
    users = database.get()
    user = transcribeName(str(intent['slots']['user']['value']))
    names = database.freshname()
    if (len(names) == 1):
        if (intent["confirmationStatus"]=="CONFIRMED"):
            for name in names:           
                database.add(name, user)
            session_ranks = Ranks(user, name)
            speech_output = name + " has been added with username " + user + " successfully, " + name + " is now the active profile"
            database = Database(str(usid))
        else:
            speech_output = "Okay I won't add " + str(user)
    else:
        speech_output = "Please enter a name first and try again"
    session_attributes = {}
    card_title = "adduser"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, should_end_session))


def get_seasonreward_response():
    session_attributes = {}
    card_title = "seasonreward"
    speech_output = "" + str(session_ranks.seasonrank())
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, should_end_session))

def get_all_response():
    session_attributes = {}
    card_title = "all"
    speech_output = "" + str(session_ranks.all())
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, should_end_session))

def get_duel_response():
    session_attributes = {}
    card_title = "all"
    speech_output = "" + str(session_ranks.duel())
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, should_end_session))

def get_doubles_response():
    session_attributes = {}
    card_title = "all"
    speech_output = "" + str(session_ranks.doubles())
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, should_end_session))

def get_standard_response():
    session_attributes = {}
    card_title = "all"
    speech_output = "" + str(session_ranks.standard())
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, should_end_session))

def get_solostandard_response():
    session_attributes = {}
    card_title = "all"
    speech_output = "" + str(session_ranks.solostandard())
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, should_end_session))

def get_hoops_response():
    session_attributes = {}
    card_title = "all"
    speech_output = "" + str(session_ranks.hoops())
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, should_end_session))

def get_rumble_response():
    session_attributes = {}
    card_title = "all"
    speech_output = "" + str(session_ranks.rumble())
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, should_end_session))

def get_dropshot_response():
    session_attributes = {}
    card_title = "all"
    speech_output = "" + str(session_ranks.dropshot())
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, should_end_session))

def get_snowday_response():
    session_attributes = {}
    card_title = "all"
    speech_output = "" + str(session_ranks.snowday())
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, should_end_session))
    

def get_welcome_response():
    session_attributes = {}
    card_title = "welcome"
    speech_output = "Rocket League rank checker opened" 
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, should_end_session))

def get_fallback_response():
    session_attributes = {}
    card_title = "fallback"
    speech_output = "I do not know that command"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, should_end_session))

def YesIntentResponse():
    session_attributes = {}
    card_title = "No"
    speech_output = "I won't do that"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, should_end_session))


def handle_session_end_request():
    global database
    global session_ranks
    database.cleanup()
    database = Database(str(usid))
    session_ranks = Ranks()
    card_title = "Session Ended"
    speech_output = "I hope your rank is as good as you hoped. " \
                    "Keep grinding gamer! "
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, should_end_session))

# --------------- automatic requests ------------------
    

def on_launch(launch_request, session):
    global usid
    usid = session["user"]["userId"]
    global database
    database = Database(str(usid))
    return get_welcome_response()


def on_intent(intent_request, session):

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    if intent_name == "all":
        return get_all_response()
    elif intent_name == "refresh":
        return refresh_request()
    elif intent_name == "change":
        return get_session_change_request(intent, session)
    elif intent_name == "addname":
        return add_name_request(intent, session)
    elif intent_name == "adduser":
        return add_user_request(intent, session)
    elif intent_name == "delete":
        return delete_user_request(intent, session)
    elif intent_name == "quicklookup":
        return quick_lookup_request(intent, session)
    elif intent_name == "list":
        return get_userlist_response()
    elif intent_name == "current":
        return get_current_user()
    elif intent_name == "duel":
        return get_duel_response()
    elif intent_name == "doubles":
        return get_doubles_response()
    elif intent_name == "standard":
        return get_standard_response()
    elif intent_name == "solostandard":
        return get_solostandard_response()
    elif intent_name == "hoops":
        return get_hoops_response()
    elif intent_name == "rumble":
        return get_rumble_response()
    elif intent_name == "dropshot":
        return get_dropshot_response()
    elif intent_name == "snowday":
        return get_snowday_response()
    elif intent_name == "seasonrank":
        return get_seasonreward_response()
    elif intent_name == "AMAZON.FallbackIntent":
        return get_fallback_response()
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])


# --------------- Main handler ------------------

def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])

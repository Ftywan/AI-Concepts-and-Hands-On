from re import *   # Loads the regular expression module.
import random

# contants: wordlist, sentense list, etc
# 
BICYCLE_WORD = ['Siao, yourself look like a ', 
                'Ask your dad for the ', 
                'Do I look like a ', 
                'If you get an A+ I will buy you a ',
                'Wah you crazy? Don\'t you know what does it mean of having a ']

SAD_WORD = ["Wah, Jialat already!",
            'Eh, cheer up!',
            'Oh, I feel so sorry.',
            'Oh I really hope hope something I can help with'
            ]

PUNCTUATION_PATTERN = compile(r"\,|\.|\?|\!|\;|\:")

CASE_MAP = {'i':'you', 'I':'you', 'me':'you','you':'me',
            'my':'your','your':'my',
            'yours':'mine','mine':'yours','am':'are'}

PUNTS = ['I am from Singapore, do you know?',
        'How are you ah, by the way?',
        'Eat laksa for lunch? You hungry now?',
        'Can you say it again?',
        'Good leh!',
        'You know are there any activies?',
        'By the way. Do you have any tips for an internship?',
        'Have a nice one!']

# global variable
bicycle_count = 0
punt_count = 0
memory = []

# main block, run alone only
def Joshua():
    introduce()
    # main block
    while True:
        the_input = input('TYPE HERE:>> ')
        if match('bye',the_input):
            print('Goodbye!')
            return
        respond(the_input)

def respond(the_input):
    # pre-processing of the natual language input
    wordlist = split(' ',remove_punctuation(the_input))
    wordlist[0]=wordlist[0].lower()
    mapped_wordlist = you_me_map(wordlist)
    mapped_wordlist[0]=mapped_wordlist[0].capitalize()

    # if the sentence is said
    if the_input in memory:
        respond = "Eh you have said that. Don\'t play play ah."
        return respond
    else:
        memory.append(the_input)

    # says nothing
    if wordlist[0]=='':
        respond = "Say something lah"
        return respond

    # if the talker is sad
    if 'sad' in wordlist:
        global SAD_WORD
        respond = SAD_WORD[random.randint(0, len(SAD_WORD)-1)]
        return respond

    # if the sentence starts with i am
    if wordlist[0:2] == ['i','am']:
        respond = "Wah lao! Tell me more about why you are " +\
                    stringify(mapped_wordlist[2:]) + '.'
        return respond

    # if a question is asked
    if wpred(wordlist[0]):
        respond = "Eh, I don't know leh... You tell me " + wordlist[0] + "loh."
        return respond
    
    # cycle feature; if talker wants something
    if wordlist[0:3] == ['i', 'want', 'a']:
        global bicycle_count
        global BICYCLE_WORD
        bicycle_count = bicycle_count + 1
        
        respond = BICYCLE_WORD[bicycle_count % len(BICYCLE_WORD)] +\
            stringify(mapped_wordlist[3:]) + '.'    
        return respond

    # if talkers says it has something
    if wordlist[0:2] == ['i','have']:
        respond = "How long have you had " +\
              stringify(mapped_wordlist[2:]) + '.'
        return respond

    # if the talker expersses its feeling
    if wordlist[0:2] == ['i','feel']:
        respond = "Aiyoh, I sometimes feel the same."
        return respond

    # if the talker says some reason
    if 'because' in wordlist:
        respond = "Wah, that thing is too cheem for me"
        return respond

    # if the talker says yes
    if 'yes' in wordlist:
        respond = "Come I clap for you!"
        return respond

    # if the talker start with you are
    if wordlist[0:2] == ['you','are']:
        respond = "Yah lah, I am " +\
              stringify(mapped_wordlist[2:]) + '.'
        return respond

    # if the talker ask to do something
    if verbp(wordlist[0]):
        respond = "Paiseh ah, I cannot do that"
        return respond

    # if the talker asks about the opintion
    if wordlist[0:3] == ['do','you','think']:
        respond = "Siao leh. Why do you think that!"
        return respond

    # if the talker asks about the capability
    if wordlist[0:2]==['can','you'] or wordlist[0:2]==['could','you']:
        respond = "Wah talk too much already, shag man."
        return respond

    # if the talker says about dream
    if 'dream' in wordlist:
        respond = "Eh, die die must try ah."
        return respond

    # if tha talker says about love
    if 'love' in wordlist:
        respond = "Got to chiong ah bro."
        return respond

    # if the talker negates something
    if 'no' in wordlist:
        respond = "Don\'t be so nagative meh."
        return respond

    # if the talker is uncertain about something
    if 'maybe' in wordlist:
        respond = "Don't be so kiasu mah."
        return respond

    # if 'you' in mapped_wordlist or 'You' in mapped_wordlist:
    #     respond = stringify(mapped_wordlist) + '.'
    #
    #     return respond
    
    # if we do not understand the talker
    respond = punt()
    return respond

def stringify(wordlist):
    'Create a string from wordlist, but with spaces between words.'
    return ' '.join(wordlist)

def remove_punctuation(text):
    'Returns a string without any punctuation.'
    return sub(PUNCTUATION_PATTERN ,'', text)

def wpred(w):
    'Returns True if w is one of the question words.'
    return (w in ['when','why','where','how'])

def dpred(w):
    'Returns True if w is an auxiliary verb.'
    return (w in ['do','can','should','would'])

def punt():
    'Returns one from a list of default responses.'
    global punt_count
    punt_count += 1
    return PUNTS[punt_count % 6]

def you_me(w):
    'Changes a word from 1st to 2nd person or vice-versa.'
    try:
        result = CASE_MAP[w]
    except KeyError:
        result = w
    return result

def you_me_map(wordlist):
    'Applies YOU-ME to a whole sentence or phrase.'
    return [you_me(w) for w in wordlist]

def verbp(w):
    'Returns True if w is one of these known verbs.'
    return (w in ['go', 'have', 'be', 'try', 'eat', 'take', 'help',
                  'make', 'get', 'jump', 'write', 'type', 'fill',
                  'put', 'turn', 'compute', 'think', 'drink',
                  'blink', 'crash', 'crunch', 'add'])

def agentName():
    return "Joshua"

def introduce():
    intro = "Hi my name is Johshua Ng from Singapore. You can call me Josh if you want.\n" + "I was proggrammed by Tianyuan Fu and if you have any comments to me please contact him at tyfu@uw.edu.\n" + "So, welcome to my kopitiam and what can I do for you?"
    print(intro)
    return intro

# Joshua() # Launch the program.

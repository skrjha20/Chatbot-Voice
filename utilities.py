import re
import numpy as np
from nltk.corpus import stopwords
from mssqldb import fetch_data
from datetime import date, timedelta, datetime
from date_extractor import extract_dates

stop_words = set(stopwords.words('english'))

invalid_response = ["KATA INI BELUM SAYA PELAJARI",
                    "I can ask my botmaster.", "Is there only one?",
                    "I'll ask around and get back to you.",
                    "Ask the open directory about it.",
                    "Interesting question.",
                    "I need time to formulate the reply.",
                    "Maybe my botmaster knows the answer.",
                    "What is it to you?",
                    "I have never been asked that before.",
                    "That's not something I get asked all the time.",
                    "Is that a rhetorical question?",
                    "I would do a search for it.",
                    "Have you tried a web search?",
                    "I'll come back to that later.",
                    "Searching...Searching...Please stand by.",
                    "Have you tried another program?",
                    "That's an interesting question. I'll come back to that in a minute.",
                    "I think you already know the answer.",
                    "I would look into the web for that knowledge.",
                    "There might be more than one.",
                    "Would you like to know more?",
                    "I will search for it.",
                    "I will try to find out.",
                    "I'm not that into politics. Who is it?",
                    "It depends on the historical context, because it changes from time to time.",
                    "Try searching the open directory.",
                    "Check back later and see if I learn the answer to that one.",
                    "I have to process that one for a while.",
                    "I can ask someone about it.",
                    "That's a good question.",
                    "Are you testing me?",
                    "Let me think about it.",
                    "Are you using Netscape or Explorer?",
                    ".", ""]

time_query = ["what is time",
			 "what is the time",
			 "what is the current time",
			 "what time",
			 "what is time now",
			 "what is time now?",
			 "what is current time",
			 "current time",
			 "time",
			 "what is the time now",
			 "what time is it",
			 "tell me the time"]

product =  ['c2', 'c3', 'c4', 'c5', 'c5+', 'plus', 'agp', 'lng', 'condensate', 'das', 'ethane', 'ethylene', 'export', 'fsopr',
			'fueloil', 'fuel', 'oil', 'gasoil', 'gas', 'gasoline', 'gasoline', 'granulated', 'sulphur', 'injection', 'jet', 'a1',
			'lean', 'fertilizer', 'leanfertilizer', 'leaninjection', 'leanother', 'other', 'leansalesgas', 'salesgas', 'sales',
			'liquid', 'sulphur', 'murban', 'crude', 'naphtha', 'poly', 'polyethylene', 'propylene', 'polypropylene',
			'procleaninjection', 'raw', 'natural', 'salesagp', 'saleslng', 'salessourgas' 'sourgas', 'sour', 'upper', 'zakum', 'urea',
            'lpg']
plan_type = ["plan", "planned","plant"]
actual_type = ["actual"]
query_day = ["today", "yesterday"]


def get_product(clean_words):
    prod = []
    for i in range(len(clean_words)):
        if clean_words[i] in product:
            prod.append(clean_words[i])
    prod = " ".join(str(x) for x in prod)

    if len(prod) == 0:
        prod = "Unable to identify product name, please specify product name"
    return prod


def get_date(clean_words, question):
    date1 = ''
    date2 = ''
    if "yesterday" in clean_words:
        date1 = date.today() - timedelta(1)
        date1 = date1.strftime("%Y-%m-%d")
    elif "today" in clean_words:
        date1 = date.today().strftime("%Y-%m-%d")

    if date1 == '':
        question = re.sub(r"(?<=\d)(st|nd|rd|th)\b", '', question)
        dates = extract_dates(question)
        try:
            date1 = dates[0].strftime("%Y-%m-%d")
            date2 = dates[1].strftime("%Y-%m-%d")
        except:
            pass

    date_req=[]
    if date1 == '':
        return ("Unable to identify the required day for query")
    else:
        date_req.append(date1)
        date_req.append(date2)
        return date_req


def get_actual_planned(clean_words):
    actual_planned = ''
    for i in range(len(clean_words)):
        if clean_words[i] in actual_type:
            actual_planned = "actual"
        if clean_words[i] in plan_type:
            actual_planned = "planned"
    if actual_planned == '':
        actual_planned = "Unable to identify actual or planned, please specify again"
    return actual_planned

def question_to_text(question):
    text_list = list(question.split(' '))
    clean_words = [w for w in text_list if not w in stop_words]
    reply = get_answer(clean_words,question)
    return reply

def get_answer(clean_words, question):
    product = get_product(clean_words)
    if product == "Unable to identify product name, please specify product name":
        return ("Unable to identify product name, please specify product name")

    req_day = get_date(clean_words, question)
    if req_day == "Unable to identify the required day for query":
        return ("Unable to identify the required day for query")

    actual_planned = get_actual_planned(clean_words)
    if actual_planned == "Unable to identify actual or planned, please specify again":
        return ("Unable to identify actual or planned, please specify again")

    outcome, unit = fetch_data(product, actual_planned, req_day)
    return return_reply(outcome, product, actual_planned, req_day, unit)


def return_reply(outcome, product, actual_planned, req_day, unit):
    if outcome == None:
        return( "We do not have data for the query, please ask question again")

    if type(outcome) != int:
        return outcome
    else:
        return("The " + actual_planned +" production of " + product +" was "+ str(outcome) + " " + unit + " on " + datetime.strptime(req_day[0],'%Y-%m-%d').strftime("%b %d %Y"))
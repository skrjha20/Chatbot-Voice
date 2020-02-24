import re
import aiml
import pyttsx3
import os, time
import speech_recognition as sr
from num2words import num2words
from nltk.corpus import stopwords
from utilities import get_answer, invalid_response, time_query, question_to_text
from date_extractor import extract_dates
from dateutil.parser import *
from datetime import datetime

stop_words = set(stopwords.words('english'))
db_query = ['c2', 'c3', 'c4', 'c5', 'c5+', 'plus', 'agp', 'lng', 'condensate', 'das', 'ethane', 'ethylene', 'export', 'fsopr',
			'fueloil', 'fuel', 'oil', 'gasoil', 'gas', 'gasoline', 'gasoline', 'granulated', 'sulphur', 'injection', 'jet', 'a1',
			'lean', 'fertilizer', 'leanfertilizer', 'leaninjection', 'leanother', 'other', 'leansalesgas', 'salesgas', 'sales',
			'liquid', 'sulphur', 'murban', 'crude', 'naphtha', 'poly', 'polyethylene', 'propylene', 'polypropylene',
			'procleaninjection', 'raw', 'natural', 'salesagp', 'saleslng', 'salessourgas' 'sourgas', 'sour', 'upper', 'zakum', 'urea',
			'lpg',
			'plan', 'planned', 'plant', 'actual', 'yesterday', 'today']

def convert_int2word(bot_response):
	bot_response_list = bot_response.split()
	for idx in bot_response_list:
		try:
			bot_response_list[bot_response_list.index(idx)] = num2words(int(idx))
		except ValueError:
			pass
	bot_response_string = ' '.join(map(str,bot_response_list))
	return bot_response_string

kernel = aiml.Kernel()
def load_kern(forcereload):
	if os.path.isfile("bot_brain.brn") and not forcereload:
		kernel.bootstrap(brainFile= "bot_brain.brn")
	else:
		kernel.bootstrap(learnFiles = os.path.abspath("aiml/startup.xml"), commands = "load aiml b")
		kernel.saveBrain("bot_brain.brn")

def ask(question):
	question = re.sub(r'[^\w\s\+]','',question)
	question = re.sub(r"(?<=\d)(st|nd|rd|th)\b", '', question)
	question = question.strip().lower()
	query_list = question.split(' ')
	
	try:
		now = parse(question, fuzzy=True)
		today1 = now.date()
		s = datetime.strptime("% s" % today1, "%Y-%m-%d")
		
	except:
		s = ' '
		pass

	db_query_flag = False
	for i in range(len(query_list)):
		if query_list[i] in db_query:
			db_query_flag = True
			break

	if db_query_flag == True or type(s) == datetime:
		bot_response = question_to_text(question)
		if bot_response.split(" ")[0].lower() == "unable":
			file = open("static/savechat/QueryList.txt", "r")
			lineList = file.readlines()
			file.close()

			if lineList[-1].split(":")[1].split(' ')[0].lower() == "unable" and lineList[-3].split(":")[1].split(' ')[
				0].lower() != "unable":
				appended_query = question + ' ' + lineList[-2].split(":")[1][:-1]
				bot_response = question_to_text(appended_query)
			if lineList[-1].split(":")[1].split(' ')[0].lower() == "unable" and lineList[-3].split(":")[1].split(' ')[
				0].lower() == "unable":
				appended_query = question + ' ' + lineList[-2].split(":")[1][:-1] + ' ' + \
								 lineList[-4].split(":")[1][:-1]
				bot_response = question_to_text(appended_query)

	else:
		if question in time_query:
			question = "what is the time now"
			bot_response = kernel.respond(question)
			if bot_response.rfind("?") == -1:
				bot_response = bot_response[bot_response.rfind(".")+2:]
			else:
				bot_response = bot_response[bot_response.rfind("?") + 2:]
		else:
			bot_response = kernel.respond(question)

	if bot_response in invalid_response:
		bot_response ="Sorry, I don't have answer to this question"

	if bot_response == "My name is Nameless.":
		bot_response = "My name is Shamsa."

	elif bot_response == ", I talk to people on the web. What do you do?":
		bot_response = "I talk to people on the web."

	elif bot_response == "I am in 's computer in . Where are you?" \
		or bot_response == "I am originally from . Now I live in . Where are you?" \
		or bot_response == "I am presently domiciled at .":
			bot_response = "I am in Abu Dhabi."

	elif bot_response == 'I was activated on  in .' \
		or bot_response == "I am  in human years." \
		or bot_response == "I was connected to the net on ." \
		or bot_response == 'I was first activated in .' \
		or bot_response == "I am  of your Earth years.":
			bot_response = "I am the product of over five years' research."

	elif bot_response == '':
		bot_response = "Sorry, I don't have answer to this question"

	file = open("static/savechat/QueryList.txt", "a+")
	file.write("\nQuery:" + question)
	file.write("\nBot:" + bot_response)
	file.close()

	return bot_response
	# if bot_response[-4:] == ".jpg":
	# 	return jsonify({'status': 'OK', 'answer': "Please click on below link",
	# 		 			'type': 'img', 'images': [bot_response]})
	# else:
	# 	bot_response_word = convert_int2word(bot_response)
	# 	return jsonify({"status": "ok", "answer": bot_response, "answer_word": bot_response_word})


trigger = ["shamsha", "Shamshad","Hi shamsha", "Hello shamsha","hi shamsha"]

def text_to_speech(bot_message):
	engine = pyttsx3.init()
	engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
	engine.say(bot_message)
	engine.runAndWait()
	engine.stop()

def recordAudio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		print("Say something!")
		audio = r.listen(source)
	try:
		data = r.recognize_google(audio)
		print("You said: " + data)
		return data
	except sr.UnknownValueError:
		data = "Sorry sir, but, I could not understand what you said!"
		return data
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))


if __name__ == "__main__":
	load_kern(False)
	print("Trying to always listen...")
	text_to_speech("Please say shamsha to activate me")
	data = ''

	start_listen_forever = True
	while start_listen_forever:
		start_listen = False
		while not start_listen:
			data = recordAudio()
			if data in trigger:
				start_listen = True
				text_to_speech("I am activate now, Please ask question")
			#time.sleep(1)

		while start_listen:
			data = recordAudio()
			if data == "Sorry sir, but, I could not understand what you said!":
				continue
			elif data == "exit":
				start_listen = False
				text_to_speech("I am deactivated, you can activate me saying shamsha")
				continue
			else:
				bot_response = ask(data)
				print(bot_response)
				bot_response_word = convert_int2word(bot_response)
				text_to_speech(bot_response_word)
			#time.sleep(1)
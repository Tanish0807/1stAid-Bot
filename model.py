import nltk
# nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

# import numpy
# import random
import json

# import pickle
# from keras.layers import *
# from keras.models import *

with open("intents.json") as file:
    data = json.load(file)

# print(data)


words = []
labels = []
docs_x = []
docs_y = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)  # ['What', 'to', 'do', 'if', 'Cuts', '?']
        #NLTK        wrds = pattern.split()  # ['What', 'to', 'do', 'if', 'Cuts', '?']
        words.extend(wrds)
        docs_x.append(wrds)  # input data (x)
        docs_y.append(intent["tag"])
    if intent["tag"] not in labels:
        labels.append(intent["tag"])  # all possible output data
#print(docs_x)
#print(docs_y)
docs_x = [['What', 'to', 'do', 'if', 'Cuts', '?'], ['How', 'to', 'cure', 'Cuts', '?'], ['Which', 'medicine', 'to', 'apply', 'for', 'Cuts', '?'], ['what', 'to', 'apply', 'on', 'cuts', '?'], ['Cuts'], ['how', 'do', 'you', 'treat', 'abrasions', '?'], ['Do', 'Abrasions', 'cause', 'scars', '?'], ['Abrasions'], ['what', 'to', 'do', 'if', 'abrasions', '?'], ['Which', 'medicine', 'to', 'apply', 'for', 'abrasions', '?'], ['How', 'to', 'cure', 'abrasions', '?'], ['How', 'do', 'you', 'treat', 'Sting', '?'], ['Stings'], ['What', 'to', 'do', 'if', 'you', 'get', 'a', 'sting', '?'], ['Which', 'medicine', 'to', 'apply', 'if', 'sting', '?'], ['How', 'to', 'remove', 'Splinters'], ['How', 'to', 'cure', 'Splinters', '?'], ['What', 'to', 'do', 'if', 'I', 'have', 'splinters', '?'], ['How', 'do', 'you', 'bring', 'a', 'splinter', 'to', 'the', 'surface', '?'], ['How', 'do', 'you', 'treat', 'a', 'sprain', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'sprain', '?'], ['Which', 'cream', 'to', 'apply', 'if', 'i', 'get', 'a', 'sprain', '?'], ['Which', 'medicine', 'to', 'apply', 'if', 'I', 'get', 'a', 'sprain', '?'], ['How', 'do', 'you', 'treat', 'a', 'strain', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'strain', '?'], ['Which', 'cream', 'to', 'apply', 'if', 'i', 'get', 'a', 'strain', '?'], ['Which', 'medicine', 'to', 'apply', 'if', 'I', 'get', 'a', 'strain', '?'], ['How', 'do', 'you', 'diagnose', 'a', 'strain', '?'], ['Is', 'heat', 'or', 'ice', 'better', 'for', 'a', 'pulled', 'muscle', '?'], ['How', 'do', 'you', 'treat', 'a', 'mild', 'Fever', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'mild', 'fever', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'a', 'mild', 'fever', '?'], ['fever'], ['How', 'do', 'you', 'treat', 'nasal', 'Congestion', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'nasal', 'congestion', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'have', 'a', 'nasal', 'congestion', '?'], ['what', 'to', 'do', 'if', 'i', 'have', 'a', 'blocked', 'nose', '?'], ['How', 'do', 'you', 'treat', 'a', 'blocked', 'nose', '?'], ['How', 'long', 'does', 'nasal', 'congestion', 'last', '?'], ['How', 'to', 'cure', 'cough', '?'], ['How', 'do', 'you', 'treat', 'cough', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'cough', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'cough', '?'], ['How', 'do', 'you', 'get', 'rid', 'of', 'cough', '?'], ['How', 'do', 'you', 'treat', 'sore', 'throat', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'sore', 'throat', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'a', 'sore', 'throat', '?'], ['How', 'to', 'cure', 'sore', 'throat', '?'], ['How', 'do', 'you', 'treat', 'gas', 'problems', '?'], ['what', 'to', 'do', 'if', 'i', 'have', 'Gastrointestinal', 'problems', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'gas', 'problem', '?'], ['How', 'to', 'cure', 'Gas', 'problems', '?'], ['How', 'do', 'you', 'treat', 'Skin', 'problems', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'skin', 'allergy', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'a', 'skin', 'allergy', '?'], ['How', 'to', 'cure', 'skin', 'allergy', '?'], ['How', 'do', 'you', 'treat', 'Abdonominal', 'Pain', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'Abdonominal', 'Pain', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'a', 'Abdonominal', 'Pain', '?'], ['How', 'to', 'cure', 'Abdonominal', 'Pain', '?'], ['How', 'do', 'you', 'treat', 'Bruises', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'Bruise', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'a', 'Bruise', '?'], ['How', 'to', 'cure', 'Bruises', '?'], ['How', 'do', 'you', 'treat', 'a', 'Broken', 'Toe', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'Broken', 'Toe', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'a', 'Broken', 'Toe', '?'], ['How', 'to', 'cure', 'Broken', 'Toe', '?'], ['How', 'do', 'you', 'treat', 'Choking', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'Choke', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'Choked', '?'], ['How', 'to', 'cure', 'Choking', '?'], ['How', 'do', 'you', 'treat', 'a', 'wound', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'Wound', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'wounded', '?'], ['How', 'to', 'cure', 'a', 'wound', '?'], ['How', 'do', 'you', 'treat', 'Diarrhea', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'Diarrhea', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'Diarrhea', '?'], ['How', 'to', 'cure', 'Diarrhea', '?'], ['How', 'do', 'you', 'treat', 'a', 'Frost', 'bite', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'Frost', 'bite', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'a', 'Frost', 'bite', '?'], ['How', 'to', 'cure', 'Frost', 'bite', '?'], ['How', 'do', 'you', 'treat', 'Heat', 'Exhaustion', '?'], ['what', 'to', 'do', 'if', 'i', 'feel', 'Exhausted', 'due', 'to', 'heat', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'Exhausted', '?'], ['How', 'to', 'cure', 'Heat', 'Exhaustion', '?'], ['How', 'do', 'you', 'treat', 'Heat', 'Stroke', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'Heat', 'Stroke', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'Stroke', '?'], ['How', 'to', 'cure', 'a', 'Heat', 'Stroke', '?'], ['How', 'do', 'you', 'treat', 'a', 'Insect', 'Bite', '?'], ['what', 'to', 'do', 'if', 'a', 'insect', 'bites', 'me', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'bitten', 'by', 'a', 'insect', '?'], ['How', 'to', 'cure', 'insect', 'bite', '?'], ['How', 'do', 'you', 'treat', 'a', 'bleeding', 'nose', '?'], ['what', 'to', 'do', 'if', 'i', 'my', 'nose', 'is', 'bleeding', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'nose', 'bleed', '?'], ['How', 'to', 'cure', 'nose', 'bleeding', '?'], ['How', 'do', 'you', 'treat', 'a', 'Pulled', 'Muscle', '?'], ['what', 'to', 'do', 'if', 'my', 'muscle', 'is', 'pulled', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'got', 'pulled', 'muscle', '?'], ['How', 'to', 'cure', 'a', 'pulled', 'muscle', '?'], ['How', 'do', 'you', 'treat', 'Rectal', 'Bleeding', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'Rectal', 'Bleeding', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'Rectal', 'Bleeding', '?'], ['How', 'to', 'cure', 'Rectal', 'Bleeding', '?'], ['How', 'do', 'you', 'treat', 'Sun', 'Burn', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'Sun', 'Burn', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'Sun', 'Burn', '?'], ['How', 'to', 'cure', 'a', 'Sun', 'Burn', '?'], ['How', 'do', 'you', 'treat', 'Testicle', 'Pain', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'Testicle', 'Pain', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'a', 'Testicle', 'Pain', '?'], ['How', 'to', 'cure', 'Testicle', 'Pain', '?'], ['How', 'do', 'you', 'treat', 'a', 'Vertigo', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'Vertigo', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'Vertigo', '?'], ['How', 'to', 'cure', 'a', 'Vertigo', '?'], ['How', 'do', 'you', 'treat', 'bleeding', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'Bleeding', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'bleeding', '?'], ['How', 'to', 'cure', 'Bleeding', '?'], ['How', 'do', 'you', 'treat', 'an', 'eye', 'Injury', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'eye', 'Injury', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'injured', 'my', 'eye', '?'], ['How', 'to', 'cure', 'injured', 'eye', '?'], ['How', 'do', 'you', 'treat', 'a', 'chemical', 'burn', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'Chemical', 'Burn', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'burn', 'due', 'to', 'chemicals', '?'], ['How', 'to', 'cure', 'Chemical', 'Burn', '?'], ['How', 'do', 'you', 'treat', 'a', 'Poison', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'Poison', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'am', 'poisoned', '?'], ['How', 'to', 'cure', 'Poisoning', '?'], ['How', 'do', 'you', 'treat', 'broken', 'Teeth', '?'], ['what', 'to', 'do', 'if', 'my', 'Teeth', 'got', 'broken', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'broken', 'teeth', '?'], ['cure', 'broken', 'teeth', '?'], ['How', 'do', 'you', 'treat', 'a', 'seizure', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'seizure', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'seizure', '?'], ['How', 'to', 'cure', 'seizure', '?'], ['How', 'do', 'you', 'treat', 'a', 'head', 'Injury', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'Head', 'Injury', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'injured', 'in', 'the', 'head', '?'], ['How', 'to', 'cure', 'Head', 'Injury', '?'], ['How', 'do', 'you', 'treat', 'Faint', '?'], ['what', 'to', 'do', 'if', 'i', 'feel', 'like', 'Fainting', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'a', 'Faint', '?'], ['How', 'to', 'cure', 'Fainting', '?'], ['How', 'do', 'you', 'treat', 'a', 'mild', 'Headache', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'mild', 'Headache', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'have', 'a', 'mild', 'headache', '?'], ['How', 'to', 'cure', 'a', 'mild', 'headache', '?'], ['How', 'do', 'you', 'treat', 'a', 'Cold', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'mild', 'Cold', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'have', 'a', 'Cold', '?'], ['How', 'to', 'cure', 'Cold', '?'], ['How', 'do', 'you', 'treat', 'Rashes', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'Rash', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'have', 'a', 'Rash', '?'], ['How', 'to', 'cure', 'Rash', '?'], ['How', 'do', 'you', 'treat', 'a', 'snake', 'bite', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'snake', 'bite', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'a', 'snake', 'bite', '?'], ['How', 'to', 'cure', 'snake', 'bite', '?'], ['i', 'got', 'bit', 'by', 'a', 'snake'], ['How', 'do', 'you', 'treat', 'a', 'animal', 'bite', '?'], ['How', 'do', 'you', 'treat', 'a', 'monkey', 'bite', '?'], ['How', 'do', 'you', 'treat', 'a', 'dog', 'bite', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'animal', 'bite', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'get', 'a', 'monekey', 'bite', '?'], ['How', 'to', 'cure', 'dog', 'bite', '?'], ['i', 'got', 'bit', 'by', 'a', 'dog'], ['What', 'to', 'do', 'if', 'someone', 'is', 'Drowning', '?'], ['what', 'to', 'do', 'if', 'someone', 'drowned', '?'], ['What', 'steps', 'to', 'take', 'if', 'i', 'see', 'a', 'drowning', 'person', '?'], ['How', 'to', 'help', 'a', 'drowning', 'person', '?'], ['How', 'to', 'give', 'CPR', '?', '?'], ['what', 'to', 'do', 'in', 'a', 'CPR', '?'], ['What', 'steps', 'to', 'take', 'in', 'a', 'CPR', '?', '?'], ['How', 'to', 'help', 'a', 'drowning', 'person', 'in', 'CPR', '?'], ['How', 'do', 'you', 'treat', 'a', 'Fracture', '?'], ['what', 'to', 'do', 'if', 'i', 'get', 'a', 'Fracture', '?'], ['Which', 'medicine', 'to', 'take', 'if', 'I', 'have', 'a', 'Fracture', '?'], ['How', 'to', 'cure', 'a', 'Fracture', '?']]
docs_y = ['Cuts', 'Cuts', 'Cuts', 'Cuts', 'Cuts', 'Abrasions', 'Abrasions', 'Abrasions', 'Abrasions', 'Abrasions', 'Abrasions', 'stings', 'stings', 'stings', 'stings', 'Splinter', 'Splinter', 'Splinter', 'Splinter', 'Sprains', 'Sprains', 'Sprains', 'Sprains', 'Strains', 'Strains', 'Strains', 'Strains', 'Strains', 'Strains', 'Fever', 'Fever', 'Fever', 'Fever', 'Nasal Congestion', 'Nasal Congestion', 'Nasal Congestion', 'Nasal Congestion', 'Nasal Congestion', 'Nasal Congestion', 'Cough', 'Cough', 'Cough', 'Cough', 'Cough', 'Sore Throat', 'Sore Throat', 'Sore Throat', 'Sore Throat', 'Gastrointestinal problems', 'Gastrointestinal problems', 'Gastrointestinal problems', 'Gastrointestinal problems', 'Skin problems', 'Skin problems', 'Skin problems', 'Skin problems', 'Abdonominal Pain', 'Abdonominal Pain', 'Abdonominal Pain', 'Abdonominal Pain', 'Bruises', 'Bruises', 'Bruises', 'Bruises', 'Broken Toe', 'Broken Toe', 'Broken Toe', 'Broken Toe', 'Choking', 'Choking', 'Choking', 'Choking', 'Wound', 'Wound', 'Wound', 'Wound', 'Diarrhea', 'Diarrhea', 'Diarrhea', 'Diarrhea', 'Frost bite', 'Frost bite', 'Frost bite', 'Frost bite', 'Heat Exhaustion', 'Heat Exhaustion', 'Heat Exhaustion', 'Heat Exhaustion', 'Heat Stroke', 'Heat Stroke', 'Heat Stroke', 'Heat Stroke', 'Insect Bites', 'Insect Bites', 'Insect Bites', 'Insect Bites', 'nose bleed', 'nose bleed', 'nose bleed', 'nose bleed', 'Pulled Muscle', 'Pulled Muscle', 'Pulled Muscle', 'Pulled Muscle', 'Rectal bleeding', 'Rectal bleeding', 'Rectal bleeding', 'Rectal bleeding', 'Sun Burn', 'Sun Burn', 'Sun Burn', 'Sun Burn', 'Testicle Pain', 'Testicle Pain', 'Testicle Pain', 'Testicle Pain', 'Vertigo', 'Vertigo', 'Vertigo', 'Vertigo', 'Normal Bleeding', 'Normal Bleeding', 'Normal Bleeding', 'Normal Bleeding', 'Eye Injury', 'Eye Injury', 'Eye Injury', 'Eye Injury', 'Chemical Burn', 'Chemical Burn', 'Chemical Burn', 'Chemical Burn', 'Poison', 'Poison', 'Poison', 'Poison', 'Teeth', 'Teeth', 'Teeth', 'Teeth', 'seizure', 'seizure', 'seizure', 'seizure', 'Head Injury', 'Head Injury', 'Head Injury', 'Head Injury', 'Fainting', 'Fainting', 'Fainting', 'Fainting', 'Headache', 'Headache', 'Headache', 'Headache', 'Cold', 'Cold', 'Cold', 'Cold', 'Rash', 'Rash', 'Rash', 'Rash', 'snake bite', 'snake bite', 'snake bite', 'snake bite', 'snake bite', 'animal bite', 'animal bite', 'animal bite', 'animal bite', 'animal bite', 'animal bite', 'animal bite', 'Drowning', 'Drowning', 'Drowning', 'Drowning', 'CPR', 'CPR', 'CPR', 'CPR', 'Fracture', 'Fracture', 'Fracture', 'Fracture']
words = [stemmer.stem(w.lower()) for w in words if w != "?"]
#words = ['what', 'to', 'do', 'if', 'cut', 'how', 'to', 'cur', 'cut', 'which', 'medicin', 'to', 'apply', 'for', 'cut', 'what', 'to', 'apply', 'on', 'cut', 'cut', 'how', 'do', 'you', 'tre', 'abra', 'do', 'abra', 'cau', 'scar', 'abra', 'what', 'to', 'do', 'if', 'abra', 'which', 'medicin', 'to', 'apply', 'for', 'abra', 'how', 'to', 'cur', 'abra', 'how', 'do', 'you', 'tre', 'sting', 'sting', 'what', 'to', 'do', 'if', 'you', 'get', 'a', 'sting', 'which', 'medicin', 'to', 'apply', 'if', 'sting', 'how', 'to', 'remov', 'splinters', 'how', 'to', 'cur', 'splinters', 'what', 'to', 'do', 'if', 'i', 'hav', 'splinters', 'how', 'do', 'you', 'bring', 'a', 'splinter', 'to', 'the', 'surfac', 'how', 'do', 'you', 'tre', 'a', 'sprain', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'sprain', 'which', 'cream', 'to', 'apply', 'if', 'i', 'get', 'a', 'sprain', 'which', 'medicin', 'to', 'apply', 'if', 'i', 'get', 'a', 'sprain', 'how', 'do', 'you', 'tre', 'a', 'strain', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'strain', 'which', 'cream', 'to', 'apply', 'if', 'i', 'get', 'a', 'strain', 'which', 'medicin', 'to', 'apply', 'if', 'i', 'get', 'a', 'strain', 'how', 'do', 'you', 'diagno', 'a', 'strain', 'is', 'heat', 'or', 'ic', 'bet', 'for', 'a', 'pul', 'musc', 'how', 'do', 'you', 'tre', 'a', 'mild', 'fev', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'mild', 'fev', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'a', 'mild', 'fev', 'fev', 'how', 'do', 'you', 'tre', 'nas', 'congest', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'nas', 'congest', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'hav', 'a', 'nas', 'congest', 'what', 'to', 'do', 'if', 'i', 'hav', 'a', 'block', 'nos', 'how', 'do', 'you', 'tre', 'a', 'block', 'nos', 'how', 'long', 'doe', 'nas', 'congest', 'last', 'how', 'to', 'cur', 'cough', 'how', 'do', 'you', 'tre', 'cough', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'cough', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'cough', 'how', 'do', 'you', 'get', 'rid', 'of', 'cough', 'how', 'do', 'you', 'tre', 'sor', 'throat', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'sor', 'throat', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'a', 'sor', 'throat', 'how', 'to', 'cur', 'sor', 'throat', 'how', 'do', 'you', 'tre', 'gas', 'problem', 'what', 'to', 'do', 'if', 'i', 'hav', 'gastrointestin', 'problem', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'gas', 'problem', 'how', 'to', 'cur', 'gas', 'problem', 'how', 'do', 'you', 'tre', 'skin', 'problem', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'skin', 'allergy', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'a', 'skin', 'allergy', 'how', 'to', 'cur', 'skin', 'allergy', 'how', 'do', 'you', 'tre', 'abdonomin', 'pain', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'abdonomin', 'pain', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'a', 'abdonomin', 'pain', 'how', 'to', 'cur', 'abdonomin', 'pain', 'how', 'do', 'you', 'tre', 'bru', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'bru', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'a', 'bru', 'how', 'to', 'cur', 'bru', 'how', 'do', 'you', 'tre', 'a', 'brok', 'toe', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'brok', 'toe', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'a', 'brok', 'toe', 'how', 'to', 'cur', 'brok', 'toe', 'how', 'do', 'you', 'tre', 'chok', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'chok', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'chok', 'how', 'to', 'cur', 'chok', 'how', 'do', 'you', 'tre', 'a', 'wound', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'wound', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'wound', 'how', 'to', 'cur', 'a', 'wound', 'how', 'do', 'you', 'tre', 'diarrh', 'what', 'to', 'do', 'if', 'i', 'get', 'diarrh', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'diarrh', 'how', 'to', 'cur', 'diarrh', 'how', 'do', 'you', 'tre', 'a', 'frost', 'bit', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'frost', 'bit', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'a', 'frost', 'bit', 'how', 'to', 'cur', 'frost', 'bit', 'how', 'do', 'you', 'tre', 'heat', 'exhaust', 'what', 'to', 'do', 'if', 'i', 'feel', 'exhaust', 'due', 'to', 'heat', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'exhaust', 'how', 'to', 'cur', 'heat', 'exhaust', 'how', 'do', 'you', 'tre', 'heat', 'stroke', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'heat', 'stroke', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'stroke', 'how', 'to', 'cur', 'a', 'heat', 'stroke', 'how', 'do', 'you', 'tre', 'a', 'insect', 'bit', 'what', 'to', 'do', 'if', 'a', 'insect', 'bit', 'me', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'bit', 'by', 'a', 'insect', 'how', 'to', 'cur', 'insect', 'bit', 'how', 'do', 'you', 'tre', 'a', 'ble', 'nos', 'what', 'to', 'do', 'if', 'i', 'my', 'nos', 'is', 'ble', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'nos', 'ble', 'how', 'to', 'cur', 'nos', 'ble', 'how', 'do', 'you', 'tre', 'a', 'pul', 'musc', 'what', 'to', 'do', 'if', 'my', 'musc', 'is', 'pul', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'got', 'pul', 'musc', 'how', 'to', 'cur', 'a', 'pul', 'musc', 'how', 'do', 'you', 'tre', 'rect', 'ble', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'rect', 'ble', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'rect', 'ble', 'how', 'to', 'cur', 'rect', 'ble', 'how', 'do', 'you', 'tre', 'sun', 'burn', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'sun', 'burn', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'sun', 'burn', 'how', 'to', 'cur', 'a', 'sun', 'burn', 'how', 'do', 'you', 'tre', 'test', 'pain', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'test', 'pain', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'a', 'test', 'pain', 'how', 'to', 'cur', 'test', 'pain', 'how', 'do', 'you', 'tre', 'a', 'vertigo', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'vertigo', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'vertigo', 'how', 'to', 'cur', 'a', 'vertigo', 'how', 'do', 'you', 'tre', 'ble', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'ble', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'ble', 'how', 'to', 'cur', 'ble', 'how', 'do', 'you', 'tre', 'an', 'ey', 'injury', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'ey', 'injury', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'ind', 'my', 'ey', 'how', 'to', 'cur', 'ind', 'ey', 'how', 'do', 'you', 'tre', 'a', 'chem', 'burn', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'chem', 'burn', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'burn', 'due', 'to', 'chem', 'how', 'to', 'cur', 'chem', 'burn', 'how', 'do', 'you', 'tre', 'a', 'poison', 'what', 'to', 'do', 'if', 'i', 'get', 'poison', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'am', 'poison', 'how', 'to', 'cur', 'poison', 'how', 'do', 'you', 'tre', 'brok', 'tee', 'what', 'to', 'do', 'if', 'my', 'tee', 'got', 'brok', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'brok', 'tee', 'cur', 'brok', 'tee', 'how', 'do', 'you', 'tre', 'a', 'seiz', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'seiz', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'seiz', 'how', 'to', 'cur', 'seiz', 'how', 'do', 'you', 'tre', 'a', 'head', 'injury', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'head', 'injury', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'ind', 'in', 'the', 'head', 'how', 'to', 'cur', 'head', 'injury', 'how', 'do', 'you', 'tre', 'faint', 'what', 'to', 'do', 'if', 'i', 'feel', 'lik', 'faint', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'a', 'faint', 'how', 'to', 'cur', 'faint', 'how', 'do', 'you', 'tre', 'a', 'mild', 'headach', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'mild', 'headach', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'hav', 'a', 'mild', 'headach', 'how', 'to', 'cur', 'a', 'mild', 'headach', 'how', 'do', 'you', 'tre', 'a', 'cold', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'mild', 'cold', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'hav', 'a', 'cold', 'how', 'to', 'cur', 'cold', 'how', 'do', 'you', 'tre', 'rash', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'rash', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'hav', 'a', 'rash', 'how', 'to', 'cur', 'rash', 'how', 'do', 'you', 'tre', 'a', 'snak', 'bit', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'snak', 'bit', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'a', 'snak', 'bit', 'how', 'to', 'cur', 'snak', 'bit', 'i', 'got', 'bit', 'by', 'a', 'snak', 'how', 'do', 'you', 'tre', 'a', 'anim', 'bit', 'how', 'do', 'you', 'tre', 'a', 'monkey', 'bit', 'how', 'do', 'you', 'tre', 'a', 'dog', 'bit', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'anim', 'bit', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'get', 'a', 'monekey', 'bit', 'how', 'to', 'cur', 'dog', 'bit', 'i', 'got', 'bit', 'by', 'a', 'dog', 'what', 'to', 'do', 'if', 'someon', 'is', 'drown', 'what', 'to', 'do', 'if', 'someon', 'drown', 'what', 'step', 'to', 'tak', 'if', 'i', 'see', 'a', 'drown', 'person', 'how', 'to', 'help', 'a', 'drown', 'person', 'how', 'to', 'giv', 'cpr', 'what', 'to', 'do', 'in', 'a', 'cpr', 'what', 'step', 'to', 'tak', 'in', 'a', 'cpr', 'how', 'to', 'help', 'a', 'drown', 'person', 'in', 'cpr', 'how', 'do', 'you', 'tre', 'a', 'fract', 'what', 'to', 'do', 'if', 'i', 'get', 'a', 'fract', 'which', 'medicin', 'to', 'tak', 'if', 'i', 'hav', 'a', 'fract', 'how', 'to', 'cur', 'a', 'fract']
#words = [w.lower() for w in words if w != "?"]
#print([stemmer.stem(w.lower()) for w in words if w != "?"])
#print(len([w.lower() for w in words if w != "?"]))
words = sorted(list(set(words)))

labels = sorted(labels)

# print(wrds)
# print(words)
# print(docs_x)
# print(docs_y)
# print(labels)

training = []
output = []

out_empty = [0 for _ in range(len(labels))]  # [1,2,3] [0,0,0]

for x, doc in enumerate(docs_x):

    bag = []

    #wrds = [stemmer.stem(w) for w in doc]  # doc = ['What', 'to', 'do', 'if', 'Cuts', '?']   &    wrds = ['What', 'to', 'do', 'if', 'Cut', '?']
    wrds = [w for w in doc]

    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)
    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1

    training.append(bag)
    output.append(output_row)

# print(training[0])
# print(output[0])
# print(words)
# print(len(output[0]))
# print(len(training[0]))



from keras.models import load_model
model = load_model("First_Aid_model.h5")


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    tan = [0 for _ in range(len(words))]
    #s_words = nltk.word_tokenize(s)
    s_words = s.split()
    #print([stemmer.stem(word.lower()) for word in s_words])
    #print([word.lower() for word in s_words])
    fake_words = [stemmer.stem(word.lower()) for word in s_words]
    #print(s_words)
    tanish_words = [word.lower() for word in s_words]

    for se in fake_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
    #print([bag])
    #return bag
    return bag
    for se in tanish_words:
        for i, w in enumerate(words):
            if w == se:
                tan[i] = 1
    #print([tan])
    #return tan


# Chatbot
def chat(inp):
    # print("Start Talking with the bot(type quit to stop!")
    # while True:
    # inp = input("You: ")
    # if inp.lower() == "quit":
    # break
#    return inp
    global responses
    results = model.predict([bag_of_words(inp, words)])
    # print(results)
    result = results[0]
    # results_index = numpy.argmax(result)
    result = list(result)
    results_index = result.index(max(result))
    # results_index = result
    tag = labels[results_index]
    # print(results_index)

    if result[results_index] > 0.5:
        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
        # print(random.choice(responses))
        # res = random.choice(responses).split('. ')
        # responses = array(responses)
        res = responses[0].split('. ')
        res = [res[_] + '.' for _ in range(len(res)) if not res[_].endswith('.')]
        res = '\n'.join(res)

        return res + "\n"
    # return responses[0]

    else:
        return "I didn't get that, try again"

        # chat()
        # print(bag_of_words('Fracture',words))

print(bag_of_words('Cuts', words))
print(type(model.predict([bag_of_words('Cuts', words)])))
print(chat('Cuts'))
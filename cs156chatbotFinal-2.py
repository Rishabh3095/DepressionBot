"""
CS156 DEPRESSION/DIAGNOSIS CHATBOT

Blanchy Polangcos
Daksha Divakar
Rishabh Gupta
Shweta More

CONTENTS OF THIS CLASS:
    
    - DECISION TREE (line 25)
    - MAIN CHATBOT (line 547)
    - FRAME REPRESENTATION CLASS (line 282)

"""

import random
import sys

"""
############################DECISION TREE
"""
from math import log

#The data set we are using
#Suicidal, Emotions, Social, Duration, Age, Physical, Output

#[age (youth/adult/elderly), 
            #sucidal (yes/no), 
            #emotions (sad/happy/neutral), 
            #social (lonely/stressed/stressed), 
            #duration (-2weeks/+2weeks), 
            #physical (tired/not tired), 
            #output (depression/none)]
            
#sample dataset we are using
            
dataset = [['youth', 'yes', 'sad', 'lonely', '+2weeks', 'tired', 'depression'],
        ['youth', 'yes', 'sad', 'lonely', '+2weeks', 'not tired', 'depression'],
        ['adult', 'no', 'happy', 'lonely', '+2weeks', 'not tired', 'no depression'],
    ['youth', 'yes', 'sad', 'stressed', '+2weeks', 'tired', 'depression'],
    ['youth', 'yes', 'sad', 'stressed', '-2weeks', 'tired', 'depression'],
    ['youth', 'no', 'sad', 'lonely', '+2weeks', 'tired', 'depression'],
    ['youth', 'yes', 'sad', 'stressed', '-2weeks', 'tired', 'depression'],
    ['adult', 'yes', 'sad', 'lonely', '+2weeks', 'tired', 'depression'],
    ['youth', 'no', 'happy', 'stressed', '+2weeks', 'tired', 'no depression'],
    ['youth', 'no', 'neutral', 'not stressed', '+2weeks', 'tired', 'no depression'],
    ['youth', 'no', 'happy', 'stressed', '-2weeks', 'tired', 'no depression'],
    ['adult', 'yes', 'sad', 'lonely', '+2weeks', 'not tired', 'depression'],
    ['adult', 'yes', 'sad', 'lonely', '-2weeks', 'not tired', 'depression'],
    ['adult', 'yes', 'sad', 'stressed', '+2weeks', 'tired', 'depression'],
    ['adult', 'no', 'sad', 'lonely', '+2weeks', 'tired', 'depression'],
    ['adult', 'yes', 'sad', 'stressed', '-2weeks', 'not tired', 'depression'],
    ['adult', 'yes', 'sad', 'stressed', '+2weeks', 'not tired', 'depression'],
    ['youth', 'no', 'sad', 'stressed', '-2weeks', 'not tired', 'no depression'],
    ['adult', 'no', 'sad', 'lonely', '-2weeks', 'not tired', 'no depression'],
    ['adult', 'yes', 'sad', 'stressed', '-2weeks', 'not tired', 'depression'],
    ['adult', 'no', 'sad', 'stressed', '+2weeks', 'tired', 'depression'],
    ['adult', 'no', 'sad', 'lonely', '+2weeks', 'tired', 'depression'],
    ['elderly', 'yes', 'sad', 'lonely', '+2weeks', 'tired', 'depression'],
    ['elderly', 'yes', 'sad', 'lonely', '-2weeks', 'tired', 'depression'],
    ['elderly', 'yes', 'sad', 'stressed', '+2weeks', 'not tired', 'depression'],
    ['elderly', 'no', 'sad', 'lonely', '+2weeks', 'tired', 'depression'],
    ['elderly', 'yes', 'sad', 'stressed', '+2weeks', 'tired', 'depression'],
    ['youth', 'no', 'sad', 'stressed', '-2weeks', 'not tired', 'no depression'],
    ['elderly', 'yes', 'sad', 'lonely', '+2weeks', 'not tired', 'depression'],
    ['elderly', 'yes', 'sad', 'stressed', '-2weeks', 'tired', 'depression'],
    ['youth', 'no', 'neutral', 'stressed', '-2weeks', 'not tired', 'no depression'],
    ['adult', 'no', 'sad', 'lonely', '+2weeks', 'not tired', 'no depression'],
    ['adult', 'no', 'neutral', 'lonely', '-2weeks', 'not tired', 'no depression'],
    ['youth', 'yes', 'sad', 'lonely', '-2weeks', 'not tired', 'depression'],
    ['adult', 'no', 'happy', 'stressed', '+2weeks', 'not tired', 'no depression'],
    ['adult', 'no', 'happy', 'stressed', '-2weeks', 'tired', 'no depression'],
    ['adult', 'no', 'sad', 'stressed', '-2weeks', 'not tired', 'no depression'],
    ['elderly', 'no', 'sad', 'lonely', '-2weeks', 'not tired', 'no depression'],
    ['elderly', 'no', 'happy', 'stressed', '-2weeks', 'tired', 'no depression'],
    ['elderly', 'no', 'neutral', 'stressed', '+2weeks', ' not tired', 'no depression'],
    ['elderly', 'no', 'sad', 'stressed', '-2weeks', 'not tired', 'no depression'],
    ['elderly', 'no', 'happy', 'lonely', '+2weeks', 'tired', 'no depression'],
    ['elderly', 'no', 'happy', 'stressed', '+2weeks', 'not tired', 'no depression'],
    ['elderly', 'no', 'happy', 'stressed', '-2weeks', 'tired', 'no depression'],
    ['elderly', 'no', 'neutral', 'lonely', '+2weeks', 'not tired', 'no depression']]
    
testdata=[['youth','yes','sad','lonely','Less than 2 weeks','tired','depression'],
        ['adulYt','no','sad','stress','Less than 2 weeks','not tired','None'],
        ['elderly','no','happy','lonely','More than two weeks','tired','depression'],
        ['youth','yes','anxiety','stress','More than two weeks','tired','None'],
        ['adult','yes','sad','lonely','Less than 2 weeks','not tired','depression'],
        ['elderly','yes','anxiety','none','More than two weeks','tired','None'],
        ['youth','no','happy','none','Less than 2 weeks','tired','None'],
        ['adult','no','happy','lonely','More than two weeks','not tired','depression'],
        ['elderly','yes','sad','lonely','More than two weeks','tired','None'],
        ['youth','no','happy','stress','Less than 2 weeks','not tired','depression'],
        ['adult','no','anxiety','none','More than two weeks','tired','None'],
        ['elderly','yes','anxiety','lonely','Less than 2 weeks','tired','None'],
        ['youth','yes','sad','lonely','More than two weeks','not tired','None'],
        ['adult','yes','sad','stress','Less than 2 weeks','tired','depression'],
        ['elderly','no','anxiety','stress','More than two weeks','not tired','None'],
        ['youth','no','happy','stress','Less than 2 weeks','tired','depression']]
        
        
spCount = 0
subCount = 0
#finalGain = 0.0
#caseChosen = None
#finalList = None
                                
class decTrs():

 def __init__(self, columnNumber = -1, child = None, lstChosen = None, leftNode = None, rightNode = None):
        self.columnNumber=columnNumber # columnNumberumn index of criteria being tested
        self.child=child 
        self.lstChosen=lstChosen # dict of lstChosen for a branch, None for everything except endpoints
        self.leftNode=leftNode # true decision nodes 
        self.rightNode=rightNode # false decision nodes
        
#supporter function for split function
def ischeckNominal(row, column, value):
      
      if row[column]==value:
        return True
      else:
          return False

# Splits a dataset on the specific value using the column number.
def split(dataset,column,value):
        
    sp = []
    sub = []
    
    for row in dataset:

        check = ischeckNominal(row, column, value) 

        if check:
            global spCount
            sp.insert(spCount, row)
            spCount = spCount + 1
        else:
            global subCount
            sub.insert(subCount, row)
            subCount = subCount + 1
    return (sp,sub)
    
#give the total amount of times the output comes
def resultsTotalCount(dataset):
   
    results=[]
   
    for row in dataset:
        new = []
        worth = True
        lastElement = row[len(row)-1]
        check = False
        for data in results:
            if not results:
                new.insert(0,lastElement)
                new.insert(1,1)
                check = True
            elif lastElement in data: 
                data[1] = data[1]+1
                check = True
                worth=False
        if check == False:
            new.insert(0,lastElement)
            new.insert(1,1)
        
        if worth:   
            results.append(new)        
    return results

# Entropy = prob(x)[log(prob(x))]
#sample input to check when the entropy will be zero and when it will be one.
one = [['t', 'p'], ['t', 'p'], ['t', 's'], ['t', 's']]
zero = [['t', 'p'], ['t', 'p'], ['t', 'p'], ['t', 'p']]

def suppEntropy(x):
    possib = (log(x)/log(2))
    return x*possib

def entropy(dataset):

    results=resultsTotalCount(dataset)    
    entropyValue = 0.0
    for lists in results:
        # considering probability of occurance of every possible output
        prob = float(lists[1])/len(dataset)
        entropyValue = entropyValue - suppEntropy(prob)
        
    return entropyValue
    
# uses the same algo as entropy to find the information gain
def informationGain(dataset, childEqual, childNotEqual):
    prob = float(len(childEqual)) / len(dataset)
    totalGain = entropy(dataset) - prob*entropy(childEqual) - (1-prob)*entropy(childNotEqual)
    return totalGain
    
#this is the main method. It finds the information gain of the specific values and returns
#and checks if the final gain is less that that and replaces it occordingly.
#According the cases and the final list is set and passed into the decTrs().
def decisionTree(dataset):

    finalGain = 0.0
    caseChosen = None
    finalList = None
    
    if len(dataset) == 0: 
        return decTrs()
    else:                                    
        for i in range(0, len(dataset[0]) - 1):
            
            for row in dataset:
                count = 0
                for line in row:
                    childList = []
                    childList.insert(count, line)
                    count += 1
    
                    for value in childList:
                        (childEqual, childNotEqual) = split(dataset, i, value)
                        
                        totalGain = informationGain(dataset, childEqual, childNotEqual)
                        
#                        global finalGain
 #                     global caseChosen
  #                  global finalList
                        
                        if len(childEqual) != 0 and totalGain  > finalGain and len(childNotEqual) != 0 and len(childEqual) > 0 and len(childNotEqual) > 0:
                        
                            finalGain = totalGain 
                            caseChosen = (i, value)
                            finalList = (childEqual, childNotEqual)
    
        if finalGain != 0 and finalGain > 0:
            
            nodeOnLeft = decisionTree(finalList[0])
            nodeOnRight = decisionTree(finalList[1])
            
            return decTrs(columnNumber = caseChosen[0], child = caseChosen[1], leftNode = nodeOnLeft, rightNode = nodeOnRight)
        else:
            return decTrs(lstChosen = resultsTotalCount(dataset))
            
#This builds the tree in the node form and evaluates the user input to give an answer as 'depression' and 'not depression'
def evaluate(tree, row):

    if tree.lstChosen!=None:
        return tree.lstChosen[0][0]
    else:
        # Print the criteria
        if row[tree.columnNumber] == tree.child:
            return evaluate(tree.leftNode, row)
        else:
            return evaluate(tree.rightNode, row)
            
#evaluates data sent from chatbot
def fromChat(data):
    global dataset
    tree = decisionTree(dataset)
#    size = len(dataset)
    return evaluate(tree, data)
#    return evaluate(decisionTree(dataset), data)

"""Knowledge representation: Frame Based"""
"""
Generic frame: Mental illness
Individual frame: Depression, Anxiety, Insomnia
"""

"***************************************** frame based kb module *****************************************"

              
class Person:
    def __init__(self):
        "constructor"
    "slot1 = Name , filler = name (string)"
    def Name(self,name):
            self.Name = str(name)
    "slot2 = Age , filler = age (int)"
    #attribute number 1
    def Age(self,age):
        if age.int() < 19:
           self.age = 'youth'
        elif self.age < 51:
           self.age = 'adult'
        else:
            self.age = 'senior'
    "slot3 = Gender, filler = gender (string): F,M"
    def Gender(self,gender):
        def IF_ADDED(gender):
            if gender.lower() == 'male':
                return 'M'
            elif gender.lower() == 'female':
                return 'F'
            self.Gender = str(IF_ADDED(gender))
     
class Patient(Person):
    def __init__(self):
        self.is_a = []
        self.is_a.append(Person)        
        self.as_instance = {}
        self.symptoms = []
    "slot1 = IS_A, filler = frame (<class>)"
    def IS_A(self,frame):
        self.is_a.append(frame)
    "slot2 = IS_A, filler = frame (<class>)"
    def AS_INSTANCE(self, frame):
        "{ClassName : ClassInstance (Class())}"
        self.as_instance[frame.__name__] = frame()
    "slot3 = Symptoms , filler = symptom (Symptom)"
    def Symptoms(self,symptom):
        if isinstance(symptom, Symptom):
            self.symptoms.append(symptom)

        
"Generic frame"
class TherapyPatient:
    def __init__(self):
        "list of Condition objects"
        self.diagnosis = []
        self.as_instance = {}
    "slot1 = IS_A, filler = frame (<class>)"
    def AS_INSTANCE(self, frame):
        "{ClassName : ClassInstance (Class())}"
        self.as_instance[frame.__name__] = frame()
    "slot2 = Diagnosis , filler  = condition (Condition)"
    def Diagnosis(self,mentill):
        if isinstance(mentill, MentalIllness):
            self.diagnosis.append(mentill)


"Generic frame"
class Symptom:
    def __init__(self):
        self.synonyms = []
    "slot1 = Name, filler = name (string)"
    def Name(self,name):
        self.Name = str(name)
    "slot2 = Synonyms, filler = synonym (string)"
    def Synonyms(self,synonym):
        self.synonyms.append(str(synonym))
        

            
"Generic frame"
class Condition:
    def __init__(self):
        "constructor"
    "Slot1 = Name , filler = name (string)" 
    def Name(self,name):
        self.Name = str(name)

            
class MentalIllness(Condition):
    def __init__(self):
        self.is_a = []
        self.is_a.append(Condition)
        self.as_instance = {}
        self.phy_symptoms = []
        self.emo_symptoms = []
    "Slot1 = IS_A, filler = frame (<class>)" 
    def IS_A(self, frame):
        self.is_a.append(frame)
    "Slot2 = AS_INSTANCE , filler = frame (<class>)"
    def AS_INSTANCE(self, frame):
        "{ClassName : ClassInstance (Class())}"
        self.as_instance[frame.__name__] = frame()
    "Slot3  = PhysicalSymptoms, filler = symptom (Symptom)"
    def PhysicalSymptoms(self,symptom):
        self.phy_symptoms.append(symptom)
    "Slot4 = EmotionalSymptoms, filler = symptom (Symptom)"
    def EmotionalSymptoms(self,symptom):
        self.emo_symptoms.append(symptom)
        
        
"""
    
    tpatient (TherapyPatient)
    attr_list (string[])
    note: list that is constructed will be list of yes's and no's
    
    IN PROGRESS!

"""        
def create_attribute_list(patient, attr_list):
    list_for_tree=[]
    
    "if list of symptoms in Patient class is empty"
    if len(patient.symptoms) == 0 or len(patient.symptoms) < len(attr_list):
        return None
    "if list of symptoms in Patient class is at least same length as attr_list"
    if len(patient.symptoms) == len(attr_list):
        "for each attribute that decision tree needs"
        for attr in attr_list:
            "for now enter 'no' for this attr in list_for_tree since attribute we are looking for may not be present"
            list_for_tree[attr_list.index(attr)] = 'no'
            "for each Symptom object look through synonyms"
            for symp in patient.symptoms:
                "go through each synonym in symp(Symptom)"
                for syn in symp.synonyms:
                    "attribute is found among synonyms change to yes"
                    if syn == attr:
                        list_for_tree[attr_list.index(attr)] = 'no'
        return list_for_tree

########## The Frames
class theFrames:

    supposed_attribute_list_for_tree = ['Sad','Tired', 'Lonely', 'Sleep Changes']        
    p = Patient()
    create_attribute_list(p, supposed_attribute_list_for_tree)

    "create Depression frame"
    depressionFrame = MentalIllness()
    depressionFrame.Name("Depression")
    
    "create Symptom frames for Depression frames"
    "emotional"
    
    #attribute number 3
    sadFrame = Symptom()
    sadFrame.Name('sad')
    sad_syns = ['Low', 'Down', 'Unhappy', 'Downcast', 'Heartbroken','Glum','Gloomy','Doleful','Despairing']
    for x in sad_syns:
        sadFrame.Synonyms(x)
    depressionFrame.EmotionalSymptoms(sadFrame)
    
    #attribute number 6
    "physical"
    tiredFrame = Symptom()
    tiredFrame.Name('tired')
    tired_syns = ['Exhausted','Weary', 'Fatigued','Drained','Enervated']
    for x in tired_syns:
        tiredFrame.Synonyms(x)
    depressionFrame.PhysicalSymptoms(tiredFrame)
    
    energyFrame = Symptom()
    energyFrame.Name('not tired')
    energy_syns = ['refreshed', 'fresh', 'energetic', 'fine', 'ok', 'okay', 'productive']
    for x in tired_syns:
        energyFrame.Synonyms(x)
    depressionFrame.PhysicalSymptoms(energyFrame)
        
    weightFrame = Symptom()
    weightFrame.Name('weight Change')
    weight_syns = ['Weight gain','Weight loss', 'Fatter', 'Skinnier', 'Thinner']
    for x in weight_syns:
        weightFrame.Synonyms(x)   
    depressionFrame.PhysicalSymptoms(weightFrame)
 
        
    sleepFrame = Symptom()
    sleepFrame.Name('Sleep Changes')
    sleep_syns = ['Early','Awakening', 'Excess sleepiness', 'Insomnia', 'Restless sleep', 'Sleepier']
    for x in sleep_syns:
        sleepFrame.Synonyms(x)
    depressionFrame.PhysicalSymptoms(sleepFrame)

    
    appetiteFrame = Symptom()
    appetiteFrame.Name('Appetite Changes')
    appetite_syns = ['More hungry', 'Less Hungry', 'Hungrier', 'Starving']
    for x in appetite_syns:
        appetiteFrame.Synonyms(x)
    depressionFrame.PhysicalSymptoms(appetiteFrame)

    #attribute for attribute 2
    suicideFrame = Symptom()
    suicideFrame.Name('suicide')
    suicide_syns = ['suicidal', 'desire to kill oneself']
    for x in suicide_syns:
        suicideFrame.Synonyms(x)
    depressionFrame.EmotionalSymptoms(x)
    
    cognitiveFrame = Symptom()
    cognitiveFrame.Name('cognitive Changes')
    cog_syns = ['lack of concentration', 'slowness in activity']
    for x in cog_syns:
        cognitiveFrame.Synonyms(x)    
    depressionFrame.PhysicalSymptoms(cognitiveFrame)
    
    #for attribute number 4
    socialFrame = Symptom()
    socialFrame.Name("Social life")
    social_life_syns = ['lonely', 'stressed','normal']
    for x in social_life_syns:
        socialFrame.Synonyms(x)
   
    lonelyFrame = Symptom()
    lonelyFrame.Name("lonely")
    lonely_syns = ['lonely', 'by myself','nobody']
    for x in lonely_syns:
        lonelyFrame.Synonyms(x)
        
    stressedFrame = Symptom()
    stressedFrame.Name("stressed")
    stressed_syns = ['stressed', 'overwhelmed','anxious']
    for x in stressed_syns:
        stressedFrame.Synonyms(x)
        
    normalFrame = Symptom()
    normalFrame.Name("normal")
    normal_syns = ['fun', 'ok','fine', 'supportive']
    for x in social_life_syns:
        lonelyFrame.Synonyms(x)
   
    #for attribute number 3
    happyFrame = Symptom()
    happyFrame.Name('happy')
    happy_syns = ['Happy',"Joyful", 'glad', 'escatic']
    for x in happy_syns:
        happyFrame.Synonyms(x)    

    #for attribute number 3
    neutralFrame = Symptom()
    neutralFrame.Name('neutral')
    neutral_syns = ['neutral', 'nothing','impartial']
    for x in neutral_syns:
        neutralFrame.Synonyms(x)

    #for attribute number 5
    durationFrame = Symptom()
    durationFrame.Name('Duration')
    duration_syns = ['-2weeks','+2weeks']
    for x in happy_syns:
        durationFrame.Synonyms(x) 

"""
--------------------------- CHATBOT ----------------------------------
"""

"""
prompts, questions, responses
"""

#Age, Suicidal, Emotions, Social, Duration, Physical, 
data_for_tree = [None, None, None, None, None, None]

patient_info = [None, None, None, None, None, None, None] #name, age, feeling, physical, social, time, suicide

STARTUP_PROMPT = "COMMANDS:\n[h]elp [q]uit [s]ymptomlist\nHello, I am a chatbot."
DIAGNOSIS_PROMPT = "It appears you may be showing signs of {diagnosis}. Does that sound correct?"
NEXTPATIENT_PROMPT = "Next session; say \'hello\' to start:"
HELP_STRING = "If the chatbot has trouble understanding you, try using simpler sentences like \'I feel ____.\'\nUse \'s\' to show what symptoms the chatbot has gathered from your input."

FAMILY_TOPICS = ["family", "mother", "brother", "brothers", "sister", "sisters", "pet","boyfriend", "girlfriend"]
SCHOOL_TOPICS = ["school", "college", "class", "classes", "grades"]
DEATH_TOPICS = ["death","died","passed away"]
COMMON_TOPICS = [FAMILY_TOPICS, SCHOOL_TOPICS, DEATH_TOPICS]

QUESTION_KEYWORDS = ["who","what","when","where","why"]
NEGATION_KEYWORDS = ["not", "n\'t"]
COMMON_VERBS = ["am","feel","feeling","want","wanting","have","having","go","going"]
SUICIDE_KEYWORDS = ["suicide", "suicidal", "kill myself"]
YES_KEYWORDS = ["yes","yeah", "yep","I think so"]
NO_KEYWORDS = ["no", "nope", "I don\'t think so"]

#question flag = name
NAME_RESPONSE = "It is nice to meet you, {name}."

#question flag = age
AGE_CHILD_RESPONSE = "Often, depression in youths go unnoticed. Even though you are young, it\'s important to take your mental health seriously."
AGE_ADULT_RESPONSE = "Often, the stresses of adult life can bring on symptoms of depression. It\'s important not to neglect your mental health."

#question flag = physical/emotional
NEGATIVE_FEELING_RESPONSES = "I\'m sorry that {emotion}."
FEELING_CONFIRMATION = "So your general emotion is {emotion}?"

DEFAULT_RESPONSES = ["I\'m sorry, could you rephrase that?", "I don\'t understand what you said."]
CONFUSED_RESPONSE = "I\'m not sure what you said. Is there another word to describe it?"
SUICIDE_RESPONSE = "If thoughts of suicide or self harm ever arise, don't hesitate to get help.\nThe National Suicide Prevention Hotline is available at 1-800-273-8255, if you would like to speak to someone."
THANKS_RESPONSE = ["No problem.","I will do anything I can to help.","I hope this helps you in some way."] #keywords need to be written/implemented
APOLOGY_RESPONSE = "Oh, my apologies. I will keep this in my files and we can revisit this in a new session."
TWOWEEKS_RESPONSE = "For your symptoms to have persisted as long as they have may indicate a persistent condition."
TWOWEEKSNO_RESPONSE = "Everyone goes through slumps, but sometimes its a sign of a more persistent condition."

NAME_QUESTION = "What is your name?"
AGE_QUESTION = "How old are you?"
FEELING_QUESTION = "How are you feeling, emotionally?"
PHYSICAL_QUESTION = "How have you been feeling, energy-wise?"
SOCIAL_QUESTION = "How have you been feeling, in regards to relationships with peers and family?"
SUICIDE_QUESTION = "Have you been experiencing any suicidal ideation?"
TIME_QUESTION = "Have the issues you've described been present for longer than several weeks?"
WHY_QUESTION = "Can you think of anything in your life that may be a factor in feeling {emotion}?"
HOW_QUESTION = "How do you feel about {thing}?"
FOLLOWUP_QUESTION = "How are you feeling now?"

DIAGNOSIS = "Name: {name}\nAge: {age}\nTwo weeks?: {time}\nGeneral Emotion: {emotion}\nGeneral Physical: {physical}\nSocial: {social}\nSuicidal?: {suicidal}"
QUESTIONS = [NAME_QUESTION, AGE_QUESTION, FEELING_QUESTION, PHYSICAL_QUESTION, SOCIAL_QUESTION, TIME_QUESTION, SUICIDE_QUESTION, DIAGNOSIS]

fb = theFrames()

SOCIAL_FRAMES = [fb.lonelyFrame, fb.stressedFrame, fb.normalFrame]
EMOTION_FRAMES = [fb.sadFrame, fb.happyFrame, fb.neutralFrame]
TIRED_FRAMES = [fb.tiredFrame, fb.energyFrame]

#----------------------------------------------------------

def send_for_learning(outcome):
    """sends results of session to tree for learning"""
    dat = [None,None,None,None,None,None,None]
    dat[0] = patient_info[1]
    dat[1] = patient_info[6]
    dat[2] = patient_info[2]
    dat[3] = patient_info[4]
    dat[4] = patient_info[5]
    dat[5] = patient_info[3]
    dat[6] = outcome
    dataset.insert(len(dataset), dat)
    

def send_to_tree():
    """
    formats dataset and sends to tree
    returns diagnosis string and diagnosis
    """
    diagnosis = "Analyzing symptoms...\n" + diagnosis_reply()
    #reorders patient info into desicision tree for processing
    data_for_tree[0] = patient_info[1]
    data_for_tree[1] = patient_info[6]
    data_for_tree[2] = patient_info[2]
    data_for_tree[3] = patient_info[4]
    data_for_tree[4] = patient_info[5]
    data_for_tree[5] = patient_info[3]
    #
    query = fromChat(data_for_tree) # should query tree here using info from data_for_tree
    if query.lower() == 'depression':
        diagnosis = diagnosis + "\n\nIt appears you may have developed depression.\nI encourage you to support further resources such as\nthe Anxiety and Depression Association of America (http://www.adaa.org)\n"
    else:
        diagnosis = diagnosis + "\n\nThe likeliness of you having depression is low.\nHowever, if you are ever in doubt, don't hesitate to consult a doctor."
    return [diagnosis, query]

def split_at(words, verb):
    """
    splits sentence in half at the given verb
    """
    if verb in words:
        i = words.index(verb)
        first_half = words[0:i]
        second_half = words[i+1:]
        return [first_half, second_half]
    else:
        return -1

def punctuation_remover(words):
    """
    removes punctuation from user input
    """
    words = words.replace('?','')
    words = words.replace('!','')
    words = words.replace('.','')
    return words 

def pronoun_switch(words):
    """
    switches pronouns in user input
    """
    for x in words:
        if x == "you":
            x = "I"
        elif x == "I":
            x = "you"
        elif x == "am":
            x = "are"
        elif x == "my":
            x = "your"
        elif x == "we":
            x = "you"
        elif x == "our":
            x = "your"
        elif x == "us":
            x = "you"
    return words 

def diagnosis_reply():
    """
    gives list of patient info
    """
    return DIAGNOSIS.format(**{'name':patient_info[0], 'age': patient_info[1], 'emotion':patient_info[2], 'physical': patient_info[3], 'social': patient_info[4], 'time': patient_info[5], 'suicidal':patient_info[6]})

def default_reply():
    """
    chatbot will express confusion.
    """
    return random.choice(DEFAULT_RESPONSES)
    
def suicide_reply():
    """
    If SUICIDE_KEYWORDS is detected, offer SUICIDE_RESPONSE
    """
    return random.choice(SUICIDE_RESPONSE)

def is_firstperson(words):
    """
    check if input starts with first person pronouns
    """
    if words[0].lower() in ["i", "i'm", "i am"]: #first person
        return True
    else:
        return False

def name_reply(sentence):
    """
    reply to user inputting name
    """
    wordsarray = sentence.split()
    if "my name is" in sentence:
        sent_chunks = split_at(wordsarray,"is")
        patient_info[0] = sent_chunks[1]
    elif "i'm" in sentence:
        sent_chunks = split_at(wordsarray, "i'm")
        patient_info[0] = sent_chunks[1]
    elif "i am" in sentence:
        sent_chunks = split_at(wordsarray, "am")
        patient_info[0] = sent_chunks[1]
    else:
        patient_info[0] = sentence
    return NAME_RESPONSE.format(**{'name':patient_info[0]})
    
def age_reply(sentence):
    """
    reply to user inputting age (must be integer)
    """
    try:
        age = int(sentence)
    except ValueError:
        return "Please enter a number."
    if age < 19:
        patient_info[1] = 'youth'
    elif age < 51:
        patient_info[1] = 'adult'
    else:
        patient_info[1] = 'senior'
    if age < 18:
        return AGE_CHILD_RESPONSE
    else:
        return AGE_ADULT_RESPONSE
    
def feeling_reply(sentence):
    """
    reply to user inputting their emotion
    """
    negation_flag = False
    if sentence.split()[0] in NEGATION_KEYWORDS:
        negation_flag = True
        sentence = " ".join(sentence.split()[1:])
    if sentence.split()[0] in COMMON_VERBS:
        sentence = sentence[1:]
    if 'happy' in sentence:
        if negation_flag:
            return feeling_reply('sad')
        patient_info[2] = 'happy'
        return "I'm glad to hear that you're happy."
    elif 'sad' in sentence:
        if negation_flag:
            return feeling_reply('happy')
        patient_info[2] = 'sad'
        return "I'm sorry you feel that way."
    elif 'neutral' in sentence:
        patient_info[2] = 'neutral'
        return "Feeling plain calmness is okay."
    else:
        for x in EMOTION_FRAMES:
            syns = x.synonyms
            for y in syns:
                if y.lower() in sentence:
                    print x.Name
                    return feeling_reply(x.Name)
        clarify = raw_input("Would you describe that as being generally 'happy', 'neutral', or 'sad'?")
        if clarify == 'q':
                print "Goodbye."
                sys.exit()
        return feeling_reply(clarify)
    
def time_reply(sentence):
    """
    reply to user inputting whether or not the symptoms have persisted for more than two weeks
    """
    time = None
    reply = default_reply()
    if sentence in YES_KEYWORDS:
        reply = TWOWEEKS_RESPONSE
        time = "+2weeks"
    elif sentence in NO_KEYWORDS:
        reply = TWOWEEKSNO_RESPONSE
        time = "-2weeks"
    else:
        clarify = raw_input("Would you say that's a 'yes' or a 'no'?")
        if clarify == 'q':
                print "Goodbye."
                sys.exit()
        return time_reply(clarify)
    patient_info[5] = time
    return reply
    
def physical_reply(sentence):
    """
    reply to user inputting their physical state
    """
    negation_flag = False
    if sentence.split()[0] in NEGATION_KEYWORDS:
        negation_flag = True
    if 'tired' in sentence:
        if negation_flag:
            return physical_reply('okay')
        patient_info[3] = 'tired'
        return "You can try chamomile tea before bed."
    elif 'okay' in sentence:
        patient_info[3] = 'not tired'
        return "I'm glad to hear you have energy."
    else:
        for x in TIRED_FRAMES:
            syns = x.synonyms
            for y in syns:
                if y.lower() in sentence:
                    return physical_reply(x.Name)
        clarify = raw_input("Would you say you feel 'tired' or 'okay'?")
        if clarify == 'q':
                print "Goodbye."
                sys.exit()
        return physical_reply(clarify)
    
def social_reply(sentence):
    """
    reply to user inputting their outlook on their social connections
    """
    if 'lonely' in sentence:
        patient_info[4] = 'lonely'
        return "It might not seem like it right now, but you're not alone."
    elif 'stressed' in sentence:
        patient_info[4] = 'stressed'
        return "I'm sorry you feel stressed"
    elif 'normal' in sentence:
        patient_info[4] = 'normal'
        return "I'm glad you're getting along with your peers."
    else:
        for x in SOCIAL_FRAMES:
            syns = x.synonyms
            for y in syns:
                if y.lower() in sentence:
                    return social_reply(x.Name)
        clarify = raw_input('Would you say it makes you feel lonely, stressed, or does it feel normal?')
        if clarify == 'q':
                print "Goodbye."
                sys.exit()
        return social_reply(clarify)
    
def suicide_resp(sentence):
    """
    response to user inputting whether or not they are suicidal
    """
    if sentence in ['yes', 'sometimes', 'often']:
        patient_info[6] = 'yes'
        return SUICIDE_RESPONSE
    elif sentence == 'no':
        patient_info[6] = 'no'
        return "You have stated that you are not currently experiencing suicidal thoughts.\n" + SUICIDE_RESPONSE
    else:
        clarify = raw_input("Please answer 'no', 'sometimes', or 'yes'")
        if clarify == 'q':
                print "Goodbye."
                sys.exit()
        return suicide_resp(clarify)
    
def is_question(sentence):
    """
    check if user input question
    """
    if sentence[0].lower == QUESTION_KEYWORDS:
        return True
    else:
        return False

def question_reply(sentence,x):
    """
    x is index of question list
    checks what question has been asked by the chatbot 
    processes the input sentence
    and sends the appropriate response
    """
    sentence = sentence.lower()
    
    global question_flag # records question asked by bot
    if len(sentence) < 1:
        return default_reply() # default reply if input cannot be comprehended
    if is_question(sentence):
        return "I'm sorry, I can't answer that."
    if is_firstperson(sentence):
        sentence = " ".join(sentence.split()[1:])
    sentence = punctuation_remover(sentence)

    if QUESTIONS[x] == NAME_QUESTION: 
        return name_reply(sentence) # hello, <name>
    elif QUESTIONS[x] == AGE_QUESTION:
        return age_reply(sentence) # reply depending on how old the user is
    elif QUESTIONS[x] == FEELING_QUESTION:
        return feeling_reply(sentence)
#    elif QUESTIONS[x] == WHY_QUESTION:
#        return why_reply(sentence) # does the user know why they may feel this way? 
                                    # bot may offer simple advice based on detected keywords
    elif QUESTIONS[x] == PHYSICAL_QUESTION:
        return physical_reply(sentence)
    elif QUESTIONS[x] == SOCIAL_QUESTION:
        return social_reply(sentence)
    elif QUESTIONS[x] == TIME_QUESTION:
        return time_reply(sentence) # how long has the user's symptoms persisted?
    elif QUESTIONS[x] == SUICIDE_QUESTION:
        return suicide_resp(sentence)


def reply(sentence, x):
    """
    x is index of question list 
    for commands to quit, help, or see symptoms
    """
    if sentence.lower() == 'q':
        return 'Goodbye.'
    elif sentence.lower() == 'h':
        return HELP_STRING
    elif sentence.lower() == 's':
        return diagnosis_reply()
    else:
        return question_reply(sentence, x)
        
def ask_question():
    """
    asks questions from the QUESTIONS list.
    loops a question until a valid answer is found
    """
    sentence = ''

    for x in range(len(QUESTIONS)-1):
        while patient_info[x] is None:
#                if QUESTIONS[x] == WHY_QUESTION:
#                    print WHY_QUESTION.format(**{'emotion':patient_info[2]})
#                else:
            print QUESTIONS[x]
            sentence = raw_input('Say: ')
#                print "%s" % sentence
            if sentence == 'q':
                print "Goodbye."
                sys.exit()
            print reply(sentence, x)
        if None not in patient_info:
            outcome = send_to_tree() 
            print outcome[0]
            answer = None
            while answer == None:
                x = raw_input("Does this sound right to you? (yes/no): ")
                if x == 'yes': #diagnosis is correct; save patient info and outcome to dataset
                    answer = x
                    send_for_learning(outcome[1])
                    print "I will keep the outcome of this conversation in mind for the next session,\n so I may further improve my diagnosis.\n Thank you for your input.\n"
                elif x == 'no': #diagnosis is wrong; change outcome to the opposite value and save with the patient info to dataset
                    answer = x
                    if outcome[1] == 'depression':
                        send_for_learning('no depression')
                    else:
                        send_for_learning('depression')
                    print "I will keep the outcome of this conversation in mind for the next session,\n so I may further improve my diagnosis.\n Thank you for your input.\n"
                    
                
    

#-------------------
if __name__ == '__main__':
    """
    program will run from here
    """
    sentence = ''
    print STARTUP_PROMPT
    while sentence != 'q' and None in patient_info[0:4]:
        ask_question()  
        restart = raw_input("To start the next session, say 'hello'.")
        if restart == 'hello':
            patient_info = [None, None, None, None, None, None, None]

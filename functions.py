from math import *
import copy
import csv
import pandas as pd

#MENTEES

class Mentee:
    
    def __init__(self, first, last, phone, email, major, second_major, job, prof_interests, hobbies, meet, utc, mbti, ie, ie_pairing, bitcoin, ethereum, defi, crypto, governance, privacy, usability, scalability, research, design, development, product, investment, community, trading, legal, marketing, entrepreneurship, skills, goals, why_blockchain, blockchain_importance):
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email
        self.major = major
        self.second_major = second_major
        self.job =job
        self.prof_interests = prof_interests
        self.hobbies = hobbies
        self.meet = meet
        self.utc = utc
        self.mbti = mbti
        self.ie = ie
        self.ie_pairing = ie_pairing
        self.bitcoin = bitcoin
        self.ethereum = ethereum 
        self.defi = defi
        self.crypto = crypto
        self.governance = governance 
        self.privacy = privacy
        self.usability = usability
        self.scalability = scalability
        self.research = research 
        self.design = design
        self.development = development
        self.product = product
        self.investment = investment 
        self.community = community
        self.trading = trading
        self.legal = legal
        self.marketing = marketing
        self.entrepreneurship = entrepreneurship
        self.skills = skills
        self.goals = goals
        self.why_blockchain = why_blockchain
        self.blockchain_importance = blockchain_importance
        self.scores = {}
        self.preferences = []
        

#Columns of Mentee DataFrame
mentee_columns = ["first", "last", "phone", "email", "major", "job", "prof_interests", "hobbies", "meet","utc","mbti", "ie", "ie_pairing", "bitcoin", "ethereum", "defi", "crypto", "governance", "privacy", "usability", "scalability", "research", "design", "development", "product", "investment", "community", "trading", "legal", "marketing", "entrepreneurship", "skills", "goals", "why_blockchain", "blockchain_importance", "second_major"]

mentorskill_mapping = {"Very unfamiliar": 0, "Somewhat familiar": 1, "Familiar with amateur experience": 2, "Experience from past projects/academia": 3, "Professional or industry-level experience": 4}

menteeskill_mapping = {"Unfamiliar": 0, "Somewhat familiar": 1, "Familiar with amateur experience": 2, "Prior experience from classes/projects": 3, "Professional or industry-level experience": 4}

#INPUT: Raw Data from application
#OUTPUT: Updated DataFrame
def output_dataframe(path, columns, num=0):
    df = pd.read_csv(path)
    df = df.drop(columns="Timestamp")
    df.columns = columns
    
    #If num = 1 then mentee
    if num == 1:
        df["bitcoin"] = df["bitcoin"].map(menteeskill_mapping)
        df["ethereum"] = df["ethereum"].map(menteeskill_mapping)
        df["defi"] = df["defi"].map(menteeskill_mapping)
        df["crypto"] = df["crypto"].map(menteeskill_mapping)
        df["governance"] = df["governance"].map(menteeskill_mapping)
        df["privacy"] = df["privacy"].map(menteeskill_mapping)
        df["usability"] = df["usability"].map(menteeskill_mapping)
        df["scalability"] = df["scalability"].map(menteeskill_mapping)
        df["research"] = df["research"].map(menteeskill_mapping)
        df["development"] = df["development"].map(menteeskill_mapping)
        df["product"] = df["product"].map(menteeskill_mapping)
        df["design"] = df["design"].map(menteeskill_mapping)
        df["investment"] = df["investment"].map(menteeskill_mapping)
        df["community"] = df["community"].map(menteeskill_mapping)
        df["trading"] = df["trading"].map(menteeskill_mapping)
        df["legal"] = df["legal"].map(menteeskill_mapping)
        df["marketing"] = df["marketing"].map(menteeskill_mapping)
        df["entrepreneurship"] = df["entrepreneurship"].map(menteeskill_mapping)
    #If num = 0 then mentor
    else: 
        df["bitcoin"] = df["bitcoin"].map(mentorskill_mapping)
        df["ethereum"] = df["ethereum"].map(mentorskill_mapping)
        df["defi"] = df["defi"].map(mentorskill_mapping)
        df["crypto"] = df["crypto"].map(mentorskill_mapping)
        df["governance"] = df["governance"].map(mentorskill_mapping)
        df["privacy"] = df["privacy"].map(mentorskill_mapping)
        df["usability"] = df["usability"].map(mentorskill_mapping)
        df["scalability"] = df["scalability"].map(mentorskill_mapping)
        df["research"] = df["research"].map(mentorskill_mapping)
        df["development"] = df["development"].map(mentorskill_mapping)
        df["product"] = df["product"].map(mentorskill_mapping)
        df["investment"] = df["investment"].map(mentorskill_mapping)
        df["community"] = df["community"].map(mentorskill_mapping)
        df["design"] = df["design"].map(mentorskill_mapping)
        df["trading"] = df["trading"].map(mentorskill_mapping)
        df["legal"] = df["legal"].map(mentorskill_mapping)
        df["marketing"] = df["marketing"].map(mentorskill_mapping)
        df["entrepreneurship"] = df["entrepreneurship"].map(mentorskill_mapping)
        
    df["utc"] = df["utc"].map(timezones)
        
    return df
        
#INPUT: Cleaned DataFrame with information on Mentees
#OUTPUT: Dictionary with mapping from IDs (positive integers) to Mentee objects.
def output_mentees(mentee_df):
    menteesList = {}
    num_mentees = mentee_df.shape[0]

    for row in range(num_mentees):
        current = mentee_df.iloc[row]

        first = current.loc["first"]
        #print(current.loc["first"])
        last = current.loc["last"]
        phone = current.loc["phone"]
        email = current.loc["email"]
        major = current.loc["major"]
        second_major = current.loc["second_major"]
        job = current.loc["job"].split(',')
        prof_interests = current.loc["prof_interests"].split(',')
        hobbies = current.loc["hobbies"].split(',')
        meet = current.loc["meet"]
        utc = current.loc["utc"]
        mbti = current.loc["mbti"]
        ie = current.loc["ie"]
        ie_pairing = current.loc["ie_pairing"]
        bitcoin = current.loc["bitcoin"]
        ethereum = current.loc["ethereum"]
        defi = current.loc["defi"]
        crypto = current.loc["crypto"]
        governance = current.loc["governance"]
        privacy = current.loc["privacy"]
        usability = current.loc["usability"]
        scalability = current.loc["scalability"]
        research = current.loc["research"]
        design = current.loc["design"]
        development = current.loc["development"]
        product = current.loc["product"]
        investment = current.loc["investment"]
        community = current.loc["community"]
        trading = current.loc["trading"]
        legal = current.loc["legal"]
        marketing = current.loc["marketing"]
        entrepreneurship = current.loc["entrepreneurship"]
        skills = current.loc["skills"].split(',')
        goals = current.loc["goals"]
        why_blockchain = current.loc["why_blockchain"]
        blockchain_importance = current.loc["blockchain_importance"]

        menteesList[row+1] = Mentee(first, last, phone, email, major, second_major, job, prof_interests, hobbies, meet, utc, mbti, ie, ie_pairing, bitcoin, ethereum, defi, crypto, governance, privacy, usability, scalability, research, design, development, product, investment, community, trading, legal, marketing, entrepreneurship, skills, goals, why_blockchain, blockchain_importance)
    return menteesList


#### MENTORS

class Mentor:
    
    def __init__(self, first, last, phone, email, major, second_major, job, prof_interests, hobbies, meet, utc, mbti, ie, ie_pairing, bitcoin, ethereum, defi, crypto, governance, privacy, usability, scalability, research, design, development, product, investment, community, trading, legal, marketing, entrepreneurship, skills, goals, why_blockchain, blockchain_importance, unlisted_profession):
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email
        self.major = major
        self.second_major = second_major
        self.job =job
        self.prof_interests = prof_interests
        self.hobbies = hobbies
        self.meet = meet
        self.utc = utc
        self.mbti = mbti
        self.ie = ie
        self.ie_pairing = ie_pairing
        self.bitcoin = bitcoin
        self.ethereum = ethereum 
        self.defi = defi
        self.crypto = crypto
        self.governance = governance 
        self.privacy = privacy
        self.usability = usability
        self.scalability = scalability
        self.research = research 
        self.design = design
        self.development = development
        self.product = product
        self.investment = investment 
        self.community = community
        self.trading = trading
        self.legal = legal
        self.marketing = marketing
        self.entrepreneurship = entrepreneurship
        self.skills = skills
        self.goals = goals
        self.why_blockchain = why_blockchain
        self.blockchain_importance = blockchain_importance
        self.unlisted_profession = unlisted_profession
        self.scores = {}
        self.preferences = []

#Columns of Mentor DataFrame
mentor_columns = ["first", "last", "phone", "email", "major","second_major", "job", "prof_interests", "hobbies", "meet","utc","mbti", "ie", "ie_pairing", "bitcoin", "ethereum", "defi", "crypto", "governance", "privacy", "usability", "scalability", "research", "design", "development", "product", "investment", "community", "trading", "legal", "marketing", "entrepreneurship", "skills", "goals", "why_blockchain", "blockchain_importance", "unlisted_profession"]

timezones = {"GMT (Greenwich Mean Time)":0,
             "ECT (European Central Time)":1, 
             "EET (Eastern European Time)":2, 
             "ART (Egypt Standard Time)":2, 
             "EAT (Eastern African Time)":3, 
             "MET (Middle East Time)":3, 
             "NET (Near East Time)":4, 
             "PLT (Pakistan Lahore Time)":5, 
             "IST (India Standard Time)":5.5, 
             "BST (Bangladesh Standard Time)":6, 
             "VST (Vietnam Standard Time)":7, 
             "CTT (China Taiwan Time)":8, 
             "JST (Japan Standard Time)":9, 
             "ACT (Australia Central Time)":9.5, 
             "AET (Australia Eastern Time)":10, 
             "SST (Solomon Standard Time)":11, 
             "NST (New Zealand Standard Time)":12, 
             "MIT (Midway Islands Time)":-11, 
             "HST (Hawaii Standard Time)":-10, 
             "AST (Alaska Standard Time)":-9, 
             "PST (Pacific Standard Time)":-8, 
             "PNT (Phoenix Standard Time)":-7, 
             "MST (Mountain Standard Time)":-7, 
             "CST (Central Standard Time)":-6, 
             "EST (Eastern Standard Time)":-5, 
             "IET (Indiana Eastern Standard Time)": -5, 
             "PRT (Puerto Rico and US Virgin Islands Time)":-4, 
             "CNT (Canada Newfoundland Time)":-3, 
             "AGT (Argentina Standard Time":-3, 
             "BET (Brazil Eastern Time)":-3, 
             "CAT (Central African Time)":-1}
        
#INPUT: Cleaned DataFrame with information on Mentors
#OUTPUT: Dictionary with mapping from IDs (negative integers) to Mentor objects.
def output_mentors(mentor_df):
    mentorsList = {}
    num_mentors = mentor_df.shape[0]

    for row in range(num_mentors):
        current = mentor_df.iloc[row]

        first = current.loc["first"]
        last = current.loc["last"]
        phone = current.loc["phone"]
        email = current.loc["email"]
        major = current.loc["major"]
        second_major = current.loc["second_major"]
        job = current.loc["job"]
        prof_interests = current.loc["prof_interests"].split(',')
        hobbies = current.loc["hobbies"].split(',')
        meet = current.loc["meet"]
        utc = current.loc["utc"]
        mbti = current.loc["mbti"]
        ie = current.loc["ie"]
        ie_pairing = current.loc["ie_pairing"]
        bitcoin = current.loc["bitcoin"]
        ethereum = current.loc["ethereum"]
        defi = current.loc["defi"]
        crypto = current.loc["crypto"]
        governance = current.loc["governance"]
        privacy = current.loc["privacy"]
        usability = current.loc["usability"]
        scalability = current.loc["scalability"]
        research = current.loc["research"]
        design = current.loc["design"]
        development = current.loc["development"]
        product = current.loc["product"]
        investment = current.loc["investment"]
        community = current.loc["community"]
        trading = current.loc["trading"]
        legal = current.loc["legal"]
        marketing = current.loc["marketing"]
        entrepreneurship = current.loc["entrepreneurship"]
        skills = current.loc["skills"].split(',')
        goals = current.loc["goals"]
        unlisted_profession = current.loc["unlisted_profession"]
        why_blockchain = current.loc["why_blockchain"]
        blockchain_importance = current.loc["blockchain_importance"]

        mentorsList[-1*(row+1)] = Mentor(first, last, phone, email, major, second_major, job, prof_interests, hobbies, meet, utc, mbti, ie, ie_pairing, bitcoin, ethereum, defi, crypto, governance, privacy, usability, scalability, research, design, development, product, investment, community, trading, legal, marketing, entrepreneurship, skills, goals, unlisted_profession, why_blockchain, blockchain_importance)
    return mentorsList

def output_final(proposals, mentors, mentees):
    proposalkeys = proposals.keys()
    rowslist = []

    #mentee or mentor List = {id: Object}

    for i in proposalkeys:
        mentorindex = i
        mentorFirst = "Unpaired"
        mentorFirst = "Unpaired"
        mentorLast = "Unpaired"
        mentorEmail = "Unpaired"
        mentorPhone = "Unpaired"
        mentorGoals = "Unpaired"
        mentorWhy = "Unpaired"
        mentorImportance = "Unpaired"
        
        if mentorindex in mentors:
            curr_mentor = mentors.get(mentorindex)
            mentorFirst = curr_mentor.first
            mentorLast = curr_mentor.last
            mentorEmail = curr_mentor.email
            mentorPhone = curr_mentor.phone
            mentorGoals = curr_mentor.goals
            mentorWhy = curr_mentor.why_blockchain
            mentorImportance = curr_mentor.blockchain_importance

        menteeindex = proposals.get(i)
        menteeFirst = "Unpaired"
        menteeLast = "Unpaired"
        menteeEmail = "Unpaired"
        menteePhone = "Unpaired"
        menteeGoals = "Unpaired"
        menteeWhy = "Unpaired"
        menteeImportance = "Unpaired"
        
        if menteeindex in mentees:
            curr_mentee = mentees.get(menteeindex)
            menteeFirst = curr_mentee.first
            menteeLast = curr_mentee.last
            menteeEmail = curr_mentee.email
            menteePhone = curr_mentee.phone
            menteeGoals = curr_mentee.goals
            menteeWhy = curr_mentee.why_blockchain
            menteeImportance = curr_mentee.blockchain_importance
    
        columnsList = {"Mentee First":menteeFirst, "Mentee Last":menteeLast, "Mentee Email":menteeEmail,
                   "Mentee Phone": menteePhone, "(Mentee) What are your main goals for this mentorship program?":menteeGoals, 
                   "(Mentee) Why are you interested in blockchain?": menteeWhy,
                   "(Mentee) Why do you think blockchain is important?":menteeImportance,
                   "Mentor First":mentorFirst, "Mentor Last":mentorLast, 
                   "Mentor Email":mentorEmail, "Mentor Phone":mentorPhone, "(Mentor) What are your main goals for this mentorship program?": mentorGoals, 
                  "(Mentor) Why are you interested in blockchain?": mentorWhy, 
                   "(Mentor) Why do you think blockchain is important?":mentorImportance}
    
        rowslist += [columnsList]

    final = pd.DataFrame(rowslist)
    display(final)

def matchScore(menteeList, mentorList):
    
    #Mentee's score of Mentor
    
    for mentee_id in menteeList:
        mentee = menteeList.get(mentee_id)

        for mentor_id in mentorList:
            score = 0
            mentor = mentorList.get(mentor_id)
            
            #chunk 1: hobbies/interests (max 20)
            piMatches = 0
            hobbyMatches = 0
            for pi in mentee.prof_interests:
                if pi in mentor.prof_interests:
                    piMatches += 1
            for hobby in mentee.hobbies:
                if hobby in mentor.hobbies:
                    hobbyMatches += 1
            score += piMatches / 24 * 15
            score += hobbyMatches / 17 * 5

            #chunk 2: timezone (max 20)
            score += 25 * ((1 / 2) ** abs((mentee.utc - mentor.utc)))

            #chunk 3: occupation/major (max 25)
            if mentee.major == mentor.major:
                score += 15
            elif mentee.second_major == mentor.major:
                score += 15
            elif mentee.major == mentor.second_major:
                score += 15
            elif mentee.second_major == mentor.second_major:
                score += 15
            
            for job in mentee.job:
                if job == mentor.job:
                    score += 10
                elif job == mentor.unlisted_profession:
                    score += 10

            #chunk 4: personality (max 10)
            if mentee.ie_pairing == 'Extraverted':
                score += 2 * (mentor.ie > 3)
            elif mentee.ie_pairing == 'Introverted':
                score += 2 * (mentor.ie < 3)

            #chunk 5: time (max 25)
            if mentee.meet == mentor.meet:
                score += 25
            else:
                if mentee.meet == "Once a month":
                    menteeTime = 3
                elif mentee.meet == "Once every 2-3 weeks":
                    menteeTime = 2
                elif mentee.meet == "Once a week":
                    menteeTime = 1

                if mentor.meet == "Once a month":
                    mentorTime = 3
                elif mentor.meet == "Once every 2-3 weeks":
                    mentorTime = 2
                elif mentor.meet == "Once a week":
                    mentorTime = 1

                score += pow(2, (menteeTime - mentorTime)) * 6
            
            score += mentee_skills(mentee, mentor)
            
            mentee.scores[mentor_id] = score

    #Mentor's score of Mentee
    
    
    for mentor_id in mentorList:
        mentor = mentorList.get(mentor_id)
        
        for mentee_id in menteeList:
            score = 0
            mentee = menteeList.get(mentee_id)
            
            #chunk 1: hobbies/interests (max 20)
            piMatches = 0
            hobbyMatches = 0
            for pi in mentee.prof_interests:
                if pi in mentor.prof_interests:
                    piMatches += 1
            for hobby in mentee.hobbies:
                if hobby in mentor.hobbies:
                    hobbyMatches += 1
            score += piMatches / 24 * 15
            score += hobbyMatches / 17 * 5

            #chunk 2: location (max 20)
            score += 25 * ((1 / 2) ** abs((mentee.utc - mentor.utc)))
            
            #chunk 3: occupation/major (max 25)
            if mentee.major == mentor.major:
                score += 15
            elif mentee.second_major == mentor.major:
                score += 15
            elif mentee.major == mentor.second_major:
                score += 15
            elif mentee.second_major == mentor.second_major:
                score += 15
            
            for job in mentee.job:
                if job == mentor.job:
                    score += 10
                elif job == mentor.unlisted_profession:
                    score += 10
    
            if mentee.job == mentor.job:
                score += 10

            #chunk 4: personality (max 10)
            if mentor.ie_pairing == 'Extraverted':
                score += 2 * (mentee.ie > 3)
            elif mentor.ie_pairing == 'Introverted':
                score += 2 * (mentee.ie < 3)

            #chunk 5: time (max 25)
            if mentee.meet == mentor.meet:
                score += 25
            else:
                if mentee.meet == "Once a month":
                    menteeTime = 3
                elif mentee.meet == "Once every 2-3 weeks":
                    menteeTime = 2
                elif mentee.meet == "Once a week":
                    menteeTime = 1

                if mentor.meet == "Once a month":
                    mentorTime = 3
                elif mentor.meet == "Once every 2-3 weeks":
                    mentorTime = 2
                elif mentor.meet == "Once a week":
                    mentorTime = 1

                score += pow(2, (mentorTime - menteeTime)) * 6
            
            
                
            mentor.scores[mentee_id] = score

def mentee_skills(mentee, mentor):
    score = 0
    if "Bitcoin" in mentee.skills:
        score += mentor.bitcoin
    if "Ethereum" in mentee.skills:
        score += mentor.ethereum
    if "DeFi" in mentee.skills:
        score += mentor.defi
    if "Cryptography" in mentee.skills:
        score += mentor.crypto
    if "Governance" in mentee.skills:
        score += mentor.governance
    if "Privacy" in mentee.skills:
        score += mentor.privacy
    if "Usability" in mentee.skills:
        score += mentor.usability
    if "Scalability" in mentee.skills:
        score += mentor.scalability
    if "Research" in mentee.skills:
        score += mentor.research
    if "Design" in mentee.skills:
        score += mentor.design
    if "Development" in mentee.skills:
        score += mentor.development
    if "Product" in mentee.skills:
        score += mentor.product
    if "Investment" in mentee.skills:
        score += mentor.investment
    if "Community" in mentee.skills:
        score += mentor.community
    if "Trading" in mentee.skills:
        score += mentor.trading
    if "Legal" in mentee.skills:
        score += mentor.legal
    if "Marketing" in mentee.skills:
        score += mentor.marketing
    if "Entrepreneurship" in mentee.skills:
        score += mentor.entrepreneurship
    return score
    
def mentor_skills(mentee, mentor):
    score = 0
    if mentor.skills == "Experience":
        if mentor.bitcoin >= 3:
            score += (mentee.bitcoin >= 3)*4
        if mentor.ethereum >= 3:
            score += (mentee.ethereum >= 3)*4
        if mentor.defi >= 3:
            score += (mentee.defi >= 3)*4
        if mentor.crypto >= 3:
            score += (mentee.crypto >= 3)*4
        if mentor.governance >= 3:
            score += (mentee.governance >= 3)*4
        if mentor.privacy >= 3:
            score += (mentee.privacy >= 3)*4
        if mentor.usability >= 3:
            score += (mentee.usability >= 3)*4
        if mentor.scalability >= 3:
            score += (mentee.scalability >= 3)*4
        if mentor.research >= 3:
            score += (mentee.research >= 3)*4
        if mentor.design >= 3:
            score += (mentee.design >= 3)*4
        if mentor.development >= 3:
            score += (mentee.development >= 3)*4
        if mentor.product >= 3:
            score += (mentee.product >= 3)*4
        if mentor.investment >= 3:
            score += (mentee.investment >= 3)*4
        if mentor.community >= 3:
            score += (mentee.community >= 3)*4
        if mentor.trading >= 3:
            score += (mentee.trading >= 3)*4
        if mentor.legal >= 3:
            score += (mentee.legal >= 3)*4
        if mentor.marketing >= 3:
            score += (mentee.marketing >= 3)*4
        if mentor.entrepreneurship >= 3:
            score += (mentee.entrepreneurship >= 3)*4
                    
    if mentor.skills == "Familiarity or demonstrated interest":
        if mentor.bitcoin >= 3:
            score += (mentee.bitcoin >= 1)*2
        if mentor.ethereum >= 3:
             score += (mentee.ethereum >= 1)*2
        if mentor.defi >= 3:
             score += (mentee.defi >= 1)*2
        if mentor.crypto >= 3:
             score += (mentee.crypto >= 1)*2
        if mentor.governance >= 3:
             score += (mentee.governance >= 1)*2
        if mentor.privacy >= 3:
             score += (mentee.privacy >= 1)*2
        if mentor.usability >= 3:
             score += (mentee.usability >= 1)*2
        if mentor.scalability >= 3:
             score += (mentee.scalability >= 1)*2
        if mentor.research >= 3:
            score += (mentee.research >= 1)*2
        if mentor.design >= 3:
            score += (mentee.design >= 1)*2
        if mentor.development >= 3:
            score += (mentee.development >= 1)*2
        if mentor.product >= 3:
            score += (mentee.product >= 1)*2
        if mentor.investment >= 3:
            score += (mentee.investment >= 1)*2
        if mentor.community >= 3:
            score += (mentee.community >= 1)*2
        if mentor.trading >= 3:
            score += (mentee.trading >= 1)*2
        if mentor.legal >= 3:
            score += (mentee.legal >= 1)*2
        if mentor.marketing >= 3:
            score += (mentee.marketing >= 1)*2
        if mentor.entrepreneurship >= 3:
            score += (mentee.entrepreneurship >= 1)*2
    return score
           
    

def preferencelists(menteeList, mentorList):
    for menteeid in menteeList:
        mentee = menteeList.get(menteeid)
        copy = mentee.scores.copy()
        preflist = []
        while len(copy) > 0:
            bestmentor = maxscore(copy)
            preflist.append(bestmentor)
            del copy[bestmentor]
        mentee.preferences = preflist
    for mentorid in mentorList:
        mentor = mentorList.get(mentorid)
        copy = mentor.scores.copy()
        preflist = []
        while len(copy) > 0:
            bestmentee = maxscore(copy)
            preflist.append(bestmentee)
            del copy[bestmentee]
        mentor.preferences = preflist
    return


#Input: {1: 44, 2: 3.2, 6: 33.2}
#Output: 1
def maxscore(matchscores):
    bestscore = -1
    bestpairing = None
    for person in matchscores:
        score = matchscores.get(person)
        if score > bestscore:
            bestscore = score
            bestpairing = person
    return bestpairing

def same_numbers(menteePrefs, mentorPrefs):
    num_mentees = len(menteePrefs)
    num_mentors = len(mentorPrefs)
    while num_mentees < num_mentors:
        for mentor in list(mentorPrefs.keys()):
            mentorPrefs[mentor] += [num_mentees+1]
            menteePrefs[num_mentees+1] = [x*-1 for x in list(range(1,num_mentors+1))]
        num_mentees += 1
    while num_mentees > num_mentors:
        for mentee in list(menteePrefs.keys()):
            menteePrefs[mentee] += [(num_mentors+1)*-1]
            mentorPrefs[(num_mentors+1)*-1] = list(range(1,num_mentees+1))
        num_mentors += 1

def stableMarriage(mentees, mentors):
    
    menteeList = copy.deepcopy(mentees)
    mentorList = copy.deepcopy(mentors)
    
    menteePrefs = {}
    for mentee_id in menteeList:
        menteePrefs[mentee_id] = menteeList[mentee_id].preferences
    mentorPrefs = {}
    for mentor_id in mentorList:
        mentorPrefs[mentor_id] = mentorList[mentor_id].preferences
        
    same_numbers(menteePrefs, mentorPrefs)
    
    proposals = {}
    final_len = len(mentorPrefs)
    
    while len(proposals) != final_len:
        for mentor_id in mentorPrefs:
            prefs = mentorPrefs.get(mentor_id)
            if mentor_id not in proposals and len(prefs) > 0:
                bestChoice = prefs[0]
                if bestChoice in proposals.values():
                    otherMentor = None
                    for key in menteePrefs[bestChoice]:
                        if key in proposals.keys() and proposals[key] == bestChoice:
                            otherMentor = key
                    menteePref1 = menteePrefs[bestChoice].index(mentor_id)
                    menteePref2 = menteePrefs[bestChoice].index(otherMentor)
                    if menteePref1 < menteePref2:
                        proposals[mentor_id] = bestChoice
                        del proposals[otherMentor]
                        mentorPrefs[otherMentor].remove(bestChoice)
                    else:
                        mentorPrefs[mentor_id].remove(bestChoice)
                else:
                    proposals[mentor_id] = bestChoice
                    
    return proposals

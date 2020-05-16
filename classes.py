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
        why_blockchain = current.loc["why_blockchain"]
        blockchain_importance = current.loc["blockchain_importance"]

        menteesList[row+1] = Mentee(first, last, phone, email, major, second_major, job, prof_interests, hobbies, meet, utc, mbti, ie, ie_pairing, bitcoin, ethereum, defi, crypto, governance, privacy, usability, scalability, research, design, development, product, investment, community, trading, legal, marketing, entrepreneurship, skills, goals, why_blockchain, blockchain_importance)
    return menteesList


#### MENTORS

class Mentor:
    
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
        

#Columns of Mentor DataFrame
mentor_columns = ["first", "last", "phone", "email", "major","second_major", "job", "prof_interests", "hobbies", "meet","utc","mbti", "ie", "ie_pairing", "bitcoin", "ethereum", "defi", "crypto", "governance", "privacy", "usability", "scalability", "research", "design", "development", "product", "investment", "community", "trading", "legal", "marketing", "entrepreneurship", "skills", "goals", "why_blockchain", "blockchain_importance"]

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
        why_blockchain = current.loc["why_blockchain"]
        blockchain_importance = current.loc["blockchain_importance"]

        mentorsList[-1*(row+1)] = Mentor(first, last, phone, email, major, second_major, job, prof_interests, hobbies, meet, utc, mbti, ie, ie_pairing, bitcoin, ethereum, defi, crypto, governance, privacy, usability, scalability, research, design, development, product, investment, community, trading, legal, marketing, entrepreneurship, skills, goals, why_blockchain, blockchain_importance)
    return mentorsList

def output_final(proposals, mentors, mentees):
    proposalkeys = proposals.keys()
    rowslist = []

    #mentee or mentor List = {id: Object}

    for i in proposalkeys:
        menteeindex = i
        curr_mentee = mentees.get(menteeindex)

        menteeFirst = curr_mentee.first
        menteeLast = curr_mentee.last
        menteeEmail = curr_mentee.email
        menteePhone = curr_mentee.phone
        menteeGoals = curr_mentee.goals
        menteeWhy = curr_mentee.why_blockchain
        menteeImportance = curr_mentee.blockchain_importance

        mentorindex = proposals.get(i)
        curr_mentor = mentors.get(mentorindex)

        mentorFirst = curr_mentor.first
        mentorLast = curr_mentor.last
        mentorEmail = curr_mentor.email
        mentorPhone = curr_mentor.phone
        mentorGoals = curr_mentor.goals
        mentorWhy = curr_mentor.why_blockchain
        mentorImportance = curr_mentor.blockchain_importance
    
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


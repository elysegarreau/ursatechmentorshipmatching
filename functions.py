from math import *
import copy

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
   
    
    #Now menteePrefs + mentorPrefs have same # of matches. 
    #menteePrefs: {1: [-2,-3,..], 2:[-3,-4,...], ...}
    #mentorPrefs: {-1: [5, 3,..], -2:[4,2,...], ...}
    #proposals: {-1:2, -3:5, -7:4, ...}
    
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

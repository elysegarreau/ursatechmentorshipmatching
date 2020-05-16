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
            score += 25 * (1 / 2 ** abs((mentee.utc - mentor.utc)))

            #chunk 3: occupation/major (max 25)
            if mentee.major == mentor.major:
                score += 15
            elif mentee.second_major == mentor.major:
                score += 15
            elif mentee.major == mentor.second_major:
                score += 15
            elif mentee.second_major == mentor.second_major:
                score += 15
            
            if mentee.job == mentor.job:
                score += 10

            #chunk 4: personality (max 10)
            if mentee.ie_pairing == 'Extraverted':
                score += 2 * mentor.ie
            elif mentee.ie_pairing == 'Introverted':
                score -= 2 * mentor.ie

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
            score += 25 * (1 / 2 ** abs((mentee.utc - mentor.utc)))
            
            #chunk 3: occupation/major (max 25)
            if mentee.major == mentor.major:
                score += 15
            elif mentee.second_major == mentor.major:
                score += 15
            elif mentee.major == mentor.second_major:
                score += 15
            elif mentee.second_major == mentor.second_major:
                score += 15
    
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


def stableMarriage(mentees, mentors):
    
    menteeList = copy.deepcopy(mentees)
    mentorList = copy.deepcopy(mentors)
    
    menteePrefs = {}
    for mentee_id in menteeList:
        menteePrefs[mentee_id] = menteeList[mentee_id].preferences
    mentorPrefs = {}
    for mentor_id in mentorList:
        mentorPrefs[mentor_id] = mentorList[mentor_id].preferences
    
    #Example of Mentee Prefs: {3: [-3,-4,-5,...], 2: [-1,-2,-3...]}
    
    proposals = {}
    
    while len(proposals) != len(mentorPrefs):
        for mentor_id in mentorPrefs:
            
            prefs = mentorPrefs.get(mentor_id)
            bestChoice = prefs[0]
            
            if bestChoice in proposals.values():
                
                otherMentor = None
                for key in menteePrefs[bestChoice]:
                    if key in proposals.keys() and proposals[key] == bestChoice:
                        otherMentor = key
                if menteePrefs[bestChoice].index(mentor_id) > menteePrefs[bestChoice].index(otherMentor):
                    proposals[mentor_id] = bestChoice
                    del proposals[otherMentor]
                    mentorPrefs[otherMentor].remove(bestChoice)
                else:
                    mentorPrefs[mentor_id].remove(bestChoice)
            else:
                proposals[mentor_id] = bestChoice
    return proposals

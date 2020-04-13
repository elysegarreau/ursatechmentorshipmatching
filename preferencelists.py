#Creating Preference Lists



#given match scores
#create pref list



#one list of mentor objects, one list of mentee objects
def preferencelists(mentees, mentors):
    allmenteepreflists = {}
    for mentee in mentees:
        preflist = []
        copy = mentee.matches
        while copy:
            bestmentor, score = maxscore(copy)
            preflist.append(bestmentor)
            del copy[bestmentor]
        allmenteepreflists[mentee] = preflist
    allmentorpreflists = {}
    for mentor in mentors:
        preflist = []
        copy = mentor.matches
        while copy:
            bestmentee, score = maxscore(copy)
            preflist.append(bestmentee)
            del copy[bestmentee]
        allmentorpreflists[mentor] = preflist
    return allmenteepreflists, allmentorpreflists
    

def maxscore(mentormatchscores):
    max = -1
    bestmentor = None
    for person, score in mentormatchscores:
        if score > max:
            max = score
            bestmentor = person
    return bestmentor, score



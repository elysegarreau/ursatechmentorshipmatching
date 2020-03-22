#Stable Marriage algorithm

#Mentors: A, B, C
#Mentees: D, E, F
#Scores: 0-9

# Alternate algorithm to the dictionary one on master branch
# This one tries using nested lists instead of dictionaries
# NOT COMPLETE

mentorPrefs = {"A" : [["D", 0], ["E", 7], ["F",9]], 
"B" : [["D",9], ["E",8], ["F",9]], 
"C" : [["D",6], ["E",8], ["F",7]]}
menteePrefs = {"D" : [["A",7], ["B",5], ["C",8]], 
"E" : [["A",3], ["B",3], ["C",2]], 
"F" : [["A",9], ["B",9], ["C",9]]}

#returns dictionary of match pairs (e.g., {"A" : "E", "B" : "F", "C" : "D"})
def stableMarriage(mentorPrefs, menteePrefs):
    proposals = {}
    
    sortByMax = lambda lst : lst[1]
    
    for mentor, prefs in mentorPrefs.items():
        sorted(prefs, key=sortByMax)
    
    for mentee, prefs in menteePrefs.items():
        sorted(prefs, key=sortByMax)
        
    while len(proposals) != len(mentorPrefs):
        count = 0
        for mentor, prefs in mentorPrefs.items():
            bestChoice = prefs[count][0]
            if bestChoice in proposals.values():
                otherMentor = None
                for pair in menteePrefs[bestChoice]:
                    if pair[0] in proposals.keys() and proposals[pair[0]] == bestChoice:
                        otherMentor = pair[0]
                if otherMentor != None:
                    j, m, oM = 0, 0, 0
                    for pair in menteePrefs[bestChoice]:
                        if pair[0] == mentor:
                            m = j
                        if pair[0] == otherMentor:
                            oM = j
                        j += 1
                    # Edited until this point but there seem to be too many iterations of the list needed 
                    # and therefore bigger runtime so the dictionaries implementation seems more simple and efficient
                    if menteePrefs[bestChoice][m][1] > menteePrefs[bestChoice][oM][1]:
                        proposals[mentor] = bestChoice
                        del proposals[otherMentor]
                        del mentorPrefs[otherMentor][bestChoice]
                else:
                    count += 1
            else:
                proposals[mentor] = bestChoice
    return proposals
    
stableMarriage(mentorPrefs, menteePrefs)

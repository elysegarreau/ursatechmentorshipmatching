
#Stable Marriage algorithm

#Mentors: A, B, C
#Mentees: D, E, F
#Scores: 0-9

mentorPrefs = {"A" : {"D" : 0, "E" : 7, "F" : 9}, "B" : {"D" : 9, "E" : 8, "F" : 9}, "C" : {"D" : 6, "E" : 8, "F" : 7}}
menteePrefs = {"D" : {"A" : 7, "B" : 5, "C" : 8}, "E" : {"A" : 3, "B" : 3, "C" : 2}, "F" : {"A" : 9, "B" : 9, "C" : 9}}

#returns dictionary of match pairs (e.g., {"A" : "E", "B" : "F", "C" : "D"})
def stableMarriage(mentorPrefs, menteePrefs):
    proposals = {}
    while len(proposals) != len(mentorPrefs):
        for mentor, prefs in mentorPrefs.items():
            bestChoice = max(prefs, key = prefs.get)
            #prefs[index]
            if bestChoice in proposals.values():
                otherMentor = None
                for key in menteePrefs[bestChoice].keys():
                    if key in proposals.keys() and proposals[key] == bestChoice:
                        otherMentor = key
                if menteePrefs[bestChoice][mentor] > menteePrefs[bestChoice][otherMentor]:
                    proposals[mentor] = bestChoice
                    del proposals[otherMentor]
                    del mentorPrefs[otherMentor][bestChoice]
                else:
                    del mentorPrefs[mentor][bestChoice]
            else:
                proposals[mentor] = bestChoice
        #for mentor, proposal in proposals:
        #    if len(proposal) != 1:
        #        return
    return proposals

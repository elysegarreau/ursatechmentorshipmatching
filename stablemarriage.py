
#Stable Marriage algorithm

def stableMarriage(mentorPrefs, menteePrefs):
    ret = {}
    proposals = {}
    while len(ret) != len(mentorPrefs):
        for mentor, prefs in mentorPrefs:
            bestchoice = prefs[0]
            proposals[bestChoice] = mentee
        for mentor, proposal in proposals:
            if len(proposal) != 1:
                return
    return

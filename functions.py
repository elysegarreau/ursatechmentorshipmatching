def matchScore(menteeList, mentorList):
    for mentee in menteeList:
        score = 0

        for mentor in mentorList:
            #chunk 1: hobbies/interests (max 20)
            piMatches = 0
            hobbyMatches = 0
            for pi in mentee.professionalInterests:
                if pi in mentor.professionalInterests:
                    piMatches += 1
            for hobby in mentee.hobbies:
                if hobby in mentor.hobbies:
                    hobbyMatches += 1
            score += piMatches / 24 * 15
            score += hobbyMatches / 17 * 5


            #chunk 2: location (max 20)
            score += 25 * (1 / 2 ** math.abs((mentee.utc - mentor.utc)))

            #chunk 3: occupation/major (max 25)
            if mentee.major == mentor.major:
                score += 15
            if mentee.occ == mentor.occ:
                score += 10

            #chunk 4: personality (max 10)
            if mentee.want == 'Extraverted':
                score += 2 * mentor.personality
            elif mentee.want == 'Introverted':
                score -= 2 * mentor.personality


            #chunk 5: time (max 25)
            if mentee.time == mentor.time:
                score += 25
            else:
                if mentee.time == "Once a month":
                    menteeTime = 3
                elif mentee.time == "Once every 2-3 weeks":
                    menteeTime = 2
                elif mentee.time == "Once a week":
                    menteeTime = 1

                if mentor.time == "Once a month":
                    mentorTime = 3
                elif mentor.time == "Once every 2-3 weeks":
                    mentorTime = 2
                elif mentor.time == "Once a week":
                    mentorTime = 1

                score += Math.pow(2, (menteeTime - mentorTime)) * 6

            menteePreferences[mentee][mentor] = score

    for mentor in mentorList:
        for mentee in menteeList:
            #chunk 1: hobbies/interests (max 20)
            piMatches = 0
            hobbyMatches = 0
            for pi in mentee.professionalInterests:
                if pi in mentor.professionalInterests:
                    piMatches += 1
            for hobby in mentee.hobbies:
                if hobby in mentor.hobbies:
                    hobbyMatches += 1
            score += piMatches / 24 * 15
            score += hobbyMatches / 17 * 5


            #chunk 2: location (max 20)
            score += 25 * (1 / 2 ** math.abs((mentee.utc - mentor.utc)))

            #chunk 3: occupation/major (max 25)
            if mentee.major == mentor.major:
                score += 15
            if mentee.occ == mentor.occ:
                score += 10

            #chunk 4: personality (max 10)
            if mentor.want == 'Extraverted':
                score += 2 * mentee.personality
            elif mentor.want == 'Introverted':
                score -= 2 * mentee.personality


            #chunk 5: time (max 25)
            if mentee.time == mentor.time:
                score += 25
            else:
                if mentee.time == "Once a month":
                    menteeTime = 3
                elif mentee.time == "Once every 2-3 weeks":
                    menteeTime = 2
                elif mentee.time == "Once a week":
                    menteeTime = 1

                if mentor.time == "Once a month":
                    mentorTime = 3
                elif mentor.time == "Once every 2-3 weeks":
                    mentorTime = 2
                elif mentor.time == "Once a week":
                    mentorTime = 1

                score += Math.pow(2, (mentorTime - menteeTime)) * 6

            mentorPreferences[mentor][mentee] = score


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

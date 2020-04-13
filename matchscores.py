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


            #chunk 2: location (max 15)
            if mentee.location == mentor.location:
                score += 15

            #chunk 3: occupation/major (max 25)
            if mentee.major == mentor.major:
                score += 15
            if mentee.occ == mentor.occ:
                score += 10

            #chunk 4: personality (max 10)
            if mentee.want == 'Extraverted'
                score += 2 * mentor.personality
            elif mentee.want == 'Introverted':
                score -= 2 * mentor.personality

            #chunk 5: experience (max 5)


            #chunk 6: time (max 25)

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


class Mentor:
    def __init__(self, email, phone, professional, interests, goal, location, major, occupation, introvert, preference, time, level):
        self.prof = professional
        self.inter = interests
        self.goal = goal
        self.loc = location
        self.maj = major
        self.occ = occupation
        self.intro = introvert
        self.pref = preference
        self.time = time
        self.lev = level

        self.score = 0

    def location_score(self, mentee):
        if self.loc == mentee.loc:
            self.score += 10

    def major_score(self, mentee):
        major = mentee.maj.split(',|\n| ')
        for i in major:
            for x in mentee.maj.split(',|\n| '):
                if i == x:
                    self.score += 10
                    break;




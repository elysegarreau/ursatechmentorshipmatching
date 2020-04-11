import csv

class Mentee:
    def __init__(self, email, first, last, phoneNum, prof_interests, hobbies, goal, location, major, job, personality, intro_extra, paired, meetings, block_exp, tech_exp, interest, importance):
        self.email = email
        self.first = first
        self.last = last
        self.phoneNum = phoneNum
        self.prof_interests = prof_interests
        self.hobbies = hobbies
        self.goal = goal
        self.location = location
        self.major = major
        self.job = job
        self.personality = personality
        self.intro_extra = intro_extra
        self.paired = paired
        self.meetings = meetings
        self.block_exp = block_exp
        self.tech_exp = tech_exp
        self.interest = interest
        self.importance = importance
        #self.menteesList = dict(zip(email, first, last, phoneNum, prof_interests, hobbies, goal, location, major, job, personality, intro_extra, paired, meetings, block_exp, tech_exp, interest, importance))

        def output_menteesList():
            menteesList = {}
            with open('samplementee.csv') as mentee_file:
                reader = csv.reader(mentee_file, delimiter=',')
                writer = csv.writer(mentee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for row in reader:
                    writer.writerow(row)
                #mentees_data = list(reader)
                #mentees_instances = [Mentee(i, mentees_data[0]) for i in mentees_data[1:]]
                for email, first, last, phoneNum, prof_interests, hobbies, goal, location, major, job, personality, intro_extra, paired, meetings, block_exp, tech_exp, interest, importance in reader:
                    menteesList.append(Mentee(email, first, last, phoneNum, prof_interests, hobbies, goal, location, major, job, personality, intro_extra, paired, meetings, block_exp, tech_exp, interest, importance)
            return menteesList

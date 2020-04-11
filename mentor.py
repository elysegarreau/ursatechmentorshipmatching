import csv

class Mentor:
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
        #self.mentorsList = dict(zip(email, first, last, phoneNum, prof_interests, hobbies, goal, location, major, job, personality, intro_extra, paired, meetings, block_exp, tech_exp, interest, importance))

        def output_mentorsList():
            mentorsList = {}
            with open('samplementor.csv') as mentor_file:
                reader = csv.reader(mentor_file, delimiter=',')
                writer = csv.writer(mentor_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for row in reader:
                    writer.writerow(row)
                #mentors_data = list(reader)
                #mentors_instances = [Mentee(i, mentees_data[0]) for i in mentees_data[1:]]
                for email, first, last, phoneNum, prof_interests, hobbies, goal, location, major, job, personality, intro_extra, paired, meetings, block_exp, tech_exp, interest, importance in reader:
                    mentorsList.append(Mentor(email, first, last, phoneNum, prof_interests, hobbies, goal, location, major, job, personality, intro_extra, paired, meetings, block_exp, tech_exp, interest, importance)
            return mentorsList

class Language:
    difficulty = 1
    proficiency = 1
    def study(self):
        # the first argument in a class method is the object itself
        self.proficiency += 1
        print(f"new proficiency level: {self.proficiency}")

french = Language()
i = 0
while i < 5:
    print("Studying French")
    french.study()
    i += 1

# Constructor
class Sport:
    def __init__(self, name, popularity = 1, skill = 0):
        self.name = name
        self.popularity = popularity
        self.skill = skill
    def train(self):
        print(f'Training {self.name}')
        self.skill += 1
        print(f'New skill: {self.skill}')

soccer = Sport('Soccer', 10, 1)
soccer.train()
    
# Inheritance
class Natural(Language):
    speakers_count = 0
    def avarage_wage(self):
        return (100 - self.speakers_count + super().proficiency) * super().difficulty

class Programming(Language):
    def __init__(self, open_source = False, object_oriented = False):
        self.open_source = open_source
        self.object_oriented = object_oriented
    def info(self):
        return self.difficulty, self.object_oriented, self.proficiency

english = Natural()
print(english.avarage_wage())

golang = Programming(True, False)
golang.study()
print(golang.info())
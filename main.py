class Student:
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
    
    def change_name(self, newname):
        self.name = str(newname)
        return (newname)
    
    def change_age(self, newage):
        self.age = int(newage)
        return (newage)

    def add_track (self, newtracks):
        newtracks = [(self.tracks).append(newtracks)]
        return (newtracks)
    
    def get_score(self):
        return (self.score)

Bob = Student("Bob", 26, ["FE","BE"], 20.90)

# Expected methods
#Bob.change_name("Peter")
#Bob.change_age(34)
#Bob.add_track("UI/UX")
#Bob.get_score()

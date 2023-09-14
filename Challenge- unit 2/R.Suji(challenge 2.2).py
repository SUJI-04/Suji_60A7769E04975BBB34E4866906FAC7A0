#Define tha base class player
class player:
    def play(self):
        print("the player is playing cricket.")

#Define the drived class Batsman
class Batsman(player):
    def play(self):
      print("the batsman is batting.")

#Define the derived class Bowler
class Bowler(player):
    def play(self):
        print("the bowler is bowling.")

#create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

#call tha play() method for each object
batsman.play()
bowler.play()

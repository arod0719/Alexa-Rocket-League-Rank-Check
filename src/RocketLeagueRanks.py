import json
import requests
import RLnumbers

class Ranks:
    
    def __init__(self, profile = "profile_error", name = "dontexist"):
        API = '' #put api key here
        response = requests.get("https://api.rlstats.net/v1/profile/stats?apikey=" + API + "&platformid=1&playerid=" + profile) #api call
        currentSeason = "15" #easily change current season
        self.name = name
        self.user = profile
        if(self.name != "dontexist" ):
            self.player = json.loads(response.text)
            self.player = self.player["RankedSeasons"][currentSeason]
        else:
            self.player = "Error" #if player doesn't exist error
        self.name = name
        self.user = profile

    #----------------------Check ranks or return error if profile doesn't exist-----------#    
        
    def duel(self): 
        if (self.player == "Error"):
            return("A username error has occurred, please make sure you add and select a name first")
        playlistVar = "10"
        return("In 1v1 Solo Duel " + self.name + " is " + RLnumbers.createRank(self.player[playlistVar]["Tier"],self.player[playlistVar]["Division"]) + " with " + str(self.player[playlistVar]["SkillRating"]) + " MMR")
        
    def doubles(self):
        if (self.player == "Error"):
            return("A username error has occurred, please make sure you add and select a name first")
        playlistVar = "11"
        return("In 2v2 Doubles " + self.name + " is " + RLnumbers.createRank(self.player[playlistVar]["Tier"],self.player[playlistVar]["Division"]) + " with " + str(self.player[playlistVar]["SkillRating"]) + " MMR")
        
    def standard(self):
        if (self.player == "Error"):
            return("A username error has occurred, please make sure you add and select a name first")
        playlistVar = "13"
        return("In 3v3 Standard " + self.name + " is " + RLnumbers.createRank(self.player[playlistVar]["Tier"],self.player[playlistVar]["Division"]) + " with " + str(self.player[playlistVar]["SkillRating"]) + " MMR")
          
    def solostandard(self):
        if (self.player == "Error"):
            return("A username error has occurred, please make sure you add and select a name first")
        return("As of Season 1, Solo Standard has been discontinued. Sorry!")
        
    def hoops(self):
        if (self.player == "Error"):
            return("A username error has occurred, please make sure you add and select a name first")
        playlistVar = "27"
        return("In 2v2 Hoops " + self.name + " is " + RLnumbers.createRank(self.player[playlistVar]["Tier"],self.player[playlistVar]["Division"]) + " with " + str(self.player[playlistVar]["SkillRating"]) + " MMR")
        
    def rumble(self):
        if (self.player == "Error"):
            return("A username error has occurred, please make sure you add and select a name first")
        playlistVar = "28"
        return("In 3v3 Rumble " + self.name + " is " + RLnumbers.createRank(self.player[playlistVar]["Tier"],self.player[playlistVar]["Division"]) + " with " + str(self.player[playlistVar]["SkillRating"]) + " MMR")
        
    def dropshot(self):
        if (self.player == "Error"):
            return("A username error has occurred, please make sure you add and select a name first")
        playlistVar = "29"
        return("In 3v3 Dropshot " + self.name + " is " + RLnumbers.createRank(self.player[playlistVar]["Tier"],self.player[playlistVar]["Division"]) + " with " + str(self.player[playlistVar]["SkillRating"]) + " MMR")
        
    def snowday(self):
        if (self.player == "Error"):
            return("A username error has occurred, please make sure you add and select a name first")
        playlistVar = "30"
        return("In 3v3 Snowday " + self.name + " is " + RLnumbers.createRank(self.player[playlistVar]["Tier"],self.player[playlistVar]["Division"]) + " with " + str(self.player[playlistVar]["SkillRating"]) + " MMR")
        
    def seasonrank(self):
        if (self.player == "Error"):
            return("A username error has occurred, please make sure you add and select a name first")
        return(self.name + RLnumbers.createRewards(self.player["RewardLevel"]["SeasonLevel"],self.player["RewardLevel"]["SeasonLevelWins"]))

    def all(self):
        if (self.player == "Error"):
            return("A username error has occurred, please make sure you add and select a name first")
        answer = ''
        answer = self.duel() + ". " + self.doubles() + ". " + self.standard() + ". " + self.solostandard() + ". " + self.hoops() + ". " + self.rumble() + ". " + self.dropshot() + ". " + self.snowday() + ". " + self.seasonrank() + ". "
        return (answer)
    
    def test(self): #tests if user has an error
        if (self.player == "Error"):
            return("Error")
        return("Success")
        



        



import json
import requests
import RLnumbers

class Ranks:
    
    def __init__(self, profile = 'karmajuney', name= 'Alex'):
        ADD_KEY_HERE = ''
        response = requests.get("https://api.rlstats.net/v1/profile/stats?apikey=" + ADD_KEY_HERE "&platformid=1&playerid=" + profile) #api request
        currentSeason = "12" #easy way to change season
        try:
            self.player = json.loads(response.text) #convert from json to dic
            self.player = self.player["RankedSeasons"][currentSeason] #only get info from this season
        except:
            self.player = "Error" #if that name doesn't exist, set error
        self.name = name

    #------------------------------------------Create Playlists--------------------------------------#    
        
    def duel(self):
        if (self.player == "Error"):
            return("A username error has occurred")
        playlistVar = "10"
        return("In 1v1 Solo Duel " + self.name + " is " + RLnumbers.createRank(self.player[playlistVar]["Tier"],self.player[playlistVar]["Division"]) + " with " + str(self.player[playlistVar]["SkillRating"]) + " MMR")
        
    def doubles(self):
        if (self.player == "Error"):
            return("A username error has occurred")
        playlistVar = "11"
        return("In 2v2 Doubles " + self.name + " is " + RLnumbers.createRank(self.player[playlistVar]["Tier"],self.player[playlistVar]["Division"]) + " with " + str(self.player[playlistVar]["SkillRating"]) + " MMR")
        
    def standard(self):
        if (self.player == "Error"):
            return("A username error has occurred")
        playlistVar = "13"
        return("In 3v3 Standard " + self.name + " is " + RLnumbers.createRank(self.player[playlistVar]["Tier"],self.player[playlistVar]["Division"]) + " with " + str(self.player[playlistVar]["SkillRating"]) + " MMR")
          
    def solostandard(self):
        if (self.player == "Error"):
            return("A username error has occurred")
        playlistVar = "12"
        return("In 3v3 Solo Standard " + self.name + " is " + RLnumbers.createRank(self.player[playlistVar]["Tier"],self.player[playlistVar]["Division"]) + " with " + str(self.player[playlistVar]["SkillRating"]) + " MMR")
        
    def hoops(self):
        if (self.player == "Error"):
            return("A username error has occurred")
        playlistVar = "27"
        return("In 2v2 Hoops " + self.name + " is " + RLnumbers.createRank(self.player[playlistVar]["Tier"],self.player[playlistVar]["Division"]) + " with " + str(self.player[playlistVar]["SkillRating"]) + " MMR")
        
    def rumble(self):
        if (self.player == "Error"):
            return("A username error has occurred")
        playlistVar = "28"
        return("In 3v3 Rumble " + self.name + " is " + RLnumbers.createRank(self.player[playlistVar]["Tier"],self.player[playlistVar]["Division"]) + " with " + str(self.player[playlistVar]["SkillRating"]) + " MMR")
        
    def dropshot(self):
        if (self.player == "Error"):
            return("A username error has occurred")
        playlistVar = "29"
        return("In 3v3 Dropshot " + self.name + " is " + RLnumbers.createRank(self.player[playlistVar]["Tier"],self.player[playlistVar]["Division"]) + " with " + str(self.player[playlistVar]["SkillRating"]) + " MMR")
        
    def snowday(self):
        if (self.player == "Error"):
            return("A username error has occurred")
        playlistVar = "30"
        return("In 3v3 Snowday " + self.name + " is " + RLnumbers.createRank(self.player[playlistVar]["Tier"],self.player[playlistVar]["Division"]) + " with " + str(self.player[playlistVar]["SkillRating"]) + " MMR")
        
    def seasonrank(self):
        if (self.player == "Error"):
            return("A username error has occurred")
        return(self.name + RLnumbers.createRewards(self.player["RewardLevel"]["SeasonLevel"],self.player["RewardLevel"]["SeasonLevelWins"]))

    def all(self):
        if (self.player == "Error"):
            return("A username error has occurred")
        answer = ''
        answer = self.duel() + ". " + self.doubles() + ". " + self.standard() + ". " + self.solostandard() + ". " + self.hoops() + ". " + self.rumble() + ". " + self.dropshot() + ". " + self.snowday() + ". " + self.seasonrank() + ". "
        return (answer)

        



        



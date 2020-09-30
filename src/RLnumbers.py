ranks = ["Unranked","Bronze 1","Bronze 2","Bronze 3",
         "Silver 1","Silver 2", "Silver 3",
         "Gold 1", "Gold 2", "Gold 3",
         "Platinum 1", "Platinum 2", "Platinum 3",
         "Diamond 1", "Diamond 2", "Diamond 3",
         "Champion 1", "Champion 2", "Champion 3",
         "Grand Champion 1", "Grand Champion 2", "Grand Champion 3",
         "Supersonic Legend"]
#ranks is used to determine tier levels

seasonlevels = ["Unranked", "Bronze", "Silver", "Gold",
                "Platinum", "Diamond", "Champion", "Grand Champion", "Supersonic Legend"]

#seasonlevels is used to convert int into season reward level

def createRank(tier, division): #create a readable string of the users rank and division
    division = int(division) + 1 
    tier = ranks[int(tier)]
    return (tier + " division " + str(division))
    


def createRewards(level, wins): #create a readable string for user season reward rank
    if (int(level) == 8):
        return (" is currently at Supersonic Legend rewards")
    rank = seasonlevels[int(level)]
    return (" is currently at " + rank + " rewards with " + str(wins) + " out of 10 wins")

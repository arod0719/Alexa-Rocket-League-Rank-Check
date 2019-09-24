from lxml import html
from lxml import etree
import requests

class Ranks:

    def __init__(self, profile = 'karmajuney', name = 'Alex'):
        self.profile = 'https://rlstats.net/profile/Steam/' + profile
        self.playlist = []
        self.rank = []
        self.division = []
        self.mmr = []
        self.seasonrewards = []
        self.name = name
        self.user = profile
        page = requests.get(self.profile)
        html_content = html.fromstring(page.content)
        self.html_content = html_content       
        self.createRanks()
            
        
    def createRanks(self):
        self.playlist.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[1]/tr[1]/th[1]/text()'))).strip())
        self.playlist.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[1]/tr[1]/th[2]/text()'))).strip())
        self.playlist.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[1]/tr[1]/th[3]/text()'))).strip())
        self.playlist.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[1]/tr[1]/th[4]/text()'))).strip())
        self.playlist.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[2]/tr[1]/th[1]/text()'))).strip())
        self.playlist.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[2]/tr[1]/th[2]/text()'))).strip())
        self.playlist.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[2]/tr[1]/th[3]/text()'))).strip())
        self.playlist.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[2]/tr[1]/th[4]/text()'))).strip())


        self.rank.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[1]/tr[2]/td[1]/text()'))).strip())
        self.rank.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[1]/tr[2]/td[2]/text()'))).strip())
        self.rank.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[1]/tr[2]/td[3]/text()'))).strip())
        self.rank.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[1]/tr[2]/td[4]/text()'))).strip())
        self.rank.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[2]/tr[2]/td[1]/text()'))).strip())
        self.rank.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[2]/tr[2]/td[2]/text()'))).strip())
        self.rank.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[2]/tr[2]/td[3]/text()'))).strip())
        self.rank.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[2]/tr[2]/td[4]/text()'))).strip())


        self.division.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[1]/tr[3]/td[1]/text()'))).strip())
        self.division.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[1]/tr[3]/td[2]/text()'))).strip())
        self.division.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[1]/tr[3]/td[3]/text()'))).strip())
        self.division.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[1]/tr[3]/td[4]/text()'))).strip())
        self.division.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[2]/tr[3]/td[1]/text()'))).strip())
        self.division.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[2]/tr[3]/td[2]/text()'))).strip())
        self.division.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[2]/tr[3]/td[3]/text()'))).strip())
        self.division.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[2]/tr[3]/td[4]/text()'))).strip())


        self.mmr.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[1]/tr[4]/td[1]/text()'))).strip())
        self.mmr.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[1]/tr[4]/td[2]/text()'))).strip())
        self.mmr.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[1]/tr[4]/td[3]/text()'))).strip())
        self.mmr.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[1]/tr[4]/td[4]/text()'))).strip())
        self.mmr.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[2]/tr[4]/td[1]/text()'))).strip())
        self.mmr.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[2]/tr[4]/td[2]/text()'))).strip())
        self.mmr.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[2]/tr[4]/td[3]/text()'))).strip())
        self.mmr.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[2]/table[2]/tr[4]/td[4]/text()'))).strip())


        self.seasonrewards.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/h2/text()'))).strip())
        self.seasonrewards.append(''.join((self.html_content.xpath('//*[@id="skills"]/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/h2/span[1]/text()'))).strip())
        

    def duel(self):
        if (self.playlist[0] == ''):
            return("A username error has occurred")
        return("In " + self.playlist[0] + " "+ self.name + " is " + self.rank[0] + " " + self.division[0] + " with " + self.mmr[0] + " MMR")
        
    def doubles(self):
        if (self.playlist[1] == ''):
            return("A username error has occurred")
        return("In " + self.playlist[1] + " "+ self.name + " is " + self.rank[1] + " " + self.division[1] + " with " + self.mmr[1] + " MMR")
             
    def standard(self):
        if (self.playlist[2] == ''):
            return("A username error has occurred")
        return("In " + self.playlist[2] + " "+ self.name + " is " + self.rank[2] + " " + self.division[2] + " with " + self.mmr[2] + " MMR")
              
    def solostandard(self):
        if (self.playlist[3] == ''):
            return("A username error has occurred")
        return("In " + self.playlist[3] + " "+ self.name + " is " + self.rank[3] + " " + self.division[3] + " with " + self.mmr[3] + " MMR")
              
    def hoops(self):
        if (self.playlist[4] == ''):
            return("A username error has occurred")
        return("In " + self.playlist[4] + " "+ self.name + " is " + self.rank[4] + " " + self.division[4] + " with " + self.mmr[4] + " MMR")
              
    def rumble(self):
        if (self.playlist[5] == ''):
            return("A username error has occurred")
        return("In " + self.playlist[5] + " "+ self.name + " is " + self.rank[5] + " " + self.division[5] + " with " + self.mmr[5] + " MMR")
              
    def dropshot(self):
        if (self.playlist[6] == ''):
            return("A username error has occurred")
        return("In " + self.playlist[6] + " "+ self.name + " is " + self.rank[6] + " " + self.division[6] + " with " + self.mmr[6] + " MMR")
              
    def snowday(self):
        if (self.playlist[7] == ''):
            return("A username error has occurred")
        return("In " + self.playlist[7] + " "+ self.name + " is " + self.rank[7] + " " + self.division[7] + " with " + self.mmr[7] + " MMR")

    def seasonrank(self):
        if (self.playlist[0] == ''):
            return("A username error has occurred")
        if (self.seasonrewards[1] == ''):
            self.seasonrewards[1] = '10'
        return(self.name + " is currently at " + self.seasonrewards[0] + " rewards, with " + self.seasonrewards[1] + " out of 10 wins")

    def all(self):
        if (self.playlist[0] == ''):
            return("A username error has occurred")
        answer = ''
        for i in range(8):
            answer = answer + (" In " + self.playlist[i] + " "+ self.name + " is " + self.rank[i] + " " + self.division[i] + " with " + self.mmr[i] + " MMR. ")
        return (answer)

        



        


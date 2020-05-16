'''
Written By SHUcream00(https://github.com/SHUcream00)
Everything's under constructions for now

disclaimer: I do not own the data you might get by running this script. Check MLB Advanced Media, L.P's copyright
'''

import requests
from bs4 import BeautifulSoup as bs

class mlb():

    def __init__(self):
        self.test_string = "https://www.mlb.com/dodgers/search?q={0}"
        self.suggestion = "https://suggest.mlb.com/svc/suggest/v1/min_all/{0}/99999"
        self.player_page = "https://www.mlb.com/player/{0}"
        self.pitcher_zone = "https://baseballsavant.mlb.com/player/zone?player_id={0}&player_type=pitcher&season={1}&hfGT=R|" #player id, year
        self.player_api = "https://statsapi.mlb.com/api/v1/people/{0}" #player id
        self.player_api2 = "https://statsapi.mlb.com/api/v1/people/{0}?hydrate=currentTeam,team, \
                            stats(type=[yearByYear,yearByYearAdvanced,careerRegularSeason,careerAdvanced,availableStats](team(league)),leagueListId=mlb_hist)"
        self.team_api = "https://statsapi.mlb.com/api/v1/teams?sportId=1&language=en&leagueListId=mlb_hist&activeStatus=B&season={0}" #year
        self.roster_api = "https://statsapi.mlb.com/api/v1/teams/{0}/roster?hydrate=person&language=en&season={1}&rosterType=40Man" #team, year

    def get_player_info(self, *args, **kwargs):

        #Get a player's personal information from MLB.com
        player_string = kwargs['player'].replace(chr(32), '%20')
        try:
            r = requests.get(self.suggestion.format(player_string))
            print(r, type(r))
            cands = list(map(lambda x: (x.split('|')[8], x.split('|')[1], x.split('|')[9]), r.json()['suggestions']))
            print(cands, len(cands), cands[0][2])


            #Player selection part
            #If there's just one automatically go for it
            if len(cands) == 1: raw_text = requests.get(self.player_page.format(cands[0][2])).text
            else:
                #Need to get user input via input()
                cands_2 = [i[0] for i in cands]
                print("Hey, I found these guys, which one do you want? {0}\n".format(cands_2))
                answer_2 = input("Choose One...")
                if answer_2 not in cands_2: raise Exception


            soup = bs(raw_text, 'lxml')
            ##player search part can be changed so that
            player_img = soup.find(alt=cands[0][0])['src']
            player_info = self.getplayerinfo(cands[0][1])
            #basic info

            return r

        except Exception as error:
            print("Error occurred: {0}".format(error))
            return 0

    def getplayerinfo(self, id):
        #Get a player's current stats
        if not id: return
        raw = requests.get(self.player_api.format(id)).json()["people"]
        '''
        lots of params
        '''
        f
        pass

    def getplayerstat(self, id):
        #Get a player's current stats
        if not id: return
        pass

    def getgameinfo(*arg, **kwargs):
        #gameday API?
        pass

    def getschedule(*arg, **kwargs):
        #schedules page
        pass

    def getstanding(*args, **kwargs):
        #standings page
        pass

    def test():
        r = requests.get("https://www.mlb.com/player/mike-trout-545361")
        t = r.text
        soup = BS(t, "lxml").encode("utf-8")
        print(soup)

if __name__ == "__main__":
    actual = mlb()
    actual.get_player_info(player = "blah blah")


#test = mlb()
#test.get_player_info(player = "clayton kershaw")


#mlb.test()

'''
Written By Joon Choi aka SHUcream00(https://github.com/SHUcream00)
Everything's under constructions for now

disclaimer: I do not own the data you might get by running this script.

The accounts, descriptions, data and presentation in the referring page (the "Materials") are proprietary content of MLB Advanced Media, L.P ("MLBAM").
Only individual, non-commercial, non-bulk use of the Materials is permitted and any other use of the Materials is prohibited without prior written authorization from MLBAM.
Authorized users of the Materials are prohibited from using the Materials in any commercial manner other than as expressly authorized by MLBAM.
'''

import requests
from bs4 import BeautifulSoup as bs

class mlb():

    def __init__(self):
        self.test_string = "https://www.mlb.com/dodgers/search?q={0}"
        self.suggestion = "https://suggest.mlb.com/svc/suggest/v1/min_all/{0}/99999"
        self.player_page = "https://www.mlb.com/player/{0}"
        self.pitcher_zone = "https://baseballsavant.mlb.com/player/zone?player_id={0}&player_type=pitcher&season={1}&hfGT=R|" #player id, year
        self.player_api = "https://statsapi.mlb.com/api/v1/people/{0}"
        self.player_api2 = "https://statsapi.mlb.com/api/v1/people/{0}?hydrate=currentTeam,team, \
                            stats(type=[yearByYear,yearByYearAdvanced,careerRegularSeason,careerAdvanced,availableStats](team(league)),leagueListId=mlb_hist)"
        self.team_api = "https://statsapi.mlb.com/api/v1/teams?sportId=1&language=en&leagueListId=mlb_hist&activeStatus=B&season={0}" #year
        self.roster_api = "https://statsapi.mlb.com/api/v1/teams/{0}/roster?hydrate=person&language=en&season={1}&rosterType=40Man" #team, year

    def get_player_info(self, *args, **kwargs):

        #Get a player's personal information from MLB.com
        player_string = kwargs['player'].replace(chr(32), '%20')
        try:
            r = requests.get(self.suggestion.format(player_string))
            cands = list(map(lambda x: (x.split('|')[8], x.split('|')[9]), r.json()['suggestions']))
            print(cands, len(cands), cands[0][1])

            if len(cands) == 1:
                raw_text = requests.get(self.player_page.format(cands[0][1])).text
                soup = bs(raw_text, 'lxml')
                player_img = soup.find(alt=cands[0][0])['src']
                player_bio = soup.find(class='player-bio')
                print(player_bio)


            else:
                #ask user to select one player
                pass

            return r

        except Exception as error:
            print("Error occurred: {0}".format(error))
            return 0

    def get_playet_stats(*args, **kwargs):
        #Get a player's current stats
        pass

    def get_game_info(*arg, **kwargs):
        pass

    def get_future_schedule(*arg, **kwargs):
        pass

    def get_standings(*args, **kwargs):
        pass
    def test():
        r = requests.get("https://www.mlb.com/player/mike-trout-545361")
        t = r.text
        soup = BS(t, "lxml").encode("utf-8")
        print(soup)

test = mlb()
test.get_player_info(player = "clayton kershaw")
#mlb.test()

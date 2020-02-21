import requests
from bs4 import BeautifulSoup as bs

class mlb():

    def __init__(self):
        self.test_string = "https://www.mlb.com/dodgers/search?q={0}"
        self.suggestion = "https://suggest.mlb.com/svc/suggest/v1/min_all/{0}/99999"
        self.player_page = "https://www.mlb.com/player/{0}"

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

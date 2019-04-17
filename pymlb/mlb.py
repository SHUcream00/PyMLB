import requests
from bs4 import BeautifulSoup as BS

class mlb():

    def get_player_info(*args, **kwargs):

        #Get a player's personal information from MLB.com
        print(kwargs)
        TEST_STRING = "https://www.mlb.com/dodgers/search?q={0}"
        SUGGESTION = "https://suggest.mlb.com/svc/suggest/v1/min_all/{0}/99999"
        PLAYER_PAGE = "https://www.mlb.com/player/{0}"
        try:
            r = requests.get(SUGGESTION.format(kwargs['player']))
            for i,j in enumerate(r.json()['suggestions']):
                print(i, j)
                if i == 0:
                    plchldr1 = str(j).split('|')
                    print(plchldr1)
                    for k, l  in enumerate(plchldr1):
                        print(k, len(plchldr1))
                        if k == len(plchldr1) - 1:
                            r2 = requests.get(PLAYER_PAGE.format(l))
                            print(r2.text)
            return r
        except:
            return 0;

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

#mlb.get_player(player = "trout")
mlb.test()

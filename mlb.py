import aiohttp
import request

class mlb():

    def get_player(*arg, **kwargs):

        TEST_STRING = "https://www.mlb.com/dodgers/search?q=clad"
        SUGGESTION = "https://suggest.mlb.com/svc/suggest/v1/min_all/{0}/99999"
        

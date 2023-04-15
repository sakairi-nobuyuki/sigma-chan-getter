# coding: utf-8
import twint
import nest_asyncio

nest_asyncio.apply()

class TweetGetter:
    def __init__(self) -> None:
        self.c = twint.Config()
        
        # self.c.Images = True
        # self.c.Videos = True
        self.c.Limit = 1
        self.c.Store_csv = True
        self.c.output = "hoge.csv"

    def get(self, user_name: str):
        self.c.Username = user_name
        print("user name to serach: ", self.c.Username)
        return twint.run.Search(self.c)




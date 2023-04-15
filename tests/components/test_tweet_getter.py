# coding: utf-8

from sigma_chan_getter.components import TweetGetter


class TestTweetGetter:
    getter = TweetGetter()

    def test_init(self):
        assert isinstance(self.getter, TweetGetter)

    def test_get(self):
        print(self.getter.get("sohbunshu"))
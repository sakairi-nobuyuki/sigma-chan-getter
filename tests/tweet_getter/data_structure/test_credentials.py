# coding: utf-8

from sigma_chan_getter_robo.tweet_getter.data_structure import GetterRoboCredentials


class TestGetterRoboCredentials:
    def test_getter_robo_credentials(self):
        credentials = GetterRoboCredentials()

        print(credentials.access_token)

        assert isinstance(credentials, GetterRoboCredentials)

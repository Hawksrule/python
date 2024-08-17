import unittest
from television import *

class TestTelevision(unittest.TestCase):
    def test_television(self):
        self.assertEqual(Television().__str__(), f"Power - False, Channel - 0, Volume - 0")

    def test_power(self):
        tele = Television()
        tele.power()
        self.assertEqual(tele.__str__(), f"Power - True, Channel - 0, Volume - 0")
        tele.power()
        self.assertEqual(tele.__str__(), f"Power - False, Channel - 0, Volume - 0")

    def test_mute(self):
        tele = Television()
        tele.power()
        tele.volume_up()
        tele.mute()
        self.assertEqual(tele.__str__(), f"Power - True, Channel - 0, Volume - 0")
        tele.mute()
        self.assertEqual(tele.__str__(), f"Power - True, Channel - 0, Volume - 1")
        tele.power()
        tele.mute()
        self.assertEqual(tele.__str__(), f"Power - False, Channel - 0, Volume - 1")
        tele.mute()
        self.assertEqual(tele.__str__(), f"Power - False, Channel - 0, Volume - 1")

    def test_channel_up(self):
        tele = Television()
        tele.channel_up()
        self.assertEqual(tele.__str__(), f"Power - False, Channel - 0, Volume - 0")
        tele.power()
        tele.channel_up()
        self.assertEqual(tele.__str__(), f"Power - True, Channel - 1, Volume - 0")
        tele.channel_up()
        tele.channel_up()
        tele.channel_up()
        self.assertEqual(tele.__str__(), f"Power - True, Channel - 0, Volume - 0")

    def test_channel_down(self):
        tele = Television()
        tele.channel_down()
        self.assertEqual(tele.__str__(), f"Power - False, Channel - 0, Volume - 0")
        tele.power()
        tele.channel_down()
        self.assertEqual(tele.__str__(), f"Power - True, Channel - 3, Volume - 0")

    def test_volume_up(self):
        tele = Television()
        tele.volume_up()
        self.assertEqual(tele.__str__(), f"Power - False, Channel - 0, Volume - 0")
        tele.power()
        tele.volume_up()
        self.assertEqual(tele.__str__(), f"Power - True, Channel - 0, Volume - 1")
        tele.mute()
        tele.volume_up()
        self.assertEqual(tele.__str__(), f"Power - True, Channel - 0, Volume - 2")
        tele.volume_up()
        self.assertEqual(tele.__str__(), f"Power - True, Channel - 0, Volume - 2")

    def test_volume_down(self):
        tele = Television()
        tele.volume_down()
        self.assertEqual(tele.__str__(), f"Power - False, Channel - 0, Volume - 0")
        tele.power()
        tele.volume_up()
        tele.volume_up()
        tele.volume_down()
        self.assertEqual(tele.__str__(), f"Power - True, Channel - 0, Volume - 1")
        tele.volume_up()
        tele.mute()
        tele.volume_down()
        self.assertEqual(tele.__str__(), f"Power - True, Channel - 0, Volume - 1")
        tele.volume_down()
        tele.volume_down()
        self.assertEqual(tele.__str__(), f"Power - True, Channel - 0, Volume - 0")

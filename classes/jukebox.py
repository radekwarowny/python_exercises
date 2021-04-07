#!/usr/bin/env python

"""jukebox.py: Simple implementation of MVC pattern."""

__author__      = "Radek Warowny"


PRICE_PER_SONG = 1.20

# Model


class Song:
    def __init__(self, name, artist, genre, artwork):
        self.artist = artist
        self.name = name
        self.genre = genre
        self.artwork = artwork


class Library:
    def __init__(self):
        self.songs = []


class ServiceInfo:
    def __init__(self, status, engineer_name):
        self.service_date = datetime.now()
        seft.status = status
        self.engineer = engineer_name


# View


class Touchscreen:
    def select_song(self):
        pass

    def prompt_for_next_song(self, song):
        for song in songs:
            # display the song
            pass
        return "Dark Chest for Wonders"


class Speakers:
    def __init__(self):
        self.volume = 5

    def get_louder(self):
        self.volume += 1

    def get_quiter(self):
        self.volume -= 1

    def play_song(self, song):
        pass


class CoinSlot:
    def __init__(self, float_):
        self.amount = float_

    def requrest_money(self, amount):
        # wait for money
        # give change
        self.amount += amount
        return True


# Controller


class Controller:
    def __init__(self):
        self.library = Library()
        self.service_history = []
        self.audio_output = Speakers()
        self.ui = Touchscreen()
        self.bank = CoinBox()

    def play_next_song(self):
        songs_to_suggest = []
        for song in self.library:
            # filter logic
            songs_to_suggest.append(song)
        chosen_song = self.ui.prompt_for_next_song(songs_to_suggest)
        requrest_money(PRICE_PER_SONG)
        self.audio_output.play_song(chosen_song)

    # Lots more functions go here


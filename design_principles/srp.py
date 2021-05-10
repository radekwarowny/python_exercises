# Single Responsibility Principle (a.k.a Separation of Concern)

"""
The Single Responsibility Principle states that a class should only have one primary responsibility and should not take other responsibilities. 
"""
# Example 1

class Album:
    def __init__(self, name, artist, songs):
        self.name = name
        self.artist = artist
        self.songs = list(songs)

    def add_song(self, song):
        self.songs.append(song)

    def delete_song(self, song):
        self.songs.remove(song)

    """
    What if I now want to add 'search by song' functionality to this class? 
    - In order to add features to this class it would be best to create separate classess that extend the Album class functionality. 
    """

    # Additional feature

    # def search_song(self, song):
    #     if song in self.songs:
    #         print('Song present')
    #     else:
    #         print('Song not found')


    def __str__(self):
        return f"Album - {self.name} by {self.artist} Tracklist: {self.songs}"



class AlbumBrowser:
    def __init__(self, album):
        self.album = album
        
    def search_by_song(self):
        song = input("Search for song: ")
        if song in self.album.songs:
            print('Song found')
        else:
            print('Song not found')

songs = ['song 1', 'song 2', 'song 3']
album_1 = Album('Nirvana', 'Radek', songs)

print(album_1.__str__())


browser = AlbumBrowser(album_1)

browser.search_by_song()

browser.search_by_song()

print()
# Example 2

class TelephoneDirectory:
    def __init__(self):
        self.telephone_directory = {}

    def add_entry(self, name, number):
        self.telephone_directory[name] = number

    def delete_entry(self, name):
        self.telephone_directory.pop(name)

    def update_entry(self, name, number):
        self.telephone_directory[name] = number

    def lookup_entry(self, name):
        if name in self.telephone_directory:
            return self.telephone_directory[name]
        return "Entry not found"

    # Additional feature

    # def save_to_file(self):
    #     print(self.telephone_directory)
    #     print('Directory Saved to File')

    # def save_to_database(self):
    #     print(self.telephone_directory)
    #     print('Directory Saved to Database')

    def __str__(self):
        ret_dct = ""
        for key, value in self.telephone_directory.items():
            ret_dct += f"{key}: {value}\n"
        return ret_dct

class DirectorySaver:
    def __init__(self, directory):
        self.directory = directory

    def save_to_file(self):
        print(self.directory)
        print('Directory Saved to File')

    def save_to_database(self):
        print(self.directory)
        print('Directory Saved to Database')

my_dir = TelephoneDirectory()

my_dir.add_entry('radek', '12345')
my_dir.add_entry('tina', '23456')
my_dir.add_entry('connor', '34567')

print(my_dir.__str__())
print(my_dir.lookup_entry('tina'))

my_dir.delete_entry('connor')
my_dir.update_entry('tina', '000000')

print()
print(my_dir.__str__())
print()

saver = DirectorySaver(my_dir)
saver.save_to_file()
saver.save_to_database()

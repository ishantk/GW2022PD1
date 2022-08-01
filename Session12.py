class Song:

    # Add attributes to the Object
    # With default values
    def __init__(self, track="", artists="", duration=0.0):
        self.track = track
        self.artists = artists
        self.duration = duration
        self.next_song = None
        self.previous_song = None

    # To show the object data
    def show(self):
        print("------------------------")
        print(self.track, "[", self.duration, " mins ]")
        print(self.artists)
        print("------------------------")


# Song PlayList -> Linked List (Doubly Circular)
class PlayList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        print("[PlayList] Created...")

    def append(self, song):
        self.size += 1

        if self.head is None:
            self.head = song
            self.tail = song
        else:
            self.tail.next_song = song
            song.previous_song = self.tail
            self.tail = song

    def iterate(self, direction=1):

        if direction == 1:
            print("ITERATING FORWARD")
            temp = self.head
            while True:

                temp.show()
                temp = temp.next_song

                if temp.next_song is None:
                    temp.show()
                    break
        else:
            print("ITERATING BACKWARD")
            temp = self.tail
            while True:

                temp.show()
                temp = temp.previous_song

                if temp.previous_song is None:
                    temp.show()
                    break

play_list = PlayList()
print("play_list:", play_list, "Data:", vars(play_list))

song1 = Song(track="1. Kesariya", artists="Pritam, Arijit Singh", duration=4.3)
print("song1:", song1, "Data:", vars(song1))

song2 = Song(track="2. Peaches", artists="Diljit", duration=3.5)
print("song2:", song2, "Data:", vars(song2))

song3 = Song(track="3. Left and Right", artists="Charlie", duration=2.7)
print("song3:", song3, "Data:", vars(song3))

song4 = Song(track="4. Fitoor", artists="Arijit Singh", duration=5.7)
print("song4:", song4, "Data:", vars(song4))

song5 = Song(track="5. SYL", artists="Sidhu MW", duration=3.5)
print("song5:", song5, "Data:", vars(song5))


play_list.append(song=song1)
play_list.append(song=song2)
play_list.append(song=song3)
play_list.append(song=song4)
play_list.append(song=song5)

print("Size of PlayList is: ", play_list.size)

'''

song4 = Song(track="Fitoor", artists="Arijit Singh", duration=5.7)
song5 = Song(track="SYL", artists="Sidhu MW", duration=3.5)
'''

print("AFTER SONGS ADDED IN PLAYLIST")
print("song1:", song1, "Data:", vars(song1))
print("song2:", song2, "Data:", vars(song2))
print("song3:", song3, "Data:", vars(song3))
print("song4:", song4, "Data:", vars(song4))
print("song5:", song5, "Data:", vars(song5))


play_list.iterate(direction=2)
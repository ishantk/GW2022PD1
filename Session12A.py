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

    def insert_head(self):
        pass

    def insert_in_between(self, song1, song2):
        pass

    def delete_head(self):
        self.size -= 1
        temp = self.head
        self.head = self.head.next_song
        del temp

    def delete_tail(self):
        self.size -= 1
        temp = self.tail
        self.tail = self.tail.previous_song
        del temp
        # Find the Bug and Fix it :)

    def delete(self, song):
        pass


play_list = PlayList()
print("play_list:", play_list, "Data:", vars(play_list))

play_list.append(Song(track="1. Kesariya", artists="Pritam, Arijit Singh", duration=4.3))
play_list.append(Song(track="2. Peaches", artists="Diljit", duration=3.5))
play_list.append(Song(track="3. Left and Right", artists="Charlie", duration=2.7))
play_list.append(Song(track="4. Fitoor", artists="Arijit Singh", duration=5.7))
play_list.append(Song(track="5. SYL", artists="Sidhu MW", duration=3.5))

# play_list.iterate()

play_list.delete_head()
play_list.delete_tail()

play_list.delete(Song(track="3. Left and Right", artists="Charlie", duration=2.7))

play_list.iterate()
print("play_list size:", play_list.size)

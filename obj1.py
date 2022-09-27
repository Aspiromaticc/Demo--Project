class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
happy_bday = Song(["All the times are changing. \nWe're here, we are breathing, is enough for everyone of us"])
crumbles_and_cracks = Song(["Everyone is taking sides\n And they asked for what we're standing for"])
happy_bday.sing_me_a_song()
crumbles_and_cracks.sing_me_a_song()

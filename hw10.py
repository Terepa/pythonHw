# 1. Song class


class Song:
    def __init__(self, title, author, lyrics):

        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f"New Song made {title} by {author}")

    def sing(self, ):
        self.do_lyrics(self.lyrics)
        return self

    def yell(self, ):
        capital_lyrics = self.lyrics.upper()
        self.do_lyrics(capital_lyrics)
        return self

    def do_lyrics(self, lyrics):
        print(lyrics)



new_song = Song("Habits", "Ed Sheeran", "My bad habits lead to you")
new_song.sing()
new_song.yell()
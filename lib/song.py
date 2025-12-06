class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increase total song count
        Song.count += 1

        # Track genres list
        if genre not in Song.genres:
            Song.genres.append(genre)

        # Track artists list
        if artist not in Song.artists:
            Song.artists.append(artist)

        # Count number of songs per genre
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        # Count number of songs per artist
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

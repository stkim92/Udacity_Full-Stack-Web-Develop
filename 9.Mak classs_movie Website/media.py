import webbrowser

# This is Movie class including movie title, storyline, image, trailer_url.
class Movie():
    def __init__(self, movie_title, movie_storyline, movie_image, youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_image
        self.trailer_youtube_url = youtube_url

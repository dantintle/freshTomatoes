import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
    #define class variable
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    #define function init-self (like this in JS, points to whatever is being init)
    def __init__(self, movieTitle, movieStoryline, posterImage, trailerUrl, rating):
        self.title = movieTitle
        self.storyline = movieStoryline
        self.poster_image_url = posterImage
        self.trailer_youtube_url = trailerUrl
        self.rating = rating

    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)
    

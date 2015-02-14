#import media.py file/fresh_tomatoes
import media
import fresh_tomatoes

#moduleName.className. toyStory instance of movie class from media module
#init (constructor) creates memory for movie instances
mysteryTeam = media.Movie("Mystery Team",
                       "A story of a murder",
                       "http://upload.wikimedia.org/wikipedia/en/d/d0/Mystery_Team.jpg",
                       "https://www.youtube.com/watch?v=hMxEe2gnaQY",
                          "4.5 tomatoes out of 5")


iLoveYouMan = media.Movie("I Love You Man",
                          "A story of a man searching for a friend",
                          "http://www.impawards.com/2009/posters/i_love_you_man_xlg.jpg",
                          "https://www.youtube.com/watch?v=um5DuTLzw-I",
                          "4 tomatoes out of 5")


hotRod = media.Movie("Hot Rod",
                     "A story of a man chasing his dreams",
                     "http://upload.wikimedia.org/wikipedia/en/7/7f/Hot-rod-poster.jpg",
                     "https://www.youtube.com/watch?v=DhdrA9qz79o",
                     "3.5 tomatoes out of 5")


anchorman = media.Movie("Anchorman: The Legend of Ron Burgundy",
                        "A story of a man learning to accept a new status quo",
                        "https://www.movieposter.com/posters/archive/main/77/MPW-38721",
                        "https://www.youtube.com/watch?v=NJQ4qEWm9lU",
                        "4 tomatoes out of 5")

ghostbusters = media.Movie("Ghostbusters",
                           "Bill Murray and friends fight ghosts",
                           "http://upload.wikimedia.org/wikipedia/en/c/c7/Ghostbusters_cover.png",
                           "https://www.youtube.com/watch?v=vntAEVjPBzQ",
                           "4.5 tomatoes out of 5")

meanGirls = media.Movie("Mean Girls",
                            "A story of mean girls",
                            "https://lh3.googleusercontent.com/1jQU8okWPPx1wOAcHkFZGE7jkk4ddsEA6Bc3hlKryGUE82G7ukiyZ9TZwGC9SLuJ3CzfccraqpEH-Ku7F-HuckrfosgzF0Bfe3H0ZsGFM7bmzLHHi1QD01nOYTz0E0R-fg",
                            "https://www.youtube.com/watch?v=KAOmTMCtGkI",
                            "4 tomatoes out of 5")

#puts movies in list to pass to open_movies_page function from fresh_tomatoes
movies = [mysteryTeam, iLoveYouMan, hotRod, anchorman, ghostbusters, meanGirls]

fresh_tomatoes.open_movies_page(movies)


#prints documentation, name of class, name of module
print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)

import media
import fresh_tomatoes

# These are instances using Movie class.

Monster = media.Movie("The Host",
                             ":The film concerns a monster kidnapping a man's daughter, and his attempts to rescue her. According to the director, his inspiration came from a local article about a deformed fish with an S-shaped spine caught in the Han River.[2] The Host had set a new Korean box office record by reaching 10 million tickets in just 21 days. In addition, it was ranked one of the top films of 2007 on Metacritic with a score of 85. In November 2008, it was announced that Universal Studios would be remaking The Host.",
                             "http://blogfiles6.naver.net/data17/2006/7/31/28/M0010007_host_charcter_p1_1-hisson86.jpg",
                             "https://www.youtube.com/watch?v=5apcZuMpXqE")


Split = media.Movie("Split",
                             ":Split is a 2016 American psychological horror-thriller film written and directed by M. Night Shyamalan[3] and starring James McAvoy, Anya Taylor-Joy, and Betty Buckley. The film follows a man with 23 different personalities who kidnaps and imprisons three teenage girls in an isolated underground facility.",
                             "http://ticketimage.interpark.com/Movie/still_image/V17/V1700254p_01.gif",
                             "https://www.youtube.com/watch?v=84TouqfIsiI")

Thor_Ragnarok = media.Movie("Thor_Ragnarok",
                             ":Thor: Ragnarok is a 2017 American superhero film based on the Marvel Comics character Thor, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures. It is the sequel to 2011's Thor and 2013's Thor: The Dark World, and is the seventeenth film in the Marvel Cinematic Universe (MCU). ",
                             "https://d1mm3624z6jafc.cloudfront.net/movies/posters/ThorRagnarok_PayoffOneSheet_R.JPG?v=13",
                             "https://www.youtube.com/watch?v=ue80QwXMRHg")


movies = [Monster,Split,Thor_Ragnarok]

# Create an HTML file that display movies using open_movies_page function.
fresh_tomatoes.open_movies_page(movies)

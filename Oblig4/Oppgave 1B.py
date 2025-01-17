# Oppgave 1 B)

# Opprett en klasse for filmer med instansvariabler for filmtittel, utgivelsesår og score.
class Movies:
    def __init__(self, title, release_year, score):
        self.title = title
        self.release_year = release_year
        self.score = score

    # Opprett en metode i filmklassen som returnerer en tekststreng med all informasjon om en gitt film
    def movie_info(self):
        return f"{movie.title} was released in {movie.release_year}, and currently has a score of {movie.score}"

# Bruk denne klassen til å opprette et objekt for hver av de følgende filmene:
movie_Inception = Movies("Inception", 2010, 8.8)
movie_The_Martian = Movies("The Martian", 2015, 8.0)
movie_Joker = Movies("Joker", 2019, 8.4)

movie_list = [movie_Inception, movie_The_Martian, movie_Joker]

# Skriv ut all informasjon om hver film med formatet;
# "<title> was released in <year>, and currently has a score of <score>", ved å benytte de opprettede objektene.
for movie in movie_list:
    print(movie.movie_info())
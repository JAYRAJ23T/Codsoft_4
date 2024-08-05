# Define movie dataset
movies = [
    {"MovieID": 1, "Title": "Inception", "Genre": ["Sci-Fi", "Action"]},
    {"MovieID": 2, "Title": "The Matrix", "Genre": ["Sci-Fi", "Action"]},
    {"MovieID": 3, "Title": "The Godfather", "Genre": ["Drama", "Crime"]},
    {"MovieID": 4, "Title": "Interstellar", "Genre": ["Sci-Fi", "Drama"]},
    {"MovieID": 5, "Title": "Pulp Fiction", "Genre": ["Crime", "Drama"]}
]

# User preferences
user_genres = {"Sci-Fi", "Action"}

# Recommend movies
def recommend_movies(movies, user_genres):
    recommendations = []
    for movie in movies:
        movie_genres = set(movie["Genre"])
        if user_genres.intersection(movie_genres):
            recommendations.append(movie["Title"])
    return recommendations

# Get recommendations for User 1
recommended_movies = recommend_movies(movies, user_genres)
print("Recommended Movies:", recommended_movies)
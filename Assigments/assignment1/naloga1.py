from csv import DictReader

ratingsReader = DictReader(open('ratings.csv', 'rt', encoding='utf-8'))
movieReader = DictReader(open('movies.csv', 'rt', encoding='utf-8'))

for movie in movieReader:
    movieId = movie["movieId"]
    title = movie["title"]
    sumRating = 0
    counter = 0
    for row in ratingsReader:
        user = row["userId"]
        movie = row["movieId"]
        rating = row["rating"]
        if movieId == movie:
            sumRating += rating
            counter += 1
    avgRating = sumRating/counter
    print(movieId + " " + title + " " + avgRating)


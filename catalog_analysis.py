import math

# ********************************** Входные данные ***************************
movies = [
    {"title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories",
     "year": 2019,
     "genres": {"comedy", "drama"},
     "rating": 7.1,
     "duration_min": 98,
     "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours",
     "year": 2016,
     "genres": {"thriller", "drama"},
     "rating": 6.4,
     "duration_min": 112,
     "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers",
     "year": 2023,
     "genres": {"sci-fi", "action"},
     "rating": 5.9,
     "duration_min": 101,
     "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery",
     "year": 2014, "genres": {"comedy"},
     "rating": 7.8,
     "duration_min": 89,
     "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo",
     "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9,
     "duration_min": 124,
     "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static",
     "year": 2022, "genres": {"drama"},
     "rating": 4.8,
     "duration_min": 137,
     "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm",
     "year": 2024,
     "genres": {"sci-fi", "drama"},
     "rating": 9.2,
     "duration_min": 118,
     "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes",
     "year": 2011, "genres": {"comedy"},
     "rating": 6.0,
     "duration_min": 95,
     "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor",
     "year": 2018,
     "genres": {"action", "thriller"},
     "rating": 7.3,
     "duration_min": 129,
     "actors": ["P. Diaz", "T. Chalamet"]},
]

# ****************************** Этап 1 **********************************
def average_rating(movies):
    ratings = [movie["rating"] for movie in movies]
    return round(sum(ratings) / len(ratings), 1)


def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie["year"] for movie in movies]
    return (
        max(ages),
        min(ages),
        math.ceil(sum(ages) / len(ages))
    )


def duration_in_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours}ч {remaining_minutes}м"

# ****************************** Проверка этапа 1 **********************

print("Средний рейтинг:", average_rating(movies))
print()

oldest_age, newest_age, average_age = catalog_age_stats(movies)
print("Возраст самого старого фильма:", oldest_age)
print("Возраст самого нового фильма:", newest_age)
print("Средний возраст фильмов:", average_age)

print()
print("Пример продолжительности фильма:")
print(duration_in_hours(movies[0]["duration_min"]))




# ****************************** Этап 2 **********************************

def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо" if rating < 9 else "шедевр"
    elif rating >= 5:
        return "средне"
    else:
        return "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


# ************************ Проверка этапа 2 ****************************
print()
print("Категории рейтингов фильмов:")
for movie in movies:
    print(
        f"{movie['title']}: "
        f"рейтинг {movie['rating']} — {rating_tier(movie['rating'])}"
    )

print()
print("Категории фильмов по году выпуска:")
for movie in movies:
    print(
        f"{movie['title']}: "
        f"{movie['year']} — {decade_label(movie['year'])}"
    )



# ****************************** Этап 3 **********************************

def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


print()
print("Фильмы с жанром НЕ comedy:")
for movie in movies:
    if "comedy" in movie["genres"]:
        continue
    print(movie["title"])

print()
print("Поиск первого фильма с рейтингом выше 9.0:")
i = 0
while i < len(movies):
    if movies[i]["rating"] > 9.0:
        print(
            f"Найден фильм: {movies[i]['title']}, "
            f"рейтинг: {movies[i]['rating']}"
        )
        break
    i += 1
else:
    print("Шедевров не найдено")


print()
print(
    "Количество фильмов длиннее 120 минут:",
    count_long_movies(movies)
)



# ****************************** Этап 4 **********************************

def normalize_title(title):
    words = title.split()
    normalized_words = []

    for word in words:
        normalized_word = word[0].upper() + word[1:]
        normalized_words.append(normalized_word)

    return " ".join(normalized_words)


def make_slug(title):
    return normalize_title(title).lower().replace(" ", "-")


def format_report_line(movie):
    title = normalize_title(movie["title"])
    year = movie["year"]
    rating = movie["rating"]
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))

    return (
        f'"{title}" ({year}) — {rating}/10, '
        f'{duration}, жанры: {genres}'
    )


# ************************ Проверка этапа 4 ****************************
print()
print("Нормализованные названия фильмов:")
for movie in movies:
    print(normalize_title(movie["title"]))

print()
print("Слаг названий фильмов:")
for movie in movies:
    print(make_slug(movie["title"]))

print()
print("Отчет по фильмам:")
for movie in movies:
    print(format_report_line(movie))



# ****************************** Этап 5 **********************************

def titles_sorted_by_rating(movies):
    sorted_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True
    )

    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True
    )

    return [
        (movie["title"], movie["rating"])
        for movie in sorted_movies[:n]
    ]


# ************************ Проверка этапа 5 ****************************
print()
print("Названия фильмов по убыванию рейтинга:")
for title in titles_sorted_by_rating(movies):
    print(title)

print()
print("Топ-3 фильма по рейтингу:")
for item in top_n_by_rating(movies, 3):
    print(item)


# ****************************** Этап 6 **********************************

def count_by_genre(movies):
    genre_counts = {}

    for movie in movies:
        for genre in movie["genres"]:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1

    return genre_counts


def actor_filmography(movies):
    filmography = {}

    for movie in movies:
        for actor in movie["actors"]:
            filmography[actor] = filmography.get(actor, [])
            filmography[actor].append(movie["title"])

    return filmography


def above_average_movies(movies):
    average = average_rating(movies)

    return {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > average
    }


# ************************ Проверка этапа 6 ****************************
print()
print("Количество фильмов по жанрам:")
print(count_by_genre(movies))

print()
print("Фильмография актёров:")
print(actor_filmography(movies))

print()
print("Фильмы с рейтингом выше среднего:")
print(above_average_movies(movies))



# ****************************** Этап 7 **********************************

def all_genres(movies):
    genres = set()
    for movie in movies:
        genres = genres | movie["genres"]
    return genres


def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)
    return genres_a - genres_b


# ************************ Проверка этапа 7 ****************************
print()
print("Все уникальные жанры каталога:")
print(all_genres(movies))

print()
print("Пример общих актёров двух фильмов:")
print(common_actors(movies[0], movies[3]))

print()
print("Жанры, встречающиеся только в первом наборе:")
print(genres_only_in_one(movies[5:6], movies[:5]))


# ****************************** Этап 8 **********************************

def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie



# ************************ Проверка этапа 8 ****************************
print()
print("Фильмы с рейтингом не ниже установленного")
for movie in iter_high_rated(movies):
    print(format_report_line(movie))

print()
print("Суммарная длительность фильмов с рейтингом выше 7:")

total_duration = sum(
    movie["duration_min"] for movie in movies if movie["rating"] > 7
)

print(total_duration, "минут")


# ****************************** Этап 9 **********************************

def build_report(movies):
    print()
    print("Единый консольный отчет", '\n')

    # Общая статистика
    print(f"Средний рейтинг: {average_rating(movies)}")

    average_age = catalog_age_stats(movies)[2]
    print(f"Средний возраст фильмов: {average_age} лет")

    # Топ-3 фильма
    print()
    print("Топ-3 фильма:")

    top_movies = top_n_by_rating(movies, 3)

    for title, rating in top_movies:
        movie = next(
            movie for movie in movies
            if movie["title"] == title
        )
        print(f"  {format_report_line(movie)}")

    # Количество фильмов по жанрам
    print()
    print("Фильмов по жанрам:")

    genre_counts = count_by_genre(movies)

    sorted_genres = sorted(
        genre_counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    for genre, count in sorted_genres:
        print(f"  {genre} — {count}")

    # Все уникальные жанры
    print()
    genres = sorted(all_genres(movies))
    print(f"Все жанры каталога: {', '.join(genres)}")


# ************************ Запуск отчета ************************

if __name__ == "__main__":
    build_report(movies)



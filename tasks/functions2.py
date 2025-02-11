#task 1 


def answer():
    # Dictionary of movies

    movies = [
        {
            "name": "Usual Suspects",
            "imdb": 7.0,
            "category": "Thriller"
        },
        {
            "name": "Hitman",
            "imdb": 6.3,
            "category": "Action"
        },
        {
            "name": "Dark Knight",
            "imdb": 9.0,
            "category": "Adventure"
        },
        {
            "name": "The Help",
            "imdb": 8.0,
            "category": "Drama"
        },
        {
            "name": "The Choice",
            "imdb": 6.2,
            "category": "Romance"
        },
        {
            "name": "Colonia",
            "imdb": 7.4,
            "category": "Romance"
        },
        {
            "name": "Love",
            "imdb": 6.0,
            "category": "Romance"
        },
        {
            "name": "Bride Wars",
            "imdb": 5.4,
            "category": "Romance"
        },
        {
            "name": "AlphaJet",
            "imdb": 3.2,
            "category": "War"
        },
        {
            "name": "Ringing Crime",
            "imdb": 4.0,
            "category": "Crime"
        },
        {
            "name": "Joking muck",
            "imdb": 7.2,
            "category": "Comedy"
        },
        {
            "name": "What is the name",
            "imdb": 9.2,
            "category": "Suspense"
        },
        {
            "name": "Detective",
            "imdb": 7.0,
            "category": "Suspense"
        },
        {
            "name": "Exam",
            "imdb": 4.2,
            "category": "Thriller"
        },
        {
            "name": "We Two",
            "imdb": 7.2,
            "category": "Romance"
        }
    ]
    a = str(input())
    for i in movies:
        if a == i['name'] and i['imdb'] >5.5:
            print('True')
            break
answer()


#task 2
def answer():
    # Dictionary of movies

    movies = [
        {
            "name": "Usual Suspects",
            "imdb": 7.0,
            "category": "Thriller"
        },
        {
            "name": "Hitman",
            "imdb": 6.3,
            "category": "Action"
        },
        {
            "name": "Dark Knight",
            "imdb": 9.0,
            "category": "Adventure"
        },
        {
            "name": "The Help",
            "imdb": 8.0,
            "category": "Drama"
        },
        {
            "name": "The Choice",
            "imdb": 6.2,
            "category": "Romance"
        },
        {
            "name": "Colonia",
            "imdb": 7.4,
            "category": "Romance"
        },
        {
            "name": "Love",
            "imdb": 6.0,
            "category": "Romance"
        },
        {
            "name": "Bride Wars",
            "imdb": 5.4,
            "category": "Romance"
        },
        {
            "name": "AlphaJet",
            "imdb": 3.2,
            "category": "War"
        },
        {
            "name": "Ringing Crime",
            "imdb": 4.0,
            "category": "Crime"
        },
        {
            "name": "Joking muck",
            "imdb": 7.2,
            "category": "Comedy"
        },
        {
            "name": "What is the name",
            "imdb": 9.2,
            "category": "Suspense"
        },
        {
            "name": "Detective",
            "imdb": 7.0,
            "category": "Suspense"
        },
        {
            "name": "Exam",
            "imdb": 4.2,
            "category": "Thriller"
        },
        {
            "name": "We Two",
            "imdb": 7.2,
            "category": "Romance"
        }
    ]
    for i in movies:
        if i["imdb"] >5.5:
            print(i["name"])
answer()



#task 3 
def answer():
    # Dictionary of movies

    movies = [
        {
            "name": "Usual Suspects",
            "imdb": 7.0,
            "category": "Thriller"
        },
        {
            "name": "Hitman",
            "imdb": 6.3,
            "category": "Action"
        },
        {
            "name": "Dark Knight",
            "imdb": 9.0,
            "category": "Adventure"
        },
        {
            "name": "The Help",
            "imdb": 8.0,
            "category": "Drama"
        },
        {
            "name": "The Choice",
            "imdb": 6.2,
            "category": "Romance"
        },
        {
            "name": "Colonia",
            "imdb": 7.4,
            "category": "Romance"
        },
        {
            "name": "Love",
            "imdb": 6.0,
            "category": "Romance"
        },
        {
            "name": "Bride Wars",
            "imdb": 5.4,
            "category": "Romance"
        },
        {
            "name": "AlphaJet",
            "imdb": 3.2,
            "category": "War"
        },
        {
            "name": "Ringing Crime",
            "imdb": 4.0,
            "category": "Crime"
        },
        {
            "name": "Joking muck",
            "imdb": 7.2,
            "category": "Comedy"
        },
        {
            "name": "What is the name",
            "imdb": 9.2,
            "category": "Suspense"
        },
        {
            "name": "Detective",
            "imdb": 7.0,
            "category": "Suspense"
        },
        {
            "name": "Exam",
            "imdb": 4.2,
            "category": "Thriller"
        },
        {
            "name": "We Two",
            "imdb": 7.2,
            "category": "Romance"
        }
    ]
    categ = str(input())
    for i in movies:
        if categ == i['category']:
            print(i['name'])
answer()



#task 4 
def answer():
    # Dictionary of movies

    movies = [
        {
            "name": "Usual Suspects",
            "imdb": 7.0,
            "category": "Thriller"
        },
        {
            "name": "Hitman",
            "imdb": 6.3,
            "category": "Action"
        },
        {
            "name": "Dark Knight",
            "imdb": 9.0,
            "category": "Adventure"
        },
        {
            "name": "The Help",
            "imdb": 8.0,
            "category": "Drama"
        },
        {
            "name": "The Choice",
            "imdb": 6.2,
            "category": "Romance"
        },
        {
            "name": "Colonia",
            "imdb": 7.4,
            "category": "Romance"
        },
        {
            "name": "Love",
            "imdb": 6.0,
            "category": "Romance"
        },
        {
            "name": "Bride Wars",
            "imdb": 5.4,
            "category": "Romance"
        },
        {
            "name": "AlphaJet",
            "imdb": 3.2,
            "category": "War"
        },
        {
            "name": "Ringing Crime",
            "imdb": 4.0,
            "category": "Crime"
        },
        {
            "name": "Joking muck",
            "imdb": 7.2,
            "category": "Comedy"
        },
        {
            "name": "What is the name",
            "imdb": 9.2,
            "category": "Suspense"
        },
        {
            "name": "Detective",
            "imdb": 7.0,
            "category": "Suspense"
        },
        {
            "name": "Exam",
            "imdb": 4.2,
            "category": "Thriller"
        },
        {
            "name": "We Two",
            "imdb": 7.2,
            "category": "Romance"
        }
    ]
    sum = 0
    for i in movies:
        sum += i['imdb']
    print(sum/len(movies))
answer()


#task 5 
def avg(movies):
    category = input()
    sum = 0
    count = 0
    for movie in movies:
        if movie["category"] == category:
            sum += movie['imdb']
            count += 1
    print(sum / count)
        
# Dictionary of movies
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
avg(movies)
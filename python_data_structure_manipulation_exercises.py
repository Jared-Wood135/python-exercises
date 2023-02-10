# =======================================================================================================
# STUDENTS DATA STRUCTURE START
# =======================================================================================================

students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]

# =======================================================================================================
# STUDENTS DATA STRUCTURE END
# STUDENTS DATA STRUCTURE TO 20 Questions
# 20 Questions START
# =======================================================================================================

# The following questions reference the students data structure below. Write the python code to answer 
# the following questions:

# 1. How many students are there?
# 14
len(students)

# 2. How many students prefer light coffee? For each type of coffee roast
# light = 3 // medium = 5 // dark = 5
def coffee_pref():
    light_pref = sum([1 for dict in students if "light" in dict["coffee_preference"]])
    medium_pref = sum([1 for dict in students if "medium" in dict["coffee_preference"]])
    dark_pref = sum([1 for dict in students if "dark" in dict["coffee_preference"]])
    print(f"{'Light' : ^10}|{'Medium' : ^10}|{'Dark' : ^10}")
    print(f"{'-----' : ^10}|{'------' : ^10}|{'----' : ^10}")
    print(f"{light_pref : ^10}|{medium_pref : ^10}|{dark_pref : ^10}")
coffee_pref()

# 3. How many types of each pet are there?
def totalbypet():
    totalcat = sum([1 for dict in students if 'cat' in dict['pets']])
    totaldog = sum([1 for dict in students if 'dog' in dict['pets']])
    totalhorse = sum([1 for dict in students if 'horse' in dict['horse']])
    print(f"{'Horses' : ^20}|{'Cats' : ^20}|{'Dogs' : ^20}")
    print(f"{'--------------------' : ^20}|{'--------------------' : ^20}")
    print(f"{totalhorse : ^20}|{totalcat : ^20}|{totaldog : ^20}")
totalbypet()
issue?

# 4. How many grades does each student have? Do they all have the same number of grades?
def total_grades():
    print(f"{'Student Name' : ^20}|{'Total Grades' : ^20}")
    print(f"{'--------------------' : ^20}|{'--------------------' : ^20}")
    for dict in students:
        print(f"{dict['student'] : ^20}|{len(dict['grades']) : ^20}")
total_grades()

# 5. What is each student's grade average?
def avg_grade():
    print(f"{'Student Name' : ^20}|{'Average Grade' : ^20}")
    print(f"{'--------------------' : ^20}|{'--------------------' : ^20}")
    for dict in students:
        avg = sum(dict['grades']) // len(dict['grades'])
        print(f"{dict['student'] : ^20}|{avg : ^20}")
avg_grade()

# 6. How many pets does each student have?
def total_pets():
    print(f"{'Student Name' : ^20}|{'Total Pets' : ^20}")
    print(f"{'--------------------' : ^20}|{'--------------------' : ^20}")
    for dict in students:
        print(f"{dict['student'] : ^20}|{len(dict['pets']) : ^20}")
total_pets()

# 7. How many students are in web development? data science?
def totalbycourse():
    web_dev = sum([1 for dict in students if 'web development' in dict['course']])
    data_science = sum([1 for dict in students if 'data science' in dict['course']])
    print(f"{'Web Development' : ^20}|{'Data Science' : ^20}")
    print(f"{web_dev : ^20}|{data_science : ^20}")
totalbycourse()

# 8. What is the average number of pets for students in web development?
def avgpetsinwebdev():
    inwebdev = [dict for dict in students if 'web development' in dict['course']]
    totalpets = sum(len(dict['pets']) for dict in inwebdev)
    return print('Average pets per student in web development ==>', round((totalpets / len(inwebdev)), 2))
avgpetsinwebdev()

# 9. What is the average pet age for students in data science?
Skipping for now...

# 10. What is most frequent coffee preference for data science students?
# IT BE MEDIUM
def dscoffeepref():
    indatascience = [dict for dict in students if 'data science' in dict['course']]
    lightpref = sum([1 for dict in indatascience if 'light' in dict['coffee_preference']])
    medpref = sum([1 for dict in indatascience if 'medium' in dict['coffee_preference']])
    darkpref = sum([1 for dict in indatascience if 'dark' in dict['coffee_preference']])
    print(f"{'Light' : ^20}|{'Medium' : ^20}|{'Dark' : ^20}")
    print(f"{'--------------------' : ^20}|{'--------------------' : ^20}|{'---------------------' : ^20}")
    print(f"{lightpref : ^20}|{medpref : ^20}|{darkpref : ^20}")
dscoffeepref()

# 11. What is the least frequent coffee preference for web development students?
# IT BE BOTH MEDIUM AND DARK
def webdevcoffeepref():
    inwebdev = [dict for dict in students if 'web development' in dict['course']]
    lightpref = sum([1 for dict in inwebdev if 'light' in dict['coffee_preference']])
    medpref = sum([1 for dict in inwebdev if 'medium' in dict['coffee_preference']])
    darkpref = sum([1 for dict in inwebdev if 'dark' in dict['coffee_preference']])
    print(f"{'Light' : ^20}|{'Medium' : ^20}|{'Dark' : ^20}")
    print(f"{'--------------------' : ^20}|{'--------------------' : ^20}|{'---------------------' : ^20}")
    print(f"{lightpref : ^20}|{medpref : ^20}|{darkpref : ^20}")
webdevcoffeepref()

# 12. What is the average grade for students with at least 2 pets?


# 13. How many students have 3 pets?


# 14. What is the average grade for students with 0 pets?


# 15. What is the average grade for web development students? data science students?


# 16. What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?


# 17. What is the average number of pets for medium coffee drinkers?


# 18. What is the most common type of pet for web development students?


# 19. What is the average name length?


# 20. What is the highest pet age for light coffee drinkers?

# =======================================================================================================
# 20 Questions END
# =======================================================================================================
import random

question_bank = {

    "Python": [

        "Explain OOP concepts in Python.",
        "What are Python decorators?",
        "Difference between list and tuple?",
        "Explain exception handling in Python.",
        "What is lambda function?",
        "Explain *args and **kwargs.",
        "What are Python modules?",
        "Difference between deep copy and shallow copy?",
        "What is list comprehension?",
        "Explain generators in Python.",
        "What is PEP8?",
        "Difference between Python 2 and Python 3?"
    ],

    "Flask": [

        "What is Flask framework?",
        "Explain Flask routing.",
        "What is Jinja2 template engine?",
        "Difference between GET and POST methods.",
        "What is session in Flask?",
        "How to connect MySQL with Flask?",
        "Explain Flask templates.",
        "What is Flask Blueprint?",
        "Explain request and response cycle.",
        "How does Flask handle forms?"
    ],

    "SQL": [

        "What is JOIN in SQL?",
        "Explain normalization.",
        "Difference between DELETE and TRUNCATE.",
        "What is a primary key?",
        "Difference between WHERE and HAVING?",
        "What is foreign key?",
        "Explain GROUP BY clause.",
        "Difference between UNION and UNION ALL.",
        "What are SQL constraints?",
        "Explain indexing in SQL."
    ],

    "Java": [

        "Explain JVM architecture.",
        "Difference between interface and abstract class.",
        "What is method overloading?",
        "Explain inheritance in Java.",
        "What is polymorphism?",
        "Difference between == and equals()?",
        "What is constructor?",
        "Explain encapsulation.",
        "What is multithreading?",
        "Difference between ArrayList and LinkedList?"
    ],

    "HTML": [

        "What is semantic HTML?",
        "Difference between div and span?",
        "What are forms in HTML?",
        "What is iframe?",
        "Difference between id and class?",
        "Explain HTML table structure.",
        "What are meta tags?",
        "Difference between block and inline elements?"
    ],

    "CSS": [

        "What is Flexbox?",
        "Difference between margin and padding?",
        "Explain CSS Grid.",
        "What is responsive design?",
        "What are media queries?",
        "Difference between relative and absolute positioning?",
        "What is z-index?",
        "Explain CSS selectors."
    ],

    "JavaScript": [

        "What is JavaScript?",
        "Difference between let, var, and const?",
        "Explain DOM manipulation.",
        "What are arrow functions?",
        "Difference between == and ===?",
        "What is event bubbling?",
        "Explain callback functions.",
        "What is asynchronous programming?",
        "Explain promises in JavaScript.",
        "What is JSON?"
    ],

    "Django": [

        "What is Django framework?",
        "Explain Django MTV architecture.",
        "What are Django models?",
        "Difference between Django and Flask?",
        "What is Django ORM?",
        "Explain migrations in Django.",
        "What are Django templates?",
        "What is admin panel in Django?"
    ],

    "DBMS": [

        "What is DBMS?",
        "Difference between DBMS and RDBMS?",
        "Explain ACID properties.",
        "What is normalization?",
        "Explain transactions in DBMS.",
        "What is deadlock?",
        "Difference between clustered and non-clustered index?",
        "What is database schema?"
    ],

    "OOP": [

        "Explain encapsulation.",
        "What is inheritance?",
        "Explain polymorphism.",
        "What is abstraction?",
        "Difference between class and object?",
        "What is constructor?",
        "What is method overriding?",
        "Explain real-world example of OOP."
    ],

    "HR": [

        "Tell me about yourself.",
        "Why should we hire you?",
        "What are your strengths?",
        "What are your weaknesses?",
        "Where do you see yourself in 5 years?",
        "Why do you want to join our company?",
        "Explain your final year project.",
        "How do you handle pressure?",
        "Are you a team player?",
        "What motivates you?"
    ]

}

def generate_questions(skills):

    questions = []

    for skill in skills:

        if skill in question_bank:

            random_questions = random.sample(
                question_bank[skill],
                min(3, len(question_bank[skill]))
            )

            questions.extend(random_questions)

    # Always add HR questions
    hr_questions = random.sample(
        question_bank["HR"],
        3
    )

    questions.extend(hr_questions)

    random.shuffle(questions)

    return questions
def evaluate_answer(answer):
    if answer is None:
        answer = ""

    score = 0
    feedback = []

    answer = str(answer)
    answer_length = len(answer)

    # -----------------------------------
    # Length Check
    # -----------------------------------
    if answer_length > 200:
        score += 40
    elif answer_length > 100:
        score += 25
    else:
        feedback.append("Answer is too short.")

    # -----------------------------------
    # Technical Keywords
    # -----------------------------------
    keywords = [
        'class',
        'object',
        'inheritance',
        'polymorphism',
        'encapsulation',
        'abstraction',
        'database',
        'API',
        'framework',
        'function'
    ]

    found_keywords = 0
    lower_answer = answer.lower()

    for word in keywords:
        if word.lower() in lower_answer:
            found_keywords += 1

    score += found_keywords * 8

    # -----------------------------------
    # Grammar / Communication
    # -----------------------------------
    if "." in answer:
        score += 10

    if "," in answer:
        score += 5

    # -----------------------------------
    # Feedback
    # -----------------------------------
    if found_keywords < 2:
        feedback.append("Add more technical explanation.")

    if answer_length < 100:
        feedback.append("Explain your answer in more detail.")

    # -----------------------------------
    # Final Result
    # -----------------------------------
    if score > 100:
        score = 100

    if score >= 80:
        result = "Excellent Performance"
    elif score >= 60:
        result = "Good Attempt"
    else:
        result = "Needs Improvement"

    return {
        'score': score,
        'result': result,
        'feedback': feedback
    }


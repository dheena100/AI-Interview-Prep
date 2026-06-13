skills_list = [
'Python',
'Java',
'C',
'C++',
'SQL',
'Flask',
'Django',
'Machine Learning',
'HTML',
'CSS',
'JavaScript',
'React',
'MySQL',
'Git',
'GitHub',
'Data Structures',
'OOP'
]

def extract_skills(text):
    found_skills = []

    for skill in skills_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills


    return found_skills


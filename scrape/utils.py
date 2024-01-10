possible_employment_type_values = [
    "Office",
    "Remote",
    "Гібридна робота",
    "Тільки віддалено",
    "Тільки офіс",
    "Office або Remote"
]
possible_english_levels = [
    "Beginner",
    "Elementary",
    "Pre-Intermediate",
    "Intermediate",
    "Upper-Intermediate",
    "Advanced",
    "Fluent"
]
possible_experience_values = [
    "Без досвіду",
    "1 рік досвіду",
    "2 роки досвіду",
    "3 роки досвіду",
    "4 роки досвіду",
    "5 років досвіду"
]


def get_match(values_list, job_info):
    match = set(values_list) & set(job_info)
    if match:
        return match.pop()
    else:
        return None


def get_experience_number(experience):
    if experience[0].isdigit():
        return experience[0]
    else:
        return 0


def get_salary_range(salary):
    if salary:
        salary_range = salary.text.replace("$", "")

        if "до" in salary_range:
            salary_range = salary_range.replace("до ", "<")

        return salary_range
    else:
        return None

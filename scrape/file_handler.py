import csv
import os.path
from dataclasses import astuple, fields

from vacancy_dto import VacancyDTO


def write_vacancies(vacancies: list[VacancyDTO], file_path: str) -> None:
    with open(os.path.join("scrapped_data", file_path), "a", encoding="utf8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([field.name for field in fields(VacancyDTO)])
        writer.writerows([astuple(vacancy) for vacancy in vacancies])

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

from config import SPECIALIZATION_URLS, GRADES, TECHNOLOGIES
from driver import ChromeDriver
from file_handler import write_vacancies
from logger import configure_logging
from utils import (
    get_match,
    possible_english_levels,
    possible_employment_type_values,
    possible_experience_values,
    get_experience_number,
    get_salary_range,
)
from vacancy_dto import VacancyDTO


def get_job_info(vacancy_soup):
    job_info_div = vacancy_soup.find("div", class_="job-list-item__job-info font-weight-500")
    spans = job_info_div.select("span")
    lst = []
    for span in spans[1:]:
        text_content = span.get_text(strip=True).replace("·", "")
        if text_content:
            lst.append(text_content)
    return lst


def parse_single_vacancy(vacancy_soup: BeautifulSoup) -> VacancyDTO:
    print()
    company, title = vacancy_soup.select("div:nth-child(1) > a")[1:]

    job_info = get_job_info(vacancy_soup)

    english = get_match(possible_english_levels, job_info)
    experience = get_match(possible_experience_values, job_info)
    employment_type = get_match(possible_employment_type_values, job_info)

    salary = vacancy_soup.select_one(".public-salary-item")

    counts_elements = vacancy_soup.select("div.d-flex.align-items-center.font-size-small.mb-2 > span.job-list-item__counts.d-none.d-lg-inline-block.nobr > span > span:nth-child(2)")
    views, appliances = counts_elements[0].select(".mr-2")

    description = vacancy_soup.select_one("div.job-list-item__description > span[data-original-text]")["data-original-text"]

    if description is not None:
        found_technologies = [tech for tech in TECHNOLOGIES if tech.lower() in description.lower()]
    else:
        found_technologies = []

    return VacancyDTO(
        company=company.get_text(strip=True),
        title=title.get_text(strip=True),
        location=vacancy_soup.select_one(".location-text").get_text(strip=True).replace("\n", ""),
        description=description,
        technologies=found_technologies,
        salary=get_salary_range(salary),
        english=english,
        years_of_experience=get_experience_number(experience),
        employment_type=employment_type,
        views=views["data-original-title"].split(" ")[0],
        appliances=appliances["data-original-title"].split(" ")[0],
    )


def parse_page(url: str, driver: ChromeDriver, grade: str) -> list[VacancyDTO]:
    driver.get(url)

    if grade != "all":
        grade_filter = driver.find_element(By.CSS_SELECTOR, f"label[for='exp_rank_{grade}']")
        grade_filter.click()

    vacancies = []

    while True:
        try:
            next_button = driver.find_element(
                By.CSS_SELECTOR,
                'ul.pagination_with_numbers li.page-item.active + li.page-item a.page-link'
            )

            page = BeautifulSoup(
                driver.page_source, "html.parser"
            )

            vacancies_soup = page.find_all("div", class_="job-list-item position-relative")

            for vacancy_soup in vacancies_soup:
                vacancies.append(
                    parse_single_vacancy(vacancy_soup)
                )

            if "#" not in next_button.get_attribute("href"):
                next_button.click()
            else:
                return vacancies

        except NoSuchElementException:
            break

    page = BeautifulSoup(
        driver.page_source, "html.parser"
    )

    vacancies_soup = page.find_all("div", class_="job-list-item position-relative")

    for vacancy_soup in vacancies_soup:
        vacancies.append(
            parse_single_vacancy(vacancy_soup)
        )
    return vacancies


def main():
    configure_logging()
    driver = ChromeDriver().web_driver
    for name, url in SPECIALIZATION_URLS.items():
        for grade in GRADES:
            vacancies = parse_page(url, driver, grade)
            write_vacancies(vacancies, f"{name}_{grade}.csv")


if __name__ == "__main__":
    main()

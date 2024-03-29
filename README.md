
# Djinni Job Board Data Analysis and Scraping 🚀

## Overview
This project is a powerhouse for scraping and analyzing job listings from the Djinni job board. The scraping script efficiently collects job details, while the analysis script unleashes powerful visualizations for profound insights.

## Project Structure

- `data_analysis/`: Beholds scripts for data analysis.
  - `output_plots/`: Stores all output plots
- `scrape/`: Embodies the scraping scripts.
- `scrapped_data/`: Sanctuary for the sacred scraped job listings data.

## Technologies Used
- Selenium for web scraping, a modern-day wand.
- BeautifulSoup for the mystical art of HTML parsing.
- Pandas, the almighty deity of data manipulation.
- Logging, the ancient scrolls for recording project history.

## Setup
1. Clone the repository:

   ```bash
   git clone https://github.com/kostomeister/py-scrape-djinni.git
   ```

2. Install the required potions:

   ```bash
   pip install -r requirements.txt
   ```

3. Execute the sacred scraping script:

   ```bash
   python scrape/scrape.py
   ```

4. Summon the main analysis script:

   ```bash
   python data_analysis/analysis.py
   ```

## Output
- The scraping script bestows job listings data in the `scrapped_data` sanctuary.
- The analysis script conjures various plots and saves them in an `output_plots` spellbook.

## Customization
- Tweak the constants in `config.py` to alter the magic within the scraping ritual.
  - Specializations and URLs
  Define specializations and corresponding URLs for scraping:
    ```python
    SPECIALIZATION_URLS = {
        "python": BASE_URL + "?primary_keyword=Python",
        # Add other specializations as needed
    }
    ```
- Specify the path from where the scraped data will be taken for analysis:
  ```python
  PATH_TO_DATA = "scrapped_data/python_all.csv"
  ```

- Embark on quests for additional analyses or visualizations based on your mystical inclinations.

## Contributors 🧙‍♂️🔮
- kostomeister

## Acknowledgments 🙏
Special thanks to the Djinni job board for providing the enchanted job listings data.

Feel free to contribute, suggest improvements, or report issues! May your code be ever magical! 🌟✨# py-scrape-djinni

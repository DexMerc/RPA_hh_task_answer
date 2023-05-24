<!-- - [eng](#web-scraper-rpa_hh_task_answer)  
- [рус](#веб-скрапер-rpa_hh_task_answer) -->

# Web scraper-RPA_hh_task_answer
During one of my interviews, I received a task to create web scraper that will collect all of the job listings with "python" word in it from the hh.kz website, then save the result in some database. hh or HeadHunter is a popular website for finding and posting job opportunites. 
Here are my 2 solutions:
- bs4_scrape.py - I have used BeautifulSoup4 for web scraping
- api.py - Here, I used the official API of hh

I have encountered an obstacle when I used the official API and it was encoding. If I record all of the data immediately after getting it from API, database will give an error for the special symbols and cyrillic characters. I have tried different formats: utf-8, cp1251, windows-1251, cp866, etc. Even, if I record it in a csv file, the results is mish mash. However, by recording the data into a Pandas dataframe and then into DB, the problem was solved.

# Веб скрапер-RPA_hh_task_answer
В одном из моих интервью, я получил задание где нужно было создать веб скрапер который будет собирать все работы с упоминанием "python" с сайта hh.kz и после записывать в датабазу. hh или HeadHunter это популярный вебсайт для поиска или размещения работ.

- bs4_scrape.py - Я использовал BeautifulSoup4 для веб скрапинга
- api.py - Здесь я использовал оффициальный API от hh
- test.ipynb - черновик

Ограничение которое я встретил это encoding данных. При записи данных сразу после подтягивания с API, дб выдавала ошибку на все символы и буквы русского алфавита. Попробовал разные форматы utf-8, cp1251, windows-1251, cp866 и тд. Даже при записи в csv, в файле видел только мишуру вместо кириллицы (англ и цифры в порядке). НО, сохраняя данные в Dataframe и после записывать в дб, дало результат, хоть и не самый желанный.  

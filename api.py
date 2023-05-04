import requests
import time
import pandas as pd
import sqlite3


def get_data_from_url(url):
    try:
        data = requests.get(url).json()
    except Exception as e:
        print("[INFO] Error getting the data. ", e)
        raise EOFError

    found = data['found']
    print(f"{found} jobs have been found.")

    if found > 100:
        i = 1
        while i * 100 <= found:
            temp_url = url + f"&page={i}"
            temp_data = requests.get(temp_url).json()

            for j in range(len(temp_data['items'])):
                data['items'].append(temp_data['items'][j])
            i += 1
            time.sleep(3)

    new_data = []
    for item in data['items']:
        temp = {
            'id': item['id'],
            'job_name': item['name'],
            'job_url': item['alternate_url'],
            'area_id': item['area']['id'],
            'area_name': item['area']['name'],
            'employer_id': item['employer']['id'],
            'employer_name': item['employer']['name'],
            'employer_url': item['employer']['alternate_url'],
            'employment_id': item['employment']['id'],
            'employment_name': item['employment']['name'],
            'snippet_requirement': item['snippet']['requirement'],
            'snippet_responsibility': item['snippet']['responsibility']}

        if item['address'] is not None:
            temp['address_building'] = item['address']['building']
            temp['address_city'] = item['address']['city']
            temp['address_id'] = item['address']['id']
            temp['address_lat'] = item['address']['lat']
            temp['address_lng'] = item['address']['lng']
            temp['address_raw'] = item['address']['raw']
            temp['address_street'] = item['address']['street']
        else:
            temp['address_building'] = None
            temp['address_city'] = None
            temp['address_id'] = None
            temp['address_lat'] = None
            temp['address_lng'] = None
            temp['address_raw'] = None
            temp['address_street'] = None

        if item['salary'] is not None:
            temp['salary_currency'] = item['salary']['currency']
            temp['salary_from'] = item['salary']['from']
            temp['salary_to'] = item['salary']['to']
            temp['salary_gross'] = item['salary']['gross']

        else:
            temp['salary_currency'] = None
            temp['salary_from'] = None
            temp['salary_to'] = None
            temp['salary_gross'] = None

        new_data.append(temp)
        del temp
    df = pd.DataFrame.from_dict(new_data)
    return df


if __name__ == '__main__':
    url = "https://api.hh.ru/vacancies?area=160&text=python&search_field=name&search_field=company_name&search_field=description&per_page=100"
    df = get_data_from_url(url)
    
    conn = sqlite3.connect('hh_jobs.sqlite')
    df.to_sql("jobs", con=conn)
    conn.close()


import csv
import copy

# Создаём шаблоны словарей
page_template = {'1_home_page': 0,
                 '2_search_page': 0,
                 '3_payment_page': 0,
                 '4_payment_confirmation_page': 0
                 }
date_template = {'2015-01': page_template.copy(),
                 '2015-02': page_template.copy(),
                 '2015-03': page_template.copy(),
                 '2015-04': page_template.copy(),
                 }
device_template = {'Desktop': copy.deepcopy(date_template),
                   'Mobile': copy.deepcopy(date_template),
                   }

# Создаём словарь для сортировки по гендеру
funnel_by_gender = {}

with open('click_stream3.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, fieldnames=['ID', 'page', 'date', 'device', 'gender'])

    for row in csv_reader:

        #  вытаскиваем нужные данные из файла
        page = list(row.items())[1][1]
        event_date = list(row.items())[2][1][:-3]
        device = list(row.items())[3][1]
        gender = list(row.items())[4][1]

        #  проверяем наличие разделов
        if gender not in funnel_by_gender:
            funnel_by_gender[gender] = copy.deepcopy(device_template)

        #  добавляем путь к словарю по полам
        if page == '1_home_page':
            funnel_by_gender[gender][device][event_date]['1_home_page'] += 1
        elif page == '2_search_page':
            funnel_by_gender[gender][device][event_date]['2_search_page'] += 1
        elif page == '3_payment_page':
            funnel_by_gender[gender][device][event_date]['3_payment_page'] += 1
        else:
            funnel_by_gender[gender][device][event_date]['4_payment_confirmation_page'] += 1

for i in funnel_by_gender.items():
    print(i)

from bs4 import BeautifulSoup
import requests
import openpyxl

book_rez = openpyxl.Workbook()
sheet_rez = book_rez.active
n = 1
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/108.0.0.0 YaBrowser/23.1.4.779 Yowser/2.5 Safari/537.36",
        }
sheet_rez.append(['номер', 'Наименование'])

for i in range(1, 8):
    response = requests.get(f"https://sport-marafon.ru/catalog/zhenskie-begovye-krossovki/?page={i}", headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    all = soup.findAll('div', class_='product-list__item-hover')
    for a in all:
        name = [n, a.find('a', class_="product-list__name").text]
        sheet_rez.append(name)
        n += 1

book_rez.save('sport-marathon_2023_03_23.xlsx')
book_rez.close()


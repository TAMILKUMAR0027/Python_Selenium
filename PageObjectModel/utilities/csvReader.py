import csv

def read_csv():
    with open("D:\Python_Selenium_Expleo\PageObjectModel\Login_data.csv", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)
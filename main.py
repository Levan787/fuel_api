import csv
import requests

url = "https://data.cityofchicago.org/resource/ijzp-q8t2.json"
req_url = requests.get(url)
res_url = req_url.json()

with open("Db.csv", 'w') as file:
    writer = csv.writer(file)

    key_data = res_url[0].keys()  # reach json file keys
    writer.writerow(key_data)
    data_set = set()
    for i in res_url:
        value_data = i.values()  # reach json file values
        writer.writerow(value_data)
        set_data = i.get('primary_type')
        data_set.add(set_data)


def final_values(key_name, values_name):
    f = open(f"{key_name}.csv", "a")
    all_files = csv.writer(f)
    all_files.writerow(values_name)  # Final result


def main_data():
    for j in res_url:
        for main_keys in data_set:  # iterate through dictionary values
            if j["primary_type"] == main_keys:
                main_values = j.values()  # take each criminal types values and distribute in specific files
                final_values(main_keys, main_values)


main_data()

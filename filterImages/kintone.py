import requests
import openpyxl
import pandas as pd
import json

wb = openpyxl.load_workbook(r'images_database.xlsx')
ws = wb.active

def addDatabase():

    iterations = []
    rows_list = []
    for index, i in enumerate(ws.iter_rows(values_only=True)): # API can only do 100 entries at a time
        row_data = {'Path': i[0], 'Time': i[1], 'Location': i[2], 'Emotion': i[3]}
        rows_list.append(row_data)
        if index % 99 == 0:
            iterations.append(rows_list)
            rows_list = []
            
    for rows_list in iterations:
        df = pd.DataFrame(rows_list, columns=['Path', 'Time', 'Location', 'Emotion'])
        print(df)

        # Import the necessary libraries
        # Define the Kintone API endpoint
        endpoint = r"https://myphotoalbumdb.kintone.com/k/v1/records.json?app=1&id=1"

        # Define the API key
        api_key = r"6I59Yzq0u6g2L3gc6oQchsMccyfBjpif7e4tfZmx"

        # Prepare the data to be imported
        data = {
            "app": 1,  # Replace with your Kintone app ID # MINE is 1
            "records": []
        }

        for index, row in df.iterrows():
            record = {
                "image_path": {"value": row["Path"]},
                "time_date": {"value": str(row["Time"])},
                "location": {"value": row["Location"]},
                "emotion": {"value": row["Emotion"]},
            }
            data["records"].append(record)

        # Make the POST request to import the data
        response = requests.post(endpoint, json=data, headers={"X-Cybozu-API-Token": api_key})

        # Check the response status
        if response.status_code == 200:
            print("Data imported successfully!")
        else:
            print("Failed to import data:", response.text)

def deleteDatabase():
    endpoint = r"https://myphotoalbumdb.kintone.com/k/v1/records.json"
    api_key = r"6I59Yzq0u6g2L3gc6oQchsMccyfBjpif7e4tfZmx"

    data = {
        'app': 1,
        'ids': [i for i in range(15, 59)]  # Replace with the actual record IDs you want to delete
    }
    response = requests.delete(endpoint, data=json.dumps(data), headers={"X-Cybozu-API-Token": api_key})
    if response.status_code == 200:
        print('Records deleted successfully')
    else:
        print('Failed to delete records:', response.text)


if __name__ == '__main__': 
    addDatabase()
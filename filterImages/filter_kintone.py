import requests

def get_filtered_records(query_list):
    url = f"https://myphotoalbumdb.kintone.com/k/v1/records.json"
    headers = {
        "X-Cybozu-API-Token": r"6I59Yzq0u6g2L3gc6oQchsMccyfBjpif7e4tfZmx",
    }
    # query = f"{field_code} = \"{value_to_match}\""
    output_list = []
    for tup in query_list:
        output_list.append(f'{tup[0]} = "{tup[1]}"')
    query = " and ".join(output_list)

    params = {
        "app": 1,
        "query": query,
        "fields": ["location", "time_date", "emotion", "image_path"]
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        records = response.json().get("records", [])
        return records
    else:
        print(f"Error: {response.status_code}, Message: {response.text}")
        return []

def clean_up_records(filtered_records):
    extracted_data = []
    for item in filtered_records:
        image_path = item.get('image_path', {}).get('value', '')
        extracted_data.append(image_path)
        
    return extracted_data

if __name__ == '__main__': 
    query_list = [('emotion', 'happy'), ('location', 'Ottawa')]
    filtered_records = get_filtered_records(query_list)
    extracted_data = clean_up_records(filtered_records)
    print(len(extracted_data))
    print(extracted_data)


import requests

def get_filtered_records(field_code, value_to_match, field_code2, value_to_match2):
    url = f"https://myphotoalbumdb.kintone.com/k/v1/records.json"
    headers = {
        "X-Cybozu-API-Token": r"6I59Yzq0u6g2L3gc6oQchsMccyfBjpif7e4tfZmx",
    }
    query = f"{field_code} = \"{value_to_match}\" AND {field_code2} = \"{value_to_match2}\" "
    params = {
        "app": 1,
        "query": query
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
    # Extract the required fields and their values
        image_path = item.get('image_path', {}).get('value', '')
        location = item.get('location', {}).get('value', '')
        datetime = item.get('date_time', {}).get('value', '')  # Assuming you want the 'date_time' field
        emotion = item.get('emotion', {}).get('value', '')

        extracted_data.append({
        'image_path': image_path,
        'location': location,
        'datetime': datetime,
        'emotion': emotion
    })
        
    return extracted_data

if __name__ == '__main__': 
    field_code = 'location'  
    value_to_match = 'Ottawa'  
    print(value_to_match)

    filtered_records = get_filtered_records(field_code, value_to_match, 'emotion', 'fear')
    extracted_data = clean_up_records(filtered_records)

    print(extracted_data)

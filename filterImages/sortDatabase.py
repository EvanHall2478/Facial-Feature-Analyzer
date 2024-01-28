import openpyxl
import pandas as pd

wb = openpyxl.load_workbook(r'images_database.xlsx')
ws = wb.active

if __name__ == '__main__': 
    # rows_list = []
    # for i in ws.iter_rows(values_only=True):
    #     row_data = {'Path': i[0], 'Time': i[1], 'Location': i[2], 'Emotion': i[3]}
    #     rows_list.append(row_data)       

    # df = pd.DataFrame(rows_list, columns=['Path', 'Time', 'Location', 'Emotion'])
    # ottawa_df = df[(df['Location'] == 'Ottawa') & (df['Emotion'] == 'happy')]
    # print(ottawa_df)
    
    excel_path = r'images_database.xlsx'
    df = pd.read_excel(excel_path)
    print(df)
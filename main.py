#Lib import
from datetime import datetime
import requests
import json

def mosocw_op_data_downloader(target_url):

    # trying to get version of Moscow API data
    moscow_open_data_version = requests.get('https://apidata.mos.ru/version')
    print(moscow_open_data_version)
    print(moscow_open_data_version.text)
    
    #URL definition
    print("Start of data gathering...")
    url_describtion_text = "URL is {}".format(target_url)
    print(url_describtion_text)

    #date and time 
    start_time = datetime.now() # current date and time
    date_time = start_time.strftime("%m/%d/%Y, %H:%M:%S")
    print("Start date and time:",date_time)
    print("Trying to request data from server")

    #Errors
    names_data_response = requests.get(target_url)
    if names_data_response:
        print("Success")
    else:
        print("An error has occured")

    #main_body    
    print("Prepearing JSON data format...")
    data = names_data_response.json()
    
    ### ?api_key=8f9de7b0e4ac17fae2ab9f4a87aaced2

    #end time
    end_time = datetime.now() # current date and time
    date_time = end_time.strftime("%m/%d/%Y, %H:%M:%S")
    print("Ending date and time:",date_time)
    print("Completed")

    with open (file=data.txt, mode=w , encoding=utf-8 ) as f:
        f.write(data)

    if "Cells" in data[0]:
            try:
                print(f"#DEGUG {data['data']['Cells']['global_id']}")
                return data['data']['Cells']['global_id']
            except(IndexError, TypeError):
                return False
    else:
        print(f"#DEGUG error 1")
    
mosocw_op_data_downloader('https://apidata.mos.ru/v1/datasets/2009/rows?api_key=8f9de7b0e4ac17fae2ab9f4a87aaced2')
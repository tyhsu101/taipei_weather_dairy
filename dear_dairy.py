import requests
import csv
import os
from datetime import datetime

class DearDairy():
    def __init__(self):
        self.url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-433D32BF-EE12-4FE9-9C77-308096ADE698&format=JSON&locationName=%E8%87%BA%E5%8C%97%E5%B8%82'
        self.paramters = {'Authorization':open(os.path.join('taipei_weather_dairy','api_key.txt'),'r').readline(),'locationName':['臺北市']}
        self.w_ind = [0,1,3,4,2]
        self.file_path = r'c:/users/hsudy/desktop/weather_dairy.txt'
    def how_is_weather_today(self):
        self.crawler = requests.get(self.url,params=self.paramters)
        self.data = self.crawler.json()

    def write_dairy(self):
        if os.path.exists(self.file_path):
            f = open(self.file_path, 'a',newline='\n')
        else:
            f = open(self.file_path, 'w',newline='')
        f.write(f'Dear Dairy:\n\tThis is {datetime.now()}\n')
        n = 3 #len(self.data['records']['location'][0]['weatherElement'][0]['time'])
        for i in range(n):
            text = '時間:'
            #add start time
            text += self.data['records']['location'][0]['weatherElement'][0]['time'][i]['startTime']
            text += '至'
            #add end time
            text += self.data['records']['location'][0]['weatherElement'][0]['time'][i]['endTime']
            text += self.data['records']['location'][0]['weatherElement'][self.w_ind[0]]['time'][i]['parameter']['parameterName']
            text+=',降雨機率:{}%'.format(self.data['records']['location'][0]['weatherElement'][self.w_ind[1]]['time'][i]['parameter']['parameterName'])
            text+= ',體感'
            text+= self.data['records']['location'][0]['weatherElement'][self.w_ind[2]]['time'][i]['parameter']['parameterName']
            text+= ',高溫'
            text+= self.data['records']['location'][0]['weatherElement'][self.w_ind[3]]['time'][i]['parameter']['parameterName']
            text+= '度,低溫溫'
            text+= self.data['records']['location'][0]['weatherElement'][self.w_ind[4]]['time'][i]['parameter']['parameterName']
            text+='度。'
            f.write(text)
            f.write('\n')
        f.close()
def main():
    a = DearDairy()
    a.how_is_weather_today()
    a.write_dairy()
if __name__=='__main__':
    main()
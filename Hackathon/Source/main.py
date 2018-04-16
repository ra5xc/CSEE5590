#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 06:19:59 2018

@author: rohitabhishek
"""

import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import xlrd
import pygeoip
rawdata = pygeoip.GeoIP('GeoLiteCity.dat')
import socket


def ipquery(ip):
    addr=ip
    try:
        socket.inet_aton(addr)
        a="l"
        # legal
    except socket.error:
        #print("not legal")
        a="nl"
        # Not legal
    if a=="l":
        data = rawdata.record_by_name(ip)
        country = data['country_name']
        city = data['city']
        longi = data['longitude']
        lat = data['latitude']
        print ('[x] '+str(city)+',' +str(country))
        print ('[x] Latitude: '+str(lat)+ ', Longitude: '+ str(longi))



        ny_lon, ny_lat = -75.8305, 37.6618
        delhi_lon, delhi_lat = longi, lat

        '''
        plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
                 color='blue', linewidth=2, marker='o' )
        
        plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
                 color='gray', linestyle='--' )
        
        plt.text(ny_lon - 3, ny_lat - 12, 'Nasa',
                 horizontalalignment='right')
        
        plt.text(delhi_lon + 3, delhi_lat - 12, country,
                 horizontalalignment='left')
        '''

        plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
                 color='blue', linewidth=0.5, marker='o',
                 transform=ccrs.Geodetic(),
                 )

        # plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
 #                 color='gray', linestyle='--',
 #                 transform=ccrs.PlateCarree(),
 #                 )

        # plt.text(ny_lon - 3, ny_lat - 12, 'Nasa',
#                  horizontalalignment='right',
#                  transform=ccrs.Geodetic())

        plt.text(delhi_lon + 3, delhi_lat - 12, country,
                 horizontalalignment='left',
                 transform=ccrs.Geodetic())



def read_excel_all_columns(filename):
    sheetname = "Sheet1"
    workbook = xlrd.open_workbook(filename)
    worksheet = workbook.sheet_by_name(sheetname)

    num_rows = worksheet.nrows
    num_cols = worksheet.ncols

    result_data =[]
    for curr_row in range(0, num_rows, 1):
        row_data = []

        for curr_col in range(0, num_cols, 1):
            data = worksheet.cell_value(curr_row, curr_col)
            #print(data)
            row_data.append(data)

        result_data.append(row_data)

    return  result_data


if __name__ == '__main__':
    response_time_sum=0
    counter=0
    filename = "new_datset.xlsx"
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()

    ax = plt.axes(projection=ccrs.Mollweide())
    ax.stock_img()

    result_data = read_excel_all_columns(filename)
    for i in result_data:
        #print(i[5])
        method.append(i[3])
        url.append(i[4])
        response_time.append(i[5])
        bytes_lst.append(i[6])
        #response_time_sum=response_time_sum+ float(i[5])
        ipquery(i[0])
        counter=counter+1
    plt.show()
   # print(d)
    c=Counter(d)
    print("Countries")
    for i in range(10):
        print(c.most_common()[i])

    for i in range(5):
        print(Counter(response_time).most_common()[i])
    for i in range(4):
        print(Counter(method).most_common()[i])
    print("*******************\n")
    for i in range(10):
        print(Counter(url).most_common()[i])

    for i in range(10):
        print(Counter(bytes_lst).most_common()[i])



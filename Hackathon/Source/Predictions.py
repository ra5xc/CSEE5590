import xlrd
import pygeoip
rawdata = pygeoip.GeoIP('GeoLiteCity.dat')
import socket, struct
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import metrics

def ipquery(ip):
    addr=ip
    try:
        socket.inet_aton(addr)
        a="l"
        # legal
    except socket.error:
        a="nl"
        # Not legal
        ipint = 0
        country = None
    if a=="l":
        data = rawdata.record_by_name(ip)
        ipint = struct.unpack("!L", socket.inet_aton(addr))[0]
        country = data['country_name']
        city = data['city']
        longi = data['longitude']
        lat = data['latitude']
        print ('[x] '+str(city)+',' +str(country))
        print ('[x] Latitude: '+str(lat)+ ', Longitude: '+ str(longi))
    return ipint, country
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
            row_data.append(data)

        result_data.append(row_data)

    return  result_data

def build_country_database():
    xl = pd.ExcelFile("countries of the world.xls")
    df = xl.parse("Country-Region")
    return df

def assign_country_class(df,ctry):
    subdf = df[df['Country'].str.match(ctry)]
    subsub =subdf.iloc[:,subdf.columns.str.startswith('Class')]
    list1= subsub.values.flatten()
    cclass = list1[0]
    return cclass

def prediction(X,Y):
    lr = LogisticRegression()
    Xtrain,Xtest,Ytrain,Ytest=train_test_split(X,Y,test_size=0.2, random_state=0)
    Xscale = StandardScaler()
    Xtrain = Xscale.fit_transform(Xtrain)
    Xtest = Xscale.transform(Xtest)
    clf = lr
    clf.fit(Xtrain, Ytrain)
    expected = Ytest
    predicted = clf.predict(Xtest)
    print('The accuracy of the Logistic Regression method is:',metrics.accuracy_score(expected,predicted))
    

if __name__ == '__main__':

    filename = "new_datset.xlsx"

    result_data = read_excel_all_columns(filename)
    
    country_data = build_country_database()
    
    X = np.zeros((1,2), dtype = int)
    
    Y = np.array([])
    
    for i in result_data:
        ipint,country = ipquery(i[0])
        if ipint != 0:
            X = np.vstack((X, [ipint,i[2]]))
            assign_country_class(country_data,country)
            cclass1 = assign_country_class(country_data, country)
            Y = np.append(Y, cclass1)
    
    prediction(X[1:,:],Y)
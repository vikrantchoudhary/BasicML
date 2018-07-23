import numpy as np
import quandl as qd
import datetime
from matplotlib import style,pyplot
from math import ceil
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#required for ploting graph
style.use('ggplot')

#data
qd.ApiConfig.api_key = 'XXXXXXX' #user your key from quandl
df = qd.get('NSE/NDTV',start_date='2018-06-11')
#define features and labels
df = df[['Open','High','Low','Last', 'Close','Total Trade Quantity']]
df['HL_PCT'] = (df['High']- df['Close'])/df['Close'] * 100
df['CHG_PCT'] = (df['Open'] - df['Close'])/df['Close'] * 100
df['Volume'] = df['Total Trade Quantity']
df = df[['Open','Close','Volume','HL_PCT','CHG_PCT']]
print (df.head())

df.fillna(-99999,inplace=True)
forecast_level = 'Close'
forecast_out = int(ceil(0.01*len(df))) + 1
print(forecast_out)

df['label'] = df[forecast_level].shift(-forecast_out)
X = np.array(df.drop(['label'] ,1 ))

#print(len(X),len(y))

#preprocessing
X = preprocessing.scale(X)
df.dropna(inplace=True)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]
y = np.array(df['label'])

#Regression algo
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.1)
clf = LinearRegression(n_jobs=1) #try with other algos
clf.fit(X_train,y_train)
forecast_set = clf.predict(X_lately)
accuracy = clf.score(X_test,y_test)

#graph
print("Algo accuracy:", accuracy)
print("Detail data:")
print(forecast_set,accuracy,forecast_out)

#plot
# intialize forecast values
df['Forecast'] = np.nan
#define datatime
last_date = df.iloc[-1].name
print ("lastdate: " ,last_date)
one_day = 24 * 60 * 60
next_unix = last_date.timestamp()
next_day = next_unix + one_day



#graph data
for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_day)
    next_day += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns) - 1)] + [i]


#plot graph
df['Close'].plot()
df['Forecast'].plot()
pyplot.legend(loc=1)
pyplot.xlabel('Date')
pyplot.ylabel('Price')

pyplot.show()
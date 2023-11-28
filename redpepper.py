import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import datetime as dt
from dateutil.relativedelta import relativedelta

redpepper_loss = 0
redpepper_estimate_price = 0

def main():
    
    global redpepper_loss
    global redpepper_estimate_price
    
    df = pd.read_csv('redpepper11.csv', encoding='euc-kr')
    data = np.array(df)
    now_date = dt.datetime.now()
    before_one_year = now_date - relativedelta(years=1)
    date = before_one_year.strftime('%Y-%m-%d')
    k=0
    cnt = 0

    for i in range(len(data)):
      if data[i][0] == date:
        k=i
        cnt += 1
    while(True):
      if(cnt == 0):
        before_one_year = before_one_year + relativedelta(days=1)
        date = before_one_year.strftime('%Y-%m-%d')
        print(date)
        for i in range(len(data)):
          if data[i][0] == date:
            k=i
            cnt += 1
      else:
        break
        
    div1 = 78
    div2 = 191

    if k<=div1-1:
      X= data[:div1,2]
      Y= data[:div1,1]

      mean_x = np.mean(X)
      mean_y = np.mean(Y)
      n = len(X)
      temp1 = 0
      temp2 = 0
      for i in range(n):
        temp1 += (X[i] - mean_x) * (Y[i] - mean_y)
        temp2 += (X[i] - mean_x) ** 2

      beta1 = temp1 / temp2
      beta0 = mean_y - (beta1 * mean_x)


      price_pred = beta1 * X + beta0

      loss = beta1 * X[k] + beta0 - data[k,1]
      print("실제 가격: ", data[k,1])
      print("예측 가격: ", round(beta1 * X[k] + beta0, 2))
      print("오차 값: ", round(loss,2))

      redpepper_loss += round(loss,2)

      plt.scatter(X,Y)

      plt.plot(X,price_pred, color='red')
      plt.grid()

    elif div1-1<k<=div2-1:
      X= data[div1:div2,2]
      Y= data[div1:div2,1]

      mean_x = np.mean(X)
      mean_y = np.mean(Y)
      n = len(X)
      temp1 = 0
      temp2 = 0
      for i in range(n):
        temp1 += (X[i] - mean_x) * (Y[i] - mean_y)
        temp2 += (X[i] - mean_x) ** 2

      beta1 = temp1 / temp2
      beta0 = mean_y - (beta1 * mean_x)


      price_pred = beta1 * X + beta0

      loss = beta1 * X[k-div1] + beta0 - data[k,1]
      print("실제 가격: ", data[k,1])
      print("예측 가격: ", round(beta1 * X[k-div1] + beta0, 2))
      print("오차 값: ", round(loss,2))
      redpepper_loss += round(loss,2)

      plt.scatter(X,Y)

      plt.plot(X,price_pred, color='red')
      plt.grid()

    else:
      X= data[div2:,2]
      Y= data[div2:,1]

      mean_x = np.mean(X)
      mean_y = np.mean(Y)
      n = len(X)
      temp1 = 0
      temp2 = 0
      for i in range(n):
        temp1 += (X[i] - mean_x) * (Y[i] - mean_y)
        temp2 += (X[i] - mean_x) ** 2

      beta1 = temp1 / temp2
      beta0 = mean_y - (beta1 * mean_x)


      price_pred = beta1 * X + beta0

      loss = beta1 * X[k-div2] + beta0 - data[k,1]
      print("실제 가격: ", data[k,1])
      print("예측 가격: ", round(beta1 * X[k-div2] + beta0, 2))
      print("오차 값: ", round(loss,2))
      redpepper_loss += round(loss,2)

      plt.scatter(X,Y)
      plt.plot(X,price_pred, color='red')
      plt.grid()
    
def get_redpepper_loss():
    global redpepper_loss
    main()
    a = redpepper_loss
    return a

def get_redpepper_estimate_price():
    global redpepper_estimate_price
    main()
    c = redpepper_estimate_price
    return c


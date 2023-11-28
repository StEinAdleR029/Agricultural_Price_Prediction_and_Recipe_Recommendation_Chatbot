import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import datetime as dt
from dateutil.relativedelta import relativedelta

highschoolfish_loss = 0
highschoolfish_grad = 0
highschoolfish_estimate_price = 0

def main():

    global highschoolfish_loss
    global highschoolfish_grad
    global highschoolfish_estimate_price
    
    df = pd.read_csv('highschoolfish11.csv', encoding='euc-kr')
    data = np.array(df)
    date = '2022-10-25'    
    
    now_date = dt.datetime.now()
    before_one_year = now_date - relativedelta(years=1)
    date = before_one_year.strftime('%Y-%m-%d')
    print(date)
    
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
    
    k=0
    for i in range(len(data)):
      if data[i][0] == date:
        k=i

    div = 163

    if k<=div-1:
      X= data[:div,2]
      Y= data[:div,1]

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

      plt.scatter(X,Y)

      highschoolfish_loss += round(loss,2)
      highschoolfish_grad += beta1
      highschoolfish_estimate_price += round(beta1 * X[k] + beta0, 2)

      plt.plot(X,price_pred, color='red')
      #plt.axis([-14,2000,6000,6000])
      plt.grid()

    else:
      X= data[div:,2]
      Y= data[div:,1]

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

      loss = beta1 * X[k-div] + beta0 - data[k,1]
      print("실제 가격: ", data[k,1])
      print("예측 가격: ", round(beta1 * X[k-div] + beta0, 2))
      print("오차 값: ", round(loss,2))

      highschoolfish_loss += round(loss,2)
      highschoolfish_grad += beta1
      highschoolfish_estimate_price += round(beta1 * X[k-div] + beta0, 2)

      plt.scatter(X,Y)
      plt.plot(X,price_pred, color='red')
      plt.grid()

def get_highschoolfish_loss():
    global highschoolfish_loss
    main()
    a = highschoolfish_loss
    return a

def get_highschoolfish_grad():
    global highschoolfish_grad
    main()
    b = highschoolfish_grad
    return b

def get_highschoolfish_estimate_price():
    global highschoolfish_estimate_price
    main()
    c = highschoolfish_estimate_price
    return c
    
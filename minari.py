import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import datetime as dt
from dateutil.relativedelta import relativedelta

minari_loss = 0
minari_grad = 0
minari_estimate_price = 0

def main():
    
    global minari_loss
    global minari_grad
    global minari_estimate_price
    df = pd.read_csv('minari11.csv', encoding='euc-kr')
    data = np.array(df)
    date = '2022-12-14'
    
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

    first_dir = 25
    second_dir = 115
    third_dir = 142
    fourth_dir = 197

    if k<=first_dir-1:
      X= data[:first_dir,2]
      Y= data[:first_dir,1]

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

      minari_loss += round(loss,2)
      minari_grad += beta1
      minari_estimate_price += round(beta1 * X[k] + beta0, 2)
      print("실제 가격: ", data[k,1])
      print("예측 가격: ", round(beta1 * X[k] + beta0, 2))
      print("오차 값: ", round(loss,2))
      print("기울기: ", minari_grad)

      plt.scatter(X,Y)

      plt.plot(X,price_pred, color='red')
      #plt.axis([-14,2000,6000,6000])
      plt.grid()

    elif k>first_dir-1 and k<=second_dir-1:
      X= data[first_dir:second_dir,2]
      Y= data[first_dir:second_dir,1]

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

      loss = beta1 * X[k-first_dir] + beta0 - data[k,1]

      minari_loss += round(loss,2)
      minari_grad += beta1
      minari_estimate_price += round(beta1 * X[k-first_dir] + beta0, 2)
      print("실제 가격: ", data[k,1])
      print("예측 가격: ", round(beta1 * X[k-first_dir] + beta0, 2))
      print("오차 값: ", round(loss,2))
      print("기울기: ", minari_grad)

      plt.scatter(X,Y)

      plt.plot(X,price_pred, color='red')
      #plt.axis([-14,2000,6000,6000])
      plt.grid()

    elif k>second_dir-1  and k<=third_dir-1:

      X= data[second_dir:third_dir,2]
      Y= data[second_dir:third_dir,1]

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

      loss = beta1 * X[k-(second_dir + 1)] + beta0 - data[k,1]

      minari_loss += round(loss,2)
      minari_grad += beta1
      minari_estimate_price += round(beta1 * X[k-(second_dir)] + beta0, 2)
      print("실제 가격: ", data[k,1])
      print("예측 가격: ", round(beta1 * X[k-(second_dir + 1)] + beta0, 2))
      print("오차 값: ", round(loss,2))
      print("기울기: ", minari_grad)

      plt.scatter(X,Y)

      plt.plot(X,price_pred, color='red')
      #plt.axis([-14,2000,6000,6000])
      plt.grid()

    elif k>third_dir-1 and k<=fourth_dir-1:

      X= data[third_dir:fourth_dir,2]
      Y= data[third_dir:fourth_dir,1]

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

      loss = beta1 * X[k-(third_dir+1)] + beta0 - data[k,1]

      minari_loss += round(loss,2)
      minari_grad += beta1
      minari_estimate_price += round(beta1 * X[k-(third_dir)] + beta0, 2)
      print("실제 가격: ", data[k,1])
      print("예측 가격: ", round(beta1 * X[k-(third_dir+1)] + beta0, 2))
      print("오차 값: ", round(loss,2))
      print("기울기: ", minari_grad)

      plt.scatter(X,Y)

      plt.plot(X,price_pred, color='red')
      #plt.axis([-14,2000,6000,6000])
      plt.grid()

    elif k>fourth_dir and k<=238:

      X= data[fourth_dir:238,2]
      Y= data[fourth_dir:238,1]

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

      loss = beta1 * X[k-(fourth_dir+1)] + beta0 - data[k,1]

      minari_loss += round(loss,2)
      minari_grad += beta1

      print("실제 가격: ", data[k,1])
      print("예측 가격: ", round(beta1 * X[k-(fourth_dir+1)] + beta0, 2))
      print("오차 값: ", round(loss,2))
      print("기울기: ", minari_grad)

      plt.scatter(X,Y)

      plt.plot(X,price_pred, color='red')
      #plt.axis([-14,2000,6000,6000])
      plt.grid()


def get_minari_loss():
    global minari_loss
    main()
    a = minari_loss
    return a

def get_minari_grad():
    global minari_grad
    main()
    b = minari_grad
    return b

def get_minari_estimate_price():
    global minari_estimate_price
    main()
    c = minari_estimate_price
    return c
    
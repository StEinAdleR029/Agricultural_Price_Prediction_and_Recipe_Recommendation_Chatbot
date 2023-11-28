import apple
import cabbage
import getleaf
import minari
import paprika
import piment
import potato
import redpepper
import operator


apple_loss = 0
cabbage_loss = 0
getleaf_loss = 0
minari_loss = 0
paprika_loss = 0
piment_loss = 0
potato_loss = 0
redpepper_loss = 0
foods = {}

apple_estimate_price = 0
cabbage_estimate_price = 0
getleaf_estimate_price = 0
minari_estimate_price = 0
paprika_estimate_price = 0
piment_estimate_price = 0
potato_estimate_price = 0
redpepper_estimate_price = 0

def main():
    
    global apple_loss
    global cabbage_loss
    global getleaf_loss
    global minari_loss
    global paprika_loss
    global piment_loss  
    global potato_loss
    global redpepper_loss
    global foods
    
    global apple_estimate_price
    global cabbage_estimate_price
    global getleaf_estimate_price
    global minari_estimate_price
    global paprika_estimate_price
    global piment_estimate_price
    global potato_estimate_price
    global redpepper_estimate_price
    
    
    apple_loss = apple.get_apple_loss()
    apple_estimate_price = apple.get_apple_estimate_price()
    cabbage_loss = cabbage.get_cabbage_loss()
    cabbage_estimate_price = cabbage.get_cabbage_estimate_price()
    getleaf_loss = getleaf.get_getleaf_loss()
    getleaf_estimate_price = getleaf.get_getleaf_estimate_price()
    minari_loss = minari.get_minari_loss()
    minari_estimate_price = minari.get_minari_estimate_price()
    paprika_loss = paprika.get_paprika_loss()
    paprika_estimate_price = paprika.get_paprika_estimate_price()
    piment_loss = piment.get_piment_loss()
    piment_estimate_price = piment.get_piment_estimate_price()
    potato_loss = potato.get_potato_loss()
    potato_estimate_price = potato.get_potato_estimate_price()
    redpepper_loss = redpepper.get_redpepper_loss()
    redpepper_estimate_price = redpepper.get_redpepper_estimate_price()
    

    print("apple_loss : ", apple_loss)
    print("apple_estimate_price : ", apple_estimate_price)
    print("cabbage_loss : ",cabbage_loss)
    print("cabbage_estimate_price : ", cabbage_estimate_price)
    print("getleaf_loss : ",getleaf_loss)
    print("getleaf_estimate_price : ", getleaf_estimate_price)
    print("minari_loss : ", minari_loss)
    print("minari_estimate_price : ", minari_estimate_price)
    print("paprika_loss : ", paprika_loss)
    print("paprika_estimate_price : ", paprika_estimate_price)
    print("piment_loss : ", piment_loss)
    print("piment_estimate_price : ", piment_estimate_price)
    print("potato_loss : ", potato_loss)
    print("potato_estimate_price : ", potato_estimate_price)
    print("redpepper_loss : ", redpepper_loss)
    print("redpepper_estimate_price : ", redpepper_estimate_price)
    
    
    
    foods = {"사과": apple_loss, "양배추": cabbage_loss, "깻잎": getleaf_loss, "미나리": minari_loss, "파프리카": paprika_loss, "피망": piment_loss, "감자": potato_loss, "고추": redpepper_loss}
    foods = dict(sorted(foods.items(), key=operator.itemgetter(1), reverse=True))
    
    foods1 = foods
    
    
    
    
    for food in list(foods1.values()):
        if food <= 0:
            k = list(foods.values()).index(food)
            x = list(foods.keys())[k]
            del(foods[x])
            
            
    print(foods)
    return foods
    
main()
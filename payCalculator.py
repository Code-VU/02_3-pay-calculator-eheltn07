def calculatePay():
    # Implement your solution in between the two comment blocks
    # This first line is provided for you
    hrs= input("Enter Hours:")
    rate= input("Enter Rate:")
    pay= int(hrs) * float(rate)
    print("calculating pay")
    print (pay)

    # end assignment


## If you want to test locally before you try to sync
## Open your terminal and run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()

#Author: Michael Beaudet
#Title: Week 3 Program 3 
#Date: 2/7/25

def weight_conversion(weight):

    shippingCost = 0.0
    if weight <= 2: 
        shippingCost = 1.50
    if weight > 2 and weight <= 6:
        shippingCost = 3.00
    if weight > 6 and weight <= 10: 
        shippingCost = 4.00
    if weight > 10:
        shippingCost = 4.75

    return shippingCost

if __name__ == '__main__':
    weight = 0.0
    shippingCost = 0.0
    weight = float(input('Enter the weight of the package: '))
    shippingCost = weight_conversion(weight)
    print ('Shipping charge: $', format(shippingCost, '.2f'))
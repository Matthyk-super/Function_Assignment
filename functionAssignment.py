import math

def main():
    # Calculate the area of a circle
    radius = int(input("Enter radius: "))
    circle_area = calculate_area_circle(radius)
    # area = round(area, 2). This will also round
    print(circle_area)

    # Calculate total bill due
    price = int(input("Money: "))
    tax = float(input("Tax Rate percent: "))
    total = calculate_taxes_due(price, tax)
    print(total)

    # Convert from Fahrenheit to Celsius temperature
    fahrenheit_temp = int(input("Fahrenheit temp: "))
    celsius_result = fahrenheit_to_celsius(fahrenheit_temp)
    print(celsius_result)

## Computes the area of a circle.
#  @param radius the radius of the circle
#  @return the area of the circle
#
def calculate_area_circle(radius):
    area = math.pi * radius ** 2
    return round(area, 2)

## Computes the total bill with taxes included.
#  @param money the price of the item
#  @param tax_rate the tax rate
#  @return the total due amount
#

def calculate_taxes_due(money, tax_rate):
    tax_rate = tax_rate / 100
    total_due = money + (money * tax_rate)
    return round(total_due,2)

## Convert from Fahrenheit to Celsius temperature
#  @param fahrenheit_temp the temperate in Fahrenheit
#  @return the temperate in Celsius
#
def fahrenheit_to_celsius(fahrenheit_temp):
    celsius_temp = (fahrenheit_temp - 32) * (5 / 9)
    return round(celsius_temp,4)

main()

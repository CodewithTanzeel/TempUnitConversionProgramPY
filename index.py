def celsius_to_fahrenheit(celsius):
    """
   Convert celsius to fahrenheit
   Formula: (9/5) * C + 32

    """   
    
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

# Example usage
c = float(input("Enter temperature in Celsius: "))
f = celsius_to_fahrenheit(c)
print(f"{c}°C is equal to {f}°F")
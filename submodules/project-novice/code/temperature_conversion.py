def fahr_to_cels(fahr):
    # Convert temperature in Fahrenheit to Celsius
    cels = (fahr + 32) * (5 / 9)
    return cels

def fahr_to_kelv(fahr):
    # Convert temperature in Fahrenheit to Kelvin
    cels = fahr_to_cels(fahr)
    kelv = cels + 273.15
    return kelv

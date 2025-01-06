def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius*1.8 + 32
    return fahrenheit

def calculate_windchill(temperature, wind_speed):
    wind_chill = 35.74 + 0.6215*temperature - 35.75*wind_speed**0.16 + 0.4275*temperature*wind_speed**0.16
    return wind_chill

wind_speed = 5
temperature = int(input('What is the temperature? '))

scale = input('Fahrenheit or Celsius (F/C)? ').upper()
if scale == 'C':
    temperature = convert_celsius_to_fahrenheit(temperature)

while wind_speed <= 60:
   
    print(f'At temperature {temperature}F, and wind speed {wind_speed} mph, the windchill is: {calculate_windchill(temperature, wind_speed):.2f}F')
    wind_speed += 5
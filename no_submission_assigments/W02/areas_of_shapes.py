import math

## core requiments ##
# square
square_length_cm = float(input('\nWhat is the length of a side of the square in centimeters? '))
square_area_cm = square_length_cm**2
square_area_m = square_area_cm / 10000
print(f'The area of the square is: {square_area_cm} cmsq or {square_area_m} msq')

# rectangle
rectangle_length_cm = float(input('What is the length of rectangle in centimeters? '))
rectangle_width_cm = float(input('What is the width of the rectangle in centimeters? '))
rectangle_area_cm = rectangle_length_cm * rectangle_width_cm
rectangle_area_m = rectangle_area_cm / 10000
print(f'The area of the rectangle is: {rectangle_area_cm} cmsq or {rectangle_area_m} msq ')

# circle
circle_radius_cm = float(input('What is the radius of the circle in centimeters? '))
circle_area_cm = round(math.pi * (circle_radius_cm**2), 4)
circle_area_m = circle_area_cm / 10000
print(f'The area of the circle is: {circle_area_cm} cmsq or {circle_area_m} msq')


## stretch challenges ##
single_value = float(input('\nPlease enter a single value: '))

# area of the square
sv_square_area = single_value**2
print(f'The area of the square is: {sv_square_area}')

# area of the circle
sv_circle_area = round(math.pi * (single_value**2), 2)
print(f'The area of the circle is: {sv_circle_area}')

# volume of a cube
sv_cube_volume = single_value**3
print(f'the volume of a cube is: {sv_cube_volume}')

# volume of a sphere
sv_sphere_volume = round(((4/3) * math.pi * (single_value **3)), 2)
print(f'the volume of a sphere is: {sv_sphere_volume}')
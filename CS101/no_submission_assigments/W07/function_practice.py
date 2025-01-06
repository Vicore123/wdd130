import math

def compute_area_square(square_length_cm):
    square_area_cm = compute_area_rectangle(square_length_cm, square_lenght_cm)[0]
    square_area_m = square_area_cm / 1000
    return square_area_cm, square_area_m


def compute_area_rectangle(rectangle_length_cm, rectangle_width_cm):

    rectangle_area_cm = rectangle_length_cm * rectangle_width_cm
    rectangle_area_m = rectangle_area_cm / 10000
    return rectangle_area_cm, rectangle_area_m
    

def compute_area_circle(circle_radius_cm):
    circle_area_cm = math.pi * (circle_radius_cm**2)
    circle_area_m = circle_area_cm / 10000
    return circle_area_cm, circle_area_m

chose = -1
while chose != 0:

    chose = int(input('What kind of shape do you have? \n\
          0. quit\n\
          1. square\n\
          2. rectangle\n\
          3. circle\n\n'))
    
    if chose == 0:
        print('thank you for using it!')

    elif chose == 1:
        # square
        square_lenght_cm = float(input('\nWhat is the length of a side of the square in centimeters? '))
        square_area = compute_area_square(square_lenght_cm)
        print(f'The area of the square is: {square_area[0]} cmsq or {square_area[1]} msq')

    elif chose == 2:
        # rectangle
        rectangle_length_cm = float(input('What is the length of rectangle in centimeters? '))
        rectangle_width_cm = float(input('What is the width of the rectangle in centimeters? '))
        rectangle_area = compute_area_rectangle(rectangle_length_cm, rectangle_width_cm)
        print(f'The area of the rectangle is: {rectangle_area[0]} cmsq or {rectangle_area[1]} msq ')

    elif chose == 3:
        # circle
        circle_radius_cm = float(input('What is the radius of the circle in centimeters? '))
        circle_area = compute_area_circle(circle_radius_cm)
        print(f'The area of the circle is: {circle_area[0]:.2f} cmsq or {circle_area[1]:.2f} msq')

    else:
        print(f'"{chose}" is a invalid chose')
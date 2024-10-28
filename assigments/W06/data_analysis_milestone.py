lowest_life_expectancy = 1000
highest_life_expectancy = -1

with open('life-expectancy.csv') as file:
    for line in file:

        line = line.strip().split(',')
        life_expectancy = float(line[3])

        if life_expectancy < lowest_life_expectancy:
            lowest_life_expectancy = life_expectancy

        if life_expectancy > highest_life_expectancy:
            highest_life_expectancy = life_expectancy

print(f'The overall max life expectancy is: {highest_life_expectancy}')
print(f'The overall min life expectancy is: {lowest_life_expectancy}')
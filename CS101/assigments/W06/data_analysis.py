# I added input for the year as well, so now it displays the average life expectancy since it started being recorded. It also shows the
# year with the lowest and highest values along with their respective life expectancies.


min_life_expectancy = 1000
min_life_expectancy_year = 9999
min_life_expectancy_country = ''

max_life_expectancy = -1
max_life_expectancy_year = -1
max_life_expectancy_country = ''

input_year = int(input('Enter the year of interest: '))
year_life_expectancy_sum = 0
year_life_expectancy_count = 0

min_life_expectancy_in_input_year = 1000
min_country_in_input_year = ''
max_life_expectancy_in_input_year = -1
max_country_in_input_year = ''

input_country = input('Enter the country of interest: ').capitalize()
country_life_expectancy_sum = 0
country_life_expectancy_count = 0

min_life_expectancy_in_input_country = 1000
min_year_in_input_country = 9999
max_life_expectancy_in_input_country = -1
max_year_in_input_country = -1

with open('life-expectancy.csv') as file:
    next(file)
    for line in file:
        line = line.strip().split(',')

        life_expectancy = float(line[3])
        year = int(line[2])
        country = line[0]

        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
            min_life_expectancy_year = year
            min_life_expectancy_country = country

        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy
            max_life_expectancy_year = year
            max_life_expectancy_country = country

        if year == input_year:
            year_life_expectancy_sum += life_expectancy
            year_life_expectancy_count += 1

            if life_expectancy < min_life_expectancy_in_input_year:
                min_life_expectancy_in_input_year = life_expectancy
                min_country_in_input_year = country
            
            if life_expectancy > max_life_expectancy_in_input_year:
                max_life_expectancy_in_input_year = life_expectancy
                max_country_in_input_year = country
        
        if country == input_country:
            country_life_expectancy_sum += life_expectancy
            country_life_expectancy_count += 1

            if life_expectancy < min_life_expectancy_in_input_country:
                min_life_expectancy_in_input_country = life_expectancy
                min_year_in_input_country = year
            
            if life_expectancy > max_life_expectancy_in_input_country:
                max_life_expectancy_in_input_country = life_expectancy
                max_year_in_input_country = year


print(f'\nThe overall max life expectancy is: {max_life_expectancy} from {max_life_expectancy_country} in {max_life_expectancy_year}')
print(f'The overall min life expectancy is: {min_life_expectancy} from {min_life_expectancy_country} in {min_life_expectancy_year}\n')

print(f'For the year {input_year}:')
year_average_life_expectancy = year_life_expectancy_sum/year_life_expectancy_count
print(f'The average life expectancy across all countries was {year_average_life_expectancy:.2f}')
print(f'The max life expectancy was in {max_country_in_input_year} with {max_life_expectancy_in_input_year}')
print(f'The min life expectancy was in {min_country_in_input_year} with {min_life_expectancy_in_input_year}\n')

print(f'For the country {input_country}:')
country_average_life_expectancy = country_life_expectancy_sum/country_life_expectancy_count
print(f'The average life expectancy across all years was {country_average_life_expectancy:.2f}')
print(f'The max life expectancy was in {max_year_in_input_country} with {max_life_expectancy_in_input_country}')
print(f'The min life expectancy was in {min_year_in_input_country} with {min_life_expectancy_in_input_country}\n')
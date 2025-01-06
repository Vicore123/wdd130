lowest_life_expectancy = 1000
lowest_year = 9999
lowest_country = ''

highest_life_expectancy = -1
highest_year = -1
highest_country = ''


user_year = int(input('Enter the year of interest: '))
year_sum = 0
year_count = 0

user_year_lowest_life_expectancy = 1000
user_year_lowest_country = ''
user_year_highest_life_expectancy = -1
user_year_highest_country = ''


user_country = input('Enter the country of interest: ').capitalize()
country_sum = 0
country_count = 0

user_country_lowest_life_expectancy = 1000
user_country_lowest_year = 9999
user_country_highest_life_expectancy = -1
user_country_highest_year = -1


with open('life-expectancy.csv') as file:
    for line in file:
        line = line.strip().split(',')

        life_expectancy = float(line[3])
        year = int(line[2])
        country = line[0]

        if life_expectancy < lowest_life_expectancy:
            lowest_life_expectancy = life_expectancy
            lowest_year = year
            lowest_country = country

        if life_expectancy > highest_life_expectancy:
            highest_life_expectancy = life_expectancy
            highest_year = year
            highest_country = country

        if year == user_year:
            year_sum += life_expectancy
            year_count += 1

            if life_expectancy < user_year_lowest_life_expectancy:
                user_year_lowest_life_expectancy = life_expectancy
                user_year_lowest_country = country
            
            if life_expectancy > user_year_highest_life_expectancy:
                user_year_highest_life_expectancy = life_expectancy
                user_year_highest_country = country
        
        if country == user_country:
            country_sum += life_expectancy
            country_count += 1

            if life_expectancy < user_country_lowest_life_expectancy:
                user_country_lowest_life_expectancy = life_expectancy
                user_country_lowest_year = year
            
            if life_expectancy > user_country_highest_life_expectancy:
                user_country_highest_life_expectancy = life_expectancy
                user_country_highest_year = year


print(f'\nThe overall max life expectancy is: {highest_life_expectancy} from {highest_country} in {highest_year}')
print(f'The overall min life expectancy is: {lowest_life_expectancy} from {lowest_country} in {lowest_year}\n')

print(f'For the year {user_year}:')
year_average = year_sum/year_count
print(f'The average life expectancy across all countries was {year_average:.2f}')
print(f'The max life expectancy was in {user_year_highest_country} with {user_year_highest_life_expectancy}')
print(f'The min life expectancy was in {user_year_lowest_country} with {user_year_lowest_life_expectancy}\n')

print(f'For the country {user_country}:')
country_average = country_sum/country_count
print(f'The average life expectancy across all years was {country_average:.2f}')
print(f'The max life expectancy was in {user_country_highest_year} with {user_country_highest_life_expectancy}')
print(f'The min life expectancy was in {user_country_lowest_year} with {user_country_lowest_life_expectancy}\n')
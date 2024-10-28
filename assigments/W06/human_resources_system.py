with open("hr_system.txt") as file:
    for line in file:
        line = line.strip().split()

        name = line[0]
        ID = int(line[1])
        job_title = line[2]
        salary = float(line[3])/24
        if job_title == 'Engineer':
            salary += 1000
        print(f'{name} (ID: {ID}), {job_title} -- ${salary:.2f}')
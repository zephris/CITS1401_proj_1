def main(csvfile, country: str):
    country = country.lower()
    file_obj = open(csvfile, "r")
    index = file_index(file_obj, country)
    max_min(file_obj, country, index)
    #median_salary_SD(file_obj, country, index)


def file_index(_file: object, _country: object) -> object: #
    index = []
    next(_file)
    for line in _file:
        line = line.lower().split(",")
        if line[3] == _country:
            index.append(line)
        return index


def max_min(_file: object, _country: object, index:list) -> object:
    max_buffer = 0
    min_buffer = 0
    minmax_output = ["", ""]
    for row in index:
            if max_buffer < int(row[6]):
                max_buffer = int(row[6])
                minmax_output[0] = row[1]
            if min_buffer > int(row[6]) and min != 0:
                min_buffer = int(row[6])
                minmax_output[1] = row[1]
            else:
                min_buffer = int(row[6])
                minmax_output[1] = row[1]
    return print(minmax_output)

'''
def median_salary_SD(_file: object, _country: object, index: list) -> object:
    # for whole data set
    salary_buffer = []
    for row in index:
        salary_buffer.append(int(row[7]))
    mean_all = sum(salary_buffer) / len(salary_buffer)
    variance = sum([((x - mean_all) ** 2) for x in salary_buffer]) / len(salary_buffer)
    sd_whole = variance ** 0.5

    #for country
    salary_buffer.clear()
    for row in index:
        if _country == row[3]:
            salary_buffer.append(int(row[7]))
    mean_country = sum(salary_buffer) / len(salary_buffer)
    variance = sum([((x - mean_country) ** 2) for x in salary_buffer]) / len(salary_buffer)
    sd_country = variance ** 0.5
    return print(sd_whole,sd_country)
'''
main("Organisations.csv", "Algeria")

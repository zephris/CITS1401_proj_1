def main(csvfile, country: str):
    file_obj = open(csvfile, "r")
    file_index(file_obj, country)
    max_min(file_obj, country)
    median_salary_SD(file_obj, country)


def file_index(_file: object, _country: object) -> object:
    lines = 0
    index = [[], []]
    for line in _file[1:]:
        lines = + 1
        line = line.lower().split(",")
        index[lines],[].append(line)

    # for line in _file:


def max_min(_file: object, _country: object) -> object:
    max_buffer = 0
    min_buffer = 0
    minmax_output = ["", ""]
    for line in _file:
        line = line.lower().split(",")
        if _country == line[3]:
            if max_buffer < int(line[6]):
                max_buffer = int(line[6])
                minmax_output[0] = line[1]
            if min_buffer > int(line[6]) and min != 0:
                min_buffer = int(line[6])
                minmax_output[1] = line[1]
            else:
                min_buffer = int(line[6])
                minmax_output[1] = line[1]
    return minmax_output


def median_salary_SD(_file: object, _country: object) -> object:
    # for whole data set
    salary_buffer = []
    for line in _file:
        line = line.split(",")
        salary_buffer.append(int(line[7]))


"""
    mean = sum(salary_buffer) / len(salary_buffer)
    variance = sum([((x - mean) ** 2) for x in salary_buffer]) / len(salary_buffer)
    standard_deviation_whole = variance ** 0.5

    #for country
    salary_buffer = []
    for line in _file:
        line = line.split(",")
        if _country == line[3]:
            salary_buffer.append(int(line[7]))
    salary_buffer.sort()
    mean = sum(salary_buffer) / len(salary_buffer)
    variance = sum([((x - mean) ** 2) for x in salary_buffer]) / len(salary_buffer)
    standard_deviation_country = variance ** 0.5
    return print(standard_deviation_whole, standard_deviation_country)

    return median
    """
main("Organisations.csv", "Algeria")

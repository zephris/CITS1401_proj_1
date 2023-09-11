def main(csvfile, country: str):
    file_obj = open(csvfile, "r")
    file_index(file_obj, country)
    max_min(file_obj, country, index)
    median_salary_SD(file_obj, country, index)


def file_index(_file: object, _country: object) -> object: #
    index = []
    for line in _file:
        index.append(line.lower().split(","))
        return index


def max_min(_file: object, _country: object, index:list) -> object:
    max_buffer = 0
    min_buffer = 0
    minmax_output = ["", ""]
    for _ in index:
        if _country == index[_][3]:
            if max_buffer < int(index[_][6]):
                max_buffer = int(index[_][6])
                minmax_output[0] = index[_][1]
            if min_buffer > int(index[_][6]) and min != 0:
                min_buffer = int(index[_][6])
                minmax_output[1] = index[_][1]
            else:
                min_buffer = int(index[_][6])
                minmax_output[1] = index[_][1]
    return minmax_output


def median_salary_SD(_file: object, _country: object, index: list) -> object:
    # for whole data set
    salary_buffer = []
    for _ in index:
        salary_buffer.append(int(index[_][7]))
    mean_all = avg(salary_buffer)
    variance = sum([((x - mean) ** 2) for x in salary_buffer]) / len(salary_buffer)
    standard_deviation_whole = variance ** 0.5

    #for country
    salary_buffer.clear()
    for _ in index:
        if _country == index[_][3]:
            salary_buffer.append(int(line[7]))
    salary_buffer.sort()
    mean = sum(salary_buffer) / len(salary_buffer)
    variance = sum([((x - mean) ** 2) for x in salary_buffer]) / len(salary_buffer)
    standard_deviation_country = variance ** 0.5
    return median
main("Organisations.csv", "Algeria")

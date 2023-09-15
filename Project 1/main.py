
def main(csvfile, country: str):
    country = country.lower()
    index, filter, row_dict = file_io(csvfile, country)
    maxmin = max_min(filter, row_dict)
    median = median_salary_SD(filter, index, row_dict)
    ratio = profit_ratio(filter, row_dict)
    corre = correlation(filter, row_dict)
    return maxmin, median, ratio, corre


# noinspection PyTypeChecker
def file_io(_file: object, _country: object) -> object:  #
    index = []
    filter = []
    filedata = open(_file, "r")
    for line in filedata:
        line = line.lower().strip().split(",")  # split,index the file
        index.append(line)
    filedata.close()
    rowdict = {}
    for row in index[0]: # index headers
        rowdict.update({row: index[0].index(row)})
    for row in index:
        if _country in row: # filter by country
            filter.append(row)
    return index, filter, rowdict


def max_min(_filter, _rowdict: dict) -> object:
    max_buffer = 0
    min_buffer = 0
    minmax_output = ["", ""]
    for row in _filter: # find max
        if 1981 <= int(row[_rowdict.get("founded")]) <= 2000:
            if max_buffer < float(row[_rowdict.get("number of employees")]):
                max_buffer = float(row[_rowdict.get("number of employees")])
                minmax_output[0] = row[_rowdict.get("name")]
    for row in _filter: # find min
        if 1981 <= int(row[_rowdict.get("founded")]) <= 2000:
            if min_buffer > float(row[_rowdict.get("number of employees")]) and min != 0:
                min_buffer = float(row[_rowdict.get("number of employees")])
                minmax_output[1] = row[_rowdict.get("name")]
            elif min_buffer == 0:
                min_buffer = float(row[_rowdict.get("number of employees")])
                minmax_output[1] = row[_rowdict.get("name")]
    return minmax_output


def median_salary_SD(_filter, _index: list, _rowdict: dict) -> object:
    # for whole data set
    salary_buffer = []
    for row in _index[1:]: # look for median salary based on header index
        salary_buffer.append(float(row[_rowdict.get("median salary")]))
    mean_all = sum(salary_buffer) / len(salary_buffer)
    variance = sum([((x - mean_all) ** 2) for x in salary_buffer]) / (len(salary_buffer) - 1)
    sd_whole = round(variance ** 0.5, 4)
    # for country
    salary_buffer.clear()
    for row in _filter:
        salary_buffer.append(int(row[_rowdict.get("median salary")]))
    try:
        mean_country = sum(salary_buffer) / len(salary_buffer)
    except ZeroDivisionError: # if no data for country(len(salary_buffer) == 0)
        return 0
    variance = sum([((x - mean_country) ** 2) for x in salary_buffer]) / (len(salary_buffer) - 1)
    sd_country = round(variance ** 0.5, 4)
    return sd_country, sd_whole


def profit_ratio(_filter: list, _rowdict: dict):
    inc_buffer = []
    dec_buffer = []
    for row in _filter: # find profit increase and decrease
        if float(row[_rowdict.get("profits in 2020(million)")]) > float(row[_rowdict.get("profits in 2021(million)")]):
            profit_dec = float(row[_rowdict.get("profits in 2020(million)")]) - float(
                row[_rowdict.get("profits in 2021(million)")])
            dec_buffer.append(profit_dec) # add to buffer of decreased revenues
    for row in _filter:
        if float(row[_rowdict.get("profits in 2020(million)")]) < float(row[_rowdict.get("profits in 2021(million)")]):
            profit_inc = float(row[_rowdict.get("profits in 2021(million)")]) - float(
                row[_rowdict.get("profits in 2020(million)")])
            inc_buffer.append(profit_inc) # add to buffer of increased revenues
    try:
        ratio = round(sum(inc_buffer) / sum(dec_buffer),4)
    except ZeroDivisionError:
        return 0 # if no data for country(len(salary_buffer) == 0)
    return ratio


def correlation(_filter: list, _rowdict: dict):
    profit_list = []
    median_list = []
    for row in _filter: # create index of increased revenues & median salaries
        if float(row[_rowdict.get("profits in 2021(million)")]) > float(row[_rowdict.get("profits in 2020(million)")]):
            profit_list.append(float(row[_rowdict.get("profits in 2021(million)")]))
            median_list.append(float(row[_rowdict.get("median salary")]))
    try:
        average_profit = sum(profit_list) / len(profit_list)
    except ZeroDivisionError:
        return 0 # if no data for country(len(salary_buffer) == 0)
    average_median = sum(median_list) / len(median_list)
    buffer1, buffer2, buffer3 = 0, 0, 0
    for _ in range(len(profit_list)):
        buffer1 += (profit_list[_] - average_profit) * (median_list[_] - average_median)
        buffer2 += (profit_list[_] - average_profit) ** 2
        buffer3 += (median_list[_] - average_median) ** 2
    cor = round(buffer1 / ((buffer2 *buffer3) ** 0.5),4) # calculate correlation
    return cor
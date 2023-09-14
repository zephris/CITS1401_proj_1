def main(csvfile, country: str):
    country = country.lower()
    index,filter, rowdict = file_io(csvfile, country)
    sdtv = max_min(filter,rowdict)
    median, inc_buffer, inc_name = median_salary_SD(filter,index,rowdict)


def file_io(_file: object, _country: object) -> object: #
    index = []
    filter = []
    filedata = open(_file,"r")
    for line in filedata:
        line = line.lower().split(",")
        index.append(line)
    filedata.close()
    global rowdict
    rowdict = {}
    for row in index[0]:
        rowdict.update({row: index[0].index(row)})
    for row in index:
        if _country in row:
            filter.append(row)
    return index, filter,rowdict


def max_min(_filter: list, _rowdict:dict) -> object:
    max_buffer = 0
    min_buffer = 0
    minmax_output = ["", ""]
    for row in _filter:
        if 1981 <= int(row[_rowdict.get("founded")]) <= 2000:
            if max_buffer < float(row[_rowdict.get("number of employees")]):
                max_buffer = float(row[_rowdict.get("number of employees")])
                minmax_output[0] = row[_rowdict.get("name")]
            if min_buffer > float(row[_rowdict.get("number of employees")]) and min != 0:
                min_buffer = float(row[_rowdict.get("number of employees")])
                minmax_output[1] = row[_rowdict.get("name")]
            else:
                min_buffer = float(row[_rowdict.get("number of employees")])
                minmax_output[1] = row[_rowdict.get("name")]
    return minmax_output


def median_salary_SD(_filter,_index:list,_rowdict:dict) -> object:
    # for whole data set
    salary_buffer = []
    for row in _index[1:]:
            salary_buffer.append(float(row[_rowdict.get("median salary")]))
    mean_all = sum(salary_buffer) / len(salary_buffer)
    variance = sum([((x - mean_all) ** 2) for x in salary_buffer]) / len(salary_buffer)
    sd_whole = variance ** 0.5
    round(sd_whole,4)
    #for country
    salary_buffer.clear()
    for row in _filter:
        salary_buffer.append(int(row[_rowdict.get("median salary")]))
    mean_country = sum(salary_buffer) / len(salary_buffer)
    variance = sum([((x - mean_country) ** 2) for x in salary_buffer]) / len(salary_buffer)
    sd_country = variance ** 0.5
    round(sd_country,4)
    return sd_country,sd_whole

def ratio(_filter:list,_rowdict:dict):
    inc_buffer = []
    inc_name = []
    dec_buffer =[]
    for row in _filter:
        if row[_rowdict.get("profits in 2020(million)")] > row[_rowdict.get("profit in 2021(million)")]:
            profit_dec = row[_rowdict.get("profit in 2020(million)")] - row[_rowdict.get("profit in 2021(million)")]
            dec_buffer.append(profit_dec)
        else:
            profit_inc = row[_rowdict.get("profit in 2021(million)")] - row[_rowdict.get("profit in 2020(million)")]
            inc_buffer.append(profit_inc)
            inc_name.append(row[_rowdict.get("name")])
    ratio = sum(inc_buffer) / sum(dec_buffer)
    return ratio, inc_buffer


def correlation(_filter,_inc_buffer,_inc_name:list,_rowdict:dict):
    for row in _filter:
        if row[_rowdict.get("name")] in _inc_name:
            correlation.buffer[]

    pass
main("Organisations.csv", "Belgium")
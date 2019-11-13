
import os


def read_directory(directory):
    result = []

    for file_name in os.listdir(directory):
        if(file_name.endswith(".csv")):
            result.append(read_file("%s/%s" % (directory, file_name)))

    return result


def read_file(filename):
    name = filename.split('.csv')[0]
    question, engine = name.split('-')[0], name.split('-')[1]
    with open(filename, 'r') as fh:
        fh.readline()  # Ingore first line we don't need col names
        raw_data = fh.readlines()
    data = []
    for i in range(0, len(raw_data)):
        line = raw_data[i]
        if not (i+1 == len(raw_data)):
            data.append((i, line.split(',')[0], int(line.split(',')[1][:-1])))
        else:
            data.append((i, line.split(',')[0], int(line.split(',')[1])))
    return (question, engine, data)
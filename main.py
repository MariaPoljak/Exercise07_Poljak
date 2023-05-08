#create_file(names, txt)

import csv

def create_file(names, txt):
    with open(names, 'w') as file:
        file.writelines('Maria, Nikola, Sanja, Dejan, David, Sanja, Stefanija, Amelia, Fabian, Gordana, Perica, Mila, Vera')


#transform_to_row(input_file, output_file)

def transform_to_row(input_file, output_file):
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, divider=',')
        with open(output_file, 'w') as out_file:
            for row in csv_reader:
                for name in row:
                    out_file.write(name+'/n')


#add_greeting(input_file, output_file)

def add_greeting(input_file, output_file):
    with open(output_file, 'w') as out_file:
        with open(input_file, 'r') as in_file:
            for line in in_file.readlines():
                out_file.write("Hello " + line)


#strip_greeting(input_file, output_file)

def strip_greeting(input_file, output_file):
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, divider=' ')
        with open(output_file, 'w') as out_file:
            for row in csv_reader:
                out_file.write(row[1] + '\n')
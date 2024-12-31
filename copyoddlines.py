def copy_odd_lines(source_file, destination_file):
    with open(source_file, 'r') as src:
        lines = src.readlines()
    
    with open(destination_file, 'w') as dest:
        for index, line in enumerate(lines):
            if index % 2 == 0:
                dest.write(line)

source_file = 'source.txt'
destination_file = 'destination.txt'
copy_odd_lines(source_file, destination_file) 
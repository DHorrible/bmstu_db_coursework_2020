def copy_str(string):
    return (string + '.')[:-1]


def get_query(num):
    file = open(f'queries/{num}.sql', 'r')
    return file.read()

def get_keys():
    key_dict = {}
    with open('keys.txt', 'r') as infile:
        for line in infile:
            items = line.split('=')
            key_dict[items[0]] = items[1].rstrip()
    print(key_dict)
    return key_dict

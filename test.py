f = open('test.txt', 'w')


with open('data.json', 'w') as file:
    json.dump(new_data, file, indent=4)
import os, csv, json 

for f_name in [f for f in os.listdir('output_data') if os.path.isfile('output_data/'+f)] :
    os.remove('output_data/'+f_name)

cars_list, brands = ([],[]) # <<<  :)))

with open('data/input.csv') as data_file:
    csv_reader = csv.reader(data_file)
    for car in [[csv_reader.line_num, row[0], row[1], int(row[2]), int(row[3])] for row in csv_reader]:   
        cars_list.append({key:val for(key, val) in zip(['id', 'brand', 'model', 'hp', 'price'], car)})
        brands.append(cars_list[-1].get('brand'))

results = {
    'slow_cars':        filter(lambda car: car['hp'] < 120, cars_list),
    'fast_cars':        filter(lambda car: 120 <= car['hp'] < 180, cars_list),
    'sport_cars':       filter(lambda car: car['hp'] >= 180 , cars_list),
    'cheap_cars':       filter(lambda car: car['price'] < 1000, cars_list),
    'medium_cars':      filter(lambda car: 1000 <= car['price'] < 5000, cars_list),
    'expensive_cars':   filter(lambda car: car['price'] >= 5000, cars_list)
}

for brand in set(brands):
    results[brand] = list(filter(lambda car: car['brand'] == brand, cars_list))

for result in results:
    with open(f'output_data/{result}.json', 'w') as json_file:
        json.dump(list(results[result]), json_file, indent=2)

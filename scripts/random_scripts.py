import random

value = random.random() # value between 0 - 1
print(value)

value = random.uniform(1, 10) # float value between given integer
print(value)

value = random.randint(1, 6) # rand int between given values
print(value)

greetings = ['Hello', 'Hi', 'Hey', 'Howdy'] 
value = random.choice(greetings) # random.choice picks value from a list
print(value + 'Radek!')

colours = ['red', 'black', 'green']
results = random.choices(colours, weights=[18, 18, 2], k=10) # random.choices picks weighted random elements from list k times 
print(results)

deck = list(range(1,53))
random.shuffle(deck) # shuffle elements in the list
print(deck)

hand = random.sample(deck, k=5) # pick unique elements from the list
print(hand)


''' Simple script to create basic random data for tutorials '''

first_names = ['Lowri', 'Shelly', 'Julie', 'India', 'Theresa', 'Kimberly', 'Ashley', 'Darcie', 'Aidan', 'Ruby']
last_names = ['Patterson', 'Cortez', 'Glass', 'Holland', 'Oconnell', 'Mclean', 'Page', 'Dalton', 'Middleton', 'Curtis']
street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Washington']
fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Krario', 'Edoson', 'Uteley']
county_example = ['Cumbria', 'Durham', 'Northumberland', 'Tyne & Wear', ' North Yorkshire', 'Lancashire', 'Lincolnshire', 'Norfolk', 'Dorset', 'Devon']

for num in range(100):
	first = random.choice(first_names)
	last = random.choice(last_names)

	phone = f'{random.randint(100, 999)}-500-{random.randint(1000, 9999)}'

	street_num = random.randint(100, 999)
	street = random.choice(street_names)
	city = random.choice(fake_cities)
	county = random.choice(county_example)

	address = f'{street_num} {street} St., {city} {county}'
	email = first.lower() + last.lower() + 'bogusemail.com'

	print(f'{first} {last}\n{phone}\n{address}\n{email}\n')


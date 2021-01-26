""" Advent of Code exercise 8. """
""" Count the number of valid passports - those that have all required fields and valid values. 
Continue to treat cid as optional. In your batch file, how many passports are valid?"""

# description https://adventofcode.com/2020/day/4#part2
import re

def read_in_data(data):

    # split string at every new line
    passport = data.split('\n\n')

    # delete empty elements in the list
    clean_passports = [x for x in passport if x]


    return clean_passports


def validate_fields(data):
    single_string = '\n'.join(data)
    print(single_string)

    # field values
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    for i in fields:
        start_filed = single_string.find(i+':')
        end_field = single_string[start_filed:].find(' ')
        field_value = [single_string[start_filed+4:end_field]]
        print(i)
        #print(start_filed)
        #print(end_field)

        print(field_value)






def check_passports(data):

    passports = data

    # necessary fields as a list
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

    # fields found in passport
    valid_fields = []

    n = 0
    count = 0
    valid = 0
    while n < len(passports):
        passport = passports[n]
        for i in fields:
            x = re.search(i, passport)
            if x:
                count += 1
                valid_fields.append(i)
            if count == 8:
                pass
        if valid_fields == fields:
            if validate_fields(passport):
                valid += 1
        elif valid_fields == fields[:-1]:
            if validate_fields(passport):
                valid += 1
        valid_fields = []
        count = 0
        n += 1
    print("Valid passports", valid)



test = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f"""

validate_fields(read_in_data(test))
#check_passports(test)
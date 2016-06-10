# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up.

Since in the previous quiz you made a decision on which value to keep for the
"area#Land" field, you now know what has to be done.

Finish the function fix_area(). It will receive a string as an input, and it
has to return a float representing the value of the area or None.
You have to change the function fix_area. You can use extra functions if you
like, but changes to process_file will not be taken into account.
The rest of the code is just an example on how this function can be used.
"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'


def fix_area(area):
    if area == "NULL" or "":
        return None
    elif "{" in area:
        stripval = area.strip('{}')
        splitval = stripval.split(delimiter="|")
        if splitval[0].find("e+") > splitval[1].find("e+"):
            return float(splitval[0])
        else:
            return float(splitval[1])
    else:
        return float(area)


def process_file(filename):
    # CHANGES TO THIS FUNCTION WILL BE IGNORED WHEN YOU SUBMIT THE EXERCISE
    data = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        #skipping the extra metadata
        for i in range(3):
            l = reader.next()

        # processing file
        for line in reader:
            if "populationTotal" in line:
                print "----------POP CHECK----------"
                print 'BEFORE:', line['populationTotal']
                line["populationTotal"] = fix_area(line["populationTotal"])
                print 'after:', line['populationTotal']
            if "areaMetro" in line:
                print "----------AREA CHECK----------"
                print 'BEFORE:', line['areaMetro']
                line["areaMetro"] = fix_area(line["areaMetro"])
                print 'after:', line['areaMetro']
            if "postalCode" in line:
                print "----------POSTAL CHECK----------"
                print 'BEFORE:', line['postalCode']
                line["postalCode"] = fix_area(line["postalCode"])
                print 'after:', line['postalCode']



    return data

process_file(r'C:\Users\Bash\Desktop\Udacity\2_Data Analysis\P3\0610\cities.csv')

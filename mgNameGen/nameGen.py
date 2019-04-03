import csv
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def readcsv(file):
    openFile = open(file)
    csvFile = csv.reader(openFile)
    output = list(csvFile)
    return output

contentfile = '/content/'
peopleFile = dir_path + contentfile + 'people.csv'
nounsFile = contentfile + 'nouns.csv'
placesFile = contentfile + 'places.csv'

people = readcsv(peopleFile)
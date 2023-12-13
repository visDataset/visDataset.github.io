import json
import csv

def read_csv(file):
    data = []
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for line in reader:
            data.append(line)
    print('read from', file)
    return data

def write_json(data, file):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
    print('write to', file)


dataTypes = [
    'VIS','NL','VIS Type','Data','Mapping','Visual Element','Element Position','Others'
]

visTypes = [
    'Bar','Scatter','Line','Area','Pie','Others'
]

rawDataConstruction = [
    'Crawling','Extraction','Crowdsourcing','Synthesizing','Combining'
]

dataExtension = [
    'Manual','Rule-based','Learning-based'
]

techniques = [
    'Object Detection','Classification','Regression','Translation','OCR','Dimensionality Reduction'
]

tasks = [
    'Visualization Recommendation','Reverse Engineering','Feature Extraction'
]

applications = [
    'Generation','Retrieval','Exploration','Assessment'
]



fieldNameToidx = {}

def convert_data():
    input_file = 'datasets.csv'
    output_file = 'datasets.json'

    data = read_csv(input_file)
    header = data[0]
    data = data[1:]
    for i, field in enumerate(header):
        fieldNameToidx[field] = i

    output = []
    for d in data:
        idx = d[0]
        title = d[1]
        year = d[2]
        dataTypesV = []
        visTypesV = []
        rawDataConstructionV = []
        dataExtensionV = []
        techniquesV = []
        tasksV = []
        applicationsV = []

        for field in dataTypes:
            if d[fieldNameToidx[field]] == '√':
                dataTypesV.append(field)
        for field in visTypes:
            if d[fieldNameToidx[field]] == '√':
                visTypesV.append(field)
        for field in rawDataConstruction:
            if d[fieldNameToidx[field]] == '√':
                rawDataConstructionV.append(field)
        for field in dataExtension:
            if d[fieldNameToidx[field]] == '√':
                dataExtensionV.append(field)
        for field in techniques:
            if d[fieldNameToidx[field]] == '√':
                techniquesV.append(field)
        for field in tasks:
            if d[fieldNameToidx[field]] == '√':
                tasksV.append(field)
        for field in applications:
            if d[fieldNameToidx[field]] == '√':
                applicationsV.append(field)

        # useForLearning = 
        size = int(''.join(d[3].split(',')))
        stillGrow = ['No'] if d[20] == 'X' else ['Yes']
        url = d[-1]

        o = {
            'idx': idx,
            'title': title,
            'year': year,
            'dataTypes': dataTypesV,
            'visTypes': visTypesV,
            'rawDataConstruction': rawDataConstructionV,
            'dataExtension': dataExtensionV,
            'techniques': techniquesV,
            'tasks': tasksV,
            'applications': applicationsV,
            'size': size,
            'stillGrow': stillGrow,
            'url': url,
            'authors': [],
            'journal': '',
            'venue': '',
            'venueField': '',
            'doi': ''
        }

        output.append(o)
    write_json(output, output_file)

convert_data()

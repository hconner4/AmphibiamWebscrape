import pandas as pd
import numpy as np
import re
import csv
import os
import shutil
from fuzzywuzzy import fuzz
from datetime import datetime
from kmodes.kmodes import KModes

amphibian_type = []
amphibian_subtype = []
animal_ages = []
animal_prices = []
animal_types = []
animal_locations = []
animal_seller = []
filenames = []
indices = []

states = [
    'AK', 'Alaska',
    'AL', 'Alabama',
    'AR', 'Arkansas',
    'AZ', 'Arizona',
    'CA', 'California',
    'CO', 'Colorado',
    'CT', 'Connecticut',
    'DC', 'District of Columbia',
    'DE', 'Delaware',
    'FL', 'Florida',
    'GA', 'Georgia',
    'HI', 'Hawaii',
    'IA', 'Iowa',
    'ID', 'Idaho',
    'IL', 'Illinois',
    'IN', 'Indiana',
    'KS', 'Kansas',
    'KY', 'Kentucky',
    'LA', 'Louisiana',
    'MA', 'Massachusetts',
    'MD', 'Maryland',
    'ME', 'Maine',
    'MI', 'Michigan',
    'MN', 'Minnesota',
    'MO', 'Missouri',
    'MS', 'Mississippi',
    'MT', 'Montana',
    'NC', 'North Carolina',
    'ND', 'North Dakota',
    'NE', 'Nebraska',
    'NH', 'New Hampshire',
    'NJ', 'New Jersey',
    'NM', 'New Mexico',
    'NV', 'Nevada',
    'NY', 'New York',
    'OH', 'Ohio',
    'OK', 'Oklahoma',
    'OR', 'Oregon',
    'PA', 'Pennsylvania',
    'RI', 'Rhode Island',
    'SC', 'South Carolina',
    'SD', 'South Dakota',
    'TN', 'Tennessee',
    'TX', 'Texas',
    'UT', 'Utah',
    'VA', 'Virginia',
    'VT', 'Vermont',
    'WA', 'Washington',
    'WI', 'Wisconsin',
    'WV', 'West Virginia',
    'WY', 'Wyoming'
]

# I made this list by looking at the data and typeing in each type of amphibian I saw
# will need updating
type_of_amphibians = pd.read_csv(r'/Users/hconner/Downloads/amphibian_types.csv')
frogs = type_of_amphibians['Frog'].values
newts = type_of_amphibians[~type_of_amphibians['Newt'].isna()]['Newt'].values
salamanders = type_of_amphibians[~type_of_amphibians['Salamander'].isna()]['Salamander'].values
axolotls = type_of_amphibians[~type_of_amphibians['Axolotl'].isna()]['Axolotl'].values
toads = type_of_amphibians[~type_of_amphibians['Toad'].isna()]['Toad'].values
# make dicitonary for easy sorting
amphibian_dict = {'frog':frogs, 'newt':newts, 'salamander':salamanders, 'axolotl':axolotls, 'toad':toads}


#path to all stored data
dir_path = (r'/Users/hconner/AmphibianData2')
new_dir_path = (r'/Users/hconner/AmphibianData2')
for filename in os.listdir(dir_path):
    #unique files names so just grabbing all csvs in this folder #filename = 'data_0407_05042023.csv'
    if filename.endswith('.csv'):
        if filename not in filenames:
            file_path = os.path.join(dir_path, filename) # file_path = (r'/Users/hconner/AmphibianData/data_0407_05042023.csv')
            append_name = file_path.split('_')[2]

            date_object = datetime.strptime(append_name.split('.csv')[0], "%m%d%Y").date()
            #print(date_object)
            #for checking if new data structure was used (after 5/16)
            append_name.split('.csv')[0]
            with open(file_path, 'r') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                    #initialize all variables incase they are not found
                    # and the lengths of the list will be the same
                    amphibian_type_1 = 'None'
                    amphibian_type_2 = 'None'
                    animal_age = 'None'
                    animal_state = 'None'
                    seller = 'None'

                    #print(row)
                    # Sorting through data for relevant information
                    # split on new line character
                    # index of all words is 3
                    # This is only applicable after may 16
                    reference_date = datetime.strptime("05162023", "%m%d%Y").date()
                    if date_object > reference_date:
                        data_as_string = row[3].split('\n')
                    else:
                        data_as_string = row[1].split('\n')
                    
                    # find the first instance of a dollar sign so split
                    index_of_price = [idx for idx, s in enumerate(data_as_string) if '$' in s][0] #gives index of price everything before this is type of amphibian
                    
                    # animal type should be everything before price
                    animal_type = data_as_string[0:index_of_price]

                    #search for amphibian type
                    for string in animal_type: #loop through strings in list
                        words = string.split() # split into individual words since matching single words
                        for word in words: # loop through the words
                            for amphibian in ['frog', 'salamander', 'toad', 'axolotl', 'newt']: # loop through list of amphibians
                                if amphibian.upper() in word.upper(): #if match is found
                                    amphibian_type_1 = amphibian
                    

                    if amphibian_type_1 != 'None':
                        # now that you have the amphibian type you can get the subcategory
                        for_searching = amphibian_dict[amphibian_type_1]
                        for string in animal_type: #loop through strings in list
                            #words = string.split() # split into individual words since matching single words
                            #for word in words:
                            for sub_category in for_searching:
                                if sub_category.upper() in string.upper():
                                    amphibian_type_2 = sub_category
                    else:
                        for amph_type in amphibian_dict:
                            for_searching = amphibian_dict[amph_type]
                            for string in animal_type: #loop through strings in list
                                #words = string.split() # split into individual words since matching single words
                                #for word in words:
                                for sub_category in for_searching:
                                    if sub_category.upper() in string.upper():
                                        amphibian_type_2 = sub_category
                                        amphibian_type_1 = amph_type

                    #search animal type for animal age
                    #juvenile, baby, subadult, adult
                    # Need to copy the format of idx, string
                    ages = ['Baby', 'Baby/Juvenile','Juvenile', 'Subadult', 'Adult']
                    for string in animal_type:  
                        words = string.split() 
                        for word in words:
                            for age in ages:
                                if age.upper() == word.upper():
                                    animal_age = age

                    #animal price
                    animal_price = re.findall(r'\d+(?:\.\d+)?', data_as_string[index_of_price])

                    # find the animal location by matching from the list of states
                    for idx,string in enumerate(data_as_string):
                        for state in states:
                            if f" {state} " in f" {string} ":
                                animal_state = data_as_string[idx]
                                state_index = idx

                    seller = data_as_string[state_index -1]

                    # if sub type is none make type
                    if amphibian_type_2 == 'None':
                        amphibian_type_2 = amphibian_type_1

                    amphibian_type.append(amphibian_type_1)
                    amphibian_subtype.append(amphibian_type_2)
                    animal_ages.append(''.join(animal_age))
                    animal_locations.append(''.join(animal_state))
                    animal_prices.append(''.join(animal_price))
                    animal_seller.append(seller)
                    animal_types.append(' '.join(animal_type))
                    filenames.append(filename)
                    indices.append(index_of_price)

            #move files to a new location after analysis
            old_file_path = os.path.join(dir_path, filename)
            new_file_path = os.path.join(new_dir_path, filename)

            shutil.move(old_file_path, new_file_path)

# save the data as a csv
amphibian_data = pd.DataFrame({
                'filenames':filenames, 
                'animal_types':animal_types,
                'amphibian_types':amphibian_type,
                'amphibian_subtypes':amphibian_subtype,
                'animal_ages':animal_ages,
                'animal_locations':animal_locations,
                'animal_prices':animal_prices,
                'animal_sellers':animal_seller})

#current date for all data name

amphibian_data.to_csv('amphbian_data_06202023.csv')

#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import random


def total_data_points(data):
    return len(data)


def feature_per_person(data):
    random_name = random.choice(data.keys())
    return len(data[random_name])


enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print "total data points => " + str(total_data_points(enron_data))
print "features per person => " + str(feature_per_person(enron_data))

import csv
import random
# Names : Mona , Nimrod , Mohammad Joubat , Jehad , Mhinkkye ,Magdi, Rani
attributes_yes_list = []
attributes_no_list = []
positive_dataset = []
negative_dataset = []
pos_train = []
neg_train = []
training_data = []
test_data = []
g_attributes = []  # doesn't include poisonous or edible columns
g_attributes_dictionary = {}
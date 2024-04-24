import sys
import os 
from list_returner import *
from directory_lister import * 
import random
from argument_parser import *
from batch_handler import *
cli_arguments= parse_args()
batch_number = cli_arguments[0]
excluded_topics =cli_arguments[1]
excluded_genres = cli_arguments[2]
batch_output = cli_arguments[3]
set_output = cli_arguments[4]
print_output = cli_arguments[5]
print_sets = cli_arguments[6]
batch_output_dir = cli_arguments[7]
set_output_dir = cli_arguments[8]
custom_subjects_dir = cli_arguments[9]
custom_opinions_dir = cli_arguments[10]
excluded_opinions = cli_arguments[11]
output_batch(batch_number,excluded_topics,excluded_genres, batch_output, set_output, print_output, print_sets, batch_output_dir, set_output_dir, custom_subjects_dir, custom_opinions_dir, excluded_opinions)
#subject_paths =[]
#for subject in dir_lister("subjects", excluded_topics):              # start off on subjects
    #subject_paths.append("subjects/"+subject)       #for each non banned subject add its path to the list of subjects to treat
#subject_list =[]
#for subject in subject_paths:                       #for each non banned subject (each in the subject_paths array since dir_lister bans those we don't want)
    #for genre in dir_lister(subject, excluded_genres):               # take the non banned genres
        #for element in return_list(subject+"/"+genre):  #and for each non banned add all the lines one by one to the list of things to have bad takes about. this isn't required per say but we need to put it this way because we want one huge array
            #subject_list.append(element)
#
#
#
#opinion_paths = []
#for topics in dir_lister("opinions/topics"):
    #opinion_paths.append("opinions/topics/" + topics)
#
#opinion_list = []
#for path in opinion_paths:
    #opinion_topics_list = return_list(path)
    #for opinion in opinion_topics_list:
        #opinion_list.append(opinion)
#
#for i in range(batch_number):
   # print("I can't believe " + subject_list[random.randint(0,len(subject_list)-1)] + " was about " + opinion_list[random.randint(0,len(opinion_list)-1)] + " all along")


from datetime import datetime
from directory_lister import *
from list_returner import *
import random
date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
file_name = "batch-"+date

def output_batch(number,excluded_topics,excluded_genres, batch_output ,set_output, print_batch, print_sets, save_batch_to_dir, save_sets_to_dir, subject_dir_path, opinion_dir_path, excluded_opinion_topics):
    #batch_set=[]
    subject_list = get_subjects(excluded_topics, excluded_genres, subject_dir_path)
    opinion_list = get_opinions(opinion_dir_path, excluded_opinion_topics)
    returned_set = make_batches(number, subject_list, opinion_list)

    if print_batch:
        for i in range(len(returned_set)):
            print("I can't believe " + subject_list[returned_set[i][0]] + " was about " + opinion_list[returned_set[i][1]] + " all along")
    if batch_output:
        if save_batch_to_dir != "":
            try:
                f = open(save_batch_to_dir+str(number)+"-"+file_name,'x')
                f.close
            except:
                print("Couldn't create batch file in specified directory")
            try:
                for i in range(len(returned_set)):
                    with open(save_batch_to_dir+str(number)+"-"+file_name,'a') as file:
                        file.write("I can't believe " + subject_list[returned_set[i][0]] + " was about " + opinion_list[returned_set[i][1]] + " all along \n")
            except:
                print("Couldn't write batches to specified directory")
        else:
            f = open("results/output/"+str(number)+"-"+file_name,'x')
            f.close()
            for i in range(len(returned_set)):
                with open("results/output/"+str(number)+"-"+file_name,'a') as file:
                        file.write("I can't believe " + subject_list[returned_set[i][0]] + " was about " + opinion_list[returned_set[i][1]] + " all along \n")

    if set_output:
        if save_sets_to_dir != "":
            try:
                f = open(save_sets_to_dir+str(number)+"-"+"set-"+date,'x')
                f.close
            except: 
                print("Couldn't create set file in specified directory")
            try:
                for i in range(len(returned_set)):
                      with open(save_sets_to_dir+str(number)+"-"+"set-"+date,'a') as file:
                        file.write(subject_list[returned_set[i][0]]+ " | " + opinion_list[returned_set[i][1]]+ "\n")
            except:
                print("Couldn't write to the set file")
        else:
            f = open("results/sets/"+str(number)+"-"+"set-"+date,'x')
            f.close

            with open("results/sets/"+str(number)+"-"+"set-"+date,'a') as file:
                for i in range(len(returned_set)):
                    file.write(subject_list[returned_set[i][0]]+ " | " + opinion_list[returned_set[i][1]]+ "\n")
    if print_sets:
        for i in range(len(returned_set)):
            print(subject_list[returned_set[i][0]] + " | " + opinion_list[returned_set[i][1]])
def get_subjects(excluded_topics, excluded_genres, subject_dir_path):
    subject_paths =[]
    subject_dir_path_listed=subject_dir_path[:-1]
    for subject in dir_lister(subject_dir_path_listed, excluded_topics):              # start off on subjects
        subject_paths.append(subject_dir_path+subject)       #for each non banned subject add its path to the list of subjects to treat
    subject_list =[]
    for subject in subject_paths:                       #for each non banned subject (each in the subject_paths array since dir_lister bans those we don't want)
        for genre in dir_lister(subject, excluded_genres):               # take the non banned genres
            for element in return_list(subject+"/"+genre):  #and for each non banned add all the lines one by one to the list of things to have bad takes about. this isn't required per say but we need to put it this way because we want one huge array
                subject_list.append(element)
    return subject_list


def get_opinions(opinion_dir_path, excluded_opinion_topics):
    opinion_dir_path_listed=opinion_dir_path[:-1]
    opinion_paths = []
    for topics in dir_lister(opinion_dir_path_listed, excluded_opinion_topics):
        opinion_paths.append(opinion_dir_path+ topics)

    opinion_list = []
    for path in opinion_paths:
        opinion_topics_list = return_list(path)
        for opinion in opinion_topics_list:
            opinion_list.append(opinion)

    return opinion_list


def make_batches(number, subject_list,opinion_list):

    batch_set=[]

    for i in range(number):
        subject_index= random.randint(0,len(subject_list)-1)
        opinion_index = random.randint(0,len(opinion_list)-1)
        individual_set= (subject_index,opinion_index)
        if individual_set not in batch_set:
            batch_set.append(individual_set)


    return batch_set

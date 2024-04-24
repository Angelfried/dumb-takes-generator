import sys
def parse_args():
    arguments = sys.argv[1:]
    batch_number =1
    excluded_topics = []
    excluded_opinions= []
    excluded_genres = []
    batch_output = False
    set_output = False
    print_output = True
    print_set = False
    save_batch_to_dir= ""
    save_set_to_dir = ""
    custom_subjects_dir = "subjects/"
    custom_opinions_dir = "opinions/topics/"
    for arg in arguments:
        if arg[:8] == "--batch=":
            try:
                batch_number = int(arg[8:])
            except:
                print("Batch number entered wasn't an int. Stopping.")
        if arg[:10] == "--exclude=":        # the excluded broad topics
            excluded_topics.append(arg[10:])
        if arg[:16] == "--exclude-genre=": #exclude specific genres per topic    
            excluded_genres.append(arg[16:])
        if arg[:16] == "--batch-to-file=":
            parsed_arg=arg[16:]
            batch_output = bool_parser(parsed_arg)
        if arg[:15] == "--sets-to-file=":
            parsed_arg = arg[15:]
            set_output = bool_parser(parsed_arg)
        if arg[:15] == "--print-output=":
            parsed_arg = arg[15:]
            print_output = bool_parser(parsed_arg)
        if arg[:13] == "--print-sets=":
            parsed_arg = arg[13:]
            print_set = bool_parser(parsed_arg)
        if arg[:20] == "--save-batch-to-dir=":
            save_batch_to_dir = arg[20:]
        if arg[:19] == "--save-sets-to-dir=":
            save_set_to_dir = arg[19:]
        if arg[:22] == "--custom-subjects-dir=":
            custom_subjects_dir = arg[22:]
        if arg[:22] == "--custom-opinions-dir=":
            custom_opinons_dir = arg[22:]
        if arg[:24] == "--exclude-opinion-topic=":
            excluded_opinions.append(arg[24:])
        if arg[:6] == "--help":
            print("""
                Dumb Take Generator v1.0
                Syntax: python main.py [OPTIONS]
                Orders of different switches doesn't matter.
                OPTIONS:
                    Unless specified otherwise, any option that asks for a directory must end in a /
                    --batch=number
                    Will produce {number} amount of dumb takes. Has to be a positive integer equal or superior to 1. Defaults to 1.
                    --exclude=topic 
                    In the subjects/ folder you will find subfolder. These are the topics. This option allows you to exclude individual topics. If you want to exclude several topics, you have to re-add the option. I.e --exclude=topic1 --exclude=topic2
                    --exclude-genre=genre 
                    Same idea as before, except this time it bans individual files. For this reason no 2 files can have the same names.
                    If you want to exclude several genres, same logic as above, re-add them individually.
                    --batch-to-file=True|False 
                    Set it to true to save the batch of answers to a file. Set it to false to not enable that. Set to false by default. Not case sensitive and can also take in 0 or 1 as values, 1 being true. If a directory is not specified, the batches are saved in results/output. Formatted as {number of takes}-batch-{date}
                    --sets-to-file=True|False
                    Each take is made of a subject/opinion combo. This option allows you to save each individual set without the sentences. If a directory is not specified, saves them in results/sets. Formatted as {number of takes}-batch-{date}
                   --print-output=True|False 
                   Prints the batch to the screen (and to stdout). Set to True by default.
                   --print-sets=True|False
                   Prints the sets in the batch to the screen (and to stdout). Set to False by default.
                   --save-batch-to-dir=path/to/dir/ 
                   Will attempt to save the batches to a dir in particular. Will save the batch in the last dir without creating its own directory.
                   --save-sets-to-dir=path/to/dir/
                   Will attempt to save the sets to the given directory. Both of these options take in the relative path.
                    --custom_subjects_dir=path/to/dir/
                    Instead of taking in the default folders in subjects/, you can feed it your own folder of subjects. The directory needs be structured as such:
                        subjects 
                        | 
                        | - Topic
                        |     | - genre
                        |     | - genre
                        |
                        | - Topic 
                        |     | - genre 

                    With the genre being a text file with each different entry on a separate line. Note: you can use this command in conjunction with --exclude= 
                    --custom-opinions-dir=path/to/dir 
                    Instead of taking in the default opinions in opinions/ , you can feed it your own opinions file. The directory needs to contain opinion files, a single one or several. Each entry needs to be on its own separate line.
                    --exclude-opinion-topic=topic 
                    If the opinions folder contains several files, you can use this one to ban others. If you want to exclude several, you have to add the option again. I.e --exclude-opinion-topic=topic1 --exclude-opinion-topic=topic2.
                    --help
                    Print this help message.
            """)
    return batch_number, excluded_topics, excluded_genres, batch_output, set_output, print_output, print_set, save_batch_to_dir, save_set_to_dir, custom_subjects_dir, custom_opinions_dir, excluded_opinions



def bool_parser(input_arg):
    input_arg = input_arg.lower()
    returned_bool = False
    if input_arg == "true" or input_arg == "1":
        return True
    return returned_bool


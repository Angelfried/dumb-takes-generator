# dumb-takes-generator
Generates inflammatory takes designed to start pointless arguments. 
The original idea was to make this program and then make a twitter bot which would try these takes to try and start pointless arguments. However I don't have a computer to run it on. If you want to do this, go ahead.
# Setting up
```
 git clone https://github.com/Angelfried/dumb-takes-generator/
 cd dumb-takes-generator
 python main.py
```

# Adding subjects
The subjects/ folder is comprised of 'topics' (i.e books, movies, poetry, whatever you want to add). To add more of these just create folders that have the corresponding name. If you want to add more entries in total you need to create a file (or several, if you want to ban some specifically) inside each folder containing the names of whatever work you want to have dumb takes on. Each name needs to be on a separate line from the last.
You can then exclude or include certain topics/genres using the different flags.
## You cannot have 2 genre files bearing the same name.

# Adding opinions
Works relatively the same, if you want to add opinions add them in a file with each line being separate from the last. Per the same as before you can exclude/include certain files so long as they're all in the same directory.

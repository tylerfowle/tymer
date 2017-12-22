import time
import json
import os
import sys
from datetime import datetime
from datetime import timedelta


debug = False

# VARIABLES
# ================================================================================
# database file
tymer_filepath=os.path.expanduser('~/.tymer/tymers.txt')
tymer_file = open(tymer_filepath, "a+")

# set tymer vars
tymer_duration = 30
tymer_description = ""
tymers = {}
tymer = {}

# set current time vars
current_time = datetime.now()
current_time_sec = time.time()

# set future time vars
future_time = current_time + timedelta(minutes=30)
future_time_sec = current_time_sec + timedelta(minutes=30).total_seconds()

# set default options
default_duration = 30
default_description = "No Description"

# set vars in tymer dictionary
tymer['Description'] = tymer_description
tymer['start_time'] = str(current_time)
tymer['start_time_sec'] = current_time_sec
tymer['end_time'] = str(future_time)
tymer['end_time_sec'] = future_time_sec
tymer['tymer_duration'] = tymer_duration

# arguments
argument_len=len(sys.argv)
argument_list=str(sys.argv)
# ================================================================================


# MAIN
# convert tymer dict to string with pretty printing
json_output = json.dumps(tymer, sort_keys=True, indent=4, separators=(',', ': '))
print(json_output)


if debug == True:

    print argument_len
    print argument_list

    json_string = '{"first_name": "Guido", "last_name":"Rossum"}'

    parsed_json = json.loads(json_string)
    print(parsed_json['first_name'])

    print(current_time)
    print(current_time_sec)

    print(future_time)
    print(future_time_sec)

    os.system('clear')


f = open("database.txt", "a+")
f.write(json_output)
f.write(",")
f.close()


# f=open("database.txt", "r")
# contents = f.read()
# print contents

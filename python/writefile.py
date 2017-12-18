import time
import json
from datetime import datetime
from datetime import timedelta


debug = False

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

# convert tymer dict to string with pretty printing
json_output = json.dumps(tymer, sort_keys=True, indent=4, separators=(',', ': '))
print(json_output)


if debug == True:

    json_string = '{"first_name": "Guido", "last_name":"Rossum"}'

    parsed_json = json.loads(json_string)
    print(parsed_json['first_name'])

    print(current_time)
    print(current_time_sec)

    print(future_time)
    print(future_time_sec)


# f = open("writefile.txt", "a+")
# for i in range(10):
#     f.write("this is line %d\r\n" % (i+1))
# f.write("end")
# f.close()


# f=open("writefile.txt", "r")
# contents = f.read()
# print contents

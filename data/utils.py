
import json
def load_image(path):
    pass



# WRITE 
def write_options(data):
    try:
        with open("options_file.txt","w") as file:
            json.dump(data,file)
    except:
        print("Error writing data")

# READ
def read_options(initial_data):
    try:
        with open("options_file.txt") as file:
            data = json.load(file)
            return data
    except:

        print("Error reading data")
        return initial_data

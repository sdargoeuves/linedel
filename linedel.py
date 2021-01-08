import os
import sys

def linedel():
    #Check that we have input_file as argument
    if len(sys.argv) == 2:
        input_file = os.path.expanduser("~") + "/.ssh/known_hosts"
        line_arg = sys.argv[1]
    elif len(sys.argv) == 3:
        input_file = sys.argv[1]
        line_arg = sys.argv[2]
    else:
        err_msg = ("##ERR## You need to specify [src file and] the line to delete as arguments:\n"
            "python3 linedel.py [input_file] line_number_to_remove")
        sys.exit(err_msg)

    #confirm the value of the argument is an integer
    try:
        line_arg = int(line_arg)
        if line_arg > 0:
            line_rm = int(line_arg) - 1
        else:
            raise ValueError("#ERR## the value should be a Positive Integer greater than 0")
    except ValueError as err_msg:
        sys.exit(err_msg)
    except:
        err_msg = ("##ERR## Unkown error, try again:\n"
            "python3 linedel.py [input_file] line_number_to_remove")
        sys.exit(err_msg)
    
    #create variables
    output_file = "".join(["/tmp/", os.path.basename(input_file), ".bak"])
    index = 0
    line_removed = False
    
    #Confirm the file exists, and add the values in a list
    if os.path.isfile(input_file):
        with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
            for line in in_file:
                if index != line_rm:
                    out_file.write(line)
                else:
                    line_removed = True
                index += 1
    else:
        err_msg = f"##ERR## Input file '{input_file}' does not exist"
        sys.exit(err_msg)
    
    #if a line has been removed, we remove the original file and replace with the output
    if line_removed:
        os.remove(input_file)
        os.rename(output_file, input_file)
        print("##INFO## line '%s' has been removed from the file '%s'" % (line_arg, input_file))
    else:
        os.remove(output_file)
        print("##INFO## No line removed from the file '%s'" % (input_file))

if __name__ == "__main__":
    linedel()

"""
Batch Process C: Third transformation

Read from a file, transform, write to a new file.
In this case, covert degree K to degree F.

Note: 
This is a batch process, but the file objects we use are 
often called 'file-like objects' or 'streams'.
Streaming differs in that the input data is unbounded.

Use logging, very helpful when working with batch and streaming processes. 

"""

# Import from Python Standard Library

import csv
import logging

# Set up basic configuration for logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Declare program constants

INPUT_FILE_NAME = "batchfile_2_kelvin.csv"
OUTPUT_FILE_NAME = "batchfile_3_fahrenheit.csv"

# Define program functions (bits of reusable code)
# Use docstrings - and indentation matters!


def convert_k_to_f(temp_k):
    """Converts Kelvin back to Fahrenheit.
    Utilizes both float and round functions to convert the string to a float.
    All CSV values are read as strings
    When creating the round, be sure to place () correctly and indicated rounding to nearest place.
    """
    logging.debug(f"Calling convert_k_to_f() with {temp_k}.")
    fahrenheit = round((float(temp_k) - 273.15) * 1.8 + 32)
    logging.debug(f"Converted {temp_k}K to {fahrenheit}F.")
    return fahrenheit


def process_rows(input_file_name, output_file_name):
    """Reads input file and converts temperature, then writes to an output file."""
    logging.info(f"Calling process_rows(): {input_file_name} to {output_file_name}.")

    #Creating file object for input (r= read)
    with open(input_file_name, "r") as input_file:
        logging.info(f"Opened for reading: {input_file_name}.")

        #Creating CSV reader object:
        reader = csv.reader(input_file, delimiter=",")
        header = next(reader)
        logging.info(f"Skipped header row: {header}")

        #Creating a file object for output (w = write)
        with open(output_file_name, "w", newline="") as output_file:
            logging.info(f"Opened for writing: {output_file_name}.")

            #Creating CSV writer object.
            writer = csv.writer(output_file, delimiter=",")
            #Creating rules for rows in the reader and Header.
            writer.writerow(["Year", "Month", "Day", "Time", "TempF"])
            #Added Extractiosn for values from input row into names variables (Year, Month, Day, Time, TempF)
            #For each row:
            for row in reader:
                Year, Month, Day, Time, TempK = row

                #Call conversion function to pass TempK argument and assign to TempF variable.
                TempF = convert_k_to_f(TempK)

                #Write the transofrmed data to the output file.
                writer.writerow([Year, Month, Day, Time, TempF])

        #Creating CSV reader object
        #reader = csv.reader(input_file, delimiter=",")
        #header = next(reader)
        #logging.info(f"Skipped header row: {header}")
        #return


# ---------------------------------------------------------------------------
# If this is the script we are running, then call some functions and execute code!
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        logging.info("===============================================")
        logging.info("Starting batch process C.")
        process_rows(INPUT_FILE_NAME, OUTPUT_FILE_NAME)
        logging.info("Processing complete! Check for new file.")
        logging.info("===============================================")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

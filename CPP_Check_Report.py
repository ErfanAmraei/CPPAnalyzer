from os.path import exists  # Import only the exists method from the os.path module
import xml.etree.ElementTree as ElementTree  # Importing the ElementTree module to parse XML files
import pandas  # Importing the pandas library for data manipulation and exporting data to Excel
from XML_Parser import CPPCheck_xmlParser  # Importing the custom CPPCheck_xmlParser class from XML_Parser for XML parsing
import sys
from strings import CODING_ERROR_MSGS #Importing error messages
def export_Excel_File(errors):
    """
    Convert a list of errors (as dictionaries) to an Excel file.

    Args:
        errors (list): A list of dictionaries where each dictionary represents an error.
    Raises:
        ValueError: If errors is not a list, is empty, or any item in the list is not a dictionary.
    """
    
    # Check if errors is a list
    if not isinstance(errors, list):
        raise ValueError(CODING_ERROR_MSGS['list_err'])
    
    # Check if errors list is not empty
    if not errors:
        raise ValueError(CODING_ERROR_MSGS['empty_list_err'])
    
    # Check if all items in the errors list are dictionaries
    if not all(isinstance(error, dict) for error in errors):
        raise ValueError(CODING_ERROR_MSGS['list_must_be_dic_err'])

    # Convert the list of dictionaries (errors) into a pandas DataFrame for easier data manipulation
    data_frame = pandas.DataFrame(errors)

    # Define the output path for the Excel file
    xlsx_directory =  sys.argv[1].replace("\\", "/")  # Replace backslashes with forward slashes
    output_path = f"{xlsx_directory}/cppcheck_reports.xlsx"

    # Export the DataFrame to an Excel file without the row index
    data_frame.to_excel(output_path, index=False)

    # Print a confirmation message once the Excel file has been saved
    print(CODING_ERROR_MSGS['success_msg'].format(output_path=output_path))


def main():
    """
    Main function to load an XML file, extract error data using the CPPCheck_xmlParser, and export it to an Excel file.
    """
    # Define the XML file path
    xml_directory = sys.argv[1].replace("\\", "/")  # Replace backslashes with forward slashes
    xml_file_path = f"{xml_directory}/cppcheck.xml"
    # Check if the XML file exists
    if exists(xml_file_path):
        # If the file exists, parse it into an ElementTree object
        tree = ElementTree.parse(xml_file_path)

        # Create an instance of the CPPCheck_xmlParser class, passing the parsed tree and the tag to extract error information
        parser = CPPCheck_xmlParser('errors/error', tree, 'id', 'msg', 'severity', 'file', 'line', 'location', 'symbol')

        # Extract specific error data from the XML file using the extract_CPPCheck_Data_from_XML method
        errors = parser.extract_CPPCheck_Data_from_XML()
        
        # Export the extracted error data into an Excel file
        export_Excel_File(errors)
    else:
        # If the file does not exist, print an error message
        print(f"Error: The file '{xml_file_path}' does not exist.")

# If this script is executed directly, call the main function
if __name__ == "__main__":
    main()
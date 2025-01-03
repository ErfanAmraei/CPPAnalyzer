# strings.py

GUI_STRINGS = {
    'title': "CppAnalyzer V1.1",
    'source_label': "Source Code Directory:",
    'destination_label': "Destination Directory:",
    'select_source_label': "Select Source Code Directory",
    'select_destination_label': "Select Destination Directory",
    'browse_button': "Browse",
    'run_button': "Run Code Analyzer",
    'show_err_title': "Error",
    'error_no_files_message': "Cannot locate any C or C++ file",
    'empty_fields': "Please provide both source and destination paths.",
    'success_title': "Success",
    'success_message': "Cppcheck completed. Report saved in {destination}",
    'batch_execution_err': "An error occurred: {e}"
}

CODING_ERROR_MSGS = {
    'list_err': "The 'errors' argument must be a list.",
    'empty_list_err': "The 'errors' list is empty.",
    'list_must_be_dic_err': "All items in the 'errors' list must be dictionaries.",
    'success_msg': "Error information has been extracted and saved to {output_path}",
    #the following messges are used in xml_parser,py
    'tag_err': "The tag must be a string.",
    'element_tree_err': "The tree must be an instance of ElementTree.",
    'attributes_no_err': "Exactly 7 attributes_SubXMLTag must be provided.",
    'attributes_type_err': "All attributes_SubXMLTag must be strings.",
    'cppcheck_data_no_err': "Exactly 3 CPP check data must be provided.",
    'cppcheck_data_type_err': "All CPP check data must be strings.",
    'no_err': "No errors found in the XML file."
}
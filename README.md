# CPPAnalyzer  

**CPPAnalyzer** is a powerful tool for analyzing C and C++ source code, built on the foundation of **Cppcheck**. It provides a user-friendly **Graphical User Interface (GUI)** to make the analysis process seamless and efficient.  

## Important Notice:
This project is intended for **demonstration purposes only**. The code is provided to showcase specific functionalities and is not meant for modification, redistribution, or commercial use. Please respect the terms of use and refrain from altering or redistributing the code.

## Features  
- **GUI-based Workflow**: Simplifies input of source and destination paths. it can be utilize by running **CPPAnalyzer.py**.
- **Dual Output Formats**:  
  - **XML file**: For machine-readable results.  
  - **Spreadsheet file**: For human-friendly interpretation.  
- **Integration Ready**: Easily integrates with automation tools like **Jenkins** using the `Run_Cpp_Check.bat` script.  

## Getting Started  

### Prerequisites  
- Python 3.x  
- Cppcheck (ensure it is installed and added to the system PATH)  
- Required Python packages (install using `pip install -r requirements.txt`)  

### Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/ErfanAmraei/CPPAnalyzer.git  
   cd CPPAnalyzer
   python CPPAnalyzer.py

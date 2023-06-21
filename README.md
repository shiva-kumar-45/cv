# JCL Parser

A JCL parser is a python program or tool that analyzes Job Control Language (JCL) statements and extracts relevant information from them and stores the extracted information into corresponding SQLite database tables.
It is developed to extract the parameters from the following JCL statements:

1.JOB

2.EXEC

3.DD
 

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/jcl-analyzer.git

2. Change to the project directory:

   ```bash
     cd jcl-analyzer

3. Ensure Python 3.x is installed.

4. Install the required dependencies:
   ```
    pip3 install sqlalchemy

## Usage

1. Place your JCL files in the JCL input  folder.
2. Update the folder_path:
   
   folder_path = '..\JCL\INPUT'

4. Execute the script:

   ```bash
   python parser.py
5. The script will analyze each JCL file in the JCL input folder and extracts the parameters form it and stores the parameters into the SQLite database tables.

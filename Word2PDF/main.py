import os
import subprocess

# Prompt the user to enter the path to the document file
doc_file = input("Enter the path to the document file: ")

# Get the current directory
current_dir = os.getcwd()

# Construct the output file path
output_file = os.path.join(current_dir, os.path.splitext(os.path.basename(doc_file))[0] + ".pdf")

# Run the LibreOffice conversion command
subprocess.run(args=['libreoffice', 'headless', '--convert-to', 'pdf', doc_file, '--outdir', current_dir], check=True)
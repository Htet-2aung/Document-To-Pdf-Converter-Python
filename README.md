## Document Converter

This Python script allows you to convert document files (e.g., .docx, .odt) to PDF format.

## Prerequisites

- Python 3 installed on your system
- LibreOffice installed (for the document conversion functionality)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/Htet-2aung/Document-To-Pdf-Converter-Python.git
   ```

2. Change to the project directory:

   ```
   cd document-converter
   ```

3. (Optional) Create a virtual environment:

   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:

   ```
   python convert_document.py
   ```

2. When prompted, enter the full path to the document file you want to convert, e.g., `/path/to/document.docx`.

3. The script will convert the document to PDF format and save the output file in the same directory as the script.

## Examples

To convert a document named `example.docx` located in the `/path/to/documents` directory:

```
python convert_document.py
Enter the path to the document file: /path/to/documents/example.docx
```

The converted PDF file, `example.pdf`, will be saved in the same directory as the `convert_document.py` script.

## Troubleshooting

If you encounter any issues, please make sure that you have LibreOffice installed and that the `libreoffice` command is accessible from the command line.

## Contributing

If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

This README.md file provides a basic structure for your document conversion program, including instructions for installation, usage, and troubleshooting. You can customize the content and formatting as needed to suit your specific requirements.

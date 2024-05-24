
# Excel to PDF Invoice Generator

This repository contains a Python script for converting Excel files into PDF invoices. The script provides a seamless solution for generating professional-looking invoices from Excel data without the need for a graphical user interface (UI).

## Features:

- **Excel to PDF Conversion**: Converts Excel files containing invoice data into PDF format.
- **Customizable Templates**: Easily customize the script to fit specific invoice formatting requirements.
- **Automated Process**: Streamlines the invoicing process by automating the generation of PDF invoices.
- **Simple Usage**: Straightforward command-line interface for effortless execution of the script.

## Usage:

1. **Prepare Excel Data**: Ensure your invoice data is formatted correctly in an Excel spreadsheet.
2. **Run the Script**: Execute the Python script using the command line, providing the necessary input parameters.
   ```
   python invoice_generator.py input_file.xlsx output_file.pdf
   ```
   Replace `input_file.xlsx` with the path to your input Excel file and `output_file.pdf` with the desired output PDF file name.
3. **Generated PDF**: The script will process the Excel data and generate a PDF invoice based on the provided template.

## Dependencies:

This script relies on the following Python libraries:

- `openpyxl`: For reading Excel files.
- `fpdf`: For creating PDF documents.

Ensure these dependencies are installed before running the script.

## Contribution:

Contributions are welcome! If you have any ideas for improvement or would like to contribute to the project, feel free to submit a pull request or open an issue on GitHub.

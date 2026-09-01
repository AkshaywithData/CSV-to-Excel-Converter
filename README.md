# CSV to Excel Converter

## Project Overview

Its a simple Python desktop application that converts CSV files into Excel(.xlsx) format using graphical user interface(GUI).

## Features

- Convert CSV files to Excel (.xlsx)
- User-friendly Tkinter GUI
- Browse and select CSV files
- Automatic Excel file creation
- Success and error message popups
- Select an output folder

## Technologies Used

- Python
- Tkinter
- Pandas
- OpenPyXL
- OS Module

## Project Structure
```
CSV_to_Excel_Converter/
│
│── Screenshots/
│         │── Conversion to excel.png
│         └── selection window.png
│
├── csv_to_excel.py
├── requirements.txt
├── README.md
├── LICENSE
├── sample_data/
│   └── Sample.csv
└── output/
```

## Installation 

Go to the project folder

```bash
cd CSV_to_Excel_Converter
```

Install dependencies

```bash
pip install -r requirements.txt
```

## How to Use

1. Run the application

```bash
python csv_to_excel.py
```

2. Click **Browse CSV** and select a CSV file.

3. Click **Browse Folder** and choose the destination folder.

4. Click **Convert**.

5. The converted Excel file will be saved in the selected folder.


## Future Improvements

- Support multiple CSV files
- Drag-and-drop functionality
- Convert Excel to CSV

## License

This project is licensed under the MIT License.

## Author

**Akshay Gawand**

Python Automation | Data Processing | Desktop Applications
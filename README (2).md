# 📊 Automated Student Report Generator

This Python script reads student names and scores from a CSV file and generates a PDF report with summarized statistics and detailed individual scores.

## 🧰 Features

- Reads data from a CSV file (`data.csv`)
- Calculates:
  - Total number of students
  - Average score
  - Highest and lowest score
- Generates a well-formatted PDF report using ReportLab
- Automatically paginates if the content exceeds one page

## 📁 Project Structure

```
├── 0dfa57c7-42b2-4bf1-8690-95eeb8cdef67.py  # Main Python script
├── data.csv                                # Input CSV file with student data
└── report.pdf                              # Output report (generated)
```

## 📄 CSV File Format (`data.csv`)

The CSV file must have the following columns:

```
Name,Score
Alice,85
Bob,92
Charlie,78
```

## ▶️ How to Run

1. Make sure you have Python installed.
2. Install ReportLab:

```bash
pip install reportlab
```

3. Prepare your `data.csv` file in the format above.
4. Run the script:

```bash
python 0dfa57c7-42b2-4bf1-8690-95eeb8cdef67.py
```

5. A `report.pdf` file will be generated in the same directory.

## 📦 Dependencies

- `reportlab`
- `csv` and `statistics` (built-in)

## ✍️ Author

Generated using Python and ReportLab.
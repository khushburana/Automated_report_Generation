import csv
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from statistics import mean

def read_data(file_path):
    names = []
    scores = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            names.append(row['Name'])
            scores.append(int(row['Score']))
    return names, scores

def generate_pdf_report(names, scores, output_file='report.pdf'):
    c = canvas.Canvas(output_file, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Automated Report")

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, f"Total Students: {len(names)}")
    c.drawString(50, height - 120, f"Average Score: {mean(scores):.2f}")
    c.drawString(50, height - 140, f"Highest Score: {max(scores)}")
    c.drawString(50, height - 160, f"Lowest Score: {min(scores)}")

    c.drawString(50, height - 200, "Detailed Scores:")
    y = height - 220
    for name, score in zip(names, scores):
        c.drawString(70, y, f"{name}: {score}")
        y -= 20
        if y < 100:
            c.showPage()
            y = height - 50
            c.setFont("Helvetica", 12)

    c.save()
    print(f"Report saved as {output_file}")

if __name__ == "__main__":
    names, scores = read_data("data.csv")
    generate_pdf_report(names, scores)

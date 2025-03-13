import csv

def generate_gantt_chart_code(csv_file):
    tasks = []

    # Read the CSV file and build the tasks
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Get the headers
        for row in reader:
            tasks.append(row)

    # Generate Mermaid code for Gantt chart
    mermaid_code = "gantt\n    dateFormat  YYYY-MM-DD\n    title A Gantt Diagram\n"
    for row in tasks:
        if len(row) >= 4:
            mermaid_code += f"    {row[0].replace(' ', '_')}: {row[1]}, {row[2]}, {row[3]}\n"

    return mermaid_code

csv_file = 'hierarchy.csv'
mermaid_code = generate_flowchart_code(csv_file)
print(mermaid_code)

# Save the mermaid code to a file
with open('mermaid_diagram.mmd', 'w') as file:
    file.write(mermaid_code)
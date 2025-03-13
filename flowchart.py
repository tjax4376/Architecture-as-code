import csv

def generate_flowchart_code(csv_file):
    hierarchy = []

    # Read the CSV file and build the hierarchy
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Get the headers
        for row in reader:
            hierarchy.append(row)

    # Generate Mermaid code for flowchart
    mermaid_code = "graph TD\n"
    for row in hierarchy:
        for i in range(len(row) - 1):
            if row[i] and row[i+1]:
                mermaid_code += f"    {row[i].replace(' ', '_')} --> {row[i+1].replace(' ', '_')}\n"

    return mermaid_code
  

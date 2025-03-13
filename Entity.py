import csv

def generate_er_diagram_code(csv_file):
    entities = []

    # Read the CSV file and build the entities
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Get the headers
        for row in reader:
            entities.append(row)

    # Generate Mermaid code for ER diagram
    mermaid_code = "erDiagram\n"
    for row in entities:
        if len(row) >= 3:
            mermaid_code += f"    {row[0].replace(' ', '_')} ||--|| {row[1].replace(' ', '_')}: {row[2]}\n"

    return mermaid_code

csv_file = 'hierarchy.csv'
mermaid_code = generate_flowchart_code(csv_file)
print(mermaid_code)

# Save the mermaid code to a file
with open('mermaid_diagram.mmd', 'w') as file:
    file.write(mermaid_code)
import csv

def generate_class_diagram_code(csv_file):
    classes = []

    # Read the CSV file and build the classes
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Get the headers
        for row in reader:
            classes.append(row)

    # Generate Mermaid code for class diagram
    mermaid_code = "classDiagram\n"
    for row in classes:
        if len(row) >= 2:
            mermaid_code += f"    class {row[0].replace(' ', '_')} {{\n"
            for attribute in row[1:]:
                mermaid_code += f"        {attribute}\n"
            mermaid_code += "    }\n"

    return mermaid_code

csv_file = 'hierarchy.csv'
mermaid_code = generate_flowchart_code(csv_file)
print(mermaid_code)

# Save the mermaid code to a file
with open('mermaid_diagram.mmd', 'w') as file:
    file.write(mermaid_code)
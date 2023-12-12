import yaml
from tabulate import tabulate

# Load the YAML file
with open('./chart/values.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Extract the data
table_data = [{'Component': key, 'createNamespace': value.get('createNamespace', 'N/A'), 'enable': value.get('enable', 'N/A')} for key, value in data.items()]

# Generate the markdown table
table = tabulate(table_data, headers='keys', tablefmt='pipe')

# Read the README file
with open('README.md', 'r') as file:
    content = file.read()

# Split the content at the comment
parts = content.split('<!-- AUTOGENERATED CONTENT BELOW -->')

# Replace the second part with the new table
parts[1] = '\n' + table + '\n'

# Write the updated content back to the README file
with open('README.md', 'w') as file:
    file.write('<!-- AUTOGENERATED CONTENT BELOW -->'.join(parts))

import json
import xmltodict
import lxml.etree as ET

# Path to XSLT file
xslt_file = "input.xslt"

# Path to XML input file
xml_file = "input.xml"

# Create an XSLT transform object
transform = ET.XSLT(ET.parse(xslt_file))
print(transform)

# Apply the transform to the XML input and get the result
result = transform(ET.parse(xml_file))

print(result)
# Convert the resulting XML to a dictionary
xml_dict = xmltodict.parse(result)

# Convert dictionary to JSON
json_data = json.dumps(xml_dict, indent=4)

# Write JSON data to file
with open("example.json", "w") as json_file:
    json_file.write(json_data)

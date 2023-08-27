import json
from bs4 import BeautifulSoup

# Read the HTML file
with open('kkkk.html', 'r') as f:
    html_content = f.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Initialize the structure to store the municipalities
municipalities_data = {}

# Extract data from the HTML
rows = soup.find_all('tr')
for row in rows:
    columns = row.find_all('td')
    if len(columns) == 4:
        province = columns[0].text.strip()
        district = columns[1].text.strip()
        municipality = columns[2].text.strip()

        # Convert district name to title case for case-insensitive comparison
        district = district.title()

        if district not in municipalities_data:
            municipalities_data[district] = {
                "name": district,
                "municipalities": []
            }

        municipalities_data[district]["municipalities"].append(municipality)

# Update the districts.json file
with open('districts.json', 'r') as json_file:
    data = json.load(json_file)

    # Find the province entry and update the districtNames
    for province_entry in data["provinces"]:
        for district_entry in province_entry["districtNames"]:
            if district_entry["name"] in municipalities_data:
                district_entry["municipalities"] = municipalities_data[district_entry["name"]]["municipalities"]

# Write the updated data back to the file
with open('districts.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Municipalities added to districts.json")

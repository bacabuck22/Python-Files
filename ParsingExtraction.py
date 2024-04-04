import re

data = """
Center/Daycare
825 23rd Street South
Arlington, VA 22202
703-979-BABY (2229)
22.
Maria Teresa Desaba, Owner/Director; Tony Saba, Org. Director.
Web site: www.mariateresasbabies.com
Serving children 6 wks to 5yrs full-time.

National Science Foundation Child Development Center
23.
4201 Wilson Blvd., Suite 180 22203
703-292-4794
Web site: www.brighthorizons.com 112 children, ages 6 wks–5 yrs.
7:00 a.m. – 6:00 p.m. Summer Camp for children 5–9 years.

Test Daycare Center
24.
123 Test Street
City, ST 12345
555-555-5555
Web site: www.testdaycare.com
Age Range: Not specified
"""

# Split the data into individual daycare centers
centers = re.split(r'\n(?=\d+\.)', data.strip())

# Define a function to extract relevant information from each center's data
def extract_center_info(center_data):
    name, address, phone, website, age_range = "", "", "", "", "Not specified"
    lines = center_data.strip().split('\n')
    
    # Extract name and address
    name = lines[0]
    address = lines[1]
    
    # Extract phone number
    phone_match = re.search(r'\d{3}-\d{3}-\d{4}', center_data)
    if phone_match:
        phone = phone_match.group()
    
    # Extract website
    website_match = re.search(r'Web site: (www\.\S+)', center_data)
    if website_match:
        website = website_match.group(1)
    
    # Extract age range
    age_range_match = re.search(r'(\d+ \w+–\d+ \w+)', center_data)
    if age_range_match:
        age_range = age_range_match.group(1)

    return f"Name: {name}\nAddress: {address}\nPhone: {phone}\nWebsite: {website}\nAge Range: {age_range}\n"

# Create formatted output for each center
formatted_output = [extract_center_info(center) for center in centers]

# Combine the formatted outputs into a single string
formatted_output_text = "\n\n".join(formatted_output)

# Display the formatted output
print(formatted_output_text)

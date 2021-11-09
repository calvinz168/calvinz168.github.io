#mapGenerator3
import csv
import folium
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

nameL,dateL,latL,lonL,weiL=[],[],[],[],[]

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("TU20 SHEET").sheet1

# Extract and print all of the values
data = (sheet.get_all_values())
for i in range(1,len(data)):
	print(data[i])
	title = f"{data[i][1]} - Last Cleaned: {data[i][2]}"
	nameL.append(title)
	dateL.append(data[i][2])
	latL.append(float(data[i][3]))
	lonL.append(float(data[i][4]))
	weiL.append(data[i][5])
print(nameL)
print(dateL)
print(latL)
print(lonL)
print(weiL)

data = pd.DataFrame({
'lat':latL,
'lon':lonL,
'name':nameL
})
 
# Make an empty map
m = folium.Map(location=[43.53314995007733, -79.87448465762664], zoom_start=12)
 
# Add marker one by one on the map
for i in range(0,len(data)):
	folium.CircleMarker([data.iloc[i]['lat'], data.iloc[i]['lon']],
	 popup=data.iloc[i]['name'],fill=True,fill_color='#3186cc').add_to(m)
 
# Save it as html
m.save('mymap.html')
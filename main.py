import csv
import plotly.express as px

# To fetch the data
rows = []
with open ("result.csv", "r") as fetchData :
  data = csv.reader(fetchData)
  for r in data :
    rows.append(r)

# To separate the data
header = rows[0]
systemData = rows[1:]
header[0] = "no"

# To find solar system with the most number of planets
count = {}
for p in systemData :
  if count.get(p[11]) :
    count[p[11]] += 1
  else :
    count[p[11]] = 1
solarsystemMax = max(count, key=count.get)
'''print("Solar system {} has the most planets {}".format(solarsystemMax, count[solarsystemMax]))'''

planetData = []
for p in systemData :
  if solarsystemMax == p[11] :
    planetData.append(p)

'''print(planetData)
print(len(planetData))'''

# Remove "unknown" rows
tempRows = list(systemData)
for temp in tempRows :
  tempPlanetMass = temp[3]
  if tempPlanetMass.lower() == 'unknown' :
    systemData.remove(temp)
    continue
  else :
    tempPlanetMassVal = tempPlanetMass.split(" ")[0]
    tempPlanetMassRef = tempPlanetMass.split(" ")[1]
    if tempPlanetMassRef == 'Jupiters' :
      tempPlanetMassVal = float(tempPlanetMassVal) * 317.8
    temp[3] = tempPlanetMassVal
      # "Jupiter" require to change name to "Earth"
  
  tempPlanetRadius = temp[7]
  if tempPlanetRadius.lower() == 'unknown' :
    systemData.remove(temp)
    continue
  else :
    tempPlanetRadiusVal = tempPlanetRadius.split(" ")[0]
    tempPlanetRadiusRef = tempPlanetRadius.split(" ")[1]
    if tempPlanetRadiusRef == 'Jupiters' :
      tempPlanetRadiusVal = float(tempPlanetRadiusVal) * 11.2
    temp[7] = tempPlanetRadiusVal


systemName = []
systemMass = []
for i in systemData :
  systemMass.append(i[3])
  systemName.append(i[1])
systemMass.append(1)

bar = px.bar(x=systemName, y=systemMass)
bar.show()
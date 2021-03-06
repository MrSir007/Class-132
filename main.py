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

'''bar = px.bar(x=systemName, y=systemMass)
bar.show()'''

# To remove the outliers
systemData = list(systemData)
for t in systemData :
  if t[1].lower() == "HD 100546 b" :
    systemData.remove(t)
# To graph the basic statistics of the data
planetMass = []
planetRadius = []
planetName = []
for i in systemData :
  planetMass.append(i[3])
  planetRadius.append(i[7])
  planetName.append(i[11])
planetGravity = []
for index, name in enumerate(planetName) :
  gravity = (float(planetMass[index])*5.972e+24) / (float(planetRadius[index])*2*6.647e-11)
  planetGravity.append(gravity)

scatter = px.scatter(x=planetRadius, y=planetMass, size=planetGravity, hover_data=[planetName])
scatter.show()

planetLowGravity = []
for index, gravity in enumerate(planetGravity) :
  if gravity < 100 :
    planetLowGravity.append(systemData[index])
print(len(planetLowGravity))
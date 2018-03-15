import pickle

def loadData():

	fin = open('data.pickle','r')

	data = pickle.load(fin)
	fin.close()
	return data
	
def getDataObject():
	keys = ["Report_Number",
"Local_Case_Number",
"Agency_Name",
"ACRS_Report_Type",
"Crash_Date/Time",
"Route_Type",
"Road_Name",
"Cross-Street_Type",
"Cross-Street_Name",
"Off-Road_Description",
"Municipality",
"Related_Non-Motorist",
"Collision_Type",
"Weather",
"Surface_Condition",
"Light",
"Traffic_Control",
"Driver_Substance_Abuse",
"Non-Motorist_Substance_Abuse",
"Person_ID",
"Driver_At_Fault",
"Injury_Severity",
"Circumstance",
"Driver_Distracted_By",
"Drivers_License_State",
"Vehicle_ID",
"Vehicle_Damage_Extent",
"Vehicle_Body_Type",
"Vehicle_Movement",
"Latitude",
"Longitude",
"Location"]



data = loadData()
count = 1
for row in data[1:]:
	elements = row.split(',')
	if(len(elements) < 5):
		print len(elements)
		print elements
		break
	count += 1

print count

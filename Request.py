import requests
import json
import pprint
import os 

# Checking file is present or not 
# If json file is present then open and read the data 
if os.path.isfile('./courses.json'):
	file = open("courses.json")
	temp = file.read()
	data = json.loads(temp)
	file.close()
	# if json file dosn't exists then request data from the url and store the data in json
else:
	request = requests.get("http://saral.navgurukul.org/api/courses")
	data = request.json()
	s = json.dumps(data)
	with open("courses.json", "w") as file:
		file.write(s)
		file.close()

# extracting ids of the courses 
list_of_id = []
for i in range(len(data["availableCourses"])):
	print(i+1, data["availableCourses"][i]["name"])
	list_of_id.append(data["availableCourses"][i]["id"])


choice=int(input("Which course you want to join  "))
for i in range(len(list_of_id)):
	if (choice-1) == i:
		course_name = data['availableCourses'][i]["name"]
		# if individual course file exists then read the data
		if os.path.isfile("./exercises_"+course_name+".json"):
			file = open("exercises_"+course_name+".json")
			temp = file.read()
			subdata=json.loads(temp)
			file.close()
			# if individual course file edoesn't exists then request the url and a
		else:
			request1=requests.get("http://saral.navgurukul.org/api/courses/"+str(list_of_id[i])+"/exercises")
			subdata=request1.json()
			s=json.dumps(subdata)
			with open("exercises_"+course_name+".json", "w") as f:
				f.write(s)
				f.close()


parent = subdata["data"]
slugP = []
for i in range(len(parent)):
	print(str(i+1),parent[i]["name"])
	slugP.append(parent[i]["slug"])
	for j in range(len(parent[i]['childExercises'])):
		print("\t"+str(j+1),parent[i]['childExercises'][j]["name"])
		slugP.append(parent[i]['childExercises'][j]["slug"])


user_input=int(input("Enter which slug you want to see  "))

# print content of the slug
for i in range(len(slugP)):
	if (user_input-1) == i:
		if os.path.exists("./exercise_"+course_name+str(user_input)+".json"):
			file = open("exercise_"+course_name+str(user_input)+".json")
			temp = file.read()
			slug_1 = json.loads(temp)
			file.close()
			print(slug_1["content"])
		else:
			request2 = requests.get("http://saral.navgurukul.org/api/courses/12/exercise/getBySlug?slug="+str(slugP[i]))
			sc = request2.json()
			p = json.dumps(sc)
			with open("exercise_"+course_name+str(user_input)+".json", "w") as f:
				f.write(p)
				f.close()

			f = open("exercise_"+course_name+str(user_input)+".json")
			temp = f.read()
			slug_1 = json.loads(temp)
			f.close()
			print(slug_1["content"])

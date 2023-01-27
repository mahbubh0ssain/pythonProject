# dictionary means object in JS 😊
studentId = {
    "name": "Mahbub",
    "roll": 1029,
    "village": "Randhunibari",
    "district": "Sirajganj"

}
print(studentId["roll"]) #ekhane na paile error dibe.
print(studentId.get("name")) #ekhane na paile (None) dibe.
print(studentId.get("namee", "No name found")) # eta hoilo default parameter er moto, ekhane namee na paile comma er porerta dekhabe


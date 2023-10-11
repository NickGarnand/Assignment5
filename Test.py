import random
import requests

#vaariables I want to keep track of
NAME_API_URL = "https://muna.ironarachne.com/"
DND_API_URL = "https://www.dnd5eapi.co/api/"
name_num = random.randrange(0,9)
# Function to fetch a random name from the name generation API
def get_name(race):
    try:
      url = NAME_API_URL + race
      responce = requests.get(url)
      data = responce.json()
      names = data["names"]
      return names
    except:
      return "error"

#function to fetch features for DND
def get_features():
  feature_list = {}
  try:
      url = DND_API_URL + "features"
      responce = requests.get(url)
      data = responce.json()
      features = data["results"]
      feature_list = [feature["name"] for feature in features]
      return feature_list
  except:
    return "error"
  
# Main function
def main():
  features = []
  features = get_features()
  character_features = []
  
  check = False
  
  print("--------------------------------")
  print("Enter a race for the NPC")
  print("--------------------------------")
  race = input()
  answer = get_name(race)  
  
  if answer == "error":
   while check == False:
     print("-----------------------------")
     print("Please enter a valid race")
     print("-----------------------------")
     race = input()
     answer = get_name(race) 
     if answer != "error":
       check = True
     else:
       check = False
       
  check1 = False
  while check1 == False:     
    print("-----------------------------")
    print("Does this name sound good: " + answer[name_num] + "\n (Type 1 for yes and 2 for no)")
    print("-----------------------------")
    user_inp = input()
    match user_inp:
      case "1":
        check1 = True
      case "2":
        answer = get_name(race)
        check1 = False
  
    check3 = False
  while check3 == False:     
    print("-----------------------------")
    print("Does you want a special ability for this character: " + answer[name_num] + "\n (Type 1 for yes and 2 for no)")
    print("-----------------------------")
    user_inp = input()
    match user_inp:
      case "1":
        check2 = False
        while check2 == False:     
          feature_num = random.randrange(0,370)
          print("-----------------------------")
          print("Does this feature work: " + features[feature_num] + "\n (Type 1 for yes, 2 for no, and 3 to exit)")
          print("-----------------------------")
          user_inp = input()
          match user_inp:
            case "1":
              character_features.append(features[feature_num])
            case "2":
              check2 = False
            case "3":
              check3 = True
              check2 = True
      case "2":
        check3 = True
  print("-----------------------------------------")  
  print(f"Name: {answer[name_num]}")    
  print(f"Race: {race}")
  print("Abilities: ")
  for feats in character_features:
    print (f"-{feats}")     
    
main()
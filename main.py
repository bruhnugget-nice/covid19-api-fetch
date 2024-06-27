#Importing the requests lib
import requests


#define how to get the API method
def getCovidCases():
  #Docstring time~
  """
  :param - None
  :rtype: None

  Function uses the disease.sh library in order to get a number of cases, deaths, or 
  recoveries due to COVID-19 based off of user input.
  """
  
  #Get the specified data
  covidData=requests.get("https://disease.sh/v3/covid-19/historical/all?lastdays=all")

  #Check to see if the request went through
  print("\nThe status code provided from the API fetch is: " + str(covidData.status_code)+"\n")
  print("--------------------------------------------------")
  if covidData.status_code==200:
    print("The request went through successfully.")
  else:
    print("Something unexpeced happened. The status code provided from the API fetch is " + str(covidData.status_code) +".")
    
  #Get the Data  
  covidData=covidData.json()
  covidDate=str(input("Give me a date from 1/22/20 to 3/9/23, and I will give you the amount of cases, deaths, or recoveries(NOTE: For recoveries, anything after 8/4/21 is 0, just a heads up)."))

  #Choice for cases, deaths, and recoveries
  choice=input("What do you want, cases, deaths, or recoveries?(c, d, or r)")

  if choice.lower()=='c':  
    #Cases
    if covidDate in covidData["cases"].keys():
      print("The number of cases during " + str(covidDate) + " was " + str(covidData["cases"][covidDate]) +".")
    else:
      print("Invalid Input.")
  elif choice.lower()=='d':
    #Deaths
    if covidDate in covidData["deaths"].keys():
      print("The number of deaths during " + str(covidDate) + " was " + str(covidData["deaths"][covidDate]) +".")
    else:
      print("Invalid Input.")
  elif choice.lower()=='r':
    #Recoveries
    if covidDate in covidData["recovered"].keys():
      print("The number of recoveries during " + str(covidDate) + " was " + str(covidData["recovered"][covidDate]) +".")
    else:
      print("Invalid Input.")
  else:
    print("Invalid Input, sorry, try again!")

getCovidCases()

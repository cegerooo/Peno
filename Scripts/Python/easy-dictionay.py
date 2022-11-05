#!/usr/bin/python

theOne = { 
    "firstName":"Thomas", 
    "lastName":"Anderson", 
    "occupation":"Programmer"
    }
    
theOne["company"] = "MetaCortex"

print(theOne)
print(theOne["firstName"])
theOne["occupation"] = "Superhero"
print(theOne)


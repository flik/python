# A function that returns the 'year' value:
def myFunc(e):
  return e['year']

# Used lambda as function for sort year wise
myF = lambda e : e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myF) 
print(cars)
# -*- coding: utf-8
# create a maping of state to abbreviation 
states = {
'oregon':'OR',
'florida':'FL',
'california':'CA',
'new york':'NY',
'michigan':'MI'
}

# create a basic set of states and some cities in them
cities = {
'CA':'san francisco',
'MI':'detroit',
'FL':'jacksonville'
}

# add some more cities
cities['NY'] = 'new york'
cities['OR'] = 'portland'

# print out some cities
print "_" * 10
print 'NY state has: ',cities['NY']
print 'OR state has: ',cities['OR']

# print some cities
print "_" * 10
print 'michigan\'s abbreviation is: ',states['michigan']
print 'florida\'s abbreviation is: ',states['florida']

# do it by using the state then cities dict
print "_" * 10
print 'michigan has: ',cities[states['michigan']]
print 'florida has: ',cities[states['florida']]

# print every state abbreviation
print '_' * 10
for state,abbrev in states.items():
	print '%s is abbreviated %s' % (state,abbrev)
	
# print every city in state
for abbrev,city in cities.items():
	print "%s has the city %s" % (abbrev,city)
	 
# now do both at same time
print "_" * 10
for state,abbrev in states.items():
	print '%s state is abbreviated %s and has city %s' % (state,abbrev,cities[abbrev])
	
print '_' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas',None)

if not state:
	print 'sorry,no Texas.'
	
# get a city with a default value
city = cities.get('TX','does not exist')
print "the city for the state 'TX' is: %s" % city 



















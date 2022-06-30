# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
def new_damages():
  result = []
  for ndex in damages:
    if ndex == 'Damages not recorded':
      result.append(ndex)
    if ndex.endswith('M'):
      m = ndex.replace('M','')
      num_1 = float(m) * conversion['M']
      result.append(num_1)
    if ndex.endswith('B'):
      b = ndex.replace('B', '')
      num_2 = float(b) * conversion['B']
      result.append(num_2)
  return result
updated_damage = new_damages()

# 2 
# Create a Table

# Create and view the hurricanes dictionary
def hurricanes():
  ndx = 0
  hurrican_dict = {}
  for name in names:
    hurrican_dict[names[ndx]] = {"Name": names[ndx], "Month": months[ndx], "Year": years[ndx], "Max Sustained Wind": max_sustained_winds[ndx], "Areas Affected": areas_affected[ndx], "Damage": updated_damage[ndx], "Deaths": deaths[ndx]}
    ndx += 1
  return hurrican_dict
  

hurricane = hurricanes()

# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key
def hurricane_by_date():
  i = 0
  result = {}
  list_val = []
  for val in hurricane.values():
    if val['Year'] == years[i] and val['Year'] not in list_val:
      list_val.append(val)
      result[years[i]] = list_val[i]
      i += 1
      # result[years[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": updated_damage[i], "Deaths": deaths[i]}
  return result

# print(hurricane_by_date())

# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in
def count_areas():
  result = {}
  for area in areas_affected:
    for x in range(len(area)):
      if area[x] not in result:
        terr = area[x]
        result[str(terr)] = 0
      result[str(terr)] += 1
  
  return result

affected_areas = count_areas()
# print(affected_areas)

# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
sorted_result = sorted(affected_areas.items(), key=lambda n: n[1], reverse=True)
# print(sorted_result)

# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths
def deadliest_hurricane():
  results = []
  d_cane = {}
  for val in hurricane.values():
    d = val['Deaths']
    results.append(d)
  s_result = sorted(results, reverse=True)
  for k, v in hurricane.items():
    if v['Deaths'] == s_result[0]:
      d_cane[k] = v
  
  return d_cane

hurricane_info = deadliest_hurricane()
# print(hurricane_info)

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
# categorize hurricanes in new dictionary with mortality severity as key
def mortality_scale_func():
  m_scale = {}
  
  for key, val in hurricane.items():
      m = val['Deaths']
      for rating in mortality_scale:
        if m >= mortality_scale[rating]:
          m_scale[rating] = key
      
  return m_scale

# print(mortality_scale_func())

# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
# Used a nested function to clear a dictionary with values organized from top to bottom returning tuple with first value
def max_damage():
  costly = {}
  for key in hurricane:
    cost = hurricane[key]['Damage']
    if cost not in costly:
      costly[key] = [cost]

  ordered_costly = dict(sorted(costly.items(), key=lambda n: str(n[1]), reverse=True))
  # Nested function to select top value from sorted dictionary with values
  def most_costly_cane(dictionary):
    top_value = []
    for cane in dictionary.items():
      top_value.append(cane)

    return top_value[0]

  costly_canes = most_costly_cane(ordered_costly)
  return costly_canes

# print(max_damage())

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
# categorize hurricanes in new dictionary with damage severity as key
# Decided not to include the damage as not recorded to list only the list of values in the rate
def damage_rate():
  scale_dict = {0:[], 1:[], 2:[], 3:[], 4:[]}
  for cost in hurricane:
    area = hurricane[cost]['Damage']
    for key, rate in damage_scale.items():
      if area == 'Damages not recorded':
        continue
      if area >= damage_scale[4] and area not in scale_dict[4]:
        scale_dict[4].append(area)
      if area >= damage_scale[3] and area not in scale_dict[3] and area not in scale_dict[4]:
        scale_dict[3].append(area)
      if area >= damage_scale[2] and area not in scale_dict[2] and area not in scale_dict[3]:
        scale_dict[2].append(area)
      if area >= damage_scale[1] and area not in scale_dict[1] and area not in scale_dict[2]:
        scale_dict[1].append(area)
      if area <= damage_scale[1] and area not in scale_dict[0] and area not in scale_dict[1]:
        scale_dict[0].append(area)
        
  return scale_dict

cost_rate = damage_rate()

# print(cost_rate)

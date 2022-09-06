# Exercise 2
# tuples
# sample tuple


# Group D members
# ====================================================================
# Name                                        Stud/No            Reg/No
# ====================================================================
# Katamba James                      1800723396     18/U/23396/EVE
# ====================================================================
# Kisakye Joel Nkanji          1800723417     18/U/23417/EVE
# ====================================================================
# Mujambere Reagan               1800723421     18/U/23421/EVE
# ====================================================================
# Laker Sharon                        1800723399     18/U/23399/EVE
# ====================================================================


x=("samsung","iphone","tecno","redmi")
# (1) favourite brand
print("My favourite brand is "+x[3]+"\n")

# (2) using negative indexing to output the second last term
# the second last term is tecno
print("The second last term is "+x[-2]+"\n")

# (3) updating itel to iphone is impossible since tuples are immutable
# But to achieve this we have to convert our tuple to a list which is updatable
# The converted list is updated then re-assigned back to the tuple 
temp_list = list(x)
temp_list[1]="itel"
x=tuple(temp_list)
print("After update..")
print(x)

#(4) Adding something to tuple
temp_list = list(x)
temp_list.append("Huawei")
x=tuple(temp_list)
print("After adding..")
print(x)
print("\n")

# (5) Looping through the tuple
print("Looping through...")
for value in x:
	print(value)

# (6) Deleting something from tuple
temp_list = list(x)
# we delete using the remove function
temp_list.remove(temp_list[0])
x=tuple(temp_list)
print("After deletion.....")
print(x)
print("\n")


# (7)cities tuple
cities_tuple = tuple(["Kampala","Mbarara","Gulu","Arua","Entebbe"])
print("Cities-----------")
print(cities_tuple)
print("\n")

# (8)unpacking cities_tuple
city_1,city_2,city_3,city_4,city_5 = cities_tuple

print("cities unpacked......")
print(city_1)
print(city_2)
print(city_3)
print(city_4)
print(city_5)
print("\n")

# (9)getting 2nd 3rd 4th cities using range of indices
print(cities_tuple[1:4])
print("\n")


# (10)tuples of first and last names 
print("names---------")

first_names = ("James","Joel","Reagan","Sharon")
last_names  = ("Katamba","Nkanji","Mujambere","Laker")
print(first_names)
print(last_names)

# Joining the two tuples
first_and_last = first_names+last_names
print("After joining the two tuples")
print(first_and_last)
print("\n")


# (11) Colors tuple
print("Colors---------")
colors_tuple=("Red","Green","Blue")
print(colors_tuple)

# multipliying the tuple by 3
tuple_by_3 = colors_tuple*3
print("After multipliying....")
print(tuple_by_3)
print("\n")


#(12) this tuple
thistuple=(1,3,7,8,7,5,4,6,8,5)
print(thistuple)

#times of  8
times_of_8 = thistuple.count(8)
print("8 appears "+str(times_of_8)+" times")


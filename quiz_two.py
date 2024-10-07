#perform and print the following math option for all the age and allowances:


#declare the names of the members of the group
member1 = "Cristine Jhed Infante"
member2 = "Esther Rin P. Sapguian"
member3 = "Danny O. Castro"

#declare the age using string
age1 = "20"
age2 = "20"
age3 = "20"

#convert the age that declared in string to integer
ageMem1 = int(age1)
ageMem2 = int(age2)
ageMem3 = int(age3)

#declare the allowance of the members of the group
money1 = 500
money2 = 500
money3 = 500

print(member1, "Her age is", age1, "allowance per week is", money1 )
print(member2, "Her age is", age2, "allowance per week is", money2 )
print(member3, "His age is", age3, "allowance per week is", money3 )

#Get the length of members of the team
nameLen1 = len(member1)
nameLen2 = len(member2)
nameLen3 = len(member3)

print(nameLen1)
print(nameLen2)
print(nameLen3)

#perform and print (compare)

#"+" - age mem1-mem4
#"-" - age mem1-mem4
age_sum = (ageMem1 + ageMem2 + ageMem3)
age_sub = (ageMem1 - ageMem2 - ageMem3)
print(age_sum)
print(age_sub)

#multiply all the age of members to their allowances
multiAge1 = ageMem1 * money1
multiAge2 = ageMem2 * money2
multiAge3 = ageMem3 * money3
print(multiAge1)
print(multiAge2)
print(multiAge3)

#compare the age of members to thier groupmates
compare1 = (ageMem1 - ageMem2)
compare2 = (ageMem2 - ageMem3)
print(compare1)
print(compare2)

#compare the name length of members to the groupmates
compareL1 = (nameLen1 - nameLen2)
comparel2 = (nameLen2 - nameLen3)
print(compare1)
print(compare1)

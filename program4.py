# Dictionaries
main={
    "Name":"Atharva",
    "Surname":"Dalvi",
    "Marks":"95",
    "Division":"Sam Altman"
    }
print(main)
print(main["Name"])
print(main["Surname"])
print(main["Marks"])
print(main.keys())
arc=list(main.keys())
print(arc)

# Sets
colletion={1,2,3,4}
print(type(colletion))

# for empty set
collection=set()
print=(type(collection))

# Practice question 1
dictionary={
    "table":["A peice of furniture","list of facts and figures"],
    "cat":"A small animal"
    }
print(type(dictionary))
print(dictionary)


# practice question 2
sot={"java",'python',"java","C++","JvaScript","python"}
print(len(sot))

# practice question 3
d2={}
phy=int(input("Enter the marks of physics: "))
d2.update({"Physics":phy})

chem=int(input("Enter the marks of chemistry: "))
d2.update({"Chemistry":chem})

bio=int(input("Enter the marks of biology: "))
d2.update({"Biology":bio})

print(d2)

# practice question 4
se={9,"9.0"}
print(se)
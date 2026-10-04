#Sm, Lists Tuples and sets

# Lists
siblings = ["Alex", "Katie", "Andrew", "Tia", "Treyson", "Xavier", "Jake"]
length = len(siblings)
print(f"My older sister is {siblings[1]}")
print(*siblings)
print(f"The youngest is {siblings[-1]}")
siblings.append("Jayshree")
siblings.insert(3, "Vienna")
siblings.extend(["Joe", "Israel", "Zee"])
siblings.remove("Vienna")
siblings.pop(0) 
print(*siblings)
# Tuples
subjects = ("CP1", "CP2", "Advanced CP", "CSP", "Utah Studies", "US 1", "US 2", "World Civ", "World Geography", "CCA Business")
print(subjects[0])
print(*subjects)

#Sets 
visited = {"Texas", "Ohio", "Minnesoda", "Virginia", "D.C.", "Utah", "California", "Nevada"}

print(*visited)
print(len(visited))
visited.add("Idaho")
print(*visited)
visited.update({"Montana", "Arizona", "Oklahoma", "New Mexico"})
visited.remove("Arizona")
print(*visited)
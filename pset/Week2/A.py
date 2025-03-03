'''
'''

'''
precondition:
    -The location may be none
    -Not an empty string
constraints:
    -count > 0
analysis:
    -time: O(n)
    -space: O(1)

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}
print(total_treasures(treasure_map1)) 
print(total_treasures(treasure_map2)) 
15
50
'''
def total_treasure(treasure_map: dict[str,int]) -> int:
    #Init the count variable
    c= 0
    #Iterate through the numbers

    for k in treasure_map:
        if not k:
            continue
        if k:
            c+= treasure_map[k]
    #Return it
    return c
print(total_treasure( {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}))
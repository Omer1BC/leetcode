'''

-housing cars trucks motor cycles
-do not consider the size of the vehicle
-fixed capacity
-return false

-compact large small
    -in terms of class

-price transaction 
    -if no funds, don't park

-lot of transactions
    -optimzie time complexity
    -space complexity

 {small:[],medium:[],large:[]}

class Transaction:
    -class:int
        -0 small 1 medium 2 large
    -name:str
    -driver:str
    -price: int
class ParkingLot:
    slots_per_class: int
    slots: dict[int,List[int]]
    prices : dict[int,int]  --check this before any insertion
    add_vehicle (transaction) : bool --may not have enough space, or funds
    remove_vehilce (transaction): bool --vehicle may not exist 
'''

class Transaction:
    #type = 0 for small, 1 for medium, and 2 for large 
        #Represents the type of parking we are looking for 
    def __init__(self,type:int,vehicle_name:str,driver_name:str,price:int):
        self.type = type
        self.vehicle_name = vehicle_name
        self.driver_name = driver_name
        self.price = price
        self.parking_number = -1
    #Mutators
    def update_information(self,type:int,vehicle_name:str,price:int):
        self.type = type
        self.vehicle_name = vehicle_name
        self.price = price 

class ParkingLot:

    def __init__(self,slots_per_class):
        self.classes = [0,1,2]
        self.prices = [100,200,300]

        self.slots = {k:range(slots_per_class) for k in self.classes}
        self.prices_per_class = {key:value for key,value in zip(self.classes,self.prices)}

    def add_vehicle(self, transaction: Optional[Transaction]) -> bool:
        #check the price
        if (self.prices_per_slot[transaction.type] <= transaction.price):
            #Available space
            if (self.slots[transaction.type]):
                space = self.slots[transaction.type].pop()
                transaction.parking_slot = space
                transaction.price -= self.prices_per_class[transaction.type]
            else:
                return False 
        else:
            return False
    def remove_vehicle(self,transaction: Optional[Transaction]) -> bool:
        #If we don't find the vehicle
        if not transaction or transaction.parking_number == -1:
            return False
        else:
            self.slots[transaction.type].append(transaction.parking_number)
            transaction.parking_number = -1
            return True
            









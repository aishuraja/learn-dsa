# class :
  # constructor 
   # fucntions/methods:
      # instrance of the class - object 


# define class
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity

    
    # define hash function to map keys to indexes
    def hash_function(self, key):
        return hash(key)% self.capacity  # hash(key) gives the hash value 
    
    # define function to insert the key/ value pair to the hash table 
    def insert(self,key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
            
        else:
            self.table[index].append((key, value))

    # define function to get/retrive a value by its key 
    def get(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for k , v in self.table[index]:
                if k == key:
                    return v
            return None
    
    # define fucntion to access the value by its index in the table 
    def get_by_index(self, key):
        index = self.hash_function(key)
        if index< self.capacity:
            return index
        return None # index out of bounds 
    
    # object - create a hashtable with capacity 10/11/....so on 
hash_table = HashTable(10)

    # assing values 

    # insert key-value pair 
    # object.operations()
hash_table.insert("Name", "Aishu")
hash_table.insert("Age", 25)
hash_table.insert("profession", "Software Engineer")
hash_table.insert("Location", "California")

print("Name:", hash_table.get("Name"))
print("Profession of", hash_table.get("Name"), ":",hash_table.get("profession"))


    # 



        
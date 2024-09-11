class HashTable:
    def __init__(self, size):
        """Initialize the hash table with a specified size."""
        self.size = size
        self.table = [[] for _ in range(size)]  # Create a list of empty lists (for chaining)

    def hash_function(self, key):
        """A simple hash function using the modulus operator."""
        return key % self.size  # Hash function: key mod table size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        hash_key = self.hash_function(key)
        # Check if the key already exists and update it if necessary
        for idx, element in enumerate(self.table[hash_key]):
            if element[0] == key:
                self.table[hash_key][idx] = (key, value)
                return
        # If key doesn't exist, add a new entry to the chain
        self.table[hash_key].append((key, value))

    def search(self, key):
        """Retrieve the value associated with the given key."""
        hash_key = self.hash_function(key)
        # Look for the key in the chain
        for element in self.table[hash_key]:
            if element[0] == key:
                return element[1]  # Return the associated value
        return None  # Key not found

    def delete(self, key):
        """Remove a key-value pair from the hash table."""
        hash_key = self.hash_function(key)
        # Iterate through the chain and remove the matching key
        for idx, element in enumerate(self.table[hash_key]):
            if element[0] == key:
                del self.table[hash_key][idx]
                return True
        return False  # Key not found

    def display(self):
        """Display the contents of the hash table."""
        for i, chain in enumerate(self.table):
            print(f"Bucket {i}: {chain}")

# Example Run
if __name__ == "__main__":
    # Create a hash table of size 12
    hash_table = HashTable(12)

    # Insert some key-value pairs
    hash_table.insert(10, "Value for key 10")
    hash_table.insert(5, "Value for key 5")
    hash_table.insert(20, "Value for key 20")
    hash_table.insert(25, "Value for key 25")
    hash_table.insert(15, "Value for key 15")

    # Display the hash table
    print("Hash Table after insertions:")
    hash_table.display()

    # # Search for a key
    print("\nSearch results:")
    print(f"Search key 10: {hash_table.search(10)}")
    print(f"Search key 25: {hash_table.search(25)}")
    print(f"Search key 30 (not present): {hash_table.search(30)}")

    # Delete a key-value pair
    print("\nDeleting key 20...")
    hash_table.delete(20)

    # Display the hash table after deletion
    print("\nHash Table after deletion:")
    hash_table.display()
    
    # Add key 20 again 
    print("/n Adding Key 20 after removing")
    hash_table.insert(20,"The new value for key 20")

    hash_table.display()
import timeit
import random
from HashChaining import HashTable  

# Test case generation
def generate_keys(n):
    """Generate n random keys."""
    return [random.randint(1, 10000) for _ in range(n)]

# Function to test insert performance
def test_insert(hash_table, keys):
    for key in keys:
        hash_table.insert(key, f"Value for {key}")

# Function to test search performance
def test_search(hash_table, keys):
    for key in keys:
        hash_table.search(key)

# Function to test delete performance
def test_delete(hash_table, keys):
    for key in keys:
        hash_table.delete(key)

# Performance test function
def performance_test():
    table_sizes = [100, 500, 1000]  # Hash table sizes
    element_counts = [100, 500, 1000]  # Number of keys to insert/search/delete

    # Print table header
    print(f"\n{'Hash Table Size':<20}{'Number of Elements':<20}{'Insert Time (s)':<20}{'Search Time (s)':<20}{'Delete Time (s)':<20}")
    print("-" * 100)

    for table_size in table_sizes:
        for element_count in element_counts:
            # Create a hash table
            hash_table = HashTable(table_size)

            # Generate random keys
            keys = generate_keys(element_count)

            # Test insert
            insert_time = timeit.timeit(lambda: test_insert(hash_table, keys), number=1)

            # Test search
            search_time = timeit.timeit(lambda: test_search(hash_table, keys), number=1)

            # Test delete
            delete_time = timeit.timeit(lambda: test_delete(hash_table, keys), number=1)

            # Print results in tabular format
            print(f"{table_size:<20}{element_count:<20}{insert_time:<20.6f}{search_time:<20.6f}{delete_time:<20.6f}")


# Run the performance test. 
if __name__ == "__main__":
    performance_test()

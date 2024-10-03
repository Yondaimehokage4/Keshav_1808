from gcms import GCMS
from object import Color
from exceptions import NoBinFoundException
import random

if __name__ == "_main_":

    # Set the seed for random number generation to ensure identical results on different machines
    random.seed(42)

    # Initialize GCMS instance
    gcms = GCMS()

    # Function to generate random color
    def get_random_color():
        return random.choice([Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW])

    # Add 200 bins with unique IDs and random sizes
    for i in range(1, 201):
        bin_id = 4000 + i  # Unique bin IDs starting from 4001 to 4200
        bin_size = random.randint(40, 100)  # Random bin size between 40 and 100
        gcms.add_bin(bin_id, bin_size)

    # Add 400 objects with unique IDs, random colors, and sizes
    for i in range(1, 401):
        object_id = 7000 + i  # Unique object IDs starting from 7001 to 7400
        object_size = random.randint(5, 50)  # Random object size between 5 and 50
        object_color = get_random_color()

        try:
            gcms.add_object(object_id, object_size, object_color)
            # Print object info
            print(f"Added Object: {gcms.object_info(object_id)}")
        except Exception as e:
            print(f"Error adding object {object_id}: {e}")

    # Set to keep track of deleted objects
    deleted_objects = set()

    # Delete 100 objects randomly
    for _ in range(100):
        while True:
            object_id = 7000 + random.randint(1, 400)  # Randomly choose an object to delete
            if object_id not in deleted_objects:
                try:
                    gcms.delete_object(object_id)
                    deleted_objects.add(object_id)  # Mark object as deleted
                    print(f"Deleted Object: {object_id}")
                    break  # Exit the while loop if object deleted successfully
                except Exception as e:
                    print(f"Error deleting object {object_id}: {e}")
                    break  # Break if error occurs (such as the object not being found)

    # Print bin info for all 200 bins at the end
    for i in range(1, 201):
        bin_id = 4000 + i
        try:
            print(f"Bin Info: {gcms.bin_info(bin_id)}")
        except NoBinFoundException as e:
            print(f"Error fetching info for bin {bin_id}: {e}")

 

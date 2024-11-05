class Array(object):
    def __init__(self, initialSize):  # Constructor
        self.__a = [None] * initialSize  # The array stored as a list
        self.__a = 0  # No items in array initially
        self.__nItems = 0
    def __len__(self):  # Special def for len() function
        return self.__a  # Return number of items

    def get(self, n):  # Return the value at index n
        if 0 <= n < self.__a:  # Check if n is in bounds
            return self.__a[n]  # Only return item if in bounds
        return None  # If index is out of bounds

    def set(self, n, value):  # Set the value at index n
        if 0 <= n < self.__a:  # Check if n is in bounds
            self.__a[n] = value  # Only set item if in bounds

    def insert(self, item):  # Insert item at end
        if self.__nItems < len(self.__a):  # Check if there's room (corregido)
            self.__a[self.__a] = item  # Item goes at current end
            self.__a += 1  # Increment number of items
        else:
            print("Array is full")

    def find(self, item):  # Find index for item
        for j in range(self.__a):  # Among current items
            if self.__a[j] == item:  # If found,
                return j  # Return index to item
        return -1  # Not found -> return -1

    def search(self, item):  # Search for item
        index = self.find(item)  # Find index of the item
        if index != -1:
            return self.get(index)  # Return item if found
        return None  # If not found, return None

    def delete(self, item):  # Delete first occurrence
        for j in range(self.__a):  # of an item
            if self.__a[j] == item:  # Found item
                self.__a -= 1  # One fewer at end
                for k in range(j, self.__a):  # Move items from
                    self.__a[k] = self.__a[k + 1]  # right over 1
                self.__a[self.__a] = None  # Clear last item
                return True  # Return success flag
        return False  # Made it here, so couldn't find the item

    def traverse(self, function=print):  # Traverse all items
        for j in range(self.__a):  # and apply a function
            function(self.__a[j])

    def getMaxNum(self):  # Get the maximum number in the array
        max_num = None  # Initialize max_num as None
        for i in range(self.__a):
            if isinstance(self.__a[i], (int, float)):  # Check if item is a number
                if max_num is None or self.__a[i] > max_num:  # Compare with max_num
                    max_num = self.__a[i]  # Update max_num if condition met
        return max_num  # Return max_num, or None if no numbers were found
    
    def deleteMaxNum(self):  # Delete the maximum number from the array
        max_num = self.getMaxNum()  # Get the maximum number
        if max_num is not None:
            self.delete(max_num)  # Delete the max number if it exists
            print(f"Deleted the maximum number: {max_num}")
        else:
            print("No numbers found in the array.")


    def removeDupes(self):  # Method to remove duplicates
        seen = set()  # Set to track seen elements
        no_dup_items = 0  # Track number of unique items

        # Loop through the array to find unique items
        for i in range(self.__a):
           if self.__a[i] not in seen:  # If the item is not a duplicate
            seen.add(self.__a[i])  # Add it to the set
            self.__a[no_dup_items] = self.__a[i]  # Move to the unique position
            no_dup_items += 1  # Increment unique item count

          # Clear remaining positions in the array
        for i in range(no_dup_items, self.__a):
         self.__a[i] = None

        self.__a = no_dup_items  # Update number of items to reflect unique itemss

   
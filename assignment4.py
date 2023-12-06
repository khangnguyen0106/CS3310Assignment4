import time

class Games:
    def __init__(self, game_id, name, avg_user_rating, rating_count, developer, size):
        self.id = game_id
        self.name = name
        self.average_user_rating = avg_user_rating
        self.user_rating_count = rating_count
        self.developer = developer
        self.size = size

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Avg Rating: {self.average_user_rating}, Rating Count: {self.user_rating_count}, Developer: {self.developer}, Size: {self.size}"

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        

class GamesLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            current_node = self.head
            while current_node:
                if current_node.data.name == data.name:
                    if current_node.data.user_rating_count < data.user_rating_count:
                        current_node.data = data
                    return  # Stop if duplicate is found
                current_node = current_node.next

            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def gamesCount(self):
        count = 0
        current_node = self.head

        while current_node:
            count += 1
            current_node = current_node.next

        return count
    
    def printFirstFive(self):
        current_node = self.head
        count = 0

        while current_node and count < 5:
            game_data = current_node.data
            print(game_data.__str__())
            current_node = current_node.next
            count += 1

    def insertion_sort(self):
        start_time = time.time_ns()

        if not self.head:
            return

        sorted_head = None
        current = self.head

        while current:
            next_node = current.next
            sorted_head = self.insert_into_sorted(sorted_head, current)
            current = next_node

        self.head = sorted_head

        end_time = time.time_ns()
        time_spent = end_time - start_time
        print(f"Time for insertion sort: {time_spent:.6f} nanoseconds")

    def insert_into_sorted(self, sorted_head, new_node):
        if not sorted_head or sorted_head.data.name >= new_node.data.name:
            new_node.next = sorted_head
            return new_node

        current = sorted_head

        while current.next and current.next.data.name < new_node.data.name:
            current = current.next

        new_node.next = current.next
        current.next = new_node

        return sorted_head

    def quick_sort(self):
        start_time = time.time_ns()

        self.head = self._quick_sort(self.head)

        end_time = time.time_ns()
        time_spent = end_time - start_time
        print(f"QTime for insertion sort: {time_spent:.6f} nanoseconds")

    def _quick_sort(self, node):
        if not node or not node.next:
            return node

        pivot = node
        less_head = None
        equal_head = pivot
        greater_head = None

        current = node.next

        while current:
            next_node = current.next
            if current.data.name < pivot.data.name:
                current.next = less_head
                less_head = current
            elif current.data.name == pivot.data.name:
                current.next = equal_head
                equal_head = current
            else:
                current.next = greater_head
                greater_head = current

            current = next_node

        sorted_less = self._quick_sort(less_head)
        sorted_greater = self._quick_sort(greater_head)

        return self.concatenate(sorted_less, equal_head, sorted_greater)

    def concatenate(self, less, equal, greater):
        result = less or equal

        if result:
            last_node = result
            while last_node.next:
                last_node = last_node.next

            last_node.next = greater

        return result

    def linearSearch(self, name):
        start_time = time.time_ns()

        current_node = self.head
        while current_node:
            if current_node.data.name == name:
                end_time = time.time_ns()
                time_spent = end_time - start_time
                return current_node.data, time_spent
            current_node = current_node.next

        # If the loop completes without finding the game
        end_time = time.time_ns()
        time_spent = end_time - start_time
        return None, time_spent   
    
    def binarySearch(self, name):
        start_time = time.time()

        result = self._binarySearch(name, self.head)

        end_time = time.time()
        time_spent = end_time - start_time
        print(f"Binary Search Time: {time_spent:.6f} seconds")

        return result

    def _binarySearch(self, name, current_node):
        if not current_node:
            return None  # Game not found

        mid = self.getMiddle(current_node)
        mid_name = mid.data.name

        if mid_name == name:
            return mid.data  # Found the game
        elif mid_name < name:
            return self._binarySearch(name, mid.next)
        else:
            return self._binarySearch(name, current_node)

    def getMiddle(self, start_node):
        slow = start_node
        fast = start_node

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

def csv_to_GamesLinkedList(file_path):
    games_linked_list = GamesLinkedList()

    with open(file_path, 'r') as file:
        header = file.readline().strip().split(',')
        for line in file:
            row_data = line.strip().split(',')
            game_data = Games(
                game_id=row_data[0],
                name=row_data[1],
                avg_user_rating=row_data[2],
                rating_count=row_data[3],
                developer=row_data[4],
                size=row_data[5]
            )
            games_linked_list.append(game_data)

    return games_linked_list

if __name__ == "__main__":
    file_path = 'C:\Khang\School\CS3310\Assignment 4\games.csv'
    games_linked_list = csv_to_GamesLinkedList(file_path)

    print("Number of elements in LinkedList: " + games_linked_list.gamesCount())

    print("*** Linear Search Test ***")

    print("Before sorting: ")
    print(games_linked_list.printFirstFive())
 
    #print("Search number 1:")
    #name1= input("Searching for: ")
    #print("Single search time: {} nanoseconds.".format())
    #print("Average search time:{} nanoseconds.". format())  
    
    print("After sorting: ")
    print(games_linked_list.printFirstFive())

    print("Time for insertion sort: ")
    print("*** Binary Search Test ***")

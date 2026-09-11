class Student:
    def __init__(self, id, name, course, year):
        self._student_id = id
        self._student_name = name
        self._course = course
        self._year_level = year

    def display_student(self):
        print(f"Student ID: {self._student_id}")
        print(f"Student Name: {self._student_name}")
        print(f"Course: {self._student_id}")
        print(f"Year Level: {self._year_level}")


class DynamicArray:
    def __init__(self):
        self._capacity = 5
        self._size = 0
        self._arr = [] 

    def _new_array(self, n):        #used for 
        return [None] * n
        

    def _resize(self, new_capacity):
        b_arr = self._new_array(new_capacity)   #make new array based on new capacity
        for i in range(self._size):             #copy
            b_arr[i] = self._arr[i]
        self._arr = b_arr                       #use the new resized array and update capacity
        self._capacity = new_capacity

    def add(self, item):
        if self._size == self._capacity:                    #checks if there size is reaching capacity
            self._resize(self._capacity * 2)
        self._arr[self._size] = item                        #add new item to the end of the array
        self._size += 1

class StudentManager:
    def __init__(self):
        self.record = DynamicArray()

    def add(self):
        pass

    def display(self):
        pass

    def search(self):
        pass

    def update(self):
        pass

    def remove(self):
        pass

if __name__ == "__main__":
    dynamic_arr = DynamicArray()
    running = True

    while running:
        print("================================")
        print("STUDENT RECORD MANAGER")
        print("================================")
        print("1. Add Student")
        print("2. Display Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Remove Student")
        print("6. Display Array Information")
        print("7. Exit")

        user = int(input("Enter your choice: "))

        match user:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                running = False
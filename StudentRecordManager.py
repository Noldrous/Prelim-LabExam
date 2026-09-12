class Student:
    def __init__(self, id, name, course, year):
        self._student_id = id
        self._student_name = name
        self._course = course
        self._year_level = year

    def display(self):
        print(f"Student ID: {self._student_id}")
        print(f"Student Name: {self._student_name}")
        print(f"Course: {self._course}")
        print(f"Year Level: {self._year_level}")

    def display_name(self):
        print(f"[{self._student_name}]", end=" ")

    def update_id(self, id):
        self._student_id = id

    def update_name(self, name):
        self._student_name = name

    def update_course(self, course):
        self._course = course

    def update_year(self, year):
        self._year_level = year 

    def get_id(self):
        return self._student_id

class DynamicArray:
    def __init__(self):
        self._capacity = 5
        self._size = 0
        self._arr = [None] * self._capacity

    def _new_array(self, n):        #helper method for _resize
        return [None] * n
        
    def _resize(self, new_capacity):
        b_arr = self._new_array(new_capacity)   #make new array based on new capacity
        for i in range(self._size):             #copy
            b_arr[i] = self._arr[i]
        self._arr = b_arr                       #use the new resized array and update capacity
        self._capacity = new_capacity

    def add(self, item):          #equivalent to .append()
        if self._size == self._capacity:                    #checks if there size is reaching capacity
            self._resize(self._capacity * 2)
        self._arr[self._size] = item                        #add new item to the end of the array
        self._size += 1

    def display_students(self):
        for i in range(self._size):
            print(":" * 36)
            self._arr[i].display()
        print(":" * 36)
        print("")

    def search(self, id):
        for i in range(self._size):
            if self._arr[i].get_id() == id:
                return i
        return -1

    def display_student(self, id):
        index = self.search(id)
        if index != -1:
            self._arr[index].display()

    def update_id(self, id, stud_id):
        index = self.search(id)
        if index != -1:
            self._arr[index].update_id(stud_id)

    def update_name(self, id, name):
        index = self.search(id)
        if index != -1:
            self._arr[index].update_name(name)

    def update_course(self, id, course):
        index = self.search(id)
        if index != -1:
            self._arr[index].update_course(course)

    def update_year(self, id, year):
        index = self.search(id)
        if index != -1:
            self._arr[index].update_year(year)

    def update_all(self, id, stud_id, name, course, year):
        index = self.search(id)
        if index != -1:
            self._arr[index].update_id(stud_id)
            self._arr[index].update_name(name)
            self._arr[index].update_course(course)
            self._arr[index].update_year(year)

    def remove(self, id):
        index = self.search(id)
        if index != -1:
            for i in range(index, self._size - 1):
                self._arr[i] = self._arr[i + 1]
            self._arr[self._size - 1] = None
            self._size -= 1

    def display_array(self):
        print(f"Capacity: {self._capacity}")
        print(f"Size: {self._size}")
        for i in range(self._size):
            self._arr[i].display_name()
        empty = self._capacity - self._size
        print(" [] " * empty)

class StudentManager:
    def __init__(self):
        self.record = DynamicArray()

    def add_student(self):
        print("\n--------- ADDING STUDENT ---------")
        id = input("Enter Student ID: ")

        if self.record.search(id) != -1:
            print("This Student ID already exists.")
            user = int(input("Do you want to enter another ID? \n1. Yes \n2. NO \n- "))
            match user:
                case 1:
                    self.add_student()
                    return
                case 2:
                    return

        name = input("Enter Student Name: ")
        course = input("Enter Course: ")
        year = int(input("Enter Year Level: "))

        new_student = Student(id, name, course, year)

        self.record.add(new_student)
        cont = input("\nPRESS ENTER TO CONTINUE...\n")

    def display_students(self):
        print("\n++++++++++ STUDENT RECORD ++++++++++")
        self.record.display_students()
        cont = input("\nPRESS ENTER TO CONTINUE...\n")
            
    def search_student(self):
        stud_id = input("\n⌕ Enter Student ID to search: ")
        print("\n+++++++++++ STUDENT FOUND +++++++++++")
        self.record.display_student(stud_id)
        cont = input("\nPRESS ENTER TO CONTINUE...\n")

    def update_student(self):
        id = input("\n⌕ Enter Student ID to update its info: ")
        print("\n+++++++++++ STUDENT FOUND +++++++++++")
        print("\n/// What do you want to update? \\\\\\")
        print("1. Student ID")
        print("2. Student Name")
        print("3. Course")
        print("4. Year Level")
        print("5. All")
        user = int(input("\nEnter your choice: "))

        match user:
            case 1:
                stud_id = input("Enter NEW Student ID: ")
                self.record.update_id(id, stud_id)
                print("ID updated.")
                cont = input("\nPRESS ENTER TO CONTINUE...\n")
            case 2:
                name = input("Enter NEW Student Name: ")
                self.record.update_name(id, name)
                print("Student Name Updated.")
                cont = input("\nPRESS ENTER TO CONTINUE...\n")
            case 3:
                course = input("Enter NEW Course: ")
                self.record.update_course(id, course)
                print("Course Updated.")
                cont = input("\nPRESS ENTER TO CONTINUE...\n")
            case 4:
                year = int(input("Enter NEW Year Level: "))
                self.record.update_year(id, year)
                print("Year Level Updated.")
                cont = input("\nPRESS ENTER TO CONTINUE...\n")
            case 5:
                stud_id = input("Enter NEW Student ID: ")
                name = input("Enter NEW Student Name: ")
                course = input("Enter NEW Course: ")
                year = int(input("Enter NEW Year Level: "))
                self.record.update_all(id, stud_id, name, course, year)
                print("Information Updated.")
                cont = input("\nPRESS ENTER TO CONTINUE...\n")

    def remove_student(self):
        id = input("\n⌕ Enter Student ID to remove: ")
        user = int(input("Are you sure? \n1. Yes \n2. No \n- "))
        
        match user:
            case 1:
                self.record.remove(id)
                print("\nStudent Removed.\n")
                cont = input("\nPRESS ENTER TO CONTINUE...\n")
            case 2:
                print("Operation Cancelled.\n")
                cont = input("\nPRESS ENTER TO CONTINUE...\n")
                return

    def display_array(self):
        print("\n----- Array Information -----")
        self.record.display_array()
        print("")

def start_menu():
        print("=" * 36)
        print("STUDENT RECORD MANAGER")
        print("=" * 36)
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Remove Student")
        print("6. Display Array Information")
        print("7. Exit\n")

def main():
    s_manager = StudentManager()
    running = True

    while running:
        start_menu()
        user = int(input("Enter your choice: "))

        match user:
            case 1:
                s_manager.add_student()
            case 2:
                s_manager.display_students()
            case 3:
                s_manager.search_student()
            case 4:
                s_manager.update_student()
            case 5:
                s_manager.remove_student()
            case 6:
                s_manager.display_array()
            case 7:
                print("Closing Manager...")
                running = False

if __name__ == "__main__":
    main()
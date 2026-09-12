class Song:
    def __init__(self, id, title, artist, duration):
        self._song_id = id
        self._song_title = title
        self._artist = artist
        self._duration = duration

    def display(self):
        print(f"Song ID: {self._song_id}")
        print(f"Song Title: {self._song_title}")
        print(f"Artist: {self._artist}")
        print(f"Duration: {self._duration}")

    def display_title(self):
        print(f"[{self._song_title}]", end=" -> ")

    def get_id(self):
        return self._song_id

    def get_title(self):
        return self._song_title
    
    def get_artist(self):
        return self._artist

    def get_duration(self):
        return self._duration

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def display(self):
        self.value.display()

    def display_title(self):
        self.value.display_title()

class SinglyLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def insert_first(self, value):
        new_node = Node(value)
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    def insert_last(self, value):
        node = self._head
        new_node = Node(value)

        if node == None:
            self._head = new_node
        else:
            while node.next is not None:
                node = node.next
            node.next = new_node
        self._size += 1

    def insert_at(self, pos, value):
        if 0 <= pos <= self._size:
            if pos < 0:
                print("Cannot Accept Negative Value.")

            if pos == 1:
                return self.insert_first(value)

            node = self._head
            new_node = Node(value)
            count = 1

            while node is not None and count < pos - 1:
                node = node.next
                count += 1

            new_node.next = node.next
            node.next = new_node
        else:
            print("Position out of bounds.")

    def display_playlist(self):
        node = self._head
        if not node:
            print("No Music Available.")
            return  
        while node is not None:
            print(">" * 36)
            node.display()
            node = node.next
        print(">" * 36)

    def search(self, id):
        node = self._head

        while node is not None:
            if node.value.get_id() == id:
                print(f"Song ID: {node.value.get_id()}")
                print(f"Song Title: {node.value.get_title()}")
                print(f"Artist: {node.value.get_artist()}")
                print(f"Duration: {node.value.get_duration()}")
                return True
            node = node.next
        print("! ! ! !  MUSIC ID NOT FOUND  ! ! ! !")
        return False

    def remove(self, id):
        previous, node = None, self._head

        while node is not None:
            if node.value.get_id() == id:
                if previous is None:
                    self._head = node.next
                else:
                    previous.next = node.next
                self._size -= 1
                return True
            previous, node = node, node.next

        return self.search(id)

    def display_size(self):
        print(f"Total Number of Songs: {self._size}")
        node = self._head
        if not node:
            print("It seems to be pretty empty here...")
            return
        while node is not None:
            node.display_title()
            node = node.next
        print("NULL")
        
class PlaylistManager:
    def __init__(self):
        self.playlist = SinglyLinkedList()

    def add_beginning(self):
        print("\n++++ ADDING MUSIC AT THE BEGINNING ++++")
        id = input("Enter Song ID: ")
        title = input("Enter Song Title: ")
        artist = input("Enter Artist: ")
        duration = input("Enter Duration: ")

        new_song = Song(id, title, artist, duration)

        self.playlist.insert_first(new_song)
        cont = input("\nPRESS ENTER TO CONTINUE...\n")

    def add_end(self):
        print("\n+++++++ ADDING MUSIC AT THE END +++++++")
        id = input("Enter Song ID: ")
        title = input("Enter Song Title: ")
        artist = input("Enter Artist: ")
        duration = input("Enter Duration: ")

        new_song = Song(id, title, artist, duration)

        self.playlist.insert_last(new_song)
        cont = input("\nPRESS ENTER TO CONTINUE...\n")

    def insert_at(self):
        print("\n+++++++ ADDING MUSIC AT POSITION +++++++")
        pos = int(input("Enter Position: "))
        id = input("Enter Song ID: ")
        title = input("Enter Song Title: ")
        artist = input("Enter Artist: ")
        duration = input("Enter Duration: ")

        new_song = Song(id, title, artist, duration)

        self.playlist.insert_at(pos, new_song)
        cont = input("\nPRESS ENTER TO CONTINUE...\n")

    def display_playlist(self):
        print("\n========== MUSIC PLAYLIST ==========")
        self.playlist.display_playlist()
        cont = input("\nPRESS ENTER TO CONTINUE...\n")

    def search_song(self):
        print("\n========== SEARCHING MUSIC ==========")
        user = input("⌕ Enter Song ID to search: ")
        print("=" * 36)
        self.playlist.search(user)
        print("=" * 36)
        cont = input("\nPRESS ENTER TO CONTINUE...\n")

    def remove(self):
        print("\n========== REMOVING MUSIC ==========")
        id = input("⌕ Enter Song ID to remove: ")
        user = int(input("Are you sure? \n1. Yes \n2. No \n- "))
        match user:
            case 1:
                if self.playlist.remove(id):
                    print("\nMusic Removed.\n")
                    cont = input("PRESS ENTER TO CONTINUE...\n")
                else:
                    print("ID not found.\n")
                    cont = input("PRESS ENTER TO CONTINUE...\n")
            case 2:
                print("Operation Cancelled.\n")
                cont = input("PRESS ENTER TO CONTINUE...\n")
                return
        

    def display_size(self):
        print("\n====== TOTAL NUMBER OF MUSIC ======")
        self.playlist.display_size()
        print("")
        cont = input("PRESS ENTER TO CONTINUE...\n")

def start_menu():
        print("=" * 36)
        print("MUSIC PLAYLIST MANAGER")
        print("=" * 36)
        print("1. Add Song at the Beginning")
        print("2. Add Song at the End")
        print("3. Insert Song at Specific Position")
        print("4. Display Playlist")
        print("5. Search Song")
        print("6. Remove Song")
        print("7. Display Playlist Size")
        print("8. Exit\n")

def main():
    p_manager = PlaylistManager()
    running = True

    while running:
        start_menu()
        user = int(input("Enter your choice: "))

        match user:
            case 1:
                p_manager.add_beginning()
            case 2:
                p_manager.add_end()
            case 3:
                p_manager.insert_at()
            case 4:
                p_manager.display_playlist()
            case 5:
                p_manager.search_song()
            case 6:
                p_manager.remove()
            case 7:
                p_manager.display_size()
            case 8:
                print("Closing Manager...")
                running = False

if __name__ == "__main__":
    main()
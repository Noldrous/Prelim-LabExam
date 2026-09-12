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
            node = new_node
        else:
            while node.next is not None:
                node = node.next
            node.next = new_node
        self._size += 1

    def insert_at(self, pos, value):
        node = self._head
        new_node = Node(value)

        if pos == 0:
            new_node.next = node
            node = new_node
            return
        
        while pos - 1 and node.next:
            node = node.next
            position -= 1
        new_node.next = node.next
        node.next = new_node 
        self._size += 1

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
        print("\n---- ADDING MUSIC AT THE BEGINNING ----")
        id = input("Enter Song ID: ")
        title = input("Enter Song Title: ")
        artist = input("Enter Artist: ")
        duration = int(input("Enter Duration: "))

        new_song = Song(id, title, artist, duration)

        self.playlist.insert_first(new_song)
        cont = input("\nPRESS ENTER TO CONTINUE...\n")

    def add_end(self):
        print("\n------- ADDING MUSIC AT THE END -------")
        id = input("Enter Song ID: ")
        title = input("Enter Song Title: ")
        artist = input("Enter Artist: ")
        duration = int(input("Enter Duration: "))

        new_song = Song(id, title, artist, duration)

        self.playlist.insert_last(new_song)
        cont = input("\nPRESS ENTER TO CONTINUE...\n")

    def insert_at(self):
        print("\n------- ADDING MUSIC AT POSITION -------")
        pos = int(input("Enter Position:"))
        id = input("Enter Song ID: ")
        title = input("Enter Song Title: ")
        artist = input("Enter Artist: ")
        duration = int(input("Enter Duration: "))

        new_song = Song(id, title, artist, duration)

        self.playlist.insert_at(pos, new_song)
        cont = input("\nPRESS ENTER TO CONTINUE...\n")

    def display_playlist(self):
        print("\n========== MUSIC PLAYLIST ==========\n")
        self.playlist.display_playlist()
        cont = input("\nPRESS ENTER TO CONTINUE...\n")

    def search_song(self):
        pass

    def remove(self):
        pass

    def display_size(self):
        print("\n====== TOTAL NUMBER OF MUSIC ======")
        self.playlist.display_size()
        print("")

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
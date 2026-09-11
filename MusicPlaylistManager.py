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

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def display(self):
        self.value.display()

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
        print(":" * 36)
        while node.next is not None:
            node = node.next
        node().display()
        print(">" * 36)
            


class PlaylistManager:
    def __init__(self):
        playlist = SinglyLinkedList()

    def add_beginning(self):
        pass


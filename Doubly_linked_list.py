
class List_Node:
    def __init__(self, data, prev = None, link = None):
        self.data = data
        self.prev = prev
        self.link = link
        if prev is not None:
            self.prev.link = self
        if link is not None:
            self.link.prev = self



class Doubly_Linked_List:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0


    def __len__(self):
        return self.length
    

    def addfirst(self, item):
        if len(self) == 0:
            self.head = self.tail =  List_Node(item, None, None)
        else:
            new_node = List_Node(item, None, self.head)
            self.head.prev = new_node
            self.head = new_node
        self.length += 1


    def addlast(self, item):
        if len(self) == 0:
            self.head = self.tail = List_Node(item, None, None)
        else:
            new_node = List_Node(item, self.tail, None)
            self.tail.link = new_node
            self.tail = new_node
        self.length += 1


    def delfirst(self):
        if len(self) == 0:
            print("!!! Список уже пуст !!!")
        else:
            if len(self) == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.link
                self.head.prev = None
            self.length -= 1


    def dellast(self):
        if len(self) == 0:
            print("!!! Список уже пуст !!!")
        else:
            if len(self) == 1:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.link = None
            self.length -= 1



    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.link
        print()




dll = Doubly_Linked_List()

# Добавление элементов в начало списка
dll.addfirst(1)
dll.addfirst(2)
dll.addfirst(3)

# Добавление элементов в конец списка
dll.addlast(4)
dll.addlast(5)
dll.addlast(6)

# Вывод списка
dll.display()  # Ожидаемый результат: 3 2 1 4 5 6

# Удаление первого и последнего элементов
dll.delfirst()
dll.dellast()

# Вывод списка после удаления
dll.display()  # Ожидаемый результат: 2 1 4 5

# Вывод длины списка
print("Длина списка:", len(dll))  # Ожидаемый результат: 4

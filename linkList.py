class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    def __init__(self, node=None):
        self.__head = node

    def isEmpty(self):
        return self.__head is None

    def length(self):
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        linkLists = []
        cur = self.__head
        while cur is not None:
            linkLists.append(cur.elem)
            cur = cur.next
        return linkLists

    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        node = Node(item)
        if self.isEmpty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                cur = cur.next
            node = Node(item)
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == "__main__":
    linkList = SingleLinkList()
    print(linkList.isEmpty())
    print(linkList.length())
    for i in range(0, 11, 2):
        linkList.append(i)
    print(linkList.travel())
    for i in range(9, 0, -3):
        linkList.add(i)
    print(linkList.travel())
    linkList.insert(20, 12)
    print(linkList.travel())
    linkList.insert(-5, -3)
    print(linkList.travel())
    linkList.insert(8, 7)
    print(linkList.travel())
    linkList.remove(6)
    print(linkList.travel())

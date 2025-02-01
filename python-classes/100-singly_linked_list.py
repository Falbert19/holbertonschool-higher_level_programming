#!/usr/bin/python3
"""
this module defines a Node class for a singly linked list
"""


class Node:
    """
    represents a node in a singly linked list

    Attributes:
        __data (int): data on node
        __next_node (Node): next node in the list
    """

    def __init__(self, data, next_node=None):
        """
        initializes a Node

        Args:
            data (int): data stored in node
            next_node (Node): next node in the list

        Raises:
            TypeError: If data is not an integer
            TypeError: If next_node is not None or a Node object
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        retrieves the data stored in the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        sets the data of the node

        Args:
            value (int): new data value

        Raises:
            TypeError: If value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        retrieves the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        sets the next node

        Args:
            value (Node or None): new next node.

        Raises:
            TypeError: If value is not None or a Node object
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    represents a singly linked list

    Attributes:
        __head (Node): head of list
    """

    def __init__(self):
        """
        init empty singly linked list
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        innserts a new Node into the correct sorted position
        increasing order

        args:
            value (int): value to insert in the linked list
        """
        new_node = Node(value)

        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        return a string representation of the entire list

        Returns:
        str : list as a string
        """
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

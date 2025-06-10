import pytest
from singleLinkedList import SingleLinkedList, Node  # replace with actual file name if needed

def test_insert_head():
    ll = SingleLinkedList()
    ll.insert_head(10)
    assert ll.head.data == 10
    ll.insert_head(20)
    assert ll.head.data == 20

def test_insert_tail():
    ll = SingleLinkedList()
    ll.insert_tail(10)
    ll.insert_tail(20)
    assert ll.head.data == 10
    assert ll.head.next.data == 20

def test_insert_index():
    ll = SingleLinkedList()
    ll.insert_tail(1)
    ll.insert_tail(3)
    ll.insert_index(2, 1)
    assert ll.head.next.data == 2

def test_delete_head():
    ll = SingleLinkedList()
    ll.insert_tail(1)
    ll.insert_tail(2)
    ll.delete_head()
    assert ll.head.data == 2

def test_delete_tail():
    ll = SingleLinkedList()
    ll.insert_tail(1)
    ll.insert_tail(2)
    ll.delete_tail()
    assert ll.head.next is None

def test_delete_index():
    ll = SingleLinkedList()
    ll.insert_tail(1)
    ll.insert_tail(2)
    ll.insert_tail(3)
    ll.delete_index(1)
    assert ll.head.next.data == 3

def test_delete_value():
    ll = SingleLinkedList()
    ll.insert_tail(1)
    ll.insert_tail(2)
    ll.insert_tail(3)
    ll.delete_value(2)
    assert ll.head.next.data == 3

def test_contains():
    ll = SingleLinkedList()
    ll.insert_tail(1)
    ll.insert_tail(2)
    assert ll.contains(2)
    assert not ll.contains(5)

def test_length():
    ll = SingleLinkedList()
    assert ll.length() == 0
    ll.insert_tail(1)
    ll.insert_tail(2)
    assert ll.length() == 2

def test_to_list():
    ll = SingleLinkedList()
    ll.insert_tail(1)
    ll.insert_tail(2)
    ll.insert_tail(3)
    assert ll.to_list() == [1, 2, 3]

def test_reverse():
    ll = SingleLinkedList()
    ll.insert_tail(1)
    ll.insert_tail(2)
    ll.insert_tail(3)
    ll.reverse()
    assert ll.to_list() == [3, 2, 1]

def test_get_middle():
    ll = SingleLinkedList()
    for i in [1, 2, 3, 4, 5]:
        ll.insert_tail(i)
    assert ll.get_middle().data == 3

def test_has_cycle_false():
    ll = SingleLinkedList()
    ll.insert_tail(1)
    ll.insert_tail(2)
    assert not ll.has_cycle()

def test_has_cycle_true():
    ll = SingleLinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3
    node3.next = node1  # cycle
    ll.head = node1
    assert ll.has_cycle()

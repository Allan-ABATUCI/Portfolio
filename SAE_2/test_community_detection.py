
from community_detection import *

def network_test():
    assert network(
        ["Muriel", "Yasmine", "Yasmine", "Joël", "Muriel", "Joël", "Yasmine", "Thomas", "Joël", "Nassim", "Andrea",
         "Ali", "Andrea", "Nassim", "Andrea", "Joël", "Ali", "Nassim", "Ali", "Joël", "Thomas", "Daria", "Thomas",
         "Carole", "Thierry", "Axel", "Thierry", "Léo", "Axel", "Léo", "Léo", "Valentin", "Valentin", "Andrea"]) == {
               'Muriel': ['Yasmine', 'Joël'], 'Yasmine': ['Muriel', 'Joël', 'Thomas'], 'Joël': ['Yasmine', 'Nassim'],
               'Thomas': ['Yasmine', 'Daria', 'Carole'], 'Nassim': ['Joël'], 'Andrea': ['Ali', 'Nassim', 'Joël'],
               'Ali': ['Andrea', 'Nassim', 'Joël'], 'Daria': ['Thomas'], 'Carole': ['Thomas'],
               'Thierry': ['Axel', 'Léo'], 'Axel': ['Thierry', 'Léo'], 'Léo': ['Thierry', 'Valentin'],
               'Valentin': ['Léo', 'Andrea']}
    assert network(["Alice", "Bob", "Alice", "Charlie", "Bob", "Denis"]) == {'Alice': ['Bob', 'Charlie'],
                                                                             'Bob': ['Alice', 'Denis'],
                                                                             'Charlie': ['Alice'], 'Denis': ['Bob']}
    assert not network(["Alice", "Bob", "Alice", "Charlie", "Bob", "Denis"]) == {'Alice': [], 'Bob': [], 'Charlie': [],
                                                                                 'Denis': []}
    assert not network(
        ["Muriel", "Yasmine", "Yasmine", "Joël", "Muriel", "Joël", "Yasmine", "Thomas", "Joël", "Nassim", "Andrea",
         "Ali", "Andrea", "Nassim", "Andrea", "Joël", "Ali", "Nassim", "Ali", "Joël", "Thomas", "Daria", "Thomas",
         "Carole", "Thierry", "Axel", "Thierry", "Léo", "Axel", "Léo", "Léo", "Valentin", "Valentin", "Andrea"]) == {
                   "": []}
    print("ok")


network_test()


def get_people_test():
    assert not get_people({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }) == []

    assert get_people({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }
    ) == ["Alice", "Bob", "Charlie", "Dominique"]

    assert not get_people({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }) == ["", "", "", ""]

    assert not get_people({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }) == ["Dominique", "Bob", "Dominique", "Charlie"]

    print("ok")


get_people_test()


def are_friends_test():
    assert are_friends({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }, "Alice", "Bob") == True

    assert are_friends({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }, "Alice", "Charlie") == False

    assert not are_friends({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }, "Alice", "Alice") == True

    assert not are_friends({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }, "Alice", "") == True

    assert not are_friends({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }, "Charlie", "Dominique") == True

    print("ok")


are_friends_test()


def all_his_friends_test():
    assert all_his_friends({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }, "Alice", ["Bob", "Dominique"]) == True

    assert all_his_friends({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }, "Alice", ["Bob", "Charlie"]) == False

    assert not all_his_friends({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }, "Alice", ["Bob", "Alice"]) == True

    assert not all_his_friends({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }, "Alice", ["Bob", ""]) == True

    print("ok")


all_his_friends_test()


def is_a_communityis_a_community_test():
    assert is_a_community({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }, ["Alice", "Bob", "Dominique"]) == True

    assert is_a_community({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }, ["Alice", "Bob", "Charlie"]) == False

    assert is_a_community({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }, ["Alice", "Alice", "Alice"]) == False

    assert is_a_community({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }, ["Alice", "", "Charlie"]) == False

    assert is_a_community({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }, ["", "", ""]) == False

    print("ok")


is_a_communityis_a_community_test()


def find_community_test():
    assert find_community({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }, ["Alice", "Bob", "Charlie", "Dominique"]) == ["Alice", "Bob", "Dominique"]

    assert find_community({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }, ["Charlie", "Alice", "Bob", "Dominique"]) == ["Charlie", "Bob"]

    assert find_community({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }, ["Charlie", "Alice", "Dominique"]) == ["Charlie"]

    assert not find_community({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }, ["Charlie", "Alice", "Dominique"]) == []

    assert not find_community({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }, ["Charlie", "Alice", "Dominique"]) == [""]

    assert not find_community({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }, ["Alice", "Bob", "Charlie", "Dominique"]) == ["Alice", "Alice", "Alice"]

    assert not find_community({
        "Alice": ["Bob", "Dominique"],
        "Bob": ["Alice", "Charlie", "Dominique"],
        "Charlie": ["Bob"],
        "Dominique": ["Alice", "Bob"]
    }, ["Alice", "Bob", "Charlie", "Dominique"]) == ["", "", ""]

    print("ok")







import unittest
class MyTestCase(unittest.TestCase):
    def order_by_decreasing_popularity(self):
        self.assertEqual(order_by_decreasing_popularity({},["Alice", "Bob", "Charlie", "Dominique"]),[])
        self.assertEqual(order_by_decreasing_popularity({"Alice" : ["Bob", "Dominique"],"Bob" : ["Alice", "Charlie", "Dominique"],"Charlie" : ["Bob"],"Dominique" : ["Alice", "Bob"]},[]), [])
        self.assertEqual(order_by_decreasing_popularity({"Alice": ["Bob", "Dominique"], "Bob": ["Alice", "Charlie", "Dominique"], "Charlie": ["Bob"],"Dominique": ["Alice", "Bob"]},["Alice", "Bob", "Charlie"]), ["Bob", "Alice", "Charlie"])
        self.assertEqual(order_by_decreasing_popularity(
            {"Alice": ["Bob", "Dominique"], "Bob": ["Charlie", "Dominique"], "Charlie": ["Bob"],
             "Dominique": ["Alice", "Bob"]}, ["Alice", "Bob", "Charlie"]), ['Alice', 'Bob', 'Charlie'])
    def test_find_community_by_decreasing_popularity(self):
        self.assertEqual(find_community_by_decreasing_popularity({}),[])
        self.assertEqual(find_community_by_decreasing_popularity({"Alice" : ["Bob", "Dominique"],"Bob" : ["Alice", "Charlie", "Dominique"],"Charlie" : ["Bob"],"Dominique" : ["Alice", "Bob"]}),["Bob", "Alice", "Dominique"])
        self.assertEqual(find_community_by_decreasing_popularity({"Alice": ["Bob", "Dominique"], "Bob": ["Charlie", "Dominique"], "Charlie": ["Bob"],
             "Dominique": ["Alice", "Bob"]}),['Alice', 'Bob', 'Dominique'])
    def test_find_community_from_person(self):
        self.assertEqual(find_community_from_person("",{"Alice": ["Bob", "Dominique"], "Bob": ["Alice", "Charlie", "Dominique"], "Charlie": ["Bob"],
             "Dominique": ["Alice", "Bob"]}), [])
        self.assertEqual(find_community_from_person("Alice",{}), [])
        self.assertEqual(find_community_from_person("Alice",
            {"Alice": ["Bob", "Dominique"], "Bob": ["Alice", "Charlie", "Dominique"], "Charlie": ["Bob"],
             "Dominique": ["Alice", "Bob"]}), ["Alice", "Bob", "Dominique"])
        self.assertEqual(find_community_by_decreasing_popularity(
            {"Alice": ["Bob", "Dominique"], "Bob": ["Charlie", "Dominique"], "Charlie": ["Bob"],
             "Dominique": ["Alice", "Bob"]}), ['Alice', 'Bob', 'Dominique'])
    def test_find_max_community(self):
        self.assertEqual(find_max_community({}),[])
        self.assertEqual(find_max_community({"Alice": ["Bob", "Dominique"], "Bob": ["Alice", "Charlie", "Dominique"], "Charlie": ["Bob"],"Dominique": ["Alice", "Bob"]}),['Bob', 'Alice', 'Dominique'])
        self.assertEqual(find_max_community({"Alice": ["Bob", "Dominique"], "Bob": ["Alice", "Dominique"], "Charlie": ["Bob"],"Dominique": ["Alice", "Bob"]}),["Alice", "Bob", "Dominique"])
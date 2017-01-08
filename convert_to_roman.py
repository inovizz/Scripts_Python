#Python script
#!/usr/bin/env python
import sys
import unittest

list_of_roman = [
    ("M", 1000), ("CM", 900), ("D", 500),
    ("CD", 400), ("C", 100),  ("XC", 90),
    ("L", 50),   ("XL", 40),  ("X", 10),
    ("IX", 9),   ("V", 5),    ("IV", 4),
    ("I", 1)
]

def roman_conversion_from_int(num=None):
    if num is None:
        return "Wrong Input"
    elif isinstance(num, str):
        return "String Input given, integer needed"
    else:
        my_list = []
        for _roman, _int in list_of_roman:
            print _roman, _int
            while _int <= num:
                num = num - _int
                print num
                my_list.append(_int)
            
    return my_list
        
print roman_conversion_from_int(134)
print roman_conversion_from_int(345)
print roman_conversion_from_int(45)

"""
class TestMyFunction(unittest.TestCase):
    def setUp(self):
        pass

    def test_my_function(self):
        self.assertEqual(roman_conversion_from_int(1), "I")
        self.assertEqual(roman_conversion_from_int(14), "XIV")
        
    def test_my_function(self):
        self.assertEqual(roman_conversion_from_int(), "Wrong Input")
        self.assertEqual(roman_conversion_from_int("xyz"), "String Input given, integer needed")

if __name__ == '__main__':
    unittest.main()
    
"""

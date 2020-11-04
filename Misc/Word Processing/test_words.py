import unittest
from word_processor import convert_to_word_list
from word_processor import words_longer_than
from word_processor import words_lengths_map
from word_processor import letters_count_map
from word_processor import most_used_character




class WordProcessorTest(unittest.TestCase):
    
    def test_step1_convert_word_list(self):
        list_words = convert_to_word_list("Hello world.")
        self.assertEqual(["hello", "world"],list_words)

    
    def test_step2_words_longer_than(self):
        words = words_longer_than(5, "So this, is nothing more then a test string. For your enjoyment?")
        self.assertEqual(["nothing", "string", "enjoyment"], words)

    
    def test_step3_words_lengths_map(self):
        map_word_legnths = words_lengths_map("Hello, my name is Liam. What is yours?")
        self.assertEqual({2: 3, 4: 3, 5: 2}, map_word_legnths)

    def test_step4_letters_count_map(self):
        letter_occurence = letters_count_map("Hello, my name is Liam Chalmers. What is yours?")
        self.assertEqual({'a': 4, 'b': 0, 'c': 1, 'd': 0, 'e': 3, 'f': 0, 'g': 0, 'h': 3, 'i': 3, 'j': 0, 'k': 0, 'l': 4, 'm': 4, 'n': 1, 'o': 2, 'p': 0, 'q': 0, 'r': 2, 's': 4, 't': 1, 'u': 1, 'v': 0, 'w': 1, 'x': 0, 'y': 2, 'z': 0}, letter_occurence)


    def test_step5_most_used_character(self):
        letter = most_used_character("Hello, my name is Liam Chalmers. What is yours?")
        self .assertEqual('a', letter)
""" The following are a few challenges to try out. 
Purpose: To see how you think through logical problems and communicate. 
Resources: Use anything you want including StackOverflow, Google, and the interviewers. 
           You can import any module that this platform supports.
Take as much time as you need, ask all the questions you want. 
Completion is not a requirement. """

"""1. Frequency sort"""
# Sort the given iterable so that its elements end up in the decreasing frequency order,
# that is, the number of times they appear in elements. If two elements have the same frequency,
# they should end up in the same order as the first appearance in the iterable.
#Input: Iterable
#Output: Iterable
#Precondition: elements can be ints or strings

def frequency_sort(items):
    # your code here
    return None

frequency = False
if frequency:
  print("Example:")
  print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
  
  # These "asserts" are used for self-checking and not for an auto-testing
  assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
  assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
  assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
  assert list(frequency_sort([])) == []
  assert list(frequency_sort([1])) == [1]
  print("frequency sort complete.")
  

"""2. Long repeat"""
#find the length of the longest substring that consists of the same letter. 
#For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa". 
#The last substring is the longest one, which makes it the answer.
#Input: String.
#Output: Int. 

def long_repeat(line: str) -> int:
    # your code here
    return 0

repeat = False
if repeat:
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print("long repeat complete")

"""3. Monkey typing"""
#You are given some text potentially including sensible words. 
#You should count how many words are included in the given text. 
#A word should be whole and may be a part of other word. 
#Text letter case does not matter. Words are given in lowercase and don't repeat. 
#If a word appears several times in the text, it should be counted only once.

#For example, text - "How aresjfhdskfhskd you?", words - ("how", "are", "you", "hello"). The result will be 3.

#Input: Two arguments. A text as a string (unicode for py2) and words as a set of strings (unicode for py2).

#Output: The number of words in the text as an integer.

#count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3
#count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2
#count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
#            {"sum", "hamlet", "infinity", "anything"}) == 1

#Precondition:
#0 < len(text) ≤ 256
#all(3 ≤ len(w) and w.islower() and w.isalpha for w in words) 


def count_words(text: str, words: set) -> int:
    return 0


count = False
if count:
    print("Example:")
    print(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))
    
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Count words complete.")




if not any([frequency, count, repeat]):
    print("Try setting one of [frequency, count, repeat] to True")

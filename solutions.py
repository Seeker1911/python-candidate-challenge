"""monkey typing"""


def count_words2(text, words):
    return sum(w in text.lower() for w in words)


def count_words(text, words):
    ans=0
    for i in words:
        if i in text.lower():
            ans+=1
    return ans 

if __name__ == '__main__':

    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
        {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print('count words complete')



"""frequency sort"""
def frequency_sort2(items):
    from collections import Counter
    frequency = Counter(items).most_common()
    res = []
    for v, c in frequency:
        res += [v for i in range(c)]
    return res


def frequency_sort(items): return sorted(items, key=lambda x: (-items.count(x), items.index(x)))

if __name__ == '__main__':
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("frequency sort complete.")


"""long repeat"""

from itertools import groupby

def long_repeat(line):
    max = 0
    now_count = 1
    last_letter = None
    for letter in line:
        if last_letter == letter:
            now_count += 1
        else:
            now_count = 1

        last_letter = letter
        if now_count > max:
            max = now_count

    return max


def long_repeat2(line):
    return max([len(group) for group
                in [list(g) for k, g in groupby(line)]], default=0)


def long_repeat3(line):
    return max((sum(1 for _ in g) for k, g in groupby(line)), default=0)

if __name__ == '__main__':
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('long repeat complete')

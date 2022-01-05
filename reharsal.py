def is_anagram(string1 , string2):
    """
    אנו צריכים לבדוק האם הסטרינגים האלו עם אותו אותיות ,לא משנה הסדר
    זה נקרא אנגרמה
    This method checks if the strings are anagrams of each other
    anagrams are words that have the same letters with the same number of occurrences
    (of letters)
    "tami" "amit" are anagrams
    "tammi" "amit" are NOT anagrams
    :param string1: first word
    :param string2: second word
    :return: a boolean that represents if strings are anagrams
    """
    # בודקים האם האורך של שני הסטרינגים שווה
    if len(string1)!=len(string2):
        return False
    frequencies_string1 = count_frequencies(string1)
    frequencies_string2 = count_frequencies(string2)
    return frequencies_string1 == frequencies_string2

# פונקציה עזר שלנו
def count_frequencies(single_string):
    frequency_dict = dict()  # עושים מילון חדש
    for letter in single_string:
        frequency_dict[letter] = frequency_dict.get(letter,0) + 1
        # אם אין לנו את המילה הזאת במילון , תשמור אותה ותוסיף לה אחד
        return frequency_dict

# מה צריך להדפיס בסוף
    if __name__ == '__main__':
        anagrams = is_anagram("amit","tami")
        print(anagrams)
        print(palindrome1("abba"))

"""
len(string) - אורך המחזורת
string[i] - האות במיקום זה , לא לשכוח שמתחילים מ-0
for letter in single_string: - לרוץ על המחרוזת
true או false == בוליאני
for index in range(8) - לרוץ על המספרים 0 עד 7 כולל 
"""

# פונקציה שבודקת לי האם סטרינג הוא פולינדרום או לא
def palindrome1(string1):
    string2 = string1[::-1]
    return string2 == string1

# abba
def palindrome2(string1):
    lenght = len(string1)
    for index in range(lenght // 2):
        if string1[index] != string1[lenght-1-index]:
            return False
    return True


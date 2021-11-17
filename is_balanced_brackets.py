import unittest


def is_balanced_brackets(phrase: str) -> bool:
    """
    Проверяет строку на наличие закрытой скобки.
    Дана строка на вход, функция должна вернуть True or False
    в зависимости от содержания в строке из:
    (), {}, [], <>
    @param phrase: str
    @return: bool
    """

    brackets = {
                ')': '(',
                '}': '{',
                ']': '[',
                '>': '<'
                }
    opened_brackets, closed_brackets = brackets.values(), brackets.keys()
    stack = []
    for letter in phrase:
        if letter in opened_brackets:
            stack.append(letter)
            continue
        if letter in closed_brackets:
            if stack and brackets[letter] == stack[-1]:
                stack.pop()
            else:
                return False
    return True if not stack else False




class TestSolutions(unittest.TestCase):
    def test_is_balanced_brackets_01(self):
        self.assertTrue(is_balanced_brackets("<Ok>"))

    def test_is_balanced_brackets_02(self):
        self.assertTrue(is_balanced_brackets("<[ok]>"))

    def test_is_balanced_brackets_03(self):
        self.assertTrue(is_balanced_brackets("<[{(yay)}]>"))

    def test_is_balanced_brackets_04(self):
        self.assertTrue(is_balanced_brackets("Тут нет скобок!"))

    def test_is_balanced_brackets_05(self):
        self.assertFalse(is_balanced_brackets("(Упс!){"))

    def test_is_balanced_brackets_06(self):
        self.assertFalse(is_balanced_brackets("{[[Слишком много открытых скобок]}"))

    def test_is_balanced_brackets_07(self):
        self.assertFalse(is_balanced_brackets(">"))

    def test_is_balanced_brackets_08(self):
        self.assertFalse(is_balanced_brackets("(Тут {слишком много} ) закрывающих. )"))

    def test_is_balanced_brackets_09(self):
        self.assertFalse(is_balanced_brackets("<{Не хорошо>}"))



if __name__ == "__main__":
    unittest.main()

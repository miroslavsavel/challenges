class Palindrom:
    def __init__(self):
        self.x = 10

    def isStrPalindrom(self, x: str) ->bool:
        return(str(x) == str(x)[::-1])

    def isNumPalindrom(self, x: int) -> bool:
        if x < 0:
            return (False)

        rev_num = 0
        digit = 0

        while (x // (10 ** digit) != 0):
            # strip digit and add to our reverse number
            rev_num = (rev_num * 10) + (x // (10 ** digit) % 10)
            # * 10 aby som posunul dane cislo na danu poziciu
            # 73 * 10 + (737 // 100) % 10
            digit += 1

        return (x == rev_num)

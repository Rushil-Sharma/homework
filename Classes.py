import os , time
for i in range(1):
    print('Write a Python class to convert an integer to a roman numeral.')
    class py_solution:
        def int_to_Roman(self, num):
            val = [
                1000, 900, 500, 400,
                100, 90, 50, 40,
                10, 9, 5, 4,
                1
                ]
            syb = [
                "M", "CM", "D", "CD",
                "C", "XC", "L", "XL",
                "X", "IX", "V", "IV",
                "I"
                ]
            roman_num = ''
            i = 0
            while  num > 0:
                for _ in range(num // val[i]):
                    roman_num += syb[i]
                    num -= val[i]
                i += 1
            return roman_num
    print(py_solution().int_to_Roman(4000))
    time.sleep(3)
    c = input('Do you want to clear this ? (y/n)  ')
    if c == 'y':
        os.system('cls')
#==============================================================================#
for i in range(1):
    print('Write a Python class to convert a roman numeral to an integer')
    class py_solution:
        def roman_to_int(self, s):
            rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            int_val = 0
            for i in range(len(s)):
                if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                    int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
                else:
                    int_val += rom_val[s[i]]
            return int_val
    print(py_solution().roman_to_int('C'))
    time.sleep(3)
    c = input('Do you want to clear this ? (y/n)  ')
    if c == 'y':
        os.system('cls')
#==============================================================================#
for i in range(1):
    class py_solution:
    def is_valid_parenthese(self, str1):
            stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
            for parenthese in str1:
                if parenthese in pchar:
                    stack.append(parenthese)
                elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                    return False
            return len(stack) == 0
    x=input("enter some thing : ")
    print(py_solution().is_valid_parenthese(x))
    time.sleep(3)
    c = input('Do you want to clear this ? (y/n)  ')
    if c == 'y':
        os.system('cls')
#==============================================================================#
for i in range(1):
    class py_solution:
        def sub_sets(self, sset):
            return self.subsetsRecur([], sorted(sset))
        
        def subsetsRecur(self, current, sset):
            if sset:
                return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
            return [current]
    print(py_solution().sub_sets([4,5,6]))
    time.sleep(3)
    c = input('Do you want to clear this ? (y/n)  ')
    if c == 'y':
        os.system('cls')
#==============================================================================#
for i in range(1):
    class py_solution:
        def pow(self, x, n):
            if x==0 or x==1 or n==1:
                return x 
            if x==-1:
                if n%2 ==0:
                    return 1
                else:
                    return -1
            if n==0:
                return 1
            if n<0:
                return 1/self.pow(x,-n)
            val = self.pow(x,n//2)
            if n%2 ==0:
                return val*val
            return val*val*x
    print(py_solution().pow(56,1))
        time.sleep(3)
        c = input('Do you want to clear this ? (y/n)  ')
        if c == 'y':
            os.system('cls')
#==============================================================================#
for i in range(1):
    class py_solution:
        def reverse_words(self, s):
            return ' '.join(reversed(s.split()))
    print(py_solution().reverse_words('hello .py'))
    time.sleep(3)
    c = input('Do you want to clear this ? (y/n)  ')
    if c == 'y':
        os.system('cls')
#==============================================================================#

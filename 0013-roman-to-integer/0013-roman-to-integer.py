class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=[]
        if "CM" in s:
            l.append(900)
            s = s.replace("CM", "N")
        if "CD" in s:
            l.append(400)
            s = s.replace("CD", "N")
        if "XL" in s:
            l.append(40)
            s = s.replace("XL", "N")
        if "XC" in s:
            l.append(90)
            s = s.replace("XC", "N")
        if "IV" in s:
            l.append(4)
            s = s.replace("IV", "N")
        if "IX" in s:
            l.append(9)
            s = s.replace("IX", "N")
        print s    
        for i in s:
            if i=='I':
                l.append(1)
            elif i=='V':
                l.append(5)
            elif i=='X':
                l.append(10)
            elif i=='L':
                l.append(50)
            elif i=='C':
                l.append(100)
            elif i=='D':
                l.append(500)
            elif i=='M':
                l.append(1000)
            elif i=='N':
                l.append(0)
        return sum(l)
        
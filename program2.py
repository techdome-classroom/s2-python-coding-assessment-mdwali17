class Solution(object):
    def romanToInt(self, s:str)-> int:
        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum=0
        for i in range(len(s)-1,-1,-1):
            num=roman[s[i]]
            if 3*num < sum:
                sum=sum-num
            else:
                sum=sum+num
        return sum
solution = Solution()
roman_numeral1="MCMXCIV"
result=solution.romanToInt(roman_numeral1)
print(result)





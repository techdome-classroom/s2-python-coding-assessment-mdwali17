class Solution(object):
    def isValid(self, s:str)->bool:
        """
        :type s: str
        :rtype: bool
        """
        while True:
            if '()' in s:
                s=s.replace('()','')
            elif '{}' in s:
                s=s.replace('{}','')
            elif '[]' in s:
                s=s.replace('[]','')
            else:
                return not s
            
if __name__ =='__main__':
    s="{[()]}"
    print(f'Is {s}valid ?:{Solution().isValid(s)}')

    s1="{[(])}"
    print(f'Is {s1}valid ?:{Solution().isValid(s1)}')







    



  


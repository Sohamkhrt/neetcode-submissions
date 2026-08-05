class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ''
        for x in strs:
            l = len(x)
            code = code + str(l) + '#'
            code = code + x
        
        print(code)

        return code


        

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 1
        anslist =[]
        while i < len(s):
            
            if s[j] == '#':
                lengthstr = int(s[i:j])
                endstr = j + lengthstr +1
                anslist.append(str(s[j+1:endstr]))
                i = endstr
                j = endstr + 1
            else:  

                j+=1
                



        
        return anslist


            
            

        









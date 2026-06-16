class Solution:
    def processStr(self, s: str) -> str:
        result = []

        for i in s:
            if i.islower():
                result.append(i)
            elif i == '*' and result:

                last_element = result.pop()
                if len(last_element) > 1:
                    n = len(last_element)-1
                    result.append(last_element[0:n])
                   
                        
            elif  i == '#' and result:
                last_letter = "".join(result)
                print(last_letter)
                result.append(last_letter)
                print(result)
            else:
                for i in range(len(result)):
                    if len(result[i]) > 1:
                        result[i] = result[i][::-1]

                result.reverse()
        return "".join(result)



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myDict = {}

        if len(s) != len(t):
            return False

        for i in range( len(s) ):

            if s[i] in myDict:
                myDict[ s[i] ] += 1
            else:
                myDict[ s[i] ] = 1

            if t[i] in myDict:
                myDict[ t[i] ] -= 1
            else:
                myDict[ t[i] ] = -1

        for n in myDict:
            print(n, myDict[n])
            if myDict[n] != 0:
                return False

        return True
                
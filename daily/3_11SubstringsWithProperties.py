'''

'''
def solve(word:str) -> int:
            precomp = [0]*len(word)
            n = len(word)
            l = 0
            constants = 0
            soln =0
            counts = defaultdict(int)
            for i in range(len(word)-1,-1,-1):
                precomp[i] = n
                if not is_vowel(word[i]):
                    n = i
            for r in range(len(word)):
                #Expand always
                if is_vowel(word[r]):
                    counts[word[r]] += 1
                else:
                    constants += 1
                #Contract only when we have too many vowels or constants
                while  (len(counts) >= 5 and (constants) >= k):
                    if len(counts) == 5 and constants == k:
                        soln += precomp[r]-r
                    if is_vowel(word[l]):
                        counts[word[l]] -= 1
                        if counts[word[l]] == 0: counts.pop(word[l])
                    else:
                        constants -= 1
                    l += 1
            return soln
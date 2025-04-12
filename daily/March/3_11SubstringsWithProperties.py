'''

'''
def solve(word:str) -> int:
    # precomp = [0]*len(word)
    # n = len(word)
    # l = 0
    # constants = 0
    # soln =0
    # counts = defaultdict(int)
    # for i in range(len(word)-1,-1,-1):
    #     precomp[i] = n
    #     if not is_vowel(word[i]):
    #         n = i
    # for r in range(len(word)):
    #     #Expand always
    #     if is_vowel(word[r]):
    #         counts[word[r]] += 1
    #     else:
    #         constants += 1
    #     #Contract only when we have too many vowels or constants
    #     while  (len(counts) >= 5 and (constants) >= k):
    #         if len(counts) == 5 and constants == k:
    #             soln += precomp[r]-r
    #         if is_vowel(word[l]):
    #             counts[word[l]] -= 1
    #             if counts[word[l]] == 0: counts.pop(word[l])
    #         else:
    #             constants -= 1
    #         l += 1
    # return soln

    count = 0
    consonants = 0
    vowel_freq = {}
    left = 0
    right = 0
    prev = -1
    while right < n:
        if prev != right:
            if self.isVowel(word[right]):
                vowel_freq[word[right]] = vowel_freq.get(word[right], 0) + 1
            else:
                consonants += 1
            prev = right

        if right >= (5 + k - 1):
            if len(vowel_freq) == 5 and consonants == k:
                count += next_consonant[right] - right

            # Move left ptr to right: Shrink window
            if (len(vowel_freq) == 5 and consonants == k) or (consonants > k):
                if self.isVowel(word[left]):
                    vowel_freq[word[left]] -= 1
                    if vowel_freq[word[left]] == 0:
                        del vowel_freq[word[left]]
                else:
                    consonants -= 1
                left += 1
            else:
                right += 1
        else:
            right += 1

    return count
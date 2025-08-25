  def groupAnagrams(self, strs):
        from collections import defaultdict    # used defaultdict for errors like if my key is not present in dict and im trying to append value in key 
        answer = defaultdict(list)
        for word in strs:
            
            count = [0] * 26  #count[0,0,0......]  a --> z
            for char in word:
                count[ord(char) - ord("a")] += 1
#  dictionay key is used as count tuple(immutable) not list(mutable) -->  (1,1,0,0........0)  and value is word
            answer[tuple(count)].append(word)   
        return answer.values()     


#   TC -> m * (n * 26) --> O(m * n)


class Solution:
    def compress(self, chars: List[str]) -> int:
        # to search through the consecutive repeating characters,
        # have a left pointer start at beginning of sequence and traverse with right till it changes
        # then move left to right, and traverse again
        # we need to modify chars in place:
        # keep a res arr to keep track of compressed arr then traverse through chars to replace with each index in res

        # if chars.length == 1
        if len(chars) == 1:
            return len(chars)
        
        index = 0
        left = 0
        right = left
        while right < len(chars):
            length = 0
            while right < len(chars) and chars[left] == chars[right]:
                length += 1
                right += 1
            
            # we've reached the end of the repeating chars so append to res
            chars[index] = chars[left]
            index += 1
            if length != 1: # means more than 1 char in a row
                # we need to separate digits if length >= 10
                string_length = str(length)
                for digit in string_length:
                    chars[index] = digit
                    index += 1
            
            # move left to start of new char to look at
            left = right
        
        return index

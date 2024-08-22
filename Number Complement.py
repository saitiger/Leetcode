class Solution:
    def findComplement(self, num: int) -> int:
        binary_rep = bin(num)[2:]
        flipped = ''.join('1' if bit == '0' else '0' for bit in binary_rep)
        return int(flipped, 2)

"""
Problem: Reverse Bits (LC #190)
Difficulty: Easy
Link: https://leetcode.com/problems/reverse-bits/

Approach:
- Iterate 32 times (fixed 32-bit integer)
- Each step: shift result left, OR with last bit of n
- Right shift n to process next bit
- Time: O(1) — always 32 iterations | Space: O(1)

ML Connection:
- Bit reversal is used in Fast Fourier Transform (FFT)
  which is applied in signal processing for audio ML
- Bitwise ops are used in hardware-efficient ML model
  quantization (1-bit and 2-bit neural networks)
"""

class Solution:
    def reverseBits(self, n):
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result

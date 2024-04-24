class Solution:
    def reverse(self, x: int) -> int:
        # Convert the absolute value of x to a string and reverse it
        integerString = str(abs(x))

        # Loop through that string and add it to a new string to reverse it
        newIntegerString = ""
        for i in integerString:
            newIntegerString = i + newIntegerString
        newInteger = int(newInteger)

        # Check if the reversed integer is within the 32-bit signed integer range
        if (-2**31 < newInteger < 2**31 - 1):
            if x < 0:
                # Return the reversed integer with the original sign
                return -newInteger
            else:
                return newInteger
        else:
            return 0

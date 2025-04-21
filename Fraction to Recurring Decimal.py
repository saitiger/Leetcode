class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []

        # Handle negative numbers
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        # Integer part
        quotient = numerator // denominator
        result.append(str(quotient))

        remainder = numerator % denominator
        if remainder == 0:
            return "".join(result)

        result.append(".")
        remainder_map = {}

        while remainder != 0:
            if remainder in remainder_map:
                idx = remainder_map[remainder]
                result.insert(idx, "(")
                result.append(")")
                break

            remainder_map[remainder] = len(result)
            remainder *= 10
            digit = remainder // denominator
            result.append(str(digit))
            remainder %= denominator

        return "".join(result)

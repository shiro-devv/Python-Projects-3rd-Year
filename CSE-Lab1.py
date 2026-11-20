def calculateIntegerRanges(bits: int):
    # The allowed maximum amount for the unsigned integer.
    unsigned_max = (1 << bits) - 1
    # The allowed minimum and maximum value for the signed integer.
    signed_min = -(1 << (bits - 1))
    signed_max = (1 << (bits - 1)) - 1
    print(f"{bits}-bit Unsigned Integer: 0 -> {unsigned_max}")
    print(f"{bits}-bit Signed Integer: {signed_min} to {signed_max}")


def getBitCount():
    while True:
        try:
            bits = int(input("How many bits do you want to calculate? "))
            if bits > 0:
                return bits
            print("Enter a positive whole number.")
        # Catches Non-Integer inputs
        except ValueError:
            print("Enter a positive whole number.")


if __name__ == "__main__":
    calculateIntegerRanges(getBitCount())
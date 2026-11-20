
def isBinary(userInput):
    return bool(userInput) and all(ch in '01' for ch in userInput)


def floatToBinary(number, bias, exponentCount, mantissaCount):
    # check the string and not the number -0.0
    signBit = '1' if str(number).startswith('-') else '0'
    number = abs(number)

    if number == 0:
        return signBit + '0' * (exponentCount + mantissaCount)

    if not 2 ** (1 - bias) <= number < 2 ** (bias + 1):
        raise ValueError('Number outside the normal range of this precision')

    exponent = 0
    while number < 1:
        number *= 2
        exponent -= 1
    while number >= 2:
        number /= 2
        exponent += 1

    exponentBits = f'{exponent + bias:0{exponentCount}b}'

    fraction = number - 1
    mantissaBits = ''
    for _ in range(mantissaCount):
        fraction *= 2
        bit = int(fraction)
        mantissaBits += str(bit)
        fraction -= bit

    return signBit + exponentBits + mantissaBits


def showValue(bits, bias, exponentCount):
    signBit = bits[0]
    exponentBits = bits[1:exponentCount + 1]
    mantissaBits = bits[exponentCount + 1:]

    rawExponent = int(exponentBits, 2)

    fraction = sum(int(bit) * 2 ** -(i + 1) for i, bit in enumerate(mantissaBits))

    print(f'Bit Pattern: {signBit} {exponentBits} {mantissaBits}')
    print(f'Raw Exponent: {rawExponent}')
    print(f'Fraction: {fraction}')

    sign = (-1) ** int(signBit)

    mantissa = 1 + fraction
    if rawExponent == 0:
        mantissa = fraction

    exponentBase = max(1, rawExponent)
    exponent = exponentBase - bias
    print(f'Exponent: {exponentBase} - {bias} = {exponent}')
    print(f'Mantissa: {mantissa}')
    print(f'Formula: (-1) ^ {signBit} * 2 ^ {exponent} * {mantissa}')

    try:
        finalValue = sign * (2 ** exponent) * mantissa
    except OverflowError:
        finalValue = 'Number too large'

    print(f'Final Value: {finalValue}')


def showPrecision(precision, value, bias, exponentCount, mantissaCount, bitCount):
    print('-' * 50)
    print(f'{precision} Precision')

    if isinstance(value, str):
        bits = value[:bitCount].ljust(bitCount, '0')
    else:
        try:
            bits = floatToBinary(value, bias, exponentCount, mantissaCount)
        except ValueError as err:
            print(err)
            return

    showValue(bits, bias, exponentCount)


def main():
    while True:
        userInput = input('What number you want convert?: ').strip()
        if not userInput:
            print('put somethings')
            continue
        if isBinary(userInput):
            value = userInput
            break
        try:
            value = float(userInput)
            break
        except ValueError:
            print('Input valid number plz')

    showPrecision('Half', value, 15, 5, 10, 16)
    showPrecision('Single', value, 127, 8, 23, 32)
    showPrecision('Double', value, 1023, 11, 52, 64)


if __name__ == '__main__':
    main()

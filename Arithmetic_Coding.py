from collections import Counter


def cumulative_frequency(frequency):
    cf = {}
    total = 0
    for i in range(256):
        if i in frequency:
            cf[i] = total
            total += frequency[i]
    return cf


def arithmethic_coding(bytes, radix):

    frequency = Counter(bytes)
    cf = cumulative_frequency(frequency)

    base = len(bytes)

    lower = 0

    product_frequency = 1

    for b in bytes:
        lower = lower * base + cf[b] * product_frequency
        product_frequency *= frequency[b]

    upper = lower + product_frequency

    pow = 0
    while True:
        product_frequency //= radix
        if product_frequency == 0:
            break
        pow += 1

    encode = (upper - 1) // radix ** pow
    return encode, pow, frequency

def arithmethic_decoding(encode, radix, pow, frequency):
    encode *= radix ** pow

    base = sum(frequency.values())

    cf = cumulative_frequency(frequency)

    dictionary = {}
    for k, v in cf.items():
        dictionary[v] = k

    lchar = None
    for i in range(base):
        if i in dictionary:
            lchar = dictionary[i]
        elif lchar is not None:
            dictionary[i] = lchar

    decoded = bytearray()
    for i in range(base - 1, -1, -1):
        pow = base ** i
        divide = encode // pow

        c = dictionary[divide]
        fv = frequency[c]
        cv = cf[c]

        remainder = (encode - pow * cv) // fv

        encode = remainder
        decoded.append(c)

    return bytes(decoded)

radix = 10
string = input('Message to encode: ')

# pretvaranje na originalnata porakata od string vo bytes
str = str.encode(string)

enc, pow, freq = arithmethic_coding(str, radix)
dec = arithmethic_decoding(enc, radix, pow, freq)

print("Encoded Message: %s * %d^%s" % (enc, radix, pow))

# pretvaranje na dekodiranata poraka od byte vo string
decoded = dec.decode()
print('Decoded Message: %s' % (decoded))
if str != dec:
    raise Exception("\tHowever that is incorrect!")
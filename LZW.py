def comp(to_comp):
    # Sozdavanje dictionary
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}

    w = ""
    result = []
    for c in to_comp:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Dodavanje na wc vo dictionary
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    # return LZW-kod
    if w:
        result.append(dictionary[w])
    return result


def decomp(to_decomp):
    from io import StringIO

    # Sozdavanje dictionary
    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}

    result = StringIO()
    w = chr(to_decomp.pop(0))
    result.write(w)

    for k in to_decomp:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Loso kompresiran k: %s' % k)
        result.write(entry)

        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry

    return result.getvalue()


to_compress = input('Enter string to be compressed: ')
LZW_comp = comp(to_compress)
print('Compressed: %s' %LZW_comp)
LZW_decomp = decomp(LZW_comp)
print('Decompressed: ' + LZW_decomp)

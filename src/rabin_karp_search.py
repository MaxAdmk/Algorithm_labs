number_of_characters = 256


def rabinKarpSearch(pat, txt, q):
    result = []
    pattern_len = len(pat)
    text_len = len(txt)
    i = 0
    j = 0
    pattern_hash_value = 0
    text_hash_value = 0
    h = 1

    for i in range(pattern_len - 1):
        h = (h * number_of_characters) % q

    for i in range(pattern_len):
        pattern_hash_value = (number_of_characters * pattern_hash_value + ord(pat[i])) % q
        text_hash_value = (number_of_characters * text_hash_value + ord(txt[i])) % q

    for i in range(text_len - pattern_len + 1):

        if pattern_hash_value == text_hash_value:
            for j in range(pattern_len):
                if txt[i + j] != pat[j]:
                    break
            else:
                result.append(i)

        if i < text_len - pattern_len:
            text_hash_value = (number_of_characters * (text_hash_value - ord(txt[i]) * h) + ord(txt[i + pattern_len])) % q

            if text_hash_value < 0:
                text_hash_value = text_hash_value + q

    return result


haystack = "adcasdabcasabc"
needle = "abc"
prime_number = 101
result = rabinKarpSearch(needle, haystack, prime_number)
print("Indices of pattern:", result)

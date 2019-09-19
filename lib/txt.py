LETTER_FREQUENCY_ENGLISH = {'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702, 'f': 0.02228,
                            'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025,
                            'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929, 'q': 0.00095, 'r': 0.05987,
                            's': 0.06327, 't': 0.09056, 'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150,
                            'y': 0.01974, 'z': 0.00074}
for k in dict(LETTER_FREQUENCY_ENGLISH):
    LETTER_FREQUENCY_ENGLISH[k.upper()] = LETTER_FREQUENCY_ENGLISH[k]

LETTER_FREQUENCY_ENGLISH_WITH_SPACE = dict(LETTER_FREQUENCY_ENGLISH)
for k in LETTER_FREQUENCY_ENGLISH_WITH_SPACE:
    LETTER_FREQUENCY_ENGLISH_WITH_SPACE[k] = LETTER_FREQUENCY_ENGLISH_WITH_SPACE[k] * (1 - 0.13)
LETTER_FREQUENCY_ENGLISH_WITH_SPACE[' '] = 0.13


def frequency_analysis(s):
    """
    perform absolute frequency analysis
    :param s: string to analyze
    :return: char-frequency dict
    """
    freq = {}
    for c in s:
        chars = freq.keys()
        if c in chars:
            freq[c] += 1
        else:
            freq[c] = 1

    return freq


def frequency_analysis_relative(s):
    """
    perform relative frequency analysis
    :param s: string to analyze
    :return: char-frequency dict
    """
    freq = frequency_analysis(s)

    for k, v in freq:
        freq[k] = v / len(s)

    return freq


def chi_squared_test(s, expectedFrequency=LETTER_FREQUENCY_ENGLISH_WITH_SPACE):
    """
    perform modified chi-squared test
    :param s: string to test
    :param expectedFrequency: char-frequency dict
    :return: goodness of fit (lower is better; 0 is ideal fit)
    """

    freq = frequency_analysis(s)

    # slightly modified calculation, to factor in if the letter is not expected
    chi = 0
    for c in expectedFrequency.keys() | freq.keys():
        chi += ((freq.get(c, 0) - expectedFrequency.get(c, 0) * len(s)) ** 2) / (
                expectedFrequency.get(c, 0.001) * len(s))
    return chi


def simple_char_score_test(s, expectedFrequency=LETTER_FREQUENCY_ENGLISH_WITH_SPACE):
    """
    count the expected score and normalize
    :param s: string to test
    :param expectedFrequency: char-frequency dict
    :return: score (higher is better)
    """

    score = 0
    for c in s:
        score += expectedFrequency.get(c, 0)

    return score


def order_by_test_score(candidates, test, ascending=False):
    """
    score and order the candidates with function f
    :param candidates: string list
    :param test: scoring function
    :param ascending: True for ascending order
    :return: ordered candidates list
    """

    score = {}
    for c in candidates:
        score[c] = test(c)

    return sorted(score.keys(), key=score.get) if ascending else sorted(score.keys(), key=score.get)[::-1]

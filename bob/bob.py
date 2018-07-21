def hey(phrase):
    phrase = phrase.strip()
    if not phrase:
        return 'Fine. Be that way!'
    elif phrase.isupper():
        if not phrase.endswith('?'):
            return "Whoa, chill out!"
        return "Calm down, I know what I'm doing!"
    elif phrase.endswith('?'):
        return "Sure."
    return 'Whatever.'

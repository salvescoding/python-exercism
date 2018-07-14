def hey(phrase):
    phrase = phrase.strip()
    if phrase.isupper():
        return "Whoa, chill out!" if not phrase[-1:] == '?' else "Calm down, I know what I'm doing!"
    elif phrase[-1:] == '?':
        return "Sure."
    elif phrase == '':
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'

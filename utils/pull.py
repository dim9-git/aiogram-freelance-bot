def pull_words(name):
    with open(name) as f:
        return [line.rstrip("\n") for line in f]

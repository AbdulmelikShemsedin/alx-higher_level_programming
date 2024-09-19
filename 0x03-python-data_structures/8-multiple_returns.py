#!/usr/bin/python3
def multiple_returns(sentence):
    new = (len(sentence), sentence[0] if len(sentence) else None)
    return new

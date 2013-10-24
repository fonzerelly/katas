from wordwrap import WordWrap, OutOfBounds
from nose.tools import *
import rpdb2; rpdb2.start_embedded_debugger("doof")
text = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."

@raises(OutOfBounds)
def test_column_0 ():
    WordWrap(text, 0) ;

def test_column_minimum():
    minimum_column = len(max(text.split(" "), key=len));
    result = WordWrap(text, minimum_column);
    for line in result.split("\n"):
        assert(len(line) <= minimum_column)


def test_column_max():
    import sys
    assert (WordWrap(text, sys.maxint)[-1] == "\n");
    assert (len(WordWrap(text, sys.maxint)) == len(text)+1)


def test_words_complete():
    result = WordWrap(text, 30)
    for line in result.split("\n"):
        last_word = line.split(" ")[-1]
        assert (last_word in text.split(" "))

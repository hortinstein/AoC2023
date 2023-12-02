import std/strutils
import std/algorithm
import std/tables
import "../util"

#let input = readStringFromFile("p1input")
const input = staticRead("p1input")

let numSpelledOut = @[
    "one","1",
    "two", "2",
    "three", "3",
    "four","4",
    "five", "5",
    "six","6",
    "seven", "7",
    "eight", "8",
    "nine", "9",
    "zero", "0"
]

import sequtils

proc convertSpelledOutToNumbers(seqs: seq[string]): seq[string] =
    let numSpelledOut = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0"
    }.toTable

    var result = newSeq[string]()

    for item in seqs:

        if item.len == 1:
            if (char(item[0])).isDigit():
                result.add(item)
        elif item.toLower() in numSpelledOut:
            result.add(numSpelledOut[item.toLower()])

    return result

proc findMatchingSubstrings(line: string, substrings: openArray[string]): seq[string] =
    var foundSubstrings = newSeq[string]()
    var i = 0

    while i < line.len:
        var found = false
        for key, value in substrings:
            if line[i..^1].startsWith(value):
                foundSubstrings.add(value)
                i += key.len - 1
                found = true
                break
        if not found:
            i += 1

    return foundSubstrings
var calSeq = newSeq[char]()
var total = 0

for line in splitLines(input):
    #go through all the chars in a line and add them up if they are a number
    echo line
    var matchingSubstrings = findMatchingSubstrings(line, numSpelledOut)
    echo matchingSubstrings
    for c in line:
        # if its a number or a spelled out number add it to the sequence
        if c.isDigit():
            calSeq.add(c)
    #get the first and last number in the sequence

    var first = calSeq[0]
    var last = calSeq[calSeq.len - 1]
    #add first and last chars together
    let number = first&last
    #convert string to int and add to total
    echo number
    calSeq= @[]
    total += parseInt(number)
    

echo total
    
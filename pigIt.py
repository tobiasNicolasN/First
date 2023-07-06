# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
def pigIt(text):
    wordList = text.split()
    finalText = ""
    for word in wordList:
        if word.isalpha() :
            wordFinal = word[1:] + word[0] + "ay"
            finalText += wordFinal + " "
        else:
            finalText += word + " "
    return finalText.strip()

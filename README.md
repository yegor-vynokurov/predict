# Generation of a pseudo-logical sentence based on a literary text.

**Task**: use the principle of Markov chains to form "predictions" based on the artistic text of the text.

## Solution:
1. A function has been written that generates two dictionaries based on text. One dictionary: keys are words from the text, values are lists of words that follow the word from the key. Another dictionary: keys are words from the text, values are lists of words that precede the word from the text. The more frequently a word occurs in a value list, the more often it follows the key.

2. A function was written that accepts any word, and based on it, using a random selection, generates an answer. You can set the length of the sentence and choose which dictionary the "prediction" will be based on.

The **get_text.py** file contains the sequence of steps for processing text, turning it into dictionaries, and saving dictionaries.

The **fnctns.py** file contains all the functions.

The **main.py** file contains the sequence for loading dictionaries from the dct folder and getting a "prediction". Also, the prediction is recorded in the file answers.txt in the **dkt folder**.

For the work, the text of the book by T. Pratchett "Equal Rites" on the russian language was used. Text has been removed to preserve copyright. You can use any text in .txt format to function get_text() and path to text and name of text. The stopword variable in get_text.py can be extended with any stopwords that need to be removed from the text.

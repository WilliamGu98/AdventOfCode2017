def file_to_set(fileName):
    with open(fileName,'r') as f:
        pass_phrases = []
        for line in f:
            pass_phrases.append(line)
    return pass_phrases


def valid_phrases(pass_phrases):
    num_valid = 0
    for line in pass_phrases:
        unique_words = set()
        words = line.split()
        for word in words:
            if (word in unique_words):
                num_valid-=1
                break
            else:
                unique_words.add(word)
        num_valid+=1
    return num_valid


def anagrams(pass_phrases):
    num_valid = 0
    for line in pass_phrases:
        words_num_letters = dict() #contains pairs of num_letters to a list of words
        words = line.split()
        for word in words: #Construct num_letters to words in list dictionary
            if len(word) in words_num_letters.keys():
                words_num_letters[len(word)].append(word)
            else:
                words_num_letters[len(word)]=[word]

        for same_letter_words in words_num_letters.values():
            if anagram_exists(same_letter_words):
                print("ANAGRAM FOUND, WORDS:", same_letter_words)
                num_valid-=1
                break

        num_valid+=1
    return num_valid


def anagram_exists(words):
    for i in range(len(words)-1):
        for j in range(i+1,len(words)):
            if is_anagram(words[i],words[j]):
                return True
    return False


def is_anagram(word1, word2):
    histogram1 = dict()
    histogram2 = dict()

    for char in list(word1):
        if char in histogram1.keys():
            histogram1[char]+=1
        else:
            histogram1[char]=0

    for char in list(word2):
        if char in histogram2.keys():
            histogram2[char]+=1
        else:
            histogram2[char]=0

    return histogram1 == histogram2


def main():
    pass_phrases = file_to_set("passphraselist.txt")

    #print(valid_phrases(pass_phrases))
    print(anagrams(pass_phrases))


if __name__ == "__main__":
    main()
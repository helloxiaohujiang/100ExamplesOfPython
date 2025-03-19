# Count Word Frequency in a String
def count_word_frequency(words):
    """Count Word Frequency in a String"""
    word_count = {}
    
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
        
    return word_count


words = ['apple', 'peach', 'celery', 'peach', 'tomato']

result = count_word_frequency(words)
print(result)
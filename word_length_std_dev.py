def word_length_std_dev(text):
    #Basics of getting the length of the sentence.
    words = text.split()
    lengths = [len(word) for word in words]
    n = len(lengths)

    if len(lengths) < 2:
        return 0
    
    # Get the average.
    mean = sum(lengths) / n

    #(x - mean)^2 for every word length
    sum_diff = sum((x - mean)**2 for x in lengths)

    # N-1 for sample std dev
    variance = sum_diff / (n - 1)

    #square rooting everything
    return variance ** 0.5

#final testing
text = 'There is wisdom in turning as often as possible from the familiar to the unfamiliar it keeps the mind nimble it kills prejudice and it fosters humor'
answer = word_length_std_dev(text)

print(f"Standard Deviation: {answer:.4f}")
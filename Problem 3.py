def char_frequency(sentence):
    d={}
    if len(sentence)==1:
        d[sentence]={1}
    else:
        for i in range(len(sentence)):
            if sentence[i] in d:
                d[sentence[i]] = d[sentence[i]]+1
            else:
                d[sentence[i]] = 1
    return d
print(char_frequency("helloworld"))
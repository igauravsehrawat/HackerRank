def unordered_anagram(a, b):
    hash1 = {}
    hash2 = {}
    for i in range(0, len(a)):
        hash1[a[i]] = 0
    for j in range(0, len(b)):
        hash2[b[j]] = 0
    for i in range(0, len(a)):
        hash1[a[i]] = hash1[a[i]]+1
    for j in range(0, len(b)):
        hash2[b[j]] = hash2[b[j]]+1
    return(hash1 == hash2)


def main():
    testcases = int(raw_input())
    while(testcases):
        count = 0
        testcases = testcases - 1
        input_string = raw_input()
        for length in range(0, len(input_string)):
            for start in range(0, len(input_string)):
                #this part generates the strings
                for match in range(start+1, len(input_string)):
                    #check if substring have same keys irrespective of the order
                    if(unordered_anagram(input_string[start:start+length+1], input_string[match:match+length+1])):
                        count = count + 1
        print count

#expected an indented line is not an error
if __name__ == "__main__":
    main()

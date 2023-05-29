

def concatenatedCount(strs):
    words = [i for i in strs.split(" ")]
    output_str = ""
    for word in words:
        count = 0
        for i in range(0, len(word)-1):
            ch1 = word[i]
            ch2 = word[i+1]
            if (ch1 < ch2):
                count += 1
        output_str += str(count)
    print(output_str)


def main():
    strs = input()
    concatenatedCount(strs)

main()




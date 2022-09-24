## Reg. No. : 21BAI10014
## Name : Aaditya More

special_words = [
        {'z':1, 'e':1, 'r':1, 'o':1},
        {'o':1, 'n':1, 'e':1},
        {'t':1, 'w':1, 'o':1},
        {'t':1, 'h':1, 'r':1, 'e':2},
        {'f':1, 'o':1, 'u':1, 'r':1},
        {'f':1, 'i':1, 'v':1, 'e':1},
        {'s':1, 'i':1, 'x':1},
        {'s':1, 'e':2, 'v':1, 'n':1},
        {'e':1, 'i':1, 'g':1, 'h':1, 't':1},
        {'n':2, 'i':1, 'e':1},
        ]


def if_present_then_remove(d1, d2):
    """

    d1 and d2 are dictrionaries with chars

    if all of d2 are present in d1 one or more times
        then remove those chars
    return the number of times d2 is present

    """

    ## making a copy to avoid modifying original d1
    d1_copy = d1.copy()

    ## initalizing count
    count = 0

    ## whether or not d2 is found in d1
    increase_count = True

    while True:
        ## check if every digit of d2 is present in d1
        ## and if prsent then reduce its count
        for i in d2:
            n = d1_copy.get(i, 0)
            if n > 0:
                d1_copy[i] = n-1
            else:
                ## digit(ie. d2) is no longer present leave the loop
                increase_count = False
                break

        ## either increase count or stop looping
        if increase_count:
            ## change d1 only if d2 is present
            d1 = d1_copy.copy()
            count=count+1
        else:
            break

    return d1, count

def find_digits(inp):
    """

    inp is a scrambelled string
    returns the digits found in it in ascending order

    """

    input_contents = {}
    for i in inp:
        input_contents[i] = input_contents.get(i,0) + 1

    final_ans = ""

    for i in range(len(special_words)):
        input_contents, n = if_present_then_remove(input_contents, special_words[i])
        final_ans = final_ans + str(i)*n

    return final_ans


def smallest_special_no(s):
    """

    str is in ascending order (ie. like 1234)
    returns the smallest possible no using all the digits

    zero cannot be on the leftmost position
        unless str is completely zero
        in which case just return "0"

    """

    if int(s) == 0:
        return "0"

    str = list(s)

    smallest_special_no = ""

    for i in str:
        if i != '0':
            smallest_special_no+=i
            str.remove(i)
            break
    for i in str:
        smallest_special_no+=i
    return smallest_special_no


if __name__ == "__main__":

    inputs = []
    answers = []

    for i in range(int(input())):
        inputs.append(input())

    for i in inputs:
        answers.append(smallest_special_no(find_digits(i)))

    for i in answers:
        print(i)

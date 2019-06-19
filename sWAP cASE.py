def swap_case(s):
    a = ""
    for let in s:
        if let.isupper() == True:
            a = a + (let.lower())
        else:
            a = a + (let.upper())
    return a
if __name__ == '__main__':
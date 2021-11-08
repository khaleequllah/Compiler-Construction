import string
if __name__ == "__main__":
    # Python program, that reads a C++ source program and identify type of Token.
    # reading data c++ code from data file
    data = open("input.txt", "r")
    inputt = []
    for input1 in data:
        inputt.append(input1)
    data.close()
    # seperators in c++ language are:
    separators = {"++", "--", "|=", "^=",
                  "&=", "<<=", ">>=", "%=", "{", "}", "(", ")", "[",
                  "]", "+", "-", "*", "/", "%", "+=", "-=", "*=", "/=",
                  "\n", "\t", "'", "//", " ", ";", "=", '"', ":",
                  ">>", "<<", "`", "^", "|", "&", "||", "&&", "!", ">=",
                  "<=", "<", ">", "!=", "==", }
    builtin_keywords = {"inline", "friend", "false",
                        "explicit", "dynamic_cast", "if", "goto", "for",
                        "float", "extern", "enum", "else", "duble", "int",
                        "long", "register", "return", "short", "signed",
                        "sizeof", "static", "namespace", "new", "operator",
                        "private", "public", "protected", "typename", "wchar_t",
                        "struct", "switch", "typedef", "union", "unsigned",
                        "void", "volatile", "while", "reinterpret_cast",
                        "static_cast", "template", "this", "throw",
                        "true", "using", "auto", "break", "case", "char", "const", "continue",
                        "defaullt", "do", "asm", "bool", "catch", "class",
                        "const_cast", "delete", "try", "using", "virtual",
                        "typeid", "mutable", }
    lexemes = []
    strings = {'"'}
    bracket_set = {"{", "}", "(", ")", "[", "]"}
    comments = {"/"}
    comment_end = {"\n"}
    ends = {" ", "\t", "\n"}
    A_operators = {"=", "+", "-", "&", "|", "<", ">", "!"}

    
    # keywords in c++ language
    
    lexemes = []
    partial_lexeme1 = ""
    partial_lexeme2 = ""
    partial_lexeme3 = ""
    partial_lexeme4 = ""

    
    # flags conditions to check operators
    
    bool0 = False
    bool1 = False
    bool2 = True
    bool3 = True
    for char in inputt:
        lexeme = ""
        i = 0
        for data1 in char:
            j = i+1
            if bool0 is True:
                if bool1 is True:
                    bool1 = False
                    continue
                bool0 = False
                continue
            if bool2 is False:
                if data1 not in strings:
                    partial_lexeme3 = partial_lexeme3 + data1
                    i = i+1
                    continue
                else:
                    partial_lexeme3 = partial_lexeme3 + data1
                    lexemes.append(partial_lexeme3)
                    i = i+1
                    bool2 = True
                    partial_lexeme3 = ""
                    continue
            if bool3 is False:
                if data1 not in comment_end:
                    partial_lexeme4 = partial_lexeme4 + data1
                    i = i+1
                    continue
                else:
                    try:
                        if char[i] in comments and char[j] in comments:
                            partial_lexeme4 = partial_lexeme4 + char[j]
                            i = j
                    except IndexError:
                        pass
                    partial_lexeme4 = partial_lexeme4 + data1
                    lexemes.append(partial_lexeme4)
                    i = i+1
                    bool3 = True
                    partial_lexeme4 = ""
                    continue
            if data1 not in separators:
                partial_lexeme1 = partial_lexeme1 + data1
            else:
                lexemes.append(partial_lexeme1)
                partial_lexeme1 = ""
                if data1 not in ends:
                    if data1 in A_operators:
                        partial_lexeme2 = ""
                        partial_lexeme2 = partial_lexeme2 + data1
                        try:
                            if char[i] in A_operators and char[j] in A_operators:
                                partial_lexeme2 = partial_lexeme2 + char[j]
                                i = j
                                bool0 = True
                                if char[j+1] in A_operators:
                                    partial_lexeme2 = partial_lexeme2 + char[j+1]
                                    i = j+1
                                    bool1 = True
                        except IndexError:
                            pass
                        lexemes.append(partial_lexeme2)
                        partial_lexeme2 = ""
                    elif data1 in strings:
                        partial_lexeme3 = ""
                        partial_lexeme3 = partial_lexeme3 + data1
                        bool2 = False
                    elif data1 in comments:
                        partial_lexeme4 = ""
                        partial_lexeme4 = partial_lexeme4 + data1
                        bool3 = False
                    else:
                        lexemes.append(data1)
            i = i+1
    if partial_lexeme2:
        lexemes.append(partial_lexeme2)
    lexemes.append(partial_lexeme1)
    lexemes.append(partial_lexeme3)
    lexemes.append(partial_lexeme4)
    lexemes = list(filter(None, lexemes))

    # reading File 1
    
    fsa1 = open("fsa1.txt", "r")
    FSA1 = []
    for line in fsa1:
        number_strings = line.split()
        numbers = [int(n) for n in number_strings]
        FSA1.append(numbers)
    fsa1.close()

    
    # reading File 2
    
    L1 = [[]]
    L1.append(list(string.ascii_letters))
    L1.append(list(string.digits))
    L1.append(list('_'))
    final_state1 = 1

    fsa2 = open("fsa2.txt", "r")
    FSA2 = []
    for line in fsa2:
        number_strings = line.split()
        numbers = [int(n) for n in number_strings]
        FSA2.append(numbers)
    fsa2.close()

    L2 = [[]]
    L2.append(list(string.digits))
    final_state2 = 0

    
    # reading File 3
    
    fsa3 = open("fsa3.txt", "r")
    FSA3 = []
    for line in fsa3:
        number_strings = line.split()
        numbers = [int(n) for n in number_strings]
        FSA3.append(numbers)
    fsa3.close()

    L3 = [[]]
    L3.append(list(string.digits))
    L3.append(list('.'))
    final_state3 = 3


    # reading File 4
    
    fsa4 = open("fsa4.txt", "r")
    FSA4 = []
    for line in fsa4:
        number_strings = line.split()
        numbers = [int(n) for n in number_strings]
        FSA4.append(numbers)
    fsa4.close()

    str1 = string.printable
    index_1 = 96
    index_2 = 76
    if len(str1) > index_1:
        str1 = str1[0: index_1:] + str1[index_1 + 1::]
    if len(str1) > index_2:
        str1 = str1[0: index_2:] + str1[index_2 + 1::]
    L4 = [[]]
    L4.append(list("/"))
    L4.append(list(str1))
    L4.append(list("\n"))
    final_state4 = 3
    # reading File 5
    fsa5 = open("fsa5.txt", "r")
    FSA5 = []
    for line in fsa5:
        number_strings = line.split()
        numbers = [int(n) for n in number_strings]
        FSA5.append(numbers)
    fsa5.close()

    str2 = string.printable
    index_3 = 63
    if len(str2) > index_3:
        str2 = str2[0: index_3:] + str2[index_3 + 1::]
    L5 = [[]]
    L5.append(list('"'))
    L5.append(list(str2))
    final_state5 = 3

    
    # Writing output file

    output = open("output.txt", "w")
    for char1 in lexemes:
        flag1 = True
        flag2 = True
        flag3 = True
        flag4 = True
        flag5 = True
        state1 = FSA1[0][0]
        state2 = FSA2[0][0]
        state3 = FSA3[0][0]
        state4 = FSA4[0][0]
        state5 = FSA5[0][0]
        for each_symbol in char1:
            # Condition for c++ keyword
            if flag1 is True:
                if each_symbol in [data1 for inside in L1 for data1 in inside]:
                    for inside1 in L1:
                        if each_symbol in inside1:
                            index = L1.index(inside1)
                            state1 = FSA1[state1][index]
                else:
                    flag1 = False
                    state1 = -1
            # Condition for c++  number
            if flag2 is True:
                if each_symbol in [data1 for inside in L2 for data1 in inside]:
                    for inside1 in L2:
                        if each_symbol in inside1:
                            index = L2.index(inside1)
                            state2 = FSA2[state2][index]
                else:
                    flag2 = False
                    state2 = -1
            # Condition for  c++ floating point
            if flag3 is True:
                if each_symbol in [data1 for inside in L3 for data1 in inside]:
                    for inside1 in L3:
                        if each_symbol in inside1:
                            index = L3.index(inside1)
                            state3 = FSA3[state3][index]
                else:
                    flag3 = False
                    state3 = -1
            # Condition for  c++ comment
            if flag4 is True:
                if each_symbol in [data1 for inside in L4 for data1 in inside]:
                    for inside1 in L4:
                        if each_symbol in inside1:
                            index = L4.index(inside1)
                            state4 = FSA4[state4][index]
                else:
                    flag4 = False
                    state4 = -1
            # Condtion  for c++ string
            if flag5 is True:
                if each_symbol in [data1 for inside in L5 for data1 in inside]:
                    for inside1 in L5:
                        if each_symbol in inside1:
                            index = L5.index(inside1)
                            state5 = FSA5[state5][index]
                else:
                    flag5 = False
                    state5 = -1
        if state1 == final_state1:
            if char1 in builtin_keywords:
                print('{:<20s}{:<25s}'.format(char1, "C++ Keyword"))
                output.write(char1+"\t\t C++ Keyword\n")
            else:
                print('{:<20s}{:<25s}'.format(char1, "Identifier"))
                output.write(char1+"\t\t C++ Identifier\n")
        elif state2 == final_state2:
            print('{:<20s}{:<25s}'.format(char1, "C++ Number"))
            output.write(char1+"\t\tC++ Number\n")
        elif state3 == final_state3:
            print('{:<20s}{:<25s}'.format(char1, "Floating Point"))
            output.write(char1+"\t\tC++ Floating Point\n")
        elif state4 == final_state4:
            print('{:<20s}{:<25s}'.format(char1, "C++ Comment"))
            output.write(char1+"\t\tC++ Comment\n")
        elif state5 == final_state5:
            print('{:<20s}{:<25s}'.format(char1, "A user entered String"))
            output.write(char1+"\t\tC++ String\n")
        else:
            if char1 in bracket_set:
                print('{:<20s}{:<25s}'.format(char1, "C++ Bracket"))
                output.write(char1+"\t\tC++ Bracket\n")
            elif char1 == ";":
                print('{:<20s}{:<25s}'.format(char1, "C++ Semi-Colon"))
                output.write(char1+"\t\tC++ Semi-Colon\n")
            elif char1 == ":":
                print('{:<20s}{:<25s}'.format(char1, "C++ Colon"))
                output.write(char1+"\t\tC++ Colon\n")
            else:
                print('{:<20s}{:<25s}'.format(char1, "C++ Operator"))
                output.write(char1+"\t\tC++ Operator\n")

# make a DFA that accepts strings over {a,b,c} such that eveyr substring
# of length 4 has at least one occurence of each letter a,b,c.




# how to make DFA
# hardest part is -  how do i do the transition function
# create a dictionary. key = state_name + inputsymbol  the element is state_name to switch to
# once i have the dictionary, i create an array of state_name 

from sys import stdin
# STATE class
class st:
    def __init__(self,name,accept):
        self.name = name
        self.accept = accept



def main():
    # create the dictionary
    # ("aa",{aa,0}) = state a on input a goes to state aa and the state a is not an accepting state etc...
    transition_mappings=dict([("emptya",st("a",0)),("emptyb",st("b",0)),("emptyc",st("c",0))
        ,("aa",st("aa",0)),("ab",st("ab",0)),("ac",st("ac",0)),("ba",st("ba",0)),("bb",st("bb",0))
        ,("bc",st("bc",0)),("ca",st("ca",0)),("cb",st("cb",0)),("cc",st("cc",0)),("aaa",st("aaa",0))
        ,("aab",st("aab",0)),("aac",st("aac",0)),("aba",st("aba",0)),("abb",st("abb",0)),("abc",st("abc",0))
        ,("aca",st("aca",0)),("acb",st("acb",0)),("acc",st("acc",0)),("baa",st("baa",0)),("bab",st("bab",0))
        ,("bac",st("bac",0)),("bba",st("bba",0)),("bbb",st("bbb",0)),("bbc",st("bbc",0)),("bca",st("bca",0))
        ,("bcb",st("bcb",0)),("bcc",st("bcc",0)),("caa",st("caa",0)),("cab",st("cab",0)),("cac",st("cac",0)),("cba",st("cba",0))
        ,("cbb",st("cbb",0)),("cbc",st("cbc",0)),("cca",st("cca",0)),("ccb",st("ccb",0)),("ccc",st("ccc",0))
        ,("aaaa",st("reject",0)),("aaab",st("reject",0)),("aaac",st("reject",0)),("aaba",st("aba",1))
        ,("aabb",st("abb",1)),("aabc",st("abc",1)),("aaca",st("aca",1)),("aacb",st("acb",1)),("aacc",st("acc",1))
        ,("abaa",st("baa",1)),("abab",st("bab",1)),("abac",st("bac",1)),("abba",st("bba",1)),("abbb",st("bbb",1))
        ,("abbc",st("bbc",1)),("abca",st("bca",1)),("abcb",st("bcb",1)),("abcc",st("bcc",1)),("acaa",st("caa",1))
        ,("acab",st("cab",1)),("acac",st("cac",1)),("acba",st("cba",1)),("acbb",st("cbb",1)),("acbc",st("cbc",1))
        ,("acca",st("cca",1)),("accb",st("ccb",1)),("accc",st("ccc",1)),("baaa",st("aaa",1)),("baab",st("aab",1))
        ,("baac",st("aac",1)),("baba",st("aba",1)),("babb",st("abb",1)),("babc",st("abc",1)),("baca",st("aca",1))
        ,("bacb",st("acb",1)),("bacc",st("acc",1)),("bbaa",st("baa",1)),("bbab",st("bab",1)),("bbac",st("bac",1))
        ,("bbba",st("reject",0)),("bbbb",st("reject",0)),("bbbc",st("reject",0)),("bbca",st("bca",1)),("bbcb",st("bcb",1))
        ,("bbcc",st("bcc",1)),("bcaa",st("caa",1)),("bcab",st("cab",1)),("bcac",st("cac",1)),("bcba",st("cba",1))
        ,("bcbb",st("cbb",1)),("bcbc",st("cbc",1)),("bcca",st("cca",1)),("bccb",st("ccb",1)),("bccc",st("ccc",1))
        ,("caaa",st("aaa",1)),("caab",st("aab",1)),("caac",st("aac",1)),("caba",st("aba",1)),("cabb",st("abb",1))
        ,("cabc",st("abc",1)),("caca",st("aca",1)),("cacb",st("acb",1)),("cacc",st("acc",1)),("cbaa",st("baa",1))
        ,("cbab",st("bab",1)),("cbac",st("bac",1)),("cbba",st("bba",1)),("cbbb",st("bbb",1)),("cbbc",st("bbc",1))
        ,("cbca",st("bca",1)),("cbcb",st("bcb",1)),("cbcc",st("bcc",1)),("ccaa",st("caa",1)),("ccab",st("cab",1))
        ,("ccac",st("cac",1)),("ccba",st("cba",1)),("ccbb",st("cbb",1)),("ccbc",st("cbc",1)),("ccca",st("reject",1))
        ,("cccb",st("reject",0)),("cccc",st("reject",0)),("rejecta",st("reject",0)),("rejectb",st("reject",0))
        ,("rejectc",st("rejectc",0))
        
        ])


    curr = "empty"#keeps track of prev 3 symbols
    state = 0 # will hold the final state
    for line in stdin:
        for n in line.strip():
            #n = next input symbol
            print(n)
            state = transition_mappings[curr+n.rstrip()]
            curr = state.name
        break

    print("final state: ",state.name)

    




main()



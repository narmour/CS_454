# make a DFA that accepts strings over {a,b,c} such that eveyr substring
# of length 4 has at least one occurence of each letter a,b,c.




# how to make DFA
# hardest part is -  how do i do the transition function
# create a dictionary. key = state_name + inputsymbol  the element is state_name to switch to
# once i have the dictionary, i create an array of state_name 

from sys import stdin
import numpy as np
# STATE class
class st:
    def __init__(self,name,accept):
        self.name = name
        self.accept = accept


#def build_dfa(K,S):



def main():
    w = int(input("size: "))
    # create the dictionary
    # ("aa",{aa,0}) = state a on input a goes to state aa and the state a is not an accepting state etc...
    transition_mappings=dict([("empty",st("empty",0)),("emptya",st("a",0)),("emptyb",st("b",0)),("emptyc",st("c",0))
        ,("aa",st("aa",0)),("ab",st("ab",0)),("ac",st("ac",0)),("ba",st("ba",0)),("bb",st("bb",0))
        ,("bc",st("bc",0)),("ca",st("ca",0)),("cb",st("cb",0)),("cc",st("cc",0)),("aaa",st("reject",0))
        ,("aab",st("aab",0)),("aac",st("aac",0)),("aba",st("aba",0)),("abb",st("abb",0)),("abc",st("abc",0))
        ,("aca",st("aca",0)),("acb",st("acb",0)),("acc",st("acc",0)),("baa",st("baa",0)),("bab",st("bab",0))
        ,("bac",st("bac",0)),("bba",st("bba",0)),("bbb",st("reject",0)),("bbc",st("bbc",0)),("bca",st("bca",0))
        ,("bcb",st("bcb",0)),("bcc",st("bcc",0)),("caa",st("caa",0)),("cab",st("cab",0)),("cac",st("cac",0)),("cba",st("cba",0))
        ,("cbb",st("cbb",0)),("cbc",st("cbc",0)),("cca",st("cca",0)),("ccb",st("ccb",0)),("ccc",st("reject",0))
        ,("aaaa",st("reject",0)),("aaab",st("reject",0)),("aaac",st("reject",0)),("aaba",st("reject",0))
        ,("aabb",st("reject",0)),("aabc",st("abc",1)),("aaca",st("reject",0)),("aacb",st("acb",1)),("aacc",st("reject",0))
        ,("abaa",st("reject",0)),("abab",st("reject",0)),("abac",st("bac",1)),("abba",st("reject",0)),("abbb",st("reject",0))
        ,("abbc",st("bbc",1)),("abca",st("bca",1)),("abcb",st("bcb",1)),("abcc",st("bcc",1)),("acaa",st("reject",0))
        ,("acab",st("cab",1)),("acac",st("reject",0)),("acba",st("cba",1)),("acbb",st("cbb",1)),("acbc",st("cbc",1))
        ,("acca",st("reject",0)),("accb",st("ccb",1)),("accc",st("reject",0)),("baaa",st("reject",0)),("baab",st("reject",0))
        ,("baac",st("aac",1)),("baba",st("reject",0)),("babb",st("reject",0)),("babc",st("abc",1)),("baca",st("aca",1))
        ,("bacb",st("acb",1)),("bacc",st("acc",1)),("bbaa",st("reject",0)),("bbab",st("reject",0)),("bbac",st("bac",1))
        ,("bbba",st("reject",0)),("bbbb",st("reject",0)),("bbbc",st("reject",0)),("bbca",st("bca",1)),("bbcb",st("reject",0))
        ,("bbcc",st("reject",0)),("bcaa",st("caa",1)),("bcab",st("cab",1)),("bcac",st("cac",1)),("bcba",st("cba",1))
        ,("bcbb",st("reject",0)),("bcbc",st("reject",0)),("bcca",st("cca",1)),("bccb",st("reject",0)),("bccc",st("reject",0))
        ,("caaa",st("reject",0)),("caab",st("aab",1)),("caac",st("reject",0)),("caba",st("aba",1)),("cabb",st("abb",1))
        ,("cabc",st("abc",1)),("caca",st("reject",0)),("cacb",st("acb",1)),("cacc",st("reject",0)),("cbaa",st("baa",1))
        ,("cbab",st("bab",1)),("cbac",st("bac",1)),("cbba",st("bba",1)),("cbbb",st("reject",0)),("cbbc",st("reject",0))
        ,("cbca",st("bca",1)),("cbcb",st("reject",0)),("cbcc",st("reject",0)),("ccaa",st("reject",0)),("ccab",st("cab",1))
        ,("ccac",st("reject",0)),("ccba",st("cba",1)),("ccbb",st("reject",0)),("ccbc",st("reject",0)),("ccca",st("reject",0))
        ,("cccb",st("reject",0)),("cccc",st("reject",0)),("rejecta",st("reject",0)),("rejectb",st("reject",0))
        ,("rejectc",st("reject",0))
        
        ])

    #set comprehension since i only want the unique states in my dfa
    states = list({state.name for name,state in transition_mappings.items() if state.name not in ["aaa","bbb","ccc","rejecta","rejectb","rejectc"]})

    # create transition matrix
    # i know this can be done in a simple list comprehension
    transition_matrix = []
    for i_state in states:
        transition_matrix.append([])
        for j_state in states:
            row = transition_matrix[-1]
            count = 0
            for c in ['a','b','c']:
                if transition_mappings[i_state+c].name == j_state:
                    count = count +1
            row.append(count)

    for row in transition_matrix:
        print(row)



    # create start_matrix
    # TODO: list comprehension
    start_vector = []
    for state in states:
        if state =="empty":
            start_vector.append(1)
        else:
            start_vector.append(0)

    # create final_vector
    # this should also be a list comprehension
    final_vector = []
    count = 0
    for state in states:
        final = 0
        for c in ['a','b','c']:
            if(transition_mappings[state+c].accept):
                final =1
        if(final):
            final_vector.append(1)
            print(state)
            count = count +1
        else:
            final_vector.append(0)

    print("FINAL STATES: ",count)
    

    
    x = np.dot(np.array(start_vector,dtype=object),np.linalg.matrix_power(np.array(transition_matrix,dtype=object),w))

    print(np.dot(x,np.array(final_vector)))

    #print(type(np.dot(np.array(start_vector),np.linalg.matrix_power(np.array(transition_matrix),10))))
    #print(np.linalg.matrix_power(np.array(transition_matrix),5).dot(np.array(start_vector).dot(np.array(final_vector))))
    #power_matrix = np.linalg.matrix_power(np.array(transition_matrix),5)
    #power_matrix = np.power(np.array(transition_matrix),5)
    #print(power_matrix)
    #curr = "empty"#keeps track of prev 3 symbols
    #state = 0 # will hold the final state
    #for line in stdin:
    #    for n in line.strip():
    #        #n = next input symbol
    #        print(n)
    #        state = transition_mappings[curr+n.rstrip()]
    #        curr = state.name
    #    break

    #print("final state: ",state.name)




main()



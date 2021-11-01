# 1. Min, Avg, Max

def get_min_avg_max(sequence):
  sum=0
  lenlist=0
  for val in sequence:
    sum=int(val)+sum
    lenlist = lenlist +1
  avg=sum/lenlist
  return min(sequence),avg,max(sequence)
print(get_min_avg_max([0,10,1,9]))

#2. Common Elements

def get_common_elements(seq1, seq2, seq3):
  A=set(seq1)
  B=set(seq2)
  C=set(seq3)
  return tuple(set.intersection(A, B, C))
print(get_common_elements("abc", ['a', 'b'], ('b', 'c')))


#3.Is there a pangram?
import string
def ispangram(str1, alphabet=string.ascii_lowercase):
  alphaset = set(alphabet)
  return alphaset <= set(str1.lower())


print(ispangram('The five boxing wizards jump quickly'))
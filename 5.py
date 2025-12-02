class stringreverser():
  def reverser(self,input_string):
    word=input_string.split()
    reversed_words= word[::-1]
    reversed_string="".join(reversed_words)
    return reversed_string
  
if __name__=="__main__":
  inputstrings="you love i "
  reverser=stringreverser()
  reversed_result=reverser.reverser(inputstrings)
  print("Orginal",inputstrings)
  print("reversed",reversed_result)
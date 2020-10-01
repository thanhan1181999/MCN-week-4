class PrefixCodeTree:
  def __init__(self):
    # setting binary tree by array
    self.tree = [0]*1000

  def insert(self,codeword,symbol):
    #find index of codeword
    index=0
    for element in codeword:
      if element == 1: 
        index = index * 2 + 2
      elif element == 0:
        index = index * 2 + 1
    #assign symbol into tree[index]
    self.tree[index]=symbol

  def decode(self,encodedData, datalen):
    # initial value
    result=""
    index=0
    # convert encodedData
    data=""
    for byte in encodedData:
      data += f'{byte:0>8b}'
    #start decode
    for i in range(datalen):
      char = data[i]
      if char == '1': 
        index = index * 2 + 2
      elif char == '0':
        index = index * 2 + 1
      #if find a symbol, add to result, go to root of tree
      if self.tree[index] != 0:
        result += " " + self.tree[index]
        index=0 
    return result
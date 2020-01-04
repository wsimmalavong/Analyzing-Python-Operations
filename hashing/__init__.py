class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size


    def put(self,key,data):
      

      items = 0
      for i in range (self.size - 1):
          if self.slots[i] != None:
              items = items + 1
      loadingFactor = items/self.size
    
      if (loadingFactor >= 0.7): 

        oldSlots = self.slots
        oldData = self.data
        self.size = self.size * 2
        self.slots = [None] * self.size
        self.data = [None] * self.size

        
        for i in range (len(oldSlots)):
          if (oldSlots[i] != None):
              hashvalue = self.hashfunction(oldSlots[i],len(self.slots))
              if self.slots[hashvalue] == None:
                self.slots[hashvalue] = oldSlots[i]
                self.data[hashvalue] = oldData[i]
              else:
                if self.slots[hashvalue] == key:
                  self.data[hashvalue] = data  #replace
                else:
                  nextslot = self.rehash(hashvalue,len(self.slots))
                  while self.slots[nextslot] != None and \
                                  self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))

                  if self.slots[nextslot] == None:
                    self.slots[nextslot]=oldSlots[i]
                    self.data[nextslot]=oldData[i]
                  else:
                    self.data[nextslot] = oldData[i] #replace
                    
                    
      hashvalue = self.hashfunction(key,len(self.slots))

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
      else:
        if self.slots[hashvalue] == key:
          self.data[hashvalue] = data  #replace
        else:
          nextslot = self.rehash(hashvalue,len(self.slots))
          while self.slots[nextslot] != None and \
                          self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot,len(self.slots))

          if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
          else:
            self.data[nextslot] = data #replace

    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
      startslot = self.hashfunction(key,len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and  \
                           not found and not stop:
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position=self.rehash(position,len(self.slots))
           if position == startslot:
               stop = True
      return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)






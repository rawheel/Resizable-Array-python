class resizable_array:
    def __init__(self,arraysize):
        self.arraysize = arraysize
        self.array = [None for i in range(self.arraysize)]
        self.temp =1
    def __insert(self,value):

        for i in range(len(self.array)):

            if self.array[i] == None:
                self.array[i] = value
                break

        print(self.array)
        return self.array


    def insertatend(self,value):

        if None not in self.array :
            self.newsize= self.temp+len(self.array)
            self.newarray = [None for i in range(self.newsize)]
            for i in range(len(self.array)):
                self.newarray[i]=self.array[i]
                # temp contains value of i
                i_temp=i

            self.newarray[i_temp+1]=value
            self.array = self.newarray
            self.newarray = None
            print(self.array)
            return self.array
        else:
            self.__insert(value)
            #print("there are None values in array call insert function to fill them!")

    def insert_first(self,value):
        self.create_new_size = len(self.array)+1
        self.create_new_size = ['insert' for i in range(self.create_new_size)]
        self.create_new_size[0] = value
        n = len(self.array)
        for i in range(1,n+1):
            self.create_new_size[i] = self.array[i-1]
        self.array = self.create_new_size
        self.create_new_size = None
        print(self.array)
        return self.array

    def deleteatend(self):
        if len(self.array) == 0:
            print("Array is empty")
        else:
            self.newsize = len(self.array)-1
            self.newarray = [None for i in range(self.newsize)]
            for i in range(len(self.array)-1):

                self.newarray[i] = self.array[i]
            self.array=self.newarray
            print(self.array)
            return(self.array)

    def Delete_First(self):
        if len(self.array) == 0:
            print('Array is empty')
        else:
            self.create_new_size = len(self.array) - 1
            self.newarray = ['insert' for i in range(self.create_new_size)]
            n = len(self.newarray)
            for i in range(0,n):
                self.newarray[i] = self.array[i+1]
            self.array = self.newarray
            self.newarray = None
            print(self.array)
            return self.array

ob1= resizable_array(2)
print("insert at end:")
ob1.insertatend(5)
ob1.insertatend(6)
ob1.insertatend(7)
ob1.insertatend(8)
print("delete at end:")
ob1.deleteatend()
print('insert at first:')
ob1.insert_first(4)
ob1.insert_first(3)
ob1.insert_first(2)
ob1.insert_first(1)
print('delete at first:')
ob1.Delete_First()
ob1.Delete_First()
ob1.Delete_First()
ob1.Delete_First()

# Sum Of list with size N 
class solutions:
    def list_sum(self,N,weights):
        i=0
        sum_of_list=0
        while i<N:
            sum_of_list=sum_of_list+weights[i]
            i=i+1;
        return sum_of_list
a=[]
n=int(input("Enter the size of list"))
for i in range(0,n):
      element=int(input())
      a.append(element)

a1=solutions()
a1.list_sum(n,a)
            
        
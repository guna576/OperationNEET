
def function6(t,d):
    ans=1
    for k,v in zip(t,d):
        cur=k+1
        val=v
        
        start=1
        end=k//2
        cur=k-1
        while(start<=end):
            mid=(start+end)//2
            dist=(k-mid)*mid
           # print(dist,mid,k)
            if val<dist:
                
                end=mid-1
            else:
                start=mid+1
        
        
        cur=cur-2*end
        if cur!=0:
            
            ans*=(cur)

    return ans



if __name__=="__main__":
    with open("input.txt","r") as f:
        line=f.readline()
        times=list(map(int,line.strip().split(":")[-1].split()))
        line1=f.readline()
        distance=list(map(int,line1.strip().split(":")[-1].split()))
        print(function6(times,distance))
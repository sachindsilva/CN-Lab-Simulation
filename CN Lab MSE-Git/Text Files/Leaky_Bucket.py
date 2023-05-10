import time

n=int(input("Enter the number of packets :"))

packets=[]

for i in range(1,n+1):
    size=int(input(f"Enter the packet {i} size : "))
    arr_time=int(input(f"Enter the arrival time of packet {i} :"))
    packets.append((size,arr_time))

bucket_capacity=int(input("Enter the Bucket Capacity :"))

output_rate=int(input("Enter the output rate :"))

t=0
dt=2
bucket_current_capacity=0

while(len(packets)>0 or bucket_current_capacity>0):
    print("Time : ",t)
    packets_at_t=[p for p in packets if p[1]==t]
    packets=[p for p in packets if p not in packets_at_t]
    
    
    for p in packets_at_t:
        if p[0]>bucket_capacity:
            print(f"Packet {p[0]} cannot be entered..")
        elif((p[0]+bucket_current_capacity)>bucket_capacity):
            print(f"Packet {p[0]} arrived but bucket overflow")
        else:
            print(f"Packet {p[0]} queued...")
            bucket_current_capacity+=p[0]
    
    if(t%dt==0):
        if(bucket_capacity>output_rate):
            print(output_rate," bytes terminated..")
            bucket_current_capacity-=output_rate
        else:
            print(bucket_current_capacity," bytes terminated..")
            bucket_current_capacity=0
    
    print("Free space in bucket is ",bucket_capacity-bucket_current_capacity)

    t+=1
    time.sleep(1)
            

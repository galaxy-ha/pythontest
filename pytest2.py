import time
lower=0
upper=input()
start_time = time.time()
count = 0
print("prime numbers between", lower,"and", upper, "are:")
for num in range (lower, upper+1):
 if num>1:
  for i in range (2,num):
   if num % i==0:
    break
  else: 
    count += 1
print ( "count_prime:", count )
print("--- %s seconds ---" % (time.time() - start_time))

A = list(map(int, input().split()))
leaders = [A[-1]]
max_element = A[-1]

for i in range(len(A) - 2, -1, -1):
    if A[i] > max_element:
        leaders.append(A[i])
        max_element = A[i]

leaders.reverse() 
print(leaders)


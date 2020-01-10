arr = [1, 2, 1, 2, 3, 4, 5, 3, 4, 5, 99]
if len(arr) % 2 == 0:
    print("Numero par de elementos!")

# Enche o array com 'false'. Pressupoe-se que todos são únicos a priori
# preenche a lista espelho com o mesmo tamanho do input
mirror = [False for item in range(0, len(arr))]

index = 0
for i in arr:
    for j in len(arr):
        if j != index and arr[i] == arr[j] and mirror[index] == False:
            mirror[index] = True
index += 1

for j in len(mirror):

    if mirror[j] == False:
        print(arr[j])
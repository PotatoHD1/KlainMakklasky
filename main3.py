N = int(input("Введите N: "))
k1 = (N + 173) % 48 + 1
k2 = (N + 173) % 8
k3 = (N + 111) % 8
k4 = (N * 97) % 256
k6 = (N + 11) % 6 + 1
k7 = (N * 11) % 6 + 1
print(f" k1 = {k1}\r\n k2 = {k2}, k3 = {k3}\r\n k4 = {k4}, {[i for i in range(8) if str(bin(k4))[2:][::-1][i] == '1']}\r\n k6 = {k6}, k7 = {k7}")
import os
os.system("clear")
st = 'hi'
sizec = int(os.get_terminal_size(0).columns / 2)
sizel = int(os.get_terminal_size(0).lines / 2)
for _ in range(sizel):
    print()
print(st.center(sizec))
for _ in range(sizel):
    print()

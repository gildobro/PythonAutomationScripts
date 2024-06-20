from pathlib import Path

p1 = Path('files/ghi.txt')

if not p1.exists():
    with open(p1, 'a') as file:
        file.write('content 3')


print(p1.name)
print(p1.stem)
print(p1.suffix)

p2 = Path('files')
print(list(p2.iterdir()))
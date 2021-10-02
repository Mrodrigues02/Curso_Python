linguagens = ('Rust', 'Typescript','Python','Kotlin','Goo','Julia','Dart','C#','Swift','JavaScript')
print('Top 10 das linguagens de programação mais amadas de 2020:')
print('(Segundo o Stack Overflow)')
for i in range(0, len(linguagens), 1):
    print(i + 1, ' - ', linguagens[i])

print('\nTOP 3:',linguagens[:3])
print('Últimos 5:',linguagens[-5:])
i = 0
while (linguagens[i] != 'python'):
   i += 1
print('Encontramos Python na {} posição"'.format(i + 1))

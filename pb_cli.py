X = 10000

for i in range(X):
    print(
        'Progress: ',
        f'|{"█" * ((i + 1) * 50 // X):50}|',
        f'{(i + 1) * 100 // X}%',
        end='\r'
    )
print('\nFinished!')

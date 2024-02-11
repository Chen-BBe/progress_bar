from progress.bar import Bar

X = 10000
with Bar('', max=X, fill='😊', suffix='%(percent).1f%% - %(eta)ds') as bar:
    for i in range(X):
        for j in range(X):
            k = j * i
        bar.next()
print('\nFinished!')

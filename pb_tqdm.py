from time import sleep
from tqdm import trange, tqdm
# from tqdm.tk import trange
# from tqdm.rich import trange

for i in trange(50, desc ="Start: "):
    sleep(.1)
print('done')

bar = tqdm(total=100)
bar.set_description('step-1')
sleep(0.5)
bar.update(25)
bar.set_description('step-2')
sleep(0.5)
bar.update(25)
bar.set_description('step-3')
sleep(0.5)
bar.update(25)
bar.set_description('step-4')
sleep(0.5)
bar.update(24)
bar.set_description('finalize')
sleep(0.5)
bar.update(1)
bar.close()
print('done')
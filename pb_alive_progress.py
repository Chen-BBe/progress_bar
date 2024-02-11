from alive_progress import alive_bar; import time, logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('alive_progress')

with alive_bar(1000) as bar:
    for i in range(1000):
        if i and i % 300 == 0:
            print('found it')
        if i in (301, 302):
            logger.info('cool')
        if i == 500:
            logger.warning('half done')            
        time.sleep(0.01)
        bar()
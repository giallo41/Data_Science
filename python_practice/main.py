import logging
import time

logging.basicConfig(level = logging.INFO, 
                    format='%(levelname)s : %(asctime)s : %(filename)s Line : %(lineno)d - %(message)s')

def main():

    empty_list = []
    for i in range(10000000):
        empty_list.append(i)

if __name__=="__main__":
    start_prog_tm = time.time()
    main()
    logging.info("Total running time : {:.2f}s".format(time.time() - start_prog_tm))
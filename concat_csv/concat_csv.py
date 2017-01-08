import csv, sys
import logging
from logging import handlers

LOG_FILENAME = "/var/log/ftp_ingestion.log"

# logging.getLogger('').setLevel(logging.DEBUG)
format = "%(asctime)s : %(name)-4s : %(levelname)-4s : %(message)s"
handler = logging.handlers.RotatingFileHandler(
                  LOG_FILENAME, maxBytes=100000, backupCount=10)
handler.setFormatter(logging.Formatter(format))
logger = logging.getLogger('ftp_ingestion')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

def main(file1, file2):
    with open(file1, 'r') as f:
        r = csv.reader(f, delimiter=',')
        file_1 = []
        for i in r:
            file_1.append(i)

    with open(file2, 'r') as f:
        r = csv.reader(f, delimiter=',')
        file_2 = []
        for i in r:
            file_2.append(i)

    concat_list = []

    if len(file_1) >= len(file_2):
        for i in range(0, len(file_1)):
            try:
                x = file_1[i]
                y = file_2[i]
                concat_list.append(x + y)
            except IndexError:
                concat_list.append(file_1[i])
    else:
        for i in range(0, len(file_2)):
            try:
                x = file_2[i]
                y = file_1[i]
                concat_list.append(x + y)
            except IndexError:
                concat_list.append(file_2[i])
    return concat_list

def write_to_csv(main_func, output_file_name):
    for i in main_func:
        with open(output_file_name, 'ab') as f:
            wr =  csv.writer(f, delimiter=',')
            wr.writerow(i)

if __name__ == '__main__':
    write_to_csv(main(sys.argv[1], sys.argv[2]), sys.argv[3])
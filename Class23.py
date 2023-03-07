import logging
logging.basicConfig(filename='sample1.log',format='%(asctime)s %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
try:
    logger.info("I enterred into calculation")
    1/0
    name = None
    name.upper()
except ZeroDivisionError as ex:
    logger.debug("Division caluclated with 0")
    print("Division caluclated with 0")
except Exception as ex:
    print(ex)
    logger.debug(ex)
    logger.debug("error occured in calculation")

#
l1 = ['c','h','a','n','d','r','a']
temp = ''.join(l1)
print(temp)

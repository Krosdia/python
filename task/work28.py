import traceback
import logging
from logging.handlers import TimedRotatingFileHandler
def logger(func):
 def inner(*args, **kwargs): 
 try:
  print "Arguments were: %s, %s" % (args, kwargs)
  func(*args, **kwargs) 
 except:
  print 'error',traceback.format_exc()
  print 'error'
 return inner
 
 
def loggerInFile(filename)
 def decorator(func):
 def inner(*args, **kwargs): 
  logFilePath = filename 
  logger = logging.getLogger()
  logger.setLevel(logging.INFO)
  handler = TimedRotatingFileHandler(logFilePath,
       when="d",
       interval=1,
       backupCount=5)
  formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
  handler.setFormatter(formatter)
  logger.addHandler(handler)
  try:
  print "Arguments were: %s, %s" % (args, kwargs)
  result = func(*args, **kwargs) 
  logger.info(result)
  except:
  logger.error(traceback.format_exc())
 return inner
 return decorator
 
@logger
def test():
 print 2/0
 
test()
 
 
@loggerInFile('newloglog')
def test2(n):
 print 100/n
 
test2(10)
test2(0)
print 'end'

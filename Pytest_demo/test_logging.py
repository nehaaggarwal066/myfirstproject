import inspect
import logging
import pytest

class logger_for_reporting:
  def test_loggingdemo():
    #loggername = inspect.stack()[1][3] # this is added because when this method will be called from child class so it take name of child and not parent class
    logger = logging.getLogger(__name__) # (__name__) if we use this it will take always parent class name
    filehandler_obj = logging.FileHandler("logfile.log")
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)")
    #asctime- will give time when error occured
    #level will give level name like DEBUG, ERROR,WARNING etc
    #name is folder_name_filename where your test is
    #message it prints the message given inside these functions.( error or info or debug or critical or warning)
    filehandler_obj.setFormatter(formatter)  #Formatter obj
    logger = logger.addHandler(filehandler_obj)  # pass filehandler object
    logger.setlevel(logging.INFO)
    # this is the hierarchy but if we want only warning error and critical then we need to set level as Warning,
    #warning and below warning all logs will be displayed

    #use below method inside the tests to put the details
    #below is the hierarchy(DIWEC)
    #logger.debug()
    logger.info("HIIIIIIIIIIIIIIIIIi")
    #logger.warning()
    #logger.error()
    #logger.critical()




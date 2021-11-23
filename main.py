
#importing packages
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.sql import SparkSession
from excelToJson import ExcelToJson
#from lib.logger import Log4j
#import log4j.properties
import logging as lg

if __name__ == '__main__':
    #Spark sessions set up
    conf = SparkConf().setAppName('Data Quality Check')
    sc = SparkContext(conf=conf)
    spark = SparkSession.builder.appName('DQCheck').getOrCreate()
    lg.basicConfig(level = lg.INFO)
    #logger = Log4j(spark)

    #Setting logger information
    #logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%y %I:%M:%S', level=logging.INFO)
    #log = logging.getLogger(__name__)
    lg.info("Starting Main Function.......")

    #reading excel sheet with parameters, checking rules and processing respective functions
    d1 = ExcelToJson()
    try:
        sourceDataPath = d1.sourceInputsToJson()
        try:
            with open(sourceDataPath, 'r') as f:
                sourceData = spark.read.option("header", True).csv(sourceDataPath)
                d1.readRule(sourceData)
        except FileNotFoundError:
            print("Data file not found!!!")
    finally:
        sc.stop()





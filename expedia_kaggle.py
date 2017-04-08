from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark.sql import SparkSession

# fw = open('result.csv', 'w')

def createDF():

	sc =SparkContext()
	sqlContext = SQLContext(sc)

	spark = SparkSession.builder\
		.appName("BigData_project")\
		.getOrCreate()

	df = spark.read.csv("/Users/sf/Documents/BigData_DS/project/data/s.csv", header=True, mode="FAILFAST")
	print df.printSchema()
	return df


def processData():




def main():
	df = createDF()
	processData(df)


if __name__ == '__main__':
	main()
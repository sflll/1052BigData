# from pyspark.sql import SQLContext
# from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegression
from pyspark.mllib.classification import LogisticRegressionWithLBFGS

# fw = open('result.csv', 'w')

def createDF():

	# sc =SparkContext()
	# sqlContext = SQLContext(sc)

	spark = SparkSession.builder\
		.appName("BigData_project")\
		.getOrCreate()

	df = spark.read.csv("/Users/sf/Documents/BigData_DS/project/data/s.csv", header=True, mode="FAILFAST")
	# print df.printSchema()
	return df


def processData(df):
	# replace NULL with 0
	new_df = df.na.replace('NULL', '0')

	# remove unused row for training
	new_df = df.drop('date_time').drop("click_bool").drop("booking_bool").drop("gross_bookings_usd").drop("position")

	return new_df


def models_predict():
	# some model selection here and return predict value
	return 0


def main():
	df = createDF()
	data = processData(df)
	# print data.head()
	
	# Split data into training (60%) and test (40%)
	training, test = data.randomSplit([0.6, 0.4], seed=11)
 	training.cache()

 	model = LogisticRegressionWithLBFGS.train(training, numClasses=3)


 # 	lr = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)
	# # Fit the model
	# lrModel = lr.fit(training)

	# # Print the coefficients and intercept for logistic regression
	# print("Coefficients: " + str(lrModel.coefficients))
	# print("Intercept: " + str(lrModel.intercept))


if __name__ == '__main__':
	main()
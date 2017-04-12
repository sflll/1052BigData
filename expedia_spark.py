# from pyspark.sql import SQLContext
# from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegression
from pyspark.mllib.classification import LogisticRegressionWithLBFGS
from pyspark.sql.types import DoubleType

from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler

# fw = open('result.csv', 'w')

def createDF():

	# sc =SparkContext()
	# sqlContext = SQLContext(sc)

	spark = SparkSession.builder\
		.appName("BigData_project")\
		.getOrCreate()

	df = spark.read.csv("/Users/sf/Documents/BigData_DS/project/data/s.csv", header=True, 
		mode="FAILFAST", inferSchema=True)
	# print df.printSchema()
	return df


def processData(df):
	# replace NULL with 0
	new_df = df.na.replace('NULL', '0')
	# print new_df.head()

	new_df = new_df.withColumn('gross_bookings_usd', new_df['gross_bookings_usd'].cast(DoubleType()))

	# remove unused row for training
	new_df = new_df.drop('date_time').drop('position')
	new_df = new_df.withColumnRenamed('booking_bool', 'label')

	# new_df.drop("click_bool").drop("booking_bool").drop("gross_bookings_usd")
	
	new_df = new_df.withColumn('visitor_hist_starrating', new_df['visitor_hist_starrating'].cast(DoubleType()))
	new_df = new_df.withColumn('visitor_hist_adr_usd', new_df['visitor_hist_adr_usd'].cast(DoubleType()))
	new_df = new_df.withColumn('prop_review_score', new_df['prop_review_score'].cast(DoubleType()))
	new_df = new_df.withColumn('prop_location_score2', new_df['prop_location_score2'].cast(DoubleType()))
	new_df = new_df.withColumn('srch_query_affinity_score', new_df['srch_query_affinity_score'].cast(DoubleType()))
	new_df = new_df.withColumn('orig_destination_distance', new_df['orig_destination_distance'].cast(DoubleType()))
	
	new_df = new_df.withColumn('comp1_rate', new_df['comp1_rate'].cast(DoubleType()))
	new_df = new_df.withColumn('comp1_inv', new_df['comp1_inv'].cast(DoubleType()))
	new_df = new_df.withColumn('comp1_rate_percent_diff', new_df['comp1_rate_percent_diff'].cast(DoubleType()))

	new_df = new_df.withColumn('comp2_rate', new_df['comp2_rate'].cast(DoubleType()))
	new_df = new_df.withColumn('comp2_inv', new_df['comp2_inv'].cast(DoubleType()))
	new_df = new_df.withColumn('comp2_rate_percent_diff', new_df['comp2_rate_percent_diff'].cast(DoubleType()))

	new_df = new_df.withColumn('comp3_rate', new_df['comp3_rate'].cast(DoubleType()))
	new_df = new_df.withColumn('comp3_inv', new_df['comp3_inv'].cast(DoubleType()))
	new_df = new_df.withColumn('comp3_rate_percent_diff', new_df['comp3_rate_percent_diff'].cast(DoubleType()))

	new_df = new_df.withColumn('comp4_rate', new_df['comp4_rate'].cast(DoubleType()))
	new_df = new_df.withColumn('comp4_inv', new_df['comp4_inv'].cast(DoubleType()))
	new_df = new_df.withColumn('comp4_rate_percent_diff', new_df['comp4_rate_percent_diff'].cast(DoubleType()))

	new_df = new_df.withColumn('comp5_rate', new_df['comp5_rate'].cast(DoubleType()))
	new_df = new_df.withColumn('comp5_inv', new_df['comp5_inv'].cast(DoubleType()))
	new_df = new_df.withColumn('comp5_rate_percent_diff', new_df['comp5_rate_percent_diff'].cast(DoubleType()))

	new_df = new_df.withColumn('comp6_rate', new_df['comp6_rate'].cast(DoubleType()))
	new_df = new_df.withColumn('comp6_inv', new_df['comp6_inv'].cast(DoubleType()))
	new_df = new_df.withColumn('comp6_rate_percent_diff', new_df['comp6_rate_percent_diff'].cast(DoubleType()))

	new_df = new_df.withColumn('comp7_rate', new_df['comp7_rate'].cast(DoubleType()))
	new_df = new_df.withColumn('comp7_inv', new_df['comp7_inv'].cast(DoubleType()))
	new_df = new_df.withColumn('comp7_rate_percent_diff', new_df['comp7_rate_percent_diff'].cast(DoubleType()))

	new_df = new_df.withColumn('comp8_rate', new_df['comp8_rate'].cast(DoubleType()))
	new_df = new_df.withColumn('comp8_inv', new_df['comp8_inv'].cast(DoubleType()))
	new_df = new_df.withColumn('comp8_rate_percent_diff', new_df['comp8_rate_percent_diff'].cast(DoubleType()))

	# print new_df.columns[:-3]
	assembler = VectorAssembler(inputCols=new_df.columns[:-3], outputCol="features")
	new_df = assembler.transform(new_df).select('features', 'label')
	# print new_df.columns
	return new_df


def models_predict():
	# some model selection here and return predict value
	return 0


def main():
	df = createDF()
	data = processData(df)
	print data.printSchema()	
	print data.head()
	
	# Split data into training (60%) and test (40%)
	training, test = data.randomSplit([0.8, 0.2], seed=11)
 	training.cache()

 	# model = LogisticRegressionWithLBFGS.train(training, numClasses=3)
 	# print model

 	lr = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)
	# Fit the model
	lrModel = lr.fit(training)
	prediction = lrModel.transform(test)
	print prediction.select("prediction", "label", "features").show(5)
	# Print the coefficients and intercept for logistic regression
	# print("Coefficients: " + str(lrModel.coefficients))
	# print("Intercept: " + str(lrModel.intercept))


if __name__ == '__main__':
	main()
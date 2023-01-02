from pyspark.ml import Pipeline
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Linear Regression") \
    .getOrCreate()

# Load the data into a Spark DataFrame
data = spark.read.csv("dataset/winequality-red.csv", header=True, inferSchema=True)

train, test, validation = data.randomSplit([0.7, 0.2, 0.1])

assembler = VectorAssembler(inputCols=["sulphates", "pH", "volatile acidity"], outputCol="Input Attributes")

lr = LinearRegression(labelCol="quality", featuresCol="Input Attributes")

pipeline = Pipeline(stages=[assembler, lr])

model = pipeline.fit(train)

test_predictions = model.transform(test)
validation_predictions = model.transform(validation)

test_predictions = test_predictions.withColumn("prediction", test_predictions.quality.cast('double'))
validation_predictions = validation_predictions.withColumn("prediction", validation_predictions.quality.cast('double'))


evaluator = MulticlassClassificationEvaluator(labelCol="quality", metricName="accuracy")

test_accuracy = evaluator.evaluate(test_predictions)

validation_accuracy = evaluator.evaluate(validation_predictions)

print(f"Test Accuracy: {test_accuracy:.2f}")
print(f"Validation Accuracy: {validation_accuracy:.2f}")

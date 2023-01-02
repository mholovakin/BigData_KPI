# Linear regression using PySpark

## Run the component

To run locally in a terminal, you must first install the dependencies:

```bash
pip install -r requirements.txt
```

And then run the command:

```bash
spark-submit src/run.py
```


# Dataset description
The dataset is related to red variant of the Portuguese "Vinho Verde" wine.
`https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009`

### Input variables (based on physicochemical tests):

1 - fixed acidity

2 - volatile acidity

3 - citric acid

4 - residual sugar

5 - chlorides

6 - free sulfur dioxide

7 - total sulfur dioxide

8 - density

9 - pH

10 - sulphates

11 - alcohol

### Output variable (based on sensory data):

12 - quality (score between 0 and 10, where 0 is bad and 10 is best)

Main goal is to determine which physiochemical properties make a wine 'good' (>6.5)

For this practical assignment I took _sulphates_, _pH_ and _volatile acidity_.

## Let's get to know this variables
**Sulphates** - are a food preservative widely used in winemaking, thanks to their ability to maintain the flavor and freshness of wine.

**pH** - the measure of the degree of relative acidity versus the relative alkalinity of any liquid, on a scale of 0 to 14, with 7 being neutral.

**Volatile acidity** - measure of the wine's gaseous acids that contributes to the smell and taste of vinegar in wine

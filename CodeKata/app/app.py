from pyspark.sql.functions import concat, format_string
from pyspark.sql.session import SparkSession
from pyspark.context import SparkContext
import numpy as np
import pandas as pd
from flask import Flask
import csv
import os
import sys
app = Flask('codeKata')


@app.route("/")
def index():
    try:
        sc = SparkContext.getOrCreate()
        spark = SparkSession(sc)

        try:
            schemaFile = spark.read.json('../input/spec.json', multiLine=True)
        except OSError as err:
            print("OS error: {0}".format(err))

        fixedWidthFile = "../input/fixedWidth.txt"
        outputCsv = '../output/output.csv'
        outputTxt = "../output/output.txt"

        data = np.random.randint(1, 10, size=(5, 10))
        pysdf = spark.createDataFrame(pd.DataFrame(columns=schemaFile.collect()[
            0][0], data=np.array(data.astype('U'))))
        isFwf = generateFixedWidthFile(outputTxt, pysdf, schemaFile)
        isDlm = generateDelimitedFile(outputCsv, fixedWidthFile, schemaFile)
    finally:
        sc.stop()
        return isFwf + ' and ' + isDlm


# Generate a fixed width file using the provided specifications.
def generateFixedWidthFile(outputTxt, pysdf, schemaFile):
    try:
        fixedWidth = schemaFile.collect()[0][4]
        ljust = []
        for w in fixedWidth:
            ljust.append(r"%-{width}s".format(width=w))
        pysdf.select(concat(*[format_string(l, c)
                              for c, l in zip(pysdf.columns, ljust)])).show(truncate=False)
        pysdf.coalesce(1).write.option("header", schemaFile.collect()[0][3]).option(
            "encoding", schemaFile.collect()[0][2]).mode("append").save(outputTxt)
    except Exception as ex:
        print("Exception: {0}".format(ex))
        return "Unable to generate fixed width file"
    return "Fixed width file generated"


# Parser that can parse the fixed width file and generate a delimited file.
def generateDelimitedFile(outputCsv, fixedWidthFile, schemaFile):
    try:
        rf = open(fixedWidthFile)
        wf = open(outputCsv, 'w', encoding=schemaFile.collect()[0][1])
        writer = csv.writer(wf)
        for row in rf.readlines():
            writer.writerow(row.split())
        rf.close()
        wf.close()
    except OSError as err:
        print("OS error: {0}".format(err))
        return "Unable to generate delimited file"
    return "Delimited file generated"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT'))

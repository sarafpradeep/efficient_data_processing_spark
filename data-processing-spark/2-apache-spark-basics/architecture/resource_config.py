import pprint
from typing import Dict

from pyspark.sql import SparkSession


def some_function(n_name: str) -> Dict[str, str]:
    return None


def run_code(spark):
    print("============================================")
    print("PRINT SPARKSESSION RESOURCE CONFIGS")
    print("============================================")
    # Get the SparkConf object
    conf = spark.sparkContext.getConf()

    # Print the resource configurations
    print("Resource Configurations:")
    pp = pprint.PrettyPrinter(
        indent=4,
    )
    pp.pprint(dict(conf.getAll()))


if __name__ == "__main__":
    spark = (
        SparkSession.builder.appName("efficient-data-processing-spark")
        .enableHiveSupport()
        .getOrCreate()
    )
    run_code(spark=spark)
    spark.stop()

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit

spark = SparkSession.builder.appName("ProductCategoryPairs").getOrCreate()

data_products = [
    (1, 'Apple'),
    (2, 'Opange'), 
    (3, 'Banana'),
    (4, 'Cherry'),
    (5, 'Strawberry'),
    (6, 'Tomato'), 
    (7, 'Potato'),
    (8, 'Onion'),
    (9, 'Cucumber'),
    (10, 'Pineapple')
    ]
df_products = spark.createDataFrame(data_products, ["id", "product_name"])

data_categories = [
    (1, 'Fruits'), 
    (2, 'Vegetables'),
    (3, 'Berries')
    ]
df_categories = spark.createDataFrame(data_categories, ["id", "category_name"])

data_product_categories = [
    (1, 1), 
    (2, 1),
    (3, 1),
    (4, 3),
    (5, 3),
    (6, 2),
    (7, 2),
    (8, 2),
    (9, 2),
    (10, 1)
    ]
df_product_categories = spark.createDataFrame(data_product_categories, ["product_id", "category_id"])

joined_df = df_product_categories.join(df_categories, on=df_product_categories.category_id == df_categories.id)

final_df = df_products.join(joined_df, on=df_products.id == joined_df.product_id, how='left')

final_df = final_df.withColumn('category_name',
                               when(final_df['category_name'].isNull(), lit('No Category'))
                                .otherwise(final_df['category_name']))

result_df = final_df.select('product_name', 'category_name')

result_df.show()
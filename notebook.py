# Databricks notebook source

with open("data.csv") as f:
  print(f.read())
  
# COMMAND ----------

%sh pwd

# COMMAND ----------

ls -l

# COMMAND ----------

%sh > /databricks/data/logs/wsfs.log

# COMMAND ----------

%sh cat /databricks/data/logs/wsfs.log | grep -aE "(LookUp|Open|Read)"

# COMMAND ----------

%sh cat /databricks/data/logs/wsfs.log

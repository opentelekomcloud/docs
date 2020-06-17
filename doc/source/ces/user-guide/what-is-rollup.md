# What Is Rollup?<a name="EN-US_TOPIC_0084812078"></a>

Rollup is the process in which Cloud Eye calculates sample raw data collected in different periods by using different rollup methods, including  **Avg.**,  **Max.**,  **Min.**,  **Sum**, and  **Variance**. The calculation period is called rollup period.

Rollup is a smooth calculation process. The longer the rollup interval, the more smoothly processing will be implemented, and the more accurate these generated data will reflect the real situation. However, the shorter the rollup interval is, the more effective alarm reporting will be.

The rollup period can be 5 minutes, 20 minutes, 1 hour, 4 hours, or 1 day.

The methods Cloud Eye uses to process collected data vary depending on data type:

-   If the data is an integer, the data will be rounded.
-   If the data is a decimal fraction, two decimal places will be retained. Any further decimal places will be rounded.

For example, the instance quantity in AS is an integer. If the rollup period is 5 minutes, the values of collected metric data are 1 and 4, while the average value is 2 instead of 2.5.

You can choose the proper rollup method to meet your service requirements.


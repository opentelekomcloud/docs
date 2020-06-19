# How Long Is the Metric Data Retained?<a name="EN-US_TOPIC_0084812080"></a>

Metric data includes raw and rolled-up data.

-   Raw data is sampled raw data and is retained for two days.
-   Rolled-up data is data aggregated based on raw data. The retention time for rolled-up data depends on the rollup period:
    -   Rollup period of 5 minutes: data retained for 10 days
    -   Rollup period of 20 minutes: data retained for 20 days
    -   Rollup period of 1 hour: data retained for 155 days
    -   Rollup period of 4 hours: data retained for 300 days
    -   Rollup period of 24 hours: data retained for 5 years


If a resource is stopped, closed, or deleted, the original metric will be deleted one hour after its raw data is not reported. After the metric data report resumes, the historical data of that metric is available.


# Tez: High-speed Computing Engine Supporting DAG Models<a name="EN-US_TOPIC_0225629156"></a>

Tez is Apache's latest open source computing framework that supports Directed Acyclic Graph \(DAG\) jobs. It can convert multiple dependent jobs into one job, greatly improving the performance of DAG jobs. If projects like Hive and Pig use Tez instead of MapReduce as the backbone of data processing, response time will be significantly reduced. Tez is built on Yarn and can run MR jobs without any modification.

MRS uses Tez as the default execution engine of Hive. Tez remarkably surpasses the original MapReduce computing engine in terms of execution efficiency.

For details about Tez, see  [https://tez.apache.org/](https://tez.apache.org/).


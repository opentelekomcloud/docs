# Can DWS SQL on OBS Replace MRS?<a name="dws_03_0011"></a>

No. Although DWS SQL on OBS fits can query DWS and OBS data, it is not suitable for the scenario where enterprises usually need to use processing frameworks such as MRS.

Apart from SQL query, MRS also provides other functions. The hosted MRS on the public cloud allows you to use the latest and common big data processing frameworks, such as Spark, Hadoop, and HBase, to process and analyze big data sets on a customizable cluster. With MRS on the public cloud, you can run data processing tasks for machine learning, graphics analysis, data conversion, streaming data processing, and applications you complied. DWS SQL on OBS can work with MRS. If you have already use MRS to process large-size data storage, DWS SQL on OBS can be used to query these data without affecting MRS tasks.

In this case, the query service, data warehouses, and complex data processing frameworks play their own roles. You only need to select appropriate tools for a specific task.

  


# What Types of Jobs Are Supported by MRS?<a name="EN-US_TOPIC_0125375535"></a>

A job functions as a program execution platform provided by MRS. Currently, MRS supports MapReduce jobs, Spark jobs, and Hive jobs.  [Table 1](#t8a95bf7963364fad8dfa2919e1123092)  describes job characteristics.

**Table  1**  Job types

<a name="t8a95bf7963364fad8dfa2919e1123092"></a>
<table><thead align="left"><tr id="re5a44c88f8bb4054b9b7ece25ae4c316"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="a49407ab4353240929c33cbbf35f1a040"><a name="a49407ab4353240929c33cbbf35f1a040"></a><a name="a49407ab4353240929c33cbbf35f1a040"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="ae58f36377c254f36b3063ac3077bb94f"><a name="ae58f36377c254f36b3063ac3077bb94f"></a><a name="ae58f36377c254f36b3063ac3077bb94f"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r2f666f24d1c44e0cbf5d79ea9fc0336f"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="a6e3f6e32b76a44ccb5540bc888509927"><a name="a6e3f6e32b76a44ccb5540bc888509927"></a><a name="a6e3f6e32b76a44ccb5540bc888509927"></a>MapReduce</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="a2db6e409da4f4742a607cbe509983654"><a name="a2db6e409da4f4742a607cbe509983654"></a><a name="a2db6e409da4f4742a607cbe509983654"></a>MapReduce is a programming model with parallel computing simplified, and is used for parallel computing of big data sets (over one TB).</p>
<p id="acc360e80d3dd4004b5d76ad1331a52c2"><a name="acc360e80d3dd4004b5d76ad1331a52c2"></a><a name="acc360e80d3dd4004b5d76ad1331a52c2"></a>Map divides one task into multiple tasks, and Reduce summarizes the processing results of these tasks and produces the final analysis result.</p>
<p id="a9e4d718340f544aaa6d051bdb21c344b"><a name="a9e4d718340f544aaa6d051bdb21c344b"></a><a name="a9e4d718340f544aaa6d051bdb21c344b"></a>After you complete code development, pack the code into a JAR file in IDEA or Eclipse, upload the file to the MRS cluster for execution, and obtain the execution result.</p>
</td>
</tr>
<tr id="r7deeb5ae16e4421f8f7f50419574e00c"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="abb8646ae27e24d7fac1cb7beff486475"><a name="abb8646ae27e24d7fac1cb7beff486475"></a><a name="abb8646ae27e24d7fac1cb7beff486475"></a>Spark</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="a3eca8c766271416d93b8dec6e311d64a"><a name="a3eca8c766271416d93b8dec6e311d64a"></a><a name="a3eca8c766271416d93b8dec6e311d64a"></a>Spark is a batch data processing engine with high processing speed. Spark has demanding requirements on memory because it performs computing based on memory. A Spark job includes:</p>
<a name="u5eeef1a8c02d4b47857dda38737f5efb"></a><a name="u5eeef1a8c02d4b47857dda38737f5efb"></a><ul id="u5eeef1a8c02d4b47857dda38737f5efb"><li>Spark: ends with&nbsp;<span class="filepath" id="f49b7a1914fb84ab99ad64a35971a7d08"><a name="f49b7a1914fb84ab99ad64a35971a7d08"></a><a name="f49b7a1914fb84ab99ad64a35971a7d08"></a><b>.jar</b></span>, which is case-insensitive.</li><li>Spark Script: ends with <span class="filepath" id="fa0b6dfbac7774cfbacd78c4a6249504a"><a name="fa0b6dfbac7774cfbacd78c4a6249504a"></a><a name="fa0b6dfbac7774cfbacd78c4a6249504a"></a><b>.sql</b></span>, which is case-insensitive.</li><li>Spark SQL: specifies standard Spark SQL statements, for example, <i><b><span class="cmdname" style="font-family:Arial" id="c30d957290ce145ddb66da8adf82b1d3b"><a name="c30d957290ce145ddb66da8adf82b1d3b"></a><a name="c30d957290ce145ddb66da8adf82b1d3b"></a>show tables;</span></b></i>.</li></ul>
</td>
</tr>
<tr id="ra2d3dc0ff4d04f1d93f0d2636c8b695e"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="a59ce0f425aa54422a90e3e09ee255586"><a name="a59ce0f425aa54422a90e3e09ee255586"></a><a name="a59ce0f425aa54422a90e3e09ee255586"></a>Hive</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="afe14fed258644449a4285e0ae61b22c8"><a name="afe14fed258644449a4285e0ae61b22c8"></a><a name="afe14fed258644449a4285e0ae61b22c8"></a>Hive is a data warehouse framework built on Hadoop. Hive provides Hive query language (HiveQL), similar to structured query language (SQL), to process structured data. Hive automatically converts HiveQL in Hive Script to a MapReduce task to query and analyze massive data stored in the Hadoop cluster.</p>
<p id="a48c371b162b34de39fa1b21adbfa058d"><a name="a48c371b162b34de39fa1b21adbfa058d"></a><a name="a48c371b162b34de39fa1b21adbfa058d"></a>An example of a standard HiveQL statement is as follows: <i><b><span class="cmdname" style="font-family:Arial" id="cd704c5579a6c4c9996d17d0ab68314ec"><a name="cd704c5579a6c4c9996d17d0ab68314ec"></a><a name="cd704c5579a6c4c9996d17d0ab68314ec"></a>create table page_view(viewTime INT,userid BIGINT,page_url STRING,referrer_uel STRING,ip STRING COMMENT 'IP Address of the User');</span></b></i></p>
</td>
</tr>
</tbody>
</table>


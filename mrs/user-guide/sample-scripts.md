# Sample Scripts<a name="EN-US_TOPIC_0127245539"></a>

## Zeppelin<a name="en-us_topic_0114990925_section2030765710246"></a>

Zeppelin is a web-based notebook that supports interactive data analysis. For more information, visit the Zeppelin official website at  [http://zeppelin.apache.org/](http://zeppelin.apache.org/).

This sample script is used to automatically install Zeppelin. Select the corresponding script path based on the region where the cluster is to be created. Enter the script path in  **Script Path** on the **Bootstrap Action**  page when adding a bootstrap action during cluster creation. You do not need to enter parameters for this script. Based on the Zeppelin usage habit, you only need to run the script on the active Master node.

-   Script path that you need to enter when adding the bootstrap action: s3a://mrs-samples-bootstrap-eu-de/zeppelin/zeppelin\_install.sh
-   Path for downloading the sample script:  [https://mrs-samples-bootstrap-eu-de.obs.eu-de.otc.t-systems.com/zeppelin/zeppelin\_install.sh](https://mrs-samples-bootstrap-eu-de.obs.eu-de.otc.t-systems.com/zeppelin/zeppelin_install.sh)


After the bootstrap action is complete, use either of the following methods to verify that Zeppelin is correctly installed.

Method 1: Log in to the active Master node as user  **root** and run **/home/apache/zeppelin-0.7.3-bin-all/bin/zeppelin-daemon.sh status**. If the message stating "Zeppelin is running \[ OK \]" is displayed, the installation is successful.

Method 2: Start a Windows ECS in the same VPC. Access port 7510 of the active Master node in the cluster. If the Zeppelin page is displayed, the installation is successful.

## Presto<a name="en-us_topic_0114990925_section1033815294364"></a>

Presto is an open-source distributed SQL query engine, which is applicable to interactive analysis and query. For more information, visit the official website at  [http://prestodb.io/](http://prestodb.io/).

The sample script can be used to automatically install Presto. The script path is as follows:

-   Script path that you need to enter when adding the bootstrap action: s3a://mrs-samples-bootstrap-eu-de/presto/presto\_install.sh
-   Path for downloading the sample script:  [https://mrs-samples-bootstrap-eu-de.obs.eu-de.otc.t-systems.com/presto/presto\_install.sh](https://mrs-samples-bootstrap-eu-de.obs.eu-de.otc.t-systems.com/presto/presto_install.sh)


Based on the Presto usage habit, you are advised to install  **dualroles** on the active Master nodes and **worker**  on the Core nodes. You are advised to add the boot operation script and configure the parameters as follows:

**Table  1**  Bootstrap action script parameters

<a name="en-us_topic_0114990925_table1611103255514"></a>
<table><tbody><tr id="en-us_topic_0114990925_row1612163275519"><th class="firstcol" valign="top" width="23%" id="mcps1.2.3.1.1"><p id="en-us_topic_0114990925_p39685885516"><a name="en-us_topic_0114990925_p39685885516"></a><a name="en-us_topic_0114990925_p39685885516"></a>Script 1</p>
</th>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0114990925_p1396185845515"><a name="en-us_topic_0114990925_p1396185845515"></a><a name="en-us_topic_0114990925_p1396185845515"></a>Name: install dualroles</p>
<p id="en-us_topic_0114990925_p8961258185519"><a name="en-us_topic_0114990925_p8961258185519"></a><a name="en-us_topic_0114990925_p8961258185519"></a>Script Path: Select the path of the <strong id="en-us_topic_0114990925_b842352706171510"><a name="en-us_topic_0114990925_b842352706171510"></a><a name="en-us_topic_0114990925_b842352706171510"></a>presto-install.sh</strong> script based on the region.</p>
<p id="en-us_topic_0114990925_p296125814555"><a name="en-us_topic_0114990925_p296125814555"></a><a name="en-us_topic_0114990925_p296125814555"></a>Execution Node: Active Master</p>
<p id="en-us_topic_0114990925_p109625855516"><a name="en-us_topic_0114990925_p109625855516"></a><a name="en-us_topic_0114990925_p109625855516"></a>Parameters: dualroles</p>
<p id="en-us_topic_0114990925_p0968581554"><a name="en-us_topic_0114990925_p0968581554"></a><a name="en-us_topic_0114990925_p0968581554"></a>Execution Time: After component start</p>
<p id="en-us_topic_0114990925_p1996105813556"><a name="en-us_topic_0114990925_p1996105813556"></a><a name="en-us_topic_0114990925_p1996105813556"></a>Failed Action: Continue</p>
</td>
</tr>
<tr id="en-us_topic_0114990925_row1312133205510"><th class="firstcol" valign="top" width="23%" id="mcps1.2.3.2.1"><p id="en-us_topic_0114990925_p096145875516"><a name="en-us_topic_0114990925_p096145875516"></a><a name="en-us_topic_0114990925_p096145875516"></a>Script 2</p>
</th>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.2.1 "><p id="en-us_topic_0114990925_p1896115835515"><a name="en-us_topic_0114990925_p1896115835515"></a><a name="en-us_topic_0114990925_p1896115835515"></a>Name: install worker</p>
<p id="en-us_topic_0114990925_p2961658195514"><a name="en-us_topic_0114990925_p2961658195514"></a><a name="en-us_topic_0114990925_p2961658195514"></a>Script Path: Select the path of the <strong id="en-us_topic_0114990925_b2926561810238"><a name="en-us_topic_0114990925_b2926561810238"></a><a name="en-us_topic_0114990925_b2926561810238"></a>presto-install.sh</strong> script based on the region.</p>
<p id="en-us_topic_0114990925_p1096658125511"><a name="en-us_topic_0114990925_p1096658125511"></a><a name="en-us_topic_0114990925_p1096658125511"></a>Execution Node: Core</p>
<p id="en-us_topic_0114990925_p179618581552"><a name="en-us_topic_0114990925_p179618581552"></a><a name="en-us_topic_0114990925_p179618581552"></a>Parameters: worker</p>
<p id="en-us_topic_0114990925_p096558205510"><a name="en-us_topic_0114990925_p096558205510"></a><a name="en-us_topic_0114990925_p096558205510"></a>Execution Time: After component start</p>
<p id="en-us_topic_0114990925_p2964587559"><a name="en-us_topic_0114990925_p2964587559"></a><a name="en-us_topic_0114990925_p2964587559"></a>Failed Action: Continue</p>
</td>
</tr>
</tbody>
</table>

After the bootstrap action is complete, you can start a Windows ECS in the same VPC of the cluster and access port 7520 of the active Master node to view the Presto web page.

You can also log in to the active Master node to try Presto and run the following commands as user  **root**:

Command for loading the environment variable:

**\#source /opt/client/bigdata\_env**

Command for viewing the process status:

**\#/home/apache/presto/presto-server-0.201/bin/launcher status**

Command for connecting to Presto and performing the operation

**\#/home/apache/presto/presto-server-0.201/bin/presto --server localhost:7520 --catalog tpch --schema sf100**

**presto:sf100\> select \* from nation;**

**presto:sf100\> select count\(\*\) from customer**

## Superset<a name="en-us_topic_0114990925_section1478618511548"></a>

Superset is a web-based enterprise-level and modern BI tool. For more information, visit the Superset official website at  [https://superset.incubator.apache.org/](https://superset.incubator.apache.org/).

This sample script is used to automatically install Superset. Select the corresponding script path based on the region where the cluster is to be created. Enter the script path in  **Script Path** on the **Bootstrap Action**  page when adding a bootstrap action during cluster creation. You do not need to enter parameters for this script. Based on the Superset usage habit, you only need to run the script on the active Master node.

-   Script path that you need to enter when adding the bootstrap action: s3a://mrs-samples-bootstrap-eu-de/superset/superset\_install.sh
-   Path for downloading the sample script:  [https://mrs-samples-bootstrap-eu-de.obs.eu-de.otctest.t-systems.com /superset/superset\_install.sh](https://mrs-samples-bootstrap-eu-de.obs.eu-de.otctest.t-systems.com /superset/superset_install.sh)

After the bootstrap action is complete, use either of the following methods to verify that Superset is correctly installed.

Method 1: Remotely log in to the active Master node as user  **root** and run the **lsof -i:38088** command. If the command output contains **LISTEN**, the installation is successful.

Method 2: Start a Windows ECS in the same VPC. Access port 38088 of the active Master node in the cluster. If the Superset page is displayed, the installation is successful.


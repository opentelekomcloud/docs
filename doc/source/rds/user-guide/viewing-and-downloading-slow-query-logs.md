# Viewing and Downloading Slow Query Logs<a name="slow_query_log-sqlserver"></a>

## Scenarios<a name="en-us_topic_0171818656_section12909141294214"></a>

Slow query logs record statements that exceed  **long\_query\_time**  \(1 second by default\). You can view log details to identify statements that are executing slowly and optimize the statements. You can also download slow query logs for service analysis.

## Parameter Description<a name="en-us_topic_0171818656_section16601112910434"></a>

**Table  1**  Parameters related to Microsoft SQL Server slow queries

<a name="en-us_topic_0171818656_table1455312241604"></a>
<table><thead align="left"><tr id="en-us_topic_0171818656_row1755318241201"><th class="cellrowborder" valign="top" width="22.79%" id="mcps1.2.3.1.1"><p id="en-us_topic_0171818656_p455311242020"><a name="en-us_topic_0171818656_p455311242020"></a><a name="en-us_topic_0171818656_p455311242020"></a><strong id="b842352706181819"><a name="b842352706181819"></a><a name="b842352706181819"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="77.21000000000001%" id="mcps1.2.3.1.2"><p id="en-us_topic_0171818656_p15534249012"><a name="en-us_topic_0171818656_p15534249012"></a><a name="en-us_topic_0171818656_p15534249012"></a><strong id="b147631718121816"><a name="b147631718121816"></a><a name="b147631718121816"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0171818656_row145532241400"><td class="cellrowborder" valign="top" width="22.79%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0171818656_p26741582414"><a name="en-us_topic_0171818656_p26741582414"></a><a name="en-us_topic_0171818656_p26741582414"></a>long_query_time</p>
</td>
<td class="cellrowborder" valign="top" width="77.21000000000001%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0171818656_p121871817112119"><a name="en-us_topic_0171818656_p121871817112119"></a><a name="en-us_topic_0171818656_p121871817112119"></a>Specifies the time greater than or equal to which slow query logs are recorded. The precision is microsecond. The default value is 1s. When the execution time of an SQL statement exceeds the value of this parameter, the SQL statement is recorded in slow query logs.</p>
<p id="en-us_topic_0171818656_p0668124910584"><a name="en-us_topic_0171818656_p0668124910584"></a><a name="en-us_topic_0171818656_p0668124910584"></a>You can modify the slow log threshold as required.</p>
<a name="en-us_topic_0171818656_ol2197921185015"></a><a name="en-us_topic_0171818656_ol2197921185015"></a><ol id="en-us_topic_0171818656_ol2197921185015"><li>Log in to the management console.</li><li>Click <a name="en-us_topic_0046585334_image192529212293"></a><a name="en-us_topic_0046585334_image192529212293"></a><span><img id="en-us_topic_0046585334_image192529212293" src="figures/region灰色图标.png"></span> in the upper left corner and select a region and a project.</li><li>Click <strong id="en-us_topic_0046585334_b653516366542"><a name="en-us_topic_0046585334_b653516366542"></a><a name="en-us_topic_0046585334_b653516366542"></a>Service List</strong>. Under <strong id="en-us_topic_0046585334_b1753663645417"><a name="en-us_topic_0046585334_b1753663645417"></a><a name="en-us_topic_0046585334_b1753663645417"></a>Database</strong>, click <strong id="en-us_topic_0046585334_b4536193645417"><a name="en-us_topic_0046585334_b4536193645417"></a><a name="en-us_topic_0046585334_b4536193645417"></a>Relational Database Service</strong> to go to the RDS console. The RDS console is displayed.</li><li>On the <strong id="b14567024141815"><a name="b14567024141815"></a><a name="b14567024141815"></a>Instance Management</strong> page, click the target DB instance.</li><li>In the navigation pane on the left, choose <span class="uicontrol" id="uicontrol19211046193919"><a name="uicontrol19211046193919"></a><a name="uicontrol19211046193919"></a><b>Logs</b></span>. On the <span class="uicontrol" id="uicontrol199218461398"><a name="uicontrol199218461398"></a><a name="uicontrol199218461398"></a><b>Slow Query Logs</b></span> page, click <a name="en-us_topic_0171818656_image3857343615410"></a><a name="en-us_topic_0171818656_image3857343615410"></a><span><img id="en-us_topic_0171818656_image3857343615410" src="figures/kwx318612-gauss-dbaas-image-71b3f418-b0b2-4306-9c75-bb4bae6c3f33.png" width="21.945" height="15.06225"></span> in the <span class="parmname" id="en-us_topic_0171818656_parmname867921612919"><a name="en-us_topic_0171818656_parmname867921612919"></a><a name="en-us_topic_0171818656_parmname867921612919"></a><b>Threshold of Slow Query Log (long_query_time)</b></span> field to change the threshold.<a name="en-us_topic_0171818656_ul1137218215315"></a><a name="en-us_topic_0171818656_ul1137218215315"></a><ul id="en-us_topic_0171818656_ul1137218215315"><li>To submit the change, click <a name="en-us_topic_0171818656_image12216421202217"></a><a name="en-us_topic_0171818656_image12216421202217"></a><span><img id="en-us_topic_0171818656_image12216421202217" src="figures/端口提交-44.png" width="19.950000000000003" height="9.289252000000001"></span>.</li><li>To cancel the change, click <a name="image12572928514"></a><a name="image12572928514"></a><span><img id="image12572928514" src="figures/kwx318612-gauss-dbaas-image-b15f2e64-dfa0-4668-b894-7b5d2c880dc4-45.png"></span>.</li></ul>
<div class="note" id="en-us_topic_0171818656_note199097234317"><a name="en-us_topic_0171818656_note199097234317"></a><a name="en-us_topic_0171818656_note199097234317"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0171818656_p2912923123111"><a name="en-us_topic_0171818656_p2912923123111"></a><a name="en-us_topic_0171818656_p2912923123111"></a>The recommended value is <strong id="b842352706195824"><a name="b842352706195824"></a><a name="b842352706195824"></a>1s</strong>. The lock wait time is not calculated into the query time.</p>
</div></div>
</li></ol>
</td>
</tr>
</tbody>
</table>

## Viewing Slow Query Logs<a name="en-us_topic_0171818656_section10218113118539"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target DB instance.
5.  In the navigation pane on the left, choose  **Logs**. On the  **Slow Query Logs**  page, find a button to enable the slow query log function.
6.  <a name="en-us_topic_0171818656_li654810813132"></a>The generated slow query logs are displayed.

    >![](/images/icon-note.gif) **NOTE:**   
    >Enabling slow query log slightly affects DB instance performance.  

7.  Connect to the DB instance through the Microsoft SQL Server client.
8.  After the DB instance is connected, run the following command to view slow query log details:

    **select \* from ::fn\_trace\_gettable\('D:\\SQLTrace\\audit\\**_XXX_**', default\)**

    >![](/images/icon-note.gif) **NOTE:**   
    >**_XXX_**  indicates the name of the slow query log recorded in  [6](#en-us_topic_0171818656_li654810813132).  

    Example:

    **select \* from ::fn\_trace\_gettable\('D:\\SQLTrace\\audit\\SQLTrace.trc', default\)**

    The result is shown in  [Figure 1](#en-us_topic_0171818656_fig19196129142415).

    **Figure  1**  Slow query log details<a name="en-us_topic_0171818656_fig19196129142415"></a>  
    ![](figures/slow-query-log-details.png "slow-query-log-details")


## Downloading a Log<a name="en-us_topic_0171818656_section1021714251349"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target DB instance.
5.  In the navigation pane on the left, choose  **Logs**. On the  **Slow Query Logs**  page, find a button to enable the slow query log function.

    >![](/images/icon-note.gif) **NOTE:**   
    >Enabling slow query log slightly affects DB instance performance.  

6.  <a name="en-us_topic_0171818656_li121912551908"></a>Locate a log to be downloaded and click  **Download**  in the  **Operation**  column.
    1.  The system automatically loads the downloading preparation tasks. The loading duration is determined by the log file size and network environment.
        -   During the downloading preparation, the log status is  **Preparing**.
        -   After the downloading preparation is complete, the log status is  **Preparation completed**.
        -   If the downloading preparation fails, the log status is  **Abnormal**.

    2.  In the displayed dialog box, click  **OK**  to download the log whose status is  **Preparation completed**. If you click  **Cancel**, the system does not download the log.

        The download link is valid for 5 minutes. After the download link expires, a message is displayed indicating that the download link has expired. You can close the window and repeat the procedure  [6](#en-us_topic_0171818656_li121912551908)  to try to download a log again.




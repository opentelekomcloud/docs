# Managing Parameter Groups<a name="dws_01_0126"></a>

You can perform operations  [Creating a Parameter Group](#section14261524455),  [Modifying a Parameter Group](#section1957519408206),  [Deleting a Parameter Group](#section988984052114), and  [Changing the Parameter Group](#section2615131874812)  on the DWS management console.

## Parameter Group Overview<a name="section1428213271147"></a>

A parameter group is a collection of database parameters. You can set the parameters for a database to better adapt to the actual situation and run services. When creating or restoring a data warehouse cluster, you must specify a parameter group for the cluster. Parameters in the specified parameter group are applied to all databases in the cluster. After a cluster is created, you can change its parameter group to another one. However, you may need to restart the cluster to make the new parameter group take effect.

DWS has a default parameter group named  **Default-Parameter-Group-DWS**. The default parameter group cannot be deleted, and its parameters cannot be modified. If you want to modify a parameter value, create a customized parameter group. The parameters in the customized group can be modified.

After clusters created before version 1.2.3 are automatically upgraded to version 1.2.3 or later, parameter values in their parameter groups are set to values in the default parameter group. You can change the parameter group for each cluster.

## Parameter Group Parameters<a name="section926416313488"></a>

**Table  1**  Parameter group parameters

<a name="table122717208620"></a>
<table><thead align="left"><tr id="row92716201567"><th class="cellrowborder" valign="top" width="23.762376237623762%" id="mcps1.2.4.1.1"><p id="p627820868"><a name="p627820868"></a><a name="p627820868"></a><strong id="b1993131717811"><a name="b1993131717811"></a><a name="b1993131717811"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="47.524752475247524%" id="mcps1.2.4.1.2"><p id="p22722018611"><a name="p22722018611"></a><a name="p22722018611"></a><strong id="b142745501728"><a name="b142745501728"></a><a name="b142745501728"></a>Description</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.71287128712871%" id="mcps1.2.4.1.3"><p id="p162719204610"><a name="p162719204610"></a><a name="p162719204610"></a><strong id="b42357640184919_1"><a name="b42357640184919_1"></a><a name="b42357640184919_1"></a>Default Value</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row7273201611"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p72792012610"><a name="p72792012610"></a><a name="p72792012610"></a>session_timeout</p>
</td>
<td class="cellrowborder" valign="top" width="47.524752475247524%" headers="mcps1.2.4.1.2 "><p id="p989412394507"><a name="p989412394507"></a><a name="p989412394507"></a>Indicates the timeout interval for idle sessions. The unit is second. Value <strong id="b12915181220515"><a name="b12915181220515"></a><a name="b12915181220515"></a>0</strong> indicates that the timeout limit is disabled.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.4.1.3 "><p id="p112719201461"><a name="p112719201461"></a><a name="p112719201461"></a>600</p>
</td>
</tr>
<tr id="row9271201464"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p99367618710"><a name="p99367618710"></a><a name="p99367618710"></a>query_dop</p>
</td>
<td class="cellrowborder" valign="top" width="47.524752475247524%" headers="mcps1.2.4.1.2 "><p id="p952165575012"><a name="p952165575012"></a><a name="p952165575012"></a>Indicates the user-defined query concurrency.</p>
<a name="ul89106417554"></a><a name="ul89106417554"></a><ul id="ul89106417554"><li>Value <strong id="b858406141813"><a name="b858406141813"></a><a name="b858406141813"></a>0</strong> indicates that the query concurrency is adaptive.</li><li>Value <strong id="b39331226152116"><a name="b39331226152116"></a><a name="b39331226152116"></a>1</strong> indicates that query concurrency is disabled.</li><li>Value <strong id="b1816765410218"><a name="b1816765410218"></a><a name="b1816765410218"></a>2</strong> indicates that the query concurrency degree is 2.</li></ul>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.4.1.3 "><p id="p1327020962"><a name="p1327020962"></a><a name="p1327020962"></a>0</p>
</td>
</tr>
<tr id="row10271220063"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p1527192012613"><a name="p1527192012613"></a><a name="p1527192012613"></a>datestyle</p>
</td>
<td class="cellrowborder" valign="top" width="47.524752475247524%" headers="mcps1.2.4.1.2 "><p id="p138941459514"><a name="p138941459514"></a><a name="p138941459514"></a>Sets the format with which date and time values will be displayed.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.4.1.3 "><p id="p02720201769"><a name="p02720201769"></a><a name="p02720201769"></a>ISO,MDY</p>
</td>
</tr>
<tr id="row6271820468"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p172711201368"><a name="p172711201368"></a><a name="p172711201368"></a>failed_login_attempts</p>
</td>
<td class="cellrowborder" valign="top" width="47.524752475247524%" headers="mcps1.2.4.1.2 "><p id="p188041435115"><a name="p188041435115"></a><a name="p188041435115"></a>If the number of incorrect password attempts reaches the value of this parameter, the account is automatically locked. If this parameter is set to <strong id="b1473010218420"><a name="b1473010218420"></a><a name="b1473010218420"></a>0</strong>, the number of consecutive incorrect password attempts is unlimited.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.4.1.3 "><p id="p17272020463"><a name="p17272020463"></a><a name="p17272020463"></a>10</p>
</td>
</tr>
<tr id="row5271202614"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p1061102513710"><a name="p1061102513710"></a><a name="p1061102513710"></a>timezone</p>
</td>
<td class="cellrowborder" valign="top" width="47.524752475247524%" headers="mcps1.2.4.1.2 "><p id="p144305236513"><a name="p144305236513"></a><a name="p144305236513"></a>Indicates the time zone for displaying and interpreting time stamps.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.4.1.3 "><p id="p102710201963"><a name="p102710201963"></a><a name="p102710201963"></a>UTC</p>
</td>
</tr>
<tr id="row42710205610"><td class="cellrowborder" valign="top" width="23.762376237623762%" headers="mcps1.2.4.1.1 "><p id="p94694329715"><a name="p94694329715"></a><a name="p94694329715"></a>log_timezone</p>
</td>
<td class="cellrowborder" valign="top" width="47.524752475247524%" headers="mcps1.2.4.1.2 "><p id="p152718204614"><a name="p152718204614"></a><a name="p152718204614"></a>Sets the time zone used for time stamps written in the server log.</p>
</td>
<td class="cellrowborder" valign="top" width="28.71287128712871%" headers="mcps1.2.4.1.3 "><p id="p10271420269"><a name="p10271420269"></a><a name="p10271420269"></a>UTC</p>
</td>
</tr>
</tbody>
</table>

## Creating a Parameter Group<a name="section14261524455"></a>

If parameters in the default parameter group cannot meet service requirements, you can customize a parameter group and modify the parameter values to better adapt to services.

To create a parameter group, perform the following steps:

1.  Log in to the management console at  [https://console.otc.t-systems.com/dws/](https://console.otc.t-systems.com/dws/).
2.  In the navigation tree on the left, click  **Parameter Group Management**.
3.  Click  **Create Parameter Group**  and set the following parameters:

    -   **Database Engine**: Select a database engine.
    -   **Parameter Group Name**: Enter the name of the new parameter group.

        Enter 4 to 64 characters. Only letters, digits, hyphens \(-\), underscores \(\_\), and periods \(.\) are allowed. The value must start with a letter. Letters are case-insensitive.

    -   **Description**: Enter the description of the new parameter group. This parameter is optional.

        The parameter group description contains 0 to 256 characters and does not support special characters !<\>'=&".

    **Figure  1**  Creating a parameter group<a name="fig1583311156813"></a>  
    ![](figures/creating-a-parameter-group.png "creating-a-parameter-group")

4.  Click  **OK**  to start creating the parameter group.

## Modifying a Parameter Group<a name="section1957519408206"></a>

You can modify the parameter values in a user-defined parameter group but cannot modify the parameter values in the default parameter group.

1.  Log in to the management console at  [https://console.otc.t-systems.com/dws/](https://console.otc.t-systems.com/dws/).
2.  In the navigation tree on the left, click  **Parameter Group Management**.
3.  In the  **Name**  column, click the name of the target parameter group. The parameter list is displayed.
4.  Enter a new value in the  **Value**  column of the parameter to be modified. After the modification, click  **Save**.

    If you modify a parameter whose  **Restart Required**  column shows  **Yes**, you need to restart the cluster after saving the modification for the new parameter values to take effect.

5.  \(Optional\) If the modified parameters take effect only after the clusters are restarted, select  **Restart all clusters associated with the parameter group.**  in the displayed  **Modification Preview**  dialog box.

    If you do not select this option, the system saves only the parameter values. Then, you need to manually restart the clusters for the new parameter values to take effect.

    **Figure  2**  Modification Preview<a name="fig5326417152212"></a>  
    ![](figures/modification-preview.png "modification-preview")

6.  In the  **Modification Preview**  dialog box, confirm the settings and click  **Save**.

## Deleting a Parameter Group<a name="section988984052114"></a>

You can delete an unnecessary parameter group or a parameter group that is not used for a long time. The default parameter group cannot be deleted. Deleted parameter groups cannot be recovered. Exercise caution when performing this operation.

Before deleting a parameter group, ensure that it is not used by any cluster. Otherwise, it cannot be deleted. If the parameter group is used by a cluster, you need to change the parameter group to another one \(the default parameter group is recommended\) by performing steps in  [Changing the Parameter Group](#section2615131874812)  and delete the original parameter group.

1.  Log in to the management console at  [https://console.otc.t-systems.com/dws/](https://console.otc.t-systems.com/dws/).
2.  In the navigation tree on the left, click  **Parameter Group Management**.
3.  In the  **Operation**  column of the parameter group to be deleted, click  **Delete**.
4.  In the displayed dialog box, click  **OK**.

## Changing the Parameter Group<a name="section2615131874812"></a>

After a cluster is created, you can change its parameter group. After the change, you may need to restart the cluster to make the new parameter group take effect.

To change a parameter group, perform the following steps:

1.  Log in to the management console at  [https://console.otc.t-systems.com/dws/](https://console.otc.t-systems.com/dws/).
2.  In the navigation tree on the left, click  **Cluster Management**.
3.  In the  **Operation**  column of the target cluster, choose  **More \> Change Parameter Group**.
4.  In the  **Change Parameter Group**  dialog box, click the drop-down list on the right of  **New Parameter Group**  and select a new parameter group.
5.  Click  **OK**.


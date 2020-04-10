# Updating the MRS Data Source Configuration<a name="en-us_topic_0065840666"></a>

## Scenario<a name="section31806539111657"></a>

For MRS, if the following parameter configurations of the HDFS cluster change, data may fail to be imported to the data warehouse cluster from the HDFS cluster. Before importing HDFS cluster data, you must update the MRS data source configuration.

<a name="table4618184514293"></a>
<table><thead align="left"><tr id="row7619194592917"><th class="cellrowborder" valign="top" width="41%" id="mcps1.1.3.1.1"><p id="p12589614152910"><a name="p12589614152910"></a><a name="p12589614152910"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.1.3.1.2"><p id="p8398249152910"><a name="p8398249152910"></a><a name="p8398249152910"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row161974518294"><td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.3.1.1 "><p id="p43291566302"><a name="p43291566302"></a><a name="p43291566302"></a>dfs.client.read.shortcircuit</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.3.1.2 "><p id="p832912693017"><a name="p832912693017"></a><a name="p832912693017"></a>Specifies whether to enable the local read function.</p>
</td>
</tr>
<tr id="row1261994522912"><td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.3.1.1 "><p id="p33296673017"><a name="p33296673017"></a><a name="p33296673017"></a>dfs.client.read.shortcircuit.skip.checksum</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.3.1.2 "><p id="p183303633019"><a name="p183303633019"></a><a name="p183303633019"></a>Specifies whether to skip data verification during the local read.</p>
</td>
</tr>
<tr id="row4193515322"><td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.3.1.1 "><p id="p233015643013"><a name="p233015643013"></a><a name="p233015643013"></a>dfs.client.block.write.replace-datanode-on-failure.enable</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.3.1.2 "><p id="p17330156163015"><a name="p17330156163015"></a><a name="p17330156163015"></a>Specifies whether to replace the location storing copies with the new node when data blocks fail to be written to HDFS.</p>
</td>
</tr>
<tr id="row519165173213"><td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.3.1.1 "><p id="p6330196133011"><a name="p6330196133011"></a><a name="p6330196133011"></a>dfs.encrypt.data.transfer</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.3.1.2 "><p id="p719295193211"><a name="p719295193211"></a><a name="p719295193211"></a>Specifies whether to enable data encryption.</p>
<div class="note" id="note3531257017930"><a name="note3531257017930"></a><a name="note3531257017930"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p4937767417930"><a name="p4937767417930"></a><a name="p4937767417930"></a>This parameter is available only for clusters with Kerberos authentication enabled.</p>
</div></div>
</td>
</tr>
<tr id="row1461015818328"><td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.3.1.1 "><p id="p233015618306"><a name="p233015618306"></a><a name="p233015618306"></a>dfs.encrypt.data.transfer.algorithm</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.3.1.2 "><p id="p1133136153015"><a name="p1133136153015"></a><a name="p1133136153015"></a>Specifies the encryption and decryption algorithm for key transmission.</p>
</td>
</tr>
<tr id="row3912191116327"><td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.3.1.1 "><p id="p691241118326"><a name="p691241118326"></a><a name="p691241118326"></a>dfs.encrypt.data.transfer.cipher.suites</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.3.1.2 "><p id="p13912191110326"><a name="p13912191110326"></a><a name="p13912191110326"></a>Specifies the encryption and decryption algorithm for the transmission of actually stored data.</p>
</td>
</tr>
<tr id="row46231942133316"><td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.3.1.1 "><p id="p12331067307"><a name="p12331067307"></a><a name="p12331067307"></a>dfs.replication</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.3.1.2 "><p id="p14623144210337"><a name="p14623144210337"></a><a name="p14623144210337"></a>Specifies the default number of data copies.</p>
</td>
</tr>
<tr id="row8714346173314"><td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.3.1.1 "><p id="p83311663010"><a name="p83311663010"></a><a name="p83311663010"></a>dfs.blocksiz</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.3.1.2 "><p id="p633114614307"><a name="p633114614307"></a><a name="p633114614307"></a>Specifies the default size of a data block.</p>
</td>
</tr>
<tr id="row15707450113318"><td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.3.1.1 "><p id="p1833110633013"><a name="p1833110633013"></a><a name="p1833110633013"></a>hadoop.security.authentication</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.3.1.2 "><p id="p137081500335"><a name="p137081500335"></a><a name="p137081500335"></a>Specifies the security authentication mode.</p>
</td>
</tr>
<tr id="row8284105503320"><td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.3.1.1 "><p id="p1033110623019"><a name="p1033110623019"></a><a name="p1033110623019"></a>hadoop.rpc.protection</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.3.1.2 "><p id="p102848555333"><a name="p102848555333"></a><a name="p102848555333"></a>Specifies the RPC communication protection mode.</p>
</td>
</tr>
<tr id="row19749125963313"><td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.3.1.1 "><p id="p6331265302"><a name="p6331265302"></a><a name="p6331265302"></a>dfs.domain.socket.path</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.3.1.2 "><p id="p874995913313"><a name="p874995913313"></a><a name="p874995913313"></a>Specifies the locally used <strong id="b842352706104642"><a name="b842352706104642"></a><a name="b842352706104642"></a>Domain socket</strong> path.</p>
</td>
</tr>
</tbody>
</table>

## Prerequisites<a name="section45940751111911"></a>

-   You have created an MRS data source connection for the data warehouse cluster.

## Impact on the System<a name="section178972158583"></a>

-   When you are updating an MRS data source connection, the data warehouse cluster will automatically restart and cannot provide services.

## Procedure<a name="section4276196111818"></a>

1.  On the DWS management console, click  **Cluster Management**.
2.  In the cluster list, click the name of a cluster. On the page that is displayed, click  **MRS Data Sources**.
3.  In the MRS data source list, select the MRS that you want to update. In the  **Operation**  column, click  **Update Configurations**.

    **MRS Cluster Status**  and  **Configuration Status**  of the current connection will be updated. During configuration update, you cannot create a new connection. The system checks whether the security group rule is correct. If the rule is incorrect, the system rectifies the fault.



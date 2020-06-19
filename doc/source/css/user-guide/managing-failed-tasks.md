# Managing Failed Tasks<a name="css_01_0060"></a>

In the  **Failed Tasks**  dialog box, you can view the failed tasks related to a cluster, such as failing to create, restart, scale out, back up, or restore a cluster. In addition, you can view the failure cause of each task and choose to delete a single or all failed tasks.

## Viewing Failed Tasks<a name="section1393913131117"></a>

1.  Log in to the CSS management console.
2.  Click  **Clusters**  to switch to the  **Clusters**  page. Click the digit next to  **Failed Tasks**  to switch to the  **Failed Tasks**  dialog box.

    **Figure  1**  Clicking the digit next to Failed Tasks<a name="fig9871436121212"></a>  
    ![](figures/clicking-the-digit-next-to-failed-tasks.png "clicking-the-digit-next-to-failed-tasks")

3.  The  **Failed Tasks**  dialog box presents all failed tasks of the current account. The following information about the failed tasks is displayed:  **Name/ID**,  **Task Status**, and  **Failure Time**.
4.  View the failure cause of a task. Specifically, click the question mark in the  **Task Status**  column to view the failure cause of a task. You are advised to troubleshoot faults based on failure causes. For details about failure causes, see  [Error Code](#section155001521193312).

    **Figure  2**  Viewing the failure cause of a task<a name="fig85418382253"></a>  
    ![](figures/viewing-the-failure-cause-of-a-task.png "viewing-the-failure-cause-of-a-task")


## Deleting a Failed Task<a name="section82881811133120"></a>

You can delete a single failed task or all failed tasks at a time.

-   To delete a failed task, perform the following operations: Locate the row where the target task resides and click  **Delete**  in the  **Operation**  column. In the displayed dialog box, confirm the task you want to delete and click  **Yes**.
-   To delete all failed tasks, perform the following operations: In the  **Failed Tasks**  dialog box, click  **Delete All**. In the displayed dialog box, confirm the information about all failed tasks and click  **Yes**.

**Figure  3**  Deleting a failed task<a name="fig1419120710386"></a>  
![](figures/deleting-a-failed-task.png "deleting-a-failed-task")

## Error Code<a name="section155001521193312"></a>

**Table  1**  Failure causes

<a name="table16751996354"></a>
<table><thead align="left"><tr id="row376129113519"><th class="cellrowborder" valign="top" width="21.512151215121513%" id="mcps1.2.4.1.1"><p id="p19760913357"><a name="p19760913357"></a><a name="p19760913357"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="37.75377537753775%" id="mcps1.2.4.1.2"><p id="p147612903518"><a name="p147612903518"></a><a name="p147612903518"></a>Failure Cause</p>
</th>
<th class="cellrowborder" valign="top" width="40.73407340734073%" id="mcps1.2.4.1.3"><p id="p14768953516"><a name="p14768953516"></a><a name="p14768953516"></a>Solution</p>
</th>
</tr>
</thead>
<tbody><tr id="row6761895353"><td class="cellrowborder" valign="top" width="21.512151215121513%" headers="mcps1.2.4.1.1 "><p id="p776189183515"><a name="p776189183515"></a><a name="p776189183515"></a>CSS.6000</p>
</td>
<td class="cellrowborder" valign="top" width="37.75377537753775%" headers="mcps1.2.4.1.2 "><p id="p187669193511"><a name="p187669193511"></a><a name="p187669193511"></a>Failed to create the cluster because of an internal error. Please contact customer service or try again later.</p>
</td>
<td class="cellrowborder" rowspan="7" valign="top" width="40.73407340734073%" headers="mcps1.2.4.1.3 "><p id="p1637191311276"><a name="p1637191311276"></a><a name="p1637191311276"></a>Try again later or contact customer service.</p>
</td>
</tr>
<tr id="row47649143514"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1576697352"><a name="p1576697352"></a><a name="p1576697352"></a>CSS.6001</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p77659123520"><a name="p77659123520"></a><a name="p77659123520"></a>Failed to scale out the cluster because of an internal error. Please contact customer service or try again later.</p>
</td>
</tr>
<tr id="row187619910350"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p16765915350"><a name="p16765915350"></a><a name="p16765915350"></a>CSS.6002</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p187619903516"><a name="p187619903516"></a><a name="p187619903516"></a>Failed to restart the cluster because of an internal error. Please contact customer service or try again later.</p>
</td>
</tr>
<tr id="row14425154151017"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p242564121017"><a name="p242564121017"></a><a name="p242564121017"></a>CSS.6003</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p7426104201017"><a name="p7426104201017"></a><a name="p7426104201017"></a>Failed to restore the cluster because of an internal error. Please contact customer service or try again later.</p>
</td>
</tr>
<tr id="row24264471015"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p194264418104"><a name="p194264418104"></a><a name="p194264418104"></a>CSS.6004</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p242694121018"><a name="p242694121018"></a><a name="p242694121018"></a>Failed to create the node because of ECS exceptions (<em id="i62088384145"><a name="i62088384145"></a><a name="i62088384145"></a>&lt;ECS error code&gt;</em>). Please contact customer service or try again later.</p>
<div class="note" id="note07226420147"><a name="note07226420147"></a><a name="note07226420147"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1072324216145"><a name="p1072324216145"></a><a name="p1072324216145"></a><em id="i1543285813142"><a name="i1543285813142"></a><a name="i1543285813142"></a>&lt;ECS error code&gt;</em> indicates the error information reported by ECS. For details about the cause and solution, see <a href="https://docs.otc.t-systems.com/en-us/api/ecs/en-us_topic_0022067717.html" target="_blank" rel="noopener noreferrer">ECS Error Code Description</a>.</p>
</div></div>
</td>
</tr>
<tr id="row144265410104"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1942618413108"><a name="p1942618413108"></a><a name="p1942618413108"></a>CSS.6005</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p154263461017"><a name="p154263461017"></a><a name="p154263461017"></a>Failed to initialize the service because of an internal error. Please contact customer service or try again later.</p>
</td>
</tr>
<tr id="row10480192161116"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p12480202121111"><a name="p12480202121111"></a><a name="p12480202121111"></a>CSS.6007</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p4480102191117"><a name="p4480102191117"></a><a name="p4480102191117"></a>Failed to create the snapshot because of an internal error. Please contact customer service or try again later.</p>
</td>
</tr>
<tr id="row1448012191118"><td class="cellrowborder" valign="top" width="21.512151215121513%" headers="mcps1.2.4.1.1 "><p id="p124817211119"><a name="p124817211119"></a><a name="p124817211119"></a>CSS.6008</p>
</td>
<td class="cellrowborder" valign="top" width="37.75377537753775%" headers="mcps1.2.4.1.2 "><p id="p8481421171113"><a name="p8481421171113"></a><a name="p8481421171113"></a>Failed to create the snapshot because the OBS bucket you select does not exist or has been deleted.</p>
</td>
<td class="cellrowborder" rowspan="3" valign="top" width="40.73407340734073%" headers="mcps1.2.4.1.3 "><p id="p2075718196277"><a name="p2075718196277"></a><a name="p2075718196277"></a>Modify the OBS bucket.</p>
</td>
</tr>
<tr id="row7481721141112"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p134819217111"><a name="p134819217111"></a><a name="p134819217111"></a>CSS.6009</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1148192161110"><a name="p1148192161110"></a><a name="p1148192161110"></a>Failed to restore the snapshot because the OBS bucket you select does not exist or has been deleted.</p>
</td>
</tr>
<tr id="row1770913013172"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p16709501175"><a name="p16709501175"></a><a name="p16709501175"></a>CSS.6010</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p87094071710"><a name="p87094071710"></a><a name="p87094071710"></a>Failed to restore the snapshot because the OBS object does not exist or has been deleted.</p>
</td>
</tr>
</tbody>
</table>


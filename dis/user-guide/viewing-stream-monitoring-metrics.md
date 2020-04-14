# Viewing Stream Monitoring Metrics<a name="dis_01_0012"></a>

You can view stream monitoring metrics on the DIS console.

1.  Use the account to log in to the DIS console.
2.  Click  ![](figures/dt_mrs_project_region_image01.png)  in the upper left corner and select  **Region**  and  **Project**.
3.  In the navigation tree on the left, choose  **Ingestion Management**  \>  **Stream Management**.
4.  In the stream list, click the name of the DIS stream whose monitoring metrics will be viewed. The monitoring page is displayed.

    **Figure  1**  Monitoring page<a name="fig20331141119419"></a>  
    ![](figures/monitoring-page.jpg "monitoring-page")

5.  On the  **Monitoring**  page, click the  **Streams**  or  **Partitions**  tab to view stream or partition monitoring metrics.  [Table 1](#table2942144318834)  describes the monitoring parameters. For details about basic stream information, see  [3](step-1-creating-a-dis-stream.md#li23032735111458).

    **Table  1**  DIS monitoring information

    <a name="table2942144318834"></a>
    <table><thead align="left"><tr id="row6686704018834"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p4752119818834"><a name="p4752119818834"></a><a name="p4752119818834"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p2401184018834"><a name="p2401184018834"></a><a name="p2401184018834"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5291185918834"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p5800220418834"><a name="p5800220418834"></a><a name="p5800220418834"></a>Time Range</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><a name="ul210231152417"></a><a name="ul210231152417"></a><ul id="ul210231152417"><li>Monitoring time range.<p id="p502247718834"><a name="p502247718834"></a><a name="p502247718834"></a>Values:</p>
    <a name="ul4520229418834"></a><a name="ul4520229418834"></a><ul id="ul4520229418834"><li>1h</li><li>2h</li><li>3h</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row1818369818834"><td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.3.1.1 mcps1.2.3.1.2 "><p id="p6359345318834"><a name="p6359345318834"></a><a name="p6359345318834"></a><strong id="b55711300181416"><a name="b55711300181416"></a><a name="b55711300181416"></a>Partitions</strong></p>
    </td>
    </tr>
    <tr id="row5079608118834"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p2084186018834"><a name="p2084186018834"></a><a name="p2084186018834"></a>Partition ID</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p1046913718834"><a name="p1046913718834"></a><a name="p1046913718834"></a>ID of the partition. It starts from 0 by default.</p>
    <p id="p2711337218834"><a name="p2711337218834"></a><a name="p2711337218834"></a>Select any of the following values from the <strong id="b15659981181416"><a name="b15659981181416"></a><a name="b15659981181416"></a>Partition ID</strong> drop-down.</p>
    </td>
    </tr>
    <tr id="row4437627918834"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p3770887818834"><a name="p3770887818834"></a><a name="p3770887818834"></a>Data Rate (KB/s)</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p3452024018834"><a name="p3452024018834"></a><a name="p3452024018834"></a>Rates at which data is sent to and retrieved from the chosen partition within the specified time range.</p>
    <p id="p4224671018834"><a name="p4224671018834"></a><a name="p4224671018834"></a>Unit: KB/s</p>
    </td>
    </tr>
    <tr id="row4467607118834"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p6199202718834"><a name="p6199202718834"></a><a name="p6199202718834"></a>Records Per Second</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p5529829118834"><a name="p5529829118834"></a><a name="p5529829118834"></a>The number of records sent to and retrieved from the chosen partition within the specified time range.</p>
    <p id="p2792257618834"><a name="p2792257618834"></a><a name="p2792257618834"></a>  </p>
    </td>
    </tr>
    <tr id="row4997660018834"><td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.3.1.1 mcps1.2.3.1.2 "><p id="p2157278518834"><a name="p2157278518834"></a><a name="p2157278518834"></a><strong id="b12291253161026"><a name="b12291253161026"></a><a name="b12291253161026"></a>Streams</strong></p>
    </td>
    </tr>
    <tr id="row256515918834"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p645129718834"><a name="p645129718834"></a><a name="p645129718834"></a>Data Rate (KB/s)</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p5279303118834"><a name="p5279303118834"></a><a name="p5279303118834"></a>Rates at which data is sent to and retrieved from the chosen DIS stream within the specified time range.</p>
    <p id="p537523918834"><a name="p537523918834"></a><a name="p537523918834"></a>Unit: KB/s</p>
    </td>
    </tr>
    <tr id="row4837715518834"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p2623545018834"><a name="p2623545018834"></a><a name="p2623545018834"></a>Records Per Second</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p4469672618834"><a name="p4469672618834"></a><a name="p4469672618834"></a>The number of records sent to and retrieved from the chosen DIS stream within the specified time range.</p>
    <p id="p6672622218834"><a name="p6672622218834"></a><a name="p6672622218834"></a>   </p>
    </td>
    </tr>
    <tr id="row6366508718834"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p5659842818834"><a name="p5659842818834"></a><a name="p5659842818834"></a>Successful Requests Per Second</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p2106997418834"><a name="p2106997418834"></a><a name="p2106997418834"></a>The number of PutRecords and GetRecords requests successfully fulfilled within the specified time range.</p>
    <p id="p5541204118834"><a name="p5541204118834"></a><a name="p5541204118834"></a>    </p>
    </td>
    </tr>
    <tr id="row2894632418834"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p6295091118834"><a name="p6295091118834"></a><a name="p6295091118834"></a>Throttled Requests Per Second</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p6585900618834"><a name="p6585900618834"></a><a name="p6585900618834"></a>The number of PutRecords and GetRecords requests rejected within the specified time range due to flow control.</p>
    <p id="p5586014518834"><a name="p5586014518834"></a><a name="p5586014518834"></a> </p>
    </td>
    </tr>
    <tr id="row3297925818834"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p5407420218834"><a name="p5407420218834"></a><a name="p5407420218834"></a>Average Request Processing Time (ms)</p>
    </td>
    <td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p1793421418834"><a name="p1793421418834"></a><a name="p1793421418834"></a>The average amount of time spent in processing a PutRecords or GetRecords request.</p>
    <p id="p2719020518834"><a name="p2719020518834"></a><a name="p2719020518834"></a>  </p>
    </td>
    </tr>
    </tbody>
    </table>



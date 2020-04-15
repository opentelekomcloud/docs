# Adding a Graph<a name="EN-US_TOPIC_0084572190"></a>

After a panel is created, you can add graphs to the panel to monitor cloud services. Currently, each panel supports a maximum of 24 graphs.

You can add a maximum of 20 metrics to one graph. Monitoring comparison between different services, dimensions, and metrics is supported.

## Procedure<a name="section57517183151922"></a>

1.  Log in to the management console.
2.  In the upper left corner, select a region and a project.
3.  Under  **Management & Deployment**, select  **Cloud Eye**.

1.  Choose  **Dashboard**  \>  **Monitoring Panels**, switch to the desired panel, and click  ![](figures/add.png)  or  **Add Graph**.

    The  **Add Graph**  window is displayed.

2.  Set parameters based on  [Table 1](#table49303610201913).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >When adding graphs, you must specify  **Resource Type**,  **Dimension**,  **Monitored Object**, and  **Metric**  one by one from left to right.  

    **Table  1**  Parameters

    <a name="table49303610201913"></a>
    <table><thead align="left"><tr id="row45163464201913"><th class="cellrowborder" valign="top" width="24.240000000000002%" id="mcps1.2.3.1.1"><p id="p40822227201913"><a name="p40822227201913"></a><a name="p40822227201913"></a><strong id="b1994854291953"><a name="b1994854291953"></a><a name="b1994854291953"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="75.76%" id="mcps1.2.3.1.2"><p id="p18266111201913"><a name="p18266111201913"></a><a name="p18266111201913"></a><strong id="b521920591953"><a name="b521920591953"></a><a name="b521920591953"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6669499513283"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.3.1.1 "><p id="p6870278132834"><a name="p6870278132834"></a><a name="p6870278132834"></a>Title</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.76%" headers="mcps1.2.3.1.2 "><p id="p19621674132834"><a name="p19621674132834"></a><a name="p19621674132834"></a>Specifies the title of the graph to be added. Only letters, digits, underscores (_), and hyphens (-) are allowed.</p>
    <p id="p128567468134"><a name="p128567468134"></a><a name="p128567468134"></a>Example value: widget-axaj</p>
    </td>
    </tr>
    <tr id="row28440509201913"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.3.1.1 "><p id="p21979859201913"><a name="p21979859201913"></a><a name="p21979859201913"></a>Resource Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.76%" headers="mcps1.2.3.1.2 "><p id="p35538154201913"><a name="p35538154201913"></a><a name="p35538154201913"></a>Specifies the type of the resource to be monitored.</p>
    <p id="p11644723141314"><a name="p11644723141314"></a><a name="p11644723141314"></a>Example value: <strong id="b23205568488"><a name="b23205568488"></a><a name="b23205568488"></a>Elastic Cloud Server</strong></p>
    </td>
    </tr>
    <tr id="row3263078104332"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.3.1.1 "><p id="p48647122104335"><a name="p48647122104335"></a><a name="p48647122104335"></a>Dimension</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.76%" headers="mcps1.2.3.1.2 "><p id="p48102820104335"><a name="p48102820104335"></a><a name="p48102820104335"></a>Specifies the metric dimension.</p>
    <p id="p113831532121317"><a name="p113831532121317"></a><a name="p113831532121317"></a>Example value: <strong id="b457400151813"><a name="b457400151813"></a><a name="b457400151813"></a>ECS</strong></p>
    </td>
    </tr>
    <tr id="row4738957214147"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.3.1.1 "><p id="p5938641614154"><a name="p5938641614154"></a><a name="p5938641614154"></a>Monitored Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.76%" headers="mcps1.2.3.1.2 "><p id="p4557041614154"><a name="p4557041614154"></a><a name="p4557041614154"></a>Specifies the object to be monitored.</p>
    <p id="p15435131138"><a name="p15435131138"></a><a name="p15435131138"></a>You can select multiple monitoring objects at a time.</p>
    </td>
    </tr>
    <tr id="row3293048201913"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.3.1.1 "><p id="p65410311201913"><a name="p65410311201913"></a><a name="p65410311201913"></a>Metric</p>
    </td>
    <td class="cellrowborder" valign="top" width="75.76%" headers="mcps1.2.3.1.2 "><p id="p63743827201913"><a name="p63743827201913"></a><a name="p63743827201913"></a>Specifies the metric name.</p>
    <p id="p1879315051419"><a name="p1879315051419"></a><a name="p1879315051419"></a>Example value: CPU Usage</p>
    </td>
    </tr>
    </tbody>
    </table>

3.  Click  **OK**.

    On the selected panel, you can view the trends of the new graph. If you hover your mouse on the graph and click  ![](figures/enlarge-3.3.png), you can view detailed metric data comparison.



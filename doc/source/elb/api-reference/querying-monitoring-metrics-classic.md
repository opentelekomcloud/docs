# Querying Monitoring Metrics<a name="EN-US_TOPIC_0096561528"></a>

## Function<a name="en-us_topic_0078894912_section3721136181744"></a>

This API is used to query all Layer-4 and Layer-7 traffic monitoring metrics.

Only common tenants can query these monitoring metrics.

## URI<a name="en-us_topic_0078894912_section13632893181751"></a>

GET /v1.0/\{project\_id\}/elbaas/monitor

**Table  1**  Parameter description

<a name="en-us_topic_0078894912_table60560348181313"></a>
<table><thead align="left"><tr id="en-us_topic_0078894912_row48803910181313"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.1"><p id="en-us_topic_0078894912_p60802653181313"><a name="en-us_topic_0078894912_p60802653181313"></a><a name="en-us_topic_0078894912_p60802653181313"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="en-us_topic_0078894912_p26067889181313"><a name="en-us_topic_0078894912_p26067889181313"></a><a name="en-us_topic_0078894912_p26067889181313"></a><strong id="en-us_topic_0078894912_b842352706192244"><a name="en-us_topic_0078894912_b842352706192244"></a><a name="en-us_topic_0078894912_b842352706192244"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="en-us_topic_0078894912_p18965123823512"><a name="en-us_topic_0078894912_p18965123823512"></a><a name="en-us_topic_0078894912_p18965123823512"></a><strong id="en-us_topic_0078894912_b84235270615453"><a name="en-us_topic_0078894912_b84235270615453"></a><a name="en-us_topic_0078894912_b84235270615453"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.2.5.1.4"><p id="en-us_topic_0078894912_p31124265181313"><a name="en-us_topic_0078894912_p31124265181313"></a><a name="en-us_topic_0078894912_p31124265181313"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0078894912_row38037550181313"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0078894912_p101243509202"><a name="en-us_topic_0078894912_p101243509202"></a><a name="en-us_topic_0078894912_p101243509202"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0078894912_p53611261181313"><a name="en-us_topic_0078894912_p53611261181313"></a><a name="en-us_topic_0078894912_p53611261181313"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0078894912_p2965203833517"><a name="en-us_topic_0078894912_p2965203833517"></a><a name="en-us_topic_0078894912_p2965203833517"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0078894912_p47544855181313"><a name="en-us_topic_0078894912_p47544855181313"></a><a name="en-us_topic_0078894912_p47544855181313"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0078894912_section162044416434"></a>

-   Request parameters

    None


-   Example request

    None


## Response<a name="en-us_topic_0078894912_section4588471118184"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="en-us_topic_0078894912_table62283620181930"></a>
    <table><thead align="left"><tr id="en-us_topic_0078894912_row31440513181930"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.1"><p id="en-us_topic_0078894912_p63653606181930"><a name="en-us_topic_0078894912_p63653606181930"></a><a name="en-us_topic_0078894912_p63653606181930"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.2"><p id="en-us_topic_0078894912_p55668476181930"><a name="en-us_topic_0078894912_p55668476181930"></a><a name="en-us_topic_0078894912_p55668476181930"></a><strong id="b876476925"><a name="b876476925"></a><a name="b876476925"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="69%" id="mcps1.2.4.1.3"><p id="en-us_topic_0078894912_p12852714181930"><a name="en-us_topic_0078894912_p12852714181930"></a><a name="en-us_topic_0078894912_p12852714181930"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0078894912_row34436953181930"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0078894912_p37929841181930"><a name="en-us_topic_0078894912_p37929841181930"></a><a name="en-us_topic_0078894912_p37929841181930"></a>act_conn</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0078894912_p52418265181930"><a name="en-us_topic_0078894912_p52418265181930"></a><a name="en-us_topic_0078894912_p52418265181930"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="69%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0078894912_p24401955171535"><a name="en-us_topic_0078894912_p24401955171535"></a><a name="en-us_topic_0078894912_p24401955171535"></a>Specifies the number of active connections.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894912_row27971718181930"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0078894912_p51116686181930"><a name="en-us_topic_0078894912_p51116686181930"></a><a name="en-us_topic_0078894912_p51116686181930"></a>cps</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0078894912_p46810915181930"><a name="en-us_topic_0078894912_p46810915181930"></a><a name="en-us_topic_0078894912_p46810915181930"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="69%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0078894912_p4755129171545"><a name="en-us_topic_0078894912_p4755129171545"></a><a name="en-us_topic_0078894912_p4755129171545"></a>Specifies the number of concurrent connections.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894912_row33854352181930"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0078894912_p57847971181930"><a name="en-us_topic_0078894912_p57847971181930"></a><a name="en-us_topic_0078894912_p57847971181930"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0078894912_p55174046181930"><a name="en-us_topic_0078894912_p55174046181930"></a><a name="en-us_topic_0078894912_p55174046181930"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0078894912_p39912746181930"><a name="en-us_topic_0078894912_p39912746181930"></a><a name="en-us_topic_0078894912_p39912746181930"></a>Specifies the report time.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894912_row23670398181930"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0078894912_p38254053181930"><a name="en-us_topic_0078894912_p38254053181930"></a><a name="en-us_topic_0078894912_p38254053181930"></a>in_Bps</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0078894912_p11570609181930"><a name="en-us_topic_0078894912_p11570609181930"></a><a name="en-us_topic_0078894912_p11570609181930"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="69%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0078894912_p64804170181930"><a name="en-us_topic_0078894912_p64804170181930"></a><a name="en-us_topic_0078894912_p64804170181930"></a>Specifies the inbound rate (bytes/s).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894912_row46366623181930"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0078894912_p64708949181930"><a name="en-us_topic_0078894912_p64708949181930"></a><a name="en-us_topic_0078894912_p64708949181930"></a>in_pps</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0078894912_p6933516181930"><a name="en-us_topic_0078894912_p6933516181930"></a><a name="en-us_topic_0078894912_p6933516181930"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="69%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0078894912_p24743915181930"><a name="en-us_topic_0078894912_p24743915181930"></a><a name="en-us_topic_0078894912_p24743915181930"></a>Specifies the number of incoming data packets.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894912_row21368650181930"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0078894912_p53139065181930"><a name="en-us_topic_0078894912_p53139065181930"></a><a name="en-us_topic_0078894912_p53139065181930"></a>inact_conn</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0078894912_p9296997181930"><a name="en-us_topic_0078894912_p9296997181930"></a><a name="en-us_topic_0078894912_p9296997181930"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="69%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0078894912_p14859253181930"><a name="en-us_topic_0078894912_p14859253181930"></a><a name="en-us_topic_0078894912_p14859253181930"></a>Specifies the number of inactive connections.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894912_row66624414181930"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0078894912_p27868448181930"><a name="en-us_topic_0078894912_p27868448181930"></a><a name="en-us_topic_0078894912_p27868448181930"></a>loadbalancer_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0078894912_p42751802181930"><a name="en-us_topic_0078894912_p42751802181930"></a><a name="en-us_topic_0078894912_p42751802181930"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0078894912_p40343957181930"><a name="en-us_topic_0078894912_p40343957181930"></a><a name="en-us_topic_0078894912_p40343957181930"></a>Specifies the load balancer ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894912_row27551298181930"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0078894912_p17062689181930"><a name="en-us_topic_0078894912_p17062689181930"></a><a name="en-us_topic_0078894912_p17062689181930"></a>loadbalancer_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0078894912_p39900564181930"><a name="en-us_topic_0078894912_p39900564181930"></a><a name="en-us_topic_0078894912_p39900564181930"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0078894912_p10720260181930"><a name="en-us_topic_0078894912_p10720260181930"></a><a name="en-us_topic_0078894912_p10720260181930"></a>Specifies the load balancer IP address.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894912_row29373478181930"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0078894912_p30441499181930"><a name="en-us_topic_0078894912_p30441499181930"></a><a name="en-us_topic_0078894912_p30441499181930"></a>loadbalancer_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0078894912_p49842369181930"><a name="en-us_topic_0078894912_p49842369181930"></a><a name="en-us_topic_0078894912_p49842369181930"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="69%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0078894912_p10700095181930"><a name="en-us_topic_0078894912_p10700095181930"></a><a name="en-us_topic_0078894912_p10700095181930"></a>Specifies the load balancer name.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894912_row29191999181930"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0078894912_p15741750181930"><a name="en-us_topic_0078894912_p15741750181930"></a><a name="en-us_topic_0078894912_p15741750181930"></a>ncps</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0078894912_p13336181930"><a name="en-us_topic_0078894912_p13336181930"></a><a name="en-us_topic_0078894912_p13336181930"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="69%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0078894912_p1080271181930"><a name="en-us_topic_0078894912_p1080271181930"></a><a name="en-us_topic_0078894912_p1080271181930"></a>Specifies the number of new connections.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894912_row9722446181930"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0078894912_p49320671181930"><a name="en-us_topic_0078894912_p49320671181930"></a><a name="en-us_topic_0078894912_p49320671181930"></a>out_Bps</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0078894912_p35551416181930"><a name="en-us_topic_0078894912_p35551416181930"></a><a name="en-us_topic_0078894912_p35551416181930"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="69%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0078894912_p61092482181930"><a name="en-us_topic_0078894912_p61092482181930"></a><a name="en-us_topic_0078894912_p61092482181930"></a>Specifies the outbound rate (bytes/s).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0078894912_row12961433181930"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0078894912_p43243151181930"><a name="en-us_topic_0078894912_p43243151181930"></a><a name="en-us_topic_0078894912_p43243151181930"></a>out_pps</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0078894912_p13034313181930"><a name="en-us_topic_0078894912_p13034313181930"></a><a name="en-us_topic_0078894912_p13034313181930"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="69%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0078894912_p49146415181930"><a name="en-us_topic_0078894912_p49146415181930"></a><a name="en-us_topic_0078894912_p49146415181930"></a>Specifies the number of outgoing data packets.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    [ 
          { 
              "act_conn": 0,
              "cps": 0,
              "create_time": "2016-05-20 16:46:49",
              "in_Bps": 0,
              "in_pps": 0,
              "inact_conn": 0,
              "loadbalancer_id": "34cf6520808d4766ae1455586ab94ba8",
              "loadbalancer_ip": "10.10.1.233",
              "loadbalancer_name": "lb0721",
              "ncps": 0,
              "out_Bps": 0,
              "out_pps": 0
           },
           {
              "act_conn": 0,
              "cps": 0,
              "create_time": "2016-05-20 16:46:49",
              "in_Bps": 0,
              "in_pps": 0,
              "inact_conn": 0,
              "loadbalancer_id": "b44533cce271437bb692365b0c450543",
              "loadbalancer_ip": "10.10.1.253",
              "loadbalancer_name": "lb0721",
              "ncps": 0,
              "out_Bps": 0,
              "out_pps": 0
           }
    ]
    ```



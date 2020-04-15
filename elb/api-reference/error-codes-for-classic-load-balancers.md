# Error Codes for Classic Load Balancers<a name="EN-US_TOPIC_0109639182"></a>

The following error code descriptions are only suitable for classic load balancers.

## Overview<a name="section57523910111232"></a>

If an error occurs when using an API, an error response will be returned, which contains the error code and a piece of message, as shown in the following example. The following table lists error codes and their descriptions.

## Example of Returned Error Information<a name="section967574811132"></a>

```
{ 
    "error": 
    { 
    "message": "listener exist, the port repeat", 
    "code": "ELB.6101" 
    } 
}
```

## Error Codes<a name="section25870391111328"></a>

**Table  1**  Error codes

<a name="en-us_topic_0020311892_table1026432311165"></a>
<table><thead align="left"><tr id="en-us_topic_0020311892_row527044611165"><th class="cellrowborder" valign="top" width="9%" id="mcps1.2.7.1.1"><p id="en-us_topic_0020311892_p23519942111442"><a name="en-us_topic_0020311892_p23519942111442"></a><a name="en-us_topic_0020311892_p23519942111442"></a>Module</p>
</th>
<th class="cellrowborder" valign="top" width="11.15%" id="mcps1.2.7.1.2"><p id="en-us_topic_0020311892_p23357924111433"><a name="en-us_topic_0020311892_p23357924111433"></a><a name="en-us_topic_0020311892_p23357924111433"></a>HTTP Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="15.559999999999999%" id="mcps1.2.7.1.3"><p id="en-us_topic_0020311892_p1833382111165"><a name="en-us_topic_0020311892_p1833382111165"></a><a name="en-us_topic_0020311892_p1833382111165"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="21.46%" id="mcps1.2.7.1.4"><p id="en-us_topic_0020311892_p54081360112548"><a name="en-us_topic_0020311892_p54081360112548"></a><a name="en-us_topic_0020311892_p54081360112548"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="24.03%" id="mcps1.2.7.1.5"><p id="en-us_topic_0020311892_p6596329011260"><a name="en-us_topic_0020311892_p6596329011260"></a><a name="en-us_topic_0020311892_p6596329011260"></a>Error Message</p>
</th>
<th class="cellrowborder" valign="top" width="18.8%" id="mcps1.2.7.1.6"><p id="en-us_topic_0020311892_p33505572112628"><a name="en-us_topic_0020311892_p33505572112628"></a><a name="en-us_topic_0020311892_p33505572112628"></a>Solution</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020311892_row48144891191210"><td class="cellrowborder" rowspan="7" valign="top" width="9%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p1684728111643"><a name="en-us_topic_0020311892_p1684728111643"></a><a name="en-us_topic_0020311892_p1684728111643"></a>Common part</p>
</td>
<td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p12943655111433"><a name="en-us_topic_0020311892_p12943655111433"></a><a name="en-us_topic_0020311892_p12943655111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p26760620191229"><a name="en-us_topic_0020311892_p26760620191229"></a><a name="en-us_topic_0020311892_p26760620191229"></a>ELB.0002</p>
</td>
<td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p20126600191229"><a name="en-us_topic_0020311892_p20126600191229"></a><a name="en-us_topic_0020311892_p20126600191229"></a>The request is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="24.03%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p53078098113015"><a name="en-us_topic_0020311892_p53078098113015"></a><a name="en-us_topic_0020311892_p53078098113015"></a>Api request is null.</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0020311892_p39227779113015"><a name="en-us_topic_0020311892_p39227779113015"></a><a name="en-us_topic_0020311892_p39227779113015"></a>Correct the parameter settings and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row2499000919126"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p41803172111433"><a name="en-us_topic_0020311892_p41803172111433"></a><a name="en-us_topic_0020311892_p41803172111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p42559049191229"><a name="en-us_topic_0020311892_p42559049191229"></a><a name="en-us_topic_0020311892_p42559049191229"></a>ELB.0004</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p24730939191229"><a name="en-us_topic_0020311892_p24730939191229"></a><a name="en-us_topic_0020311892_p24730939191229"></a>The response is empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p8675135113015"><a name="en-us_topic_0020311892_p8675135113015"></a><a name="en-us_topic_0020311892_p8675135113015"></a>Api response is null or invaild.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p15940906113015"><a name="en-us_topic_0020311892_p15940906113015"></a><a name="en-us_topic_0020311892_p15940906113015"></a>Check whether the backend ECS is running properly and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row61353763191955"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p30613761111433"><a name="en-us_topic_0020311892_p30613761111433"></a><a name="en-us_topic_0020311892_p30613761111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p43326621191957"><a name="en-us_topic_0020311892_p43326621191957"></a><a name="en-us_topic_0020311892_p43326621191957"></a>ELB.0230</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p19795394191957"><a name="en-us_topic_0020311892_p19795394191957"></a><a name="en-us_topic_0020311892_p19795394191957"></a>The project ID is left blank.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p11087470113015"><a name="en-us_topic_0020311892_p11087470113015"></a><a name="en-us_topic_0020311892_p11087470113015"></a>Tenant_id is empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p29702270113015"><a name="en-us_topic_0020311892_p29702270113015"></a><a name="en-us_topic_0020311892_p29702270113015"></a>Correct the project ID and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row2911991911165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p63795558111433"><a name="en-us_topic_0020311892_p63795558111433"></a><a name="en-us_topic_0020311892_p63795558111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p6396173011165"><a name="en-us_topic_0020311892_p6396173011165"></a><a name="en-us_topic_0020311892_p6396173011165"></a>ELB.1000</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p669896591258"><a name="en-us_topic_0020311892_p669896591258"></a><a name="en-us_topic_0020311892_p669896591258"></a>The URL length exceeds the limit.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p59926198113015"><a name="en-us_topic_0020311892_p59926198113015"></a><a name="en-us_topic_0020311892_p59926198113015"></a>The loadbalancer URL is too long.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p65437164113015"><a name="en-us_topic_0020311892_p65437164113015"></a><a name="en-us_topic_0020311892_p65437164113015"></a>Correct the URL and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row5454979411165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p57724111433"><a name="en-us_topic_0020311892_p57724111433"></a><a name="en-us_topic_0020311892_p57724111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p5645720411165"><a name="en-us_topic_0020311892_p5645720411165"></a><a name="en-us_topic_0020311892_p5645720411165"></a>ELB.1010</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p963083511165"><a name="en-us_topic_0020311892_p963083511165"></a><a name="en-us_topic_0020311892_p963083511165"></a>Failed to query the quota.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p56399755113015"><a name="en-us_topic_0020311892_p56399755113015"></a><a name="en-us_topic_0020311892_p56399755113015"></a>Query elb quota error.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p44796844113015"><a name="en-us_topic_0020311892_p44796844113015"></a><a name="en-us_topic_0020311892_p44796844113015"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row1956865411165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p4675690111433"><a name="en-us_topic_0020311892_p4675690111433"></a><a name="en-us_topic_0020311892_p4675690111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p4155717911165"><a name="en-us_topic_0020311892_p4155717911165"></a><a name="en-us_topic_0020311892_p4155717911165"></a>ELB.1020</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p1068832811165"><a name="en-us_topic_0020311892_p1068832811165"></a><a name="en-us_topic_0020311892_p1068832811165"></a>Incorrect load balancer ID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p41991988113015"><a name="en-us_topic_0020311892_p41991988113015"></a><a name="en-us_topic_0020311892_p41991988113015"></a>Lb ID is not correct.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p45907869113015"><a name="en-us_topic_0020311892_p45907869113015"></a><a name="en-us_topic_0020311892_p45907869113015"></a>Correct the parameter settings and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row2908609011165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p43186649111433"><a name="en-us_topic_0020311892_p43186649111433"></a><a name="en-us_topic_0020311892_p43186649111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p716308311165"><a name="en-us_topic_0020311892_p716308311165"></a><a name="en-us_topic_0020311892_p716308311165"></a>ELB.1030</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p4333881611165"><a name="en-us_topic_0020311892_p4333881611165"></a><a name="en-us_topic_0020311892_p4333881611165"></a>Incorrect load balancer URL.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p46622902113015"><a name="en-us_topic_0020311892_p46622902113015"></a><a name="en-us_topic_0020311892_p46622902113015"></a>Lb url is not correct.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p31010717113015"><a name="en-us_topic_0020311892_p31010717113015"></a><a name="en-us_topic_0020311892_p31010717113015"></a>Correct the URL and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row6037975411165"><td class="cellrowborder" rowspan="11" valign="top" width="9%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p23776848111651"><a name="en-us_topic_0020311892_p23776848111651"></a><a name="en-us_topic_0020311892_p23776848111651"></a>Creating a load balancer</p>
</td>
<td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p8457713111433"><a name="en-us_topic_0020311892_p8457713111433"></a><a name="en-us_topic_0020311892_p8457713111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p794632511165"><a name="en-us_topic_0020311892_p794632511165"></a><a name="en-us_topic_0020311892_p794632511165"></a>ELB.1001</p>
</td>
<td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p3967258911165"><a name="en-us_topic_0020311892_p3967258911165"></a><a name="en-us_topic_0020311892_p3967258911165"></a>Parameter <strong id="b142533121510"><a name="b142533121510"></a><a name="b142533121510"></a>type</strong>, <strong id="b15266734131515"><a name="b15266734131515"></a><a name="b15266734131515"></a>name</strong>, or <strong id="b55888631911"><a name="b55888631911"></a><a name="b55888631911"></a>admin_status_up</strong> is left blank.</p>
</td>
<td class="cellrowborder" valign="top" width="24.03%" headers="mcps1.2.7.1.5 "><p id="p105231837162913"><a name="p105231837162913"></a><a name="p105231837162913"></a>Request parameters error, private_key or certificate is nil or empty.</p>
<p id="p352983710293"><a name="p352983710293"></a><a name="p352983710293"></a>Request parameters error, lb type, name, admin_state_up one of them is empty.</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0020311892_p4186335911338"><a name="en-us_topic_0020311892_p4186335911338"></a><a name="en-us_topic_0020311892_p4186335911338"></a>Correct the parameter settings and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row2150898611165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p13986137111433"><a name="en-us_topic_0020311892_p13986137111433"></a><a name="en-us_topic_0020311892_p13986137111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p6450634011165"><a name="en-us_topic_0020311892_p6450634011165"></a><a name="en-us_topic_0020311892_p6450634011165"></a>ELB.1001</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p5763107911165"><a name="en-us_topic_0020311892_p5763107911165"></a><a name="en-us_topic_0020311892_p5763107911165"></a>The length of the load balancer name exceeds the limit.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p5096474111338"><a name="en-us_topic_0020311892_p5096474111338"></a><a name="en-us_topic_0020311892_p5096474111338"></a>Request parameter is not valid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p3450333211338"><a name="en-us_topic_0020311892_p3450333211338"></a><a name="en-us_topic_0020311892_p3450333211338"></a>Change the name and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row4891766511165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p59135289111433"><a name="en-us_topic_0020311892_p59135289111433"></a><a name="en-us_topic_0020311892_p59135289111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p290789911165"><a name="en-us_topic_0020311892_p290789911165"></a><a name="en-us_topic_0020311892_p290789911165"></a>ELB.1021</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p3421324911165"><a name="en-us_topic_0020311892_p3421324911165"></a><a name="en-us_topic_0020311892_p3421324911165"></a>Invalid load balancer name.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p7989617"><a name="p7989617"></a><a name="p7989617"></a>Request parameters error, name invalid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p2926950511338"><a name="en-us_topic_0020311892_p2926950511338"></a><a name="en-us_topic_0020311892_p2926950511338"></a>Change the name and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row3948379311165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p25229114111433"><a name="en-us_topic_0020311892_p25229114111433"></a><a name="en-us_topic_0020311892_p25229114111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p4407066111165"><a name="en-us_topic_0020311892_p4407066111165"></a><a name="en-us_topic_0020311892_p4407066111165"></a>ELB.1031</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p1295381811165"><a name="en-us_topic_0020311892_p1295381811165"></a><a name="en-us_topic_0020311892_p1295381811165"></a>The length of the load balancer description exceeds the limit.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p6395956511338"><a name="en-us_topic_0020311892_p6395956511338"></a><a name="en-us_topic_0020311892_p6395956511338"></a>Request parameters error, lb len description too long.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p1334231511338"><a name="en-us_topic_0020311892_p1334231511338"></a><a name="en-us_topic_0020311892_p1334231511338"></a>Change the description and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row4947550411165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p30292355111433"><a name="en-us_topic_0020311892_p30292355111433"></a><a name="en-us_topic_0020311892_p30292355111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p4809292111165"><a name="en-us_topic_0020311892_p4809292111165"></a><a name="en-us_topic_0020311892_p4809292111165"></a>ELB.1041</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p321253411165"><a name="en-us_topic_0020311892_p321253411165"></a><a name="en-us_topic_0020311892_p321253411165"></a>Invalid load balancer type.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p6287167611338"><a name="en-us_topic_0020311892_p6287167611338"></a><a name="en-us_topic_0020311892_p6287167611338"></a>Request parameters error, lb type is not valid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p5944095911338"><a name="en-us_topic_0020311892_p5944095911338"></a><a name="en-us_topic_0020311892_p5944095911338"></a>Correct the parameter setting and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row2891281211165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p37761725111433"><a name="en-us_topic_0020311892_p37761725111433"></a><a name="en-us_topic_0020311892_p37761725111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p6023643511165"><a name="en-us_topic_0020311892_p6023643511165"></a><a name="en-us_topic_0020311892_p6023643511165"></a>ELB.1051</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p4731305811165"><a name="en-us_topic_0020311892_p4731305811165"></a><a name="en-us_topic_0020311892_p4731305811165"></a>Invalid load balancer bandwidth.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p43571489"><a name="p43571489"></a><a name="p43571489"></a>Request parameters error, lb bandwidth is not valid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p143945911338"><a name="en-us_topic_0020311892_p143945911338"></a><a name="en-us_topic_0020311892_p143945911338"></a>Correct the parameter setting and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row2316434511165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p38800912111433"><a name="en-us_topic_0020311892_p38800912111433"></a><a name="en-us_topic_0020311892_p38800912111433"></a>4000</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p6437263211165"><a name="en-us_topic_0020311892_p6437263211165"></a><a name="en-us_topic_0020311892_p6437263211165"></a>ELB.1061</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p4680069211165"><a name="en-us_topic_0020311892_p4680069211165"></a><a name="en-us_topic_0020311892_p4680069211165"></a>The floating IP address or subnet ID is left blank.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p4273294811338"><a name="en-us_topic_0020311892_p4273294811338"></a><a name="en-us_topic_0020311892_p4273294811338"></a>Request parameters error, lb vip_address and vip_subnet_id are nil.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p3881677011338"><a name="en-us_topic_0020311892_p3881677011338"></a><a name="en-us_topic_0020311892_p3881677011338"></a>Correct the parameter setting and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row1855304411165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p55866147111433"><a name="en-us_topic_0020311892_p55866147111433"></a><a name="en-us_topic_0020311892_p55866147111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p2640155711165"><a name="en-us_topic_0020311892_p2640155711165"></a><a name="en-us_topic_0020311892_p2640155711165"></a>ELB.1071</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p5815136711165"><a name="en-us_topic_0020311892_p5815136711165"></a><a name="en-us_topic_0020311892_p5815136711165"></a>Invalid floating IP address.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p4459430511338"><a name="en-us_topic_0020311892_p4459430511338"></a><a name="en-us_topic_0020311892_p4459430511338"></a>Request parameters error, lb vip_address is not valid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p5536891511338"><a name="en-us_topic_0020311892_p5536891511338"></a><a name="en-us_topic_0020311892_p5536891511338"></a>Correct the parameter setting and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row5360025711165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p28864030111433"><a name="en-us_topic_0020311892_p28864030111433"></a><a name="en-us_topic_0020311892_p28864030111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p4665359911165"><a name="en-us_topic_0020311892_p4665359911165"></a><a name="en-us_topic_0020311892_p4665359911165"></a>ELB.1081</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p2084518511165"><a name="en-us_topic_0020311892_p2084518511165"></a><a name="en-us_topic_0020311892_p2084518511165"></a>The VPC ID is left blank.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p3151227311338"><a name="en-us_topic_0020311892_p3151227311338"></a><a name="en-us_topic_0020311892_p3151227311338"></a>Request parameters error, lb vpc_id is empty.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p235733011338"><a name="en-us_topic_0020311892_p235733011338"></a><a name="en-us_topic_0020311892_p235733011338"></a>Correct the parameter setting and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row5338894411165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p56285098111433"><a name="en-us_topic_0020311892_p56285098111433"></a><a name="en-us_topic_0020311892_p56285098111433"></a>403</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p2953717111165"><a name="en-us_topic_0020311892_p2953717111165"></a><a name="en-us_topic_0020311892_p2953717111165"></a>ELB.1091</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p4370068811165"><a name="en-us_topic_0020311892_p4370068811165"></a><a name="en-us_topic_0020311892_p4370068811165"></a>The number of load balancers exceeds the quota.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p4077234711338"><a name="en-us_topic_0020311892_p4077234711338"></a><a name="en-us_topic_0020311892_p4077234711338"></a>Lb number larger than quota.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p1422579611338"><a name="en-us_topic_0020311892_p1422579611338"></a><a name="en-us_topic_0020311892_p1422579611338"></a>Increase the quota or delete unnecessary load balancers, and then deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row5776187511165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p62799086111433"><a name="en-us_topic_0020311892_p62799086111433"></a><a name="en-us_topic_0020311892_p62799086111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p4820027911165"><a name="en-us_topic_0020311892_p4820027911165"></a><a name="en-us_topic_0020311892_p4820027911165"></a>ELB.1101</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p1190852011165"><a name="en-us_topic_0020311892_p1190852011165"></a><a name="en-us_topic_0020311892_p1190852011165"></a>The floating IP address exists.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p3584057111338"><a name="en-us_topic_0020311892_p3584057111338"></a><a name="en-us_topic_0020311892_p3584057111338"></a>Vip address is exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p2242826611338"><a name="en-us_topic_0020311892_p2242826611338"></a><a name="en-us_topic_0020311892_p2242826611338"></a>Enter another floating IP address and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row4006781611165"><td class="cellrowborder" rowspan="3" valign="top" width="9%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p2426767011165"><a name="en-us_topic_0020311892_p2426767011165"></a><a name="en-us_topic_0020311892_p2426767011165"></a>Deleting a load balancer</p>
</td>
<td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p53561235111433"><a name="en-us_topic_0020311892_p53561235111433"></a><a name="en-us_topic_0020311892_p53561235111433"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p1952429311165"><a name="en-us_topic_0020311892_p1952429311165"></a><a name="en-us_topic_0020311892_p1952429311165"></a>ELB.1002</p>
</td>
<td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p3796393311165"><a name="en-us_topic_0020311892_p3796393311165"></a><a name="en-us_topic_0020311892_p3796393311165"></a>The load balancer does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="24.03%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p40666827113518"><a name="en-us_topic_0020311892_p40666827113518"></a><a name="en-us_topic_0020311892_p40666827113518"></a>Find lb failed.</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0020311892_p5678671113518"><a name="en-us_topic_0020311892_p5678671113518"></a><a name="en-us_topic_0020311892_p5678671113518"></a>Change the load balancer ID and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row66205786191714"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p43492801111433"><a name="en-us_topic_0020311892_p43492801111433"></a><a name="en-us_topic_0020311892_p43492801111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p26409720191729"><a name="en-us_topic_0020311892_p26409720191729"></a><a name="en-us_topic_0020311892_p26409720191729"></a>ELB.1008</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p58812567191729"><a name="en-us_topic_0020311892_p58812567191729"></a><a name="en-us_topic_0020311892_p58812567191729"></a>Failed to delete the load balancer.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p46110752113518"><a name="en-us_topic_0020311892_p46110752113518"></a><a name="en-us_topic_0020311892_p46110752113518"></a>There is at least one member under the lb.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p43983438113518"><a name="en-us_topic_0020311892_p43983438113518"></a><a name="en-us_topic_0020311892_p43983438113518"></a>Correct the parameter setting and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row5292010693216"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p33255967111433"><a name="en-us_topic_0020311892_p33255967111433"></a><a name="en-us_topic_0020311892_p33255967111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p5826978393216"><a name="en-us_topic_0020311892_p5826978393216"></a><a name="en-us_topic_0020311892_p5826978393216"></a>ELB.1018</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p2223199693216"><a name="en-us_topic_0020311892_p2223199693216"></a><a name="en-us_topic_0020311892_p2223199693216"></a>The load balancer has backend ECSs added.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p52998893113518"><a name="en-us_topic_0020311892_p52998893113518"></a><a name="en-us_topic_0020311892_p52998893113518"></a>There is at least one member under the lb.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p65051903113518"><a name="en-us_topic_0020311892_p65051903113518"></a><a name="en-us_topic_0020311892_p65051903113518"></a>Correct the parameter setting and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row66243897191757"><td class="cellrowborder" rowspan="5" valign="top" width="9%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p66053032111742"><a name="en-us_topic_0020311892_p66053032111742"></a><a name="en-us_topic_0020311892_p66053032111742"></a>Modifying a load balancer</p>
</td>
<td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p9378773111433"><a name="en-us_topic_0020311892_p9378773111433"></a><a name="en-us_topic_0020311892_p9378773111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p26655022191818"><a name="en-us_topic_0020311892_p26655022191818"></a><a name="en-us_topic_0020311892_p26655022191818"></a>ELB.1005</p>
</td>
<td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p11573177191818"><a name="en-us_topic_0020311892_p11573177191818"></a><a name="en-us_topic_0020311892_p11573177191818"></a>Failed to modify the load balancer.</p>
</td>
<td class="cellrowborder" valign="top" width="24.03%" headers="mcps1.2.7.1.5 "><p id="p29192018"><a name="p29192018"></a><a name="p29192018"></a>Update request paramters error.</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0020311892_p4358413311366"><a name="en-us_topic_0020311892_p4358413311366"></a><a name="en-us_topic_0020311892_p4358413311366"></a>Check the parameters and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row5106716611165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p21483148111433"><a name="en-us_topic_0020311892_p21483148111433"></a><a name="en-us_topic_0020311892_p21483148111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p4279975211165"><a name="en-us_topic_0020311892_p4279975211165"></a><a name="en-us_topic_0020311892_p4279975211165"></a>ELB.1015</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p3119745145548"><a name="en-us_topic_0020311892_p3119745145548"></a><a name="en-us_topic_0020311892_p3119745145548"></a>The load balancer cannot be modified.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p29650864"><a name="p29650864"></a><a name="p29650864"></a>Lb can not be updated.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p4167454311366"><a name="en-us_topic_0020311892_p4167454311366"></a><a name="en-us_topic_0020311892_p4167454311366"></a>Check the parameters and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row6250651811165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p62413419111433"><a name="en-us_topic_0020311892_p62413419111433"></a><a name="en-us_topic_0020311892_p62413419111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p2986319411165"><a name="en-us_topic_0020311892_p2986319411165"></a><a name="en-us_topic_0020311892_p2986319411165"></a>ELB.1025</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p299967911165"><a name="en-us_topic_0020311892_p299967911165"></a><a name="en-us_topic_0020311892_p299967911165"></a>The length of the load balancer name exceeds the limit.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p4753566211366"><a name="en-us_topic_0020311892_p4753566211366"></a><a name="en-us_topic_0020311892_p4753566211366"></a>Udpate request parameters error,name is too long.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p2518338511366"><a name="en-us_topic_0020311892_p2518338511366"></a><a name="en-us_topic_0020311892_p2518338511366"></a>Change the name and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row2699711711165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p22322203111433"><a name="en-us_topic_0020311892_p22322203111433"></a><a name="en-us_topic_0020311892_p22322203111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p3928290211165"><a name="en-us_topic_0020311892_p3928290211165"></a><a name="en-us_topic_0020311892_p3928290211165"></a>ELB.1035</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p2779849911165"><a name="en-us_topic_0020311892_p2779849911165"></a><a name="en-us_topic_0020311892_p2779849911165"></a>Invalid load balancer name.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p45426535"><a name="p45426535"></a><a name="p45426535"></a>Update request parameters error, name is not valid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p5552476011366"><a name="en-us_topic_0020311892_p5552476011366"></a><a name="en-us_topic_0020311892_p5552476011366"></a>Change the name and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row4885990511165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p63268036111433"><a name="en-us_topic_0020311892_p63268036111433"></a><a name="en-us_topic_0020311892_p63268036111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p6533823211165"><a name="en-us_topic_0020311892_p6533823211165"></a><a name="en-us_topic_0020311892_p6533823211165"></a>ELB.1045</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p5790543111165"><a name="en-us_topic_0020311892_p5790543111165"></a><a name="en-us_topic_0020311892_p5790543111165"></a>The length of the load balancer description exceeds the limit.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p1090559611366"><a name="en-us_topic_0020311892_p1090559611366"></a><a name="en-us_topic_0020311892_p1090559611366"></a>Update request parameters error, description too long.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p1093805811366"><a name="en-us_topic_0020311892_p1093805811366"></a><a name="en-us_topic_0020311892_p1093805811366"></a>Change the description and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row5138683811165"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p52358603111442"><a name="en-us_topic_0020311892_p52358603111442"></a><a name="en-us_topic_0020311892_p52358603111442"></a>Querying details of a load balancer</p>
</td>
<td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p24437261111433"><a name="en-us_topic_0020311892_p24437261111433"></a><a name="en-us_topic_0020311892_p24437261111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p6122148911165"><a name="en-us_topic_0020311892_p6122148911165"></a><a name="en-us_topic_0020311892_p6122148911165"></a>ELB.1003</p>
</td>
<td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p5999353711165"><a name="en-us_topic_0020311892_p5999353711165"></a><a name="en-us_topic_0020311892_p5999353711165"></a>The load balancer does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="24.03%" headers="mcps1.2.7.1.5 "><p id="p11791482"><a name="p11791482"></a><a name="p11791482"></a>Lb not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0020311892_p33534675114125"><a name="en-us_topic_0020311892_p33534675114125"></a><a name="en-us_topic_0020311892_p33534675114125"></a>Check the load balancer ID.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row307092211165"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p13188426111442"><a name="en-us_topic_0020311892_p13188426111442"></a><a name="en-us_topic_0020311892_p13188426111442"></a>Querying load balancers</p>
</td>
<td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p33261086111433"><a name="en-us_topic_0020311892_p33261086111433"></a><a name="en-us_topic_0020311892_p33261086111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p1566282211165"><a name="en-us_topic_0020311892_p1566282211165"></a><a name="en-us_topic_0020311892_p1566282211165"></a>ELB.1004</p>
</td>
<td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p6072908911165"><a name="en-us_topic_0020311892_p6072908911165"></a><a name="en-us_topic_0020311892_p6072908911165"></a>Invalid query condition.</p>
</td>
<td class="cellrowborder" valign="top" width="24.03%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p37341647114143"><a name="en-us_topic_0020311892_p37341647114143"></a><a name="en-us_topic_0020311892_p37341647114143"></a>Query condition is not valid.</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0020311892_p4774563114143"><a name="en-us_topic_0020311892_p4774563114143"></a><a name="en-us_topic_0020311892_p4774563114143"></a>Change the query condition and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row969089411165"><td class="cellrowborder" rowspan="5" valign="top" width="9%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p54868046111749"><a name="en-us_topic_0020311892_p54868046111749"></a><a name="en-us_topic_0020311892_p54868046111749"></a>Common part</p>
</td>
<td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p9793440111433"><a name="en-us_topic_0020311892_p9793440111433"></a><a name="en-us_topic_0020311892_p9793440111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p2986646411165"><a name="en-us_topic_0020311892_p2986646411165"></a><a name="en-us_topic_0020311892_p2986646411165"></a>ELB.6000</p>
</td>
<td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p326452811165"><a name="en-us_topic_0020311892_p326452811165"></a><a name="en-us_topic_0020311892_p326452811165"></a>The length of the listener ID exceeds the limit.</p>
</td>
<td class="cellrowborder" valign="top" width="24.03%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p3302750011433"><a name="en-us_topic_0020311892_p3302750011433"></a><a name="en-us_topic_0020311892_p3302750011433"></a>Listener ID length is not correct.</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0020311892_p5798184711433"><a name="en-us_topic_0020311892_p5798184711433"></a><a name="en-us_topic_0020311892_p5798184711433"></a>Change the listener ID and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row2938075411165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p55071162111433"><a name="en-us_topic_0020311892_p55071162111433"></a><a name="en-us_topic_0020311892_p55071162111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p3103085511165"><a name="en-us_topic_0020311892_p3103085511165"></a><a name="en-us_topic_0020311892_p3103085511165"></a>ELB.6010</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p3047134111165"><a name="en-us_topic_0020311892_p3047134111165"></a><a name="en-us_topic_0020311892_p3047134111165"></a>Invalid listener ID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p5729114511433"><a name="en-us_topic_0020311892_p5729114511433"></a><a name="en-us_topic_0020311892_p5729114511433"></a>Listener ID content is not correct.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p1007113811433"><a name="en-us_topic_0020311892_p1007113811433"></a><a name="en-us_topic_0020311892_p1007113811433"></a>Change the listener ID and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row580661811165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p31579157111433"><a name="en-us_topic_0020311892_p31579157111433"></a><a name="en-us_topic_0020311892_p31579157111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p57402711165"><a name="en-us_topic_0020311892_p57402711165"></a><a name="en-us_topic_0020311892_p57402711165"></a>ELB.6030</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p4649625811165"><a name="en-us_topic_0020311892_p4649625811165"></a><a name="en-us_topic_0020311892_p4649625811165"></a>The listener does not belong to any load balancer.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p2699343811433"><a name="en-us_topic_0020311892_p2699343811433"></a><a name="en-us_topic_0020311892_p2699343811433"></a>Listener is not associated with loadbalancer id.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p3898489511433"><a name="en-us_topic_0020311892_p3898489511433"></a><a name="en-us_topic_0020311892_p3898489511433"></a>Check the listener ID and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row1581313811165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p7774937111433"><a name="en-us_topic_0020311892_p7774937111433"></a><a name="en-us_topic_0020311892_p7774937111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p579578611165"><a name="en-us_topic_0020311892_p579578611165"></a><a name="en-us_topic_0020311892_p579578611165"></a>ELB.6040</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p6680549811165"><a name="en-us_topic_0020311892_p6680549811165"></a><a name="en-us_topic_0020311892_p6680549811165"></a>The load balancer to which the listener is added does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p3293969011433"><a name="en-us_topic_0020311892_p3293969011433"></a><a name="en-us_topic_0020311892_p3293969011433"></a>The loadbalaner that the listener belongs to is not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p5086924611433"><a name="en-us_topic_0020311892_p5086924611433"></a><a name="en-us_topic_0020311892_p5086924611433"></a>Check the load balancer ID.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row6437857511165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p25790124111433"><a name="en-us_topic_0020311892_p25790124111433"></a><a name="en-us_topic_0020311892_p25790124111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p4728208711165"><a name="en-us_topic_0020311892_p4728208711165"></a><a name="en-us_topic_0020311892_p4728208711165"></a>ELB.6020</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p464385211165"><a name="en-us_topic_0020311892_p464385211165"></a><a name="en-us_topic_0020311892_p464385211165"></a>Incorrect listener URL.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p3958744111433"><a name="en-us_topic_0020311892_p3958744111433"></a><a name="en-us_topic_0020311892_p3958744111433"></a>Listener url is not correct.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p5246616111433"><a name="en-us_topic_0020311892_p5246616111433"></a><a name="en-us_topic_0020311892_p5246616111433"></a>Correct the URL and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row4179467011165"><td class="cellrowborder" rowspan="11" valign="top" width="9%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p5285846011182"><a name="en-us_topic_0020311892_p5285846011182"></a><a name="en-us_topic_0020311892_p5285846011182"></a>Adding a listener</p>
</td>
<td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p8625337111433"><a name="en-us_topic_0020311892_p8625337111433"></a><a name="en-us_topic_0020311892_p8625337111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p801701211165"><a name="en-us_topic_0020311892_p801701211165"></a><a name="en-us_topic_0020311892_p801701211165"></a>ELB.6001</p>
</td>
<td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p4539820711165"><a name="en-us_topic_0020311892_p4539820711165"></a><a name="en-us_topic_0020311892_p4539820711165"></a>A mandatory parameter is left blank.</p>
</td>
<td class="cellrowborder" valign="top" width="24.03%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p1249381711454"><a name="en-us_topic_0020311892_p1249381711454"></a><a name="en-us_topic_0020311892_p1249381711454"></a>Request parameters error, "..nilKey.." is nil.</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0020311892_p536627511454"><a name="en-us_topic_0020311892_p536627511454"></a><a name="en-us_topic_0020311892_p536627511454"></a>Specify the mandatory parameter and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row593068311165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p27563686111433"><a name="en-us_topic_0020311892_p27563686111433"></a><a name="en-us_topic_0020311892_p27563686111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p1062335111165"><a name="en-us_topic_0020311892_p1062335111165"></a><a name="en-us_topic_0020311892_p1062335111165"></a>ELB.6011</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p5518507011165"><a name="en-us_topic_0020311892_p5518507011165"></a><a name="en-us_topic_0020311892_p5518507011165"></a>The length of the listener name exceeds the limit.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p1970063711454"><a name="en-us_topic_0020311892_p1970063711454"></a><a name="en-us_topic_0020311892_p1970063711454"></a>Request parameters error, listener name too long.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p46805911454"><a name="en-us_topic_0020311892_p46805911454"></a><a name="en-us_topic_0020311892_p46805911454"></a>Change the name and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row2690358811165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p18066075111433"><a name="en-us_topic_0020311892_p18066075111433"></a><a name="en-us_topic_0020311892_p18066075111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p3170704211165"><a name="en-us_topic_0020311892_p3170704211165"></a><a name="en-us_topic_0020311892_p3170704211165"></a>ELB.6021</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p1813358411165"><a name="en-us_topic_0020311892_p1813358411165"></a><a name="en-us_topic_0020311892_p1813358411165"></a>Invalid listener name.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p567094311454"><a name="en-us_topic_0020311892_p567094311454"></a><a name="en-us_topic_0020311892_p567094311454"></a>Request parameters error, listener name is not valid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p5669320011454"><a name="en-us_topic_0020311892_p5669320011454"></a><a name="en-us_topic_0020311892_p5669320011454"></a>Change the name and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row2898452811165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p54065985111433"><a name="en-us_topic_0020311892_p54065985111433"></a><a name="en-us_topic_0020311892_p54065985111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p6604545011165"><a name="en-us_topic_0020311892_p6604545011165"></a><a name="en-us_topic_0020311892_p6604545011165"></a>ELB.6031</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p4808122411165"><a name="en-us_topic_0020311892_p4808122411165"></a><a name="en-us_topic_0020311892_p4808122411165"></a>The length of the listener description exceeds the limit.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p5739174811454"><a name="en-us_topic_0020311892_p5739174811454"></a><a name="en-us_topic_0020311892_p5739174811454"></a>Request parameters error, listener len description too long.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p1822005011454"><a name="en-us_topic_0020311892_p1822005011454"></a><a name="en-us_topic_0020311892_p1822005011454"></a>Change the description and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row3007783611165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p17268671111433"><a name="en-us_topic_0020311892_p17268671111433"></a><a name="en-us_topic_0020311892_p17268671111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p2038567611165"><a name="en-us_topic_0020311892_p2038567611165"></a><a name="en-us_topic_0020311892_p2038567611165"></a>ELB.6041</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p4062707711165"><a name="en-us_topic_0020311892_p4062707711165"></a><a name="en-us_topic_0020311892_p4062707711165"></a>Invalid port number.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p6197069911454"><a name="en-us_topic_0020311892_p6197069911454"></a><a name="en-us_topic_0020311892_p6197069911454"></a>Request parameters error, listener port is not in 1 ~  65535.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p5357068611454"><a name="en-us_topic_0020311892_p5357068611454"></a><a name="en-us_topic_0020311892_p5357068611454"></a>Change the port number and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row3009937411165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p56585150111433"><a name="en-us_topic_0020311892_p56585150111433"></a><a name="en-us_topic_0020311892_p56585150111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p2213019011165"><a name="en-us_topic_0020311892_p2213019011165"></a><a name="en-us_topic_0020311892_p2213019011165"></a>ELB.6051</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p677573115275"><a name="en-us_topic_0020311892_p677573115275"></a><a name="en-us_topic_0020311892_p677573115275"></a>Invalid load balancing algorithm.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p6278080611454"><a name="en-us_topic_0020311892_p6278080611454"></a><a name="en-us_topic_0020311892_p6278080611454"></a>Request parameters error, listener lb algorithm is not valid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p5208050611454"><a name="en-us_topic_0020311892_p5208050611454"></a><a name="en-us_topic_0020311892_p5208050611454"></a>Change the load balancing algorithm and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row2678126511165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p19994470111433"><a name="en-us_topic_0020311892_p19994470111433"></a><a name="en-us_topic_0020311892_p19994470111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p2179884311165"><a name="en-us_topic_0020311892_p2179884311165"></a><a name="en-us_topic_0020311892_p2179884311165"></a>ELB.6061</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p2087587811165"><a name="en-us_topic_0020311892_p2087587811165"></a><a name="en-us_topic_0020311892_p2087587811165"></a>Invalid listener protocol.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p5018101111454"><a name="en-us_topic_0020311892_p5018101111454"></a><a name="en-us_topic_0020311892_p5018101111454"></a>Request parameters error, listener protocol is not valid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p3813009711454"><a name="en-us_topic_0020311892_p3813009711454"></a><a name="en-us_topic_0020311892_p3813009711454"></a>Change the load balancer protocol and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row5366517911165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p8939358111433"><a name="en-us_topic_0020311892_p8939358111433"></a><a name="en-us_topic_0020311892_p8939358111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p5191226611165"><a name="en-us_topic_0020311892_p5191226611165"></a><a name="en-us_topic_0020311892_p5191226611165"></a>ELB.6071</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p4414401311165"><a name="en-us_topic_0020311892_p4414401311165"></a><a name="en-us_topic_0020311892_p4414401311165"></a>Invalid backend ECS protocol.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p1377173611454"><a name="en-us_topic_0020311892_p1377173611454"></a><a name="en-us_topic_0020311892_p1377173611454"></a>Request parameters error, listener backend protocol is not valid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p4176879411454"><a name="en-us_topic_0020311892_p4176879411454"></a><a name="en-us_topic_0020311892_p4176879411454"></a>Change the backend ECS protocol and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row6175180211165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p52999374111433"><a name="en-us_topic_0020311892_p52999374111433"></a><a name="en-us_topic_0020311892_p52999374111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p3584005511165"><a name="en-us_topic_0020311892_p3584005511165"></a><a name="en-us_topic_0020311892_p3584005511165"></a>ELB.6081</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="p19271119"><a name="p19271119"></a><a name="p19271119"></a>Invalid sticky session type.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p17456778"><a name="p17456778"></a><a name="p17456778"></a>Request parameters error, listener sticky_session_type is not valid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p2058788911454"><a name="en-us_topic_0020311892_p2058788911454"></a><a name="en-us_topic_0020311892_p2058788911454"></a>Check the load balancer ID.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row2205219411165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p65090911111433"><a name="en-us_topic_0020311892_p65090911111433"></a><a name="en-us_topic_0020311892_p65090911111433"></a>403</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p4139725511165"><a name="en-us_topic_0020311892_p4139725511165"></a><a name="en-us_topic_0020311892_p4139725511165"></a>ELB.6091</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p6484333611165"><a name="en-us_topic_0020311892_p6484333611165"></a><a name="en-us_topic_0020311892_p6484333611165"></a>The number of listeners reaches the limit.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p4329478611454"><a name="en-us_topic_0020311892_p4329478611454"></a><a name="en-us_topic_0020311892_p4329478611454"></a>Request lb has more than user listener quota.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p1721676311454"><a name="en-us_topic_0020311892_p1721676311454"></a><a name="en-us_topic_0020311892_p1721676311454"></a>No more listeners can be added.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row4671911911165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p37872440111433"><a name="en-us_topic_0020311892_p37872440111433"></a><a name="en-us_topic_0020311892_p37872440111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p2615232711165"><a name="en-us_topic_0020311892_p2615232711165"></a><a name="en-us_topic_0020311892_p2615232711165"></a>ELB.6101</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p3796372711165"><a name="en-us_topic_0020311892_p3796372711165"></a><a name="en-us_topic_0020311892_p3796372711165"></a>The port exists.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p166300211454"><a name="en-us_topic_0020311892_p166300211454"></a><a name="en-us_topic_0020311892_p166300211454"></a>Listener port is repeated.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p48544511454"><a name="en-us_topic_0020311892_p48544511454"></a><a name="en-us_topic_0020311892_p48544511454"></a>Change the port number and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row612922411165"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p1315300111442"><a name="en-us_topic_0020311892_p1315300111442"></a><a name="en-us_topic_0020311892_p1315300111442"></a>Deleting a listener</p>
</td>
<td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p47768834111433"><a name="en-us_topic_0020311892_p47768834111433"></a><a name="en-us_topic_0020311892_p47768834111433"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p1563467611165"><a name="en-us_topic_0020311892_p1563467611165"></a><a name="en-us_topic_0020311892_p1563467611165"></a>ELB.6002</p>
</td>
<td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.2.7.1.4 "><p id="p49465709"><a name="p49465709"></a><a name="p49465709"></a>The listener does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="24.03%" headers="mcps1.2.7.1.5 "><p id="p47299488"><a name="p47299488"></a><a name="p47299488"></a>Delete listener failed, listener does not exist.</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0020311892_p45749582114533"><a name="en-us_topic_0020311892_p45749582114533"></a><a name="en-us_topic_0020311892_p45749582114533"></a>Check the listener ID.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row5485013611165"><td class="cellrowborder" rowspan="4" valign="top" width="9%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p5548227611188"><a name="en-us_topic_0020311892_p5548227611188"></a><a name="en-us_topic_0020311892_p5548227611188"></a>Modifying a listener</p>
</td>
<td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p44070373111433"><a name="en-us_topic_0020311892_p44070373111433"></a><a name="en-us_topic_0020311892_p44070373111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p1367606811165"><a name="en-us_topic_0020311892_p1367606811165"></a><a name="en-us_topic_0020311892_p1367606811165"></a>ELB.6015</p>
</td>
<td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p3401969111165"><a name="en-us_topic_0020311892_p3401969111165"></a><a name="en-us_topic_0020311892_p3401969111165"></a>The property cannot be modified.</p>
</td>
<td class="cellrowborder" valign="top" width="24.03%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p56258241114636"><a name="en-us_topic_0020311892_p56258241114636"></a><a name="en-us_topic_0020311892_p56258241114636"></a>This listener property cannot be updated</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0020311892_p60623683114636"><a name="en-us_topic_0020311892_p60623683114636"></a><a name="en-us_topic_0020311892_p60623683114636"></a>Select a property that can be modified.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row3774176911165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p12930440111433"><a name="en-us_topic_0020311892_p12930440111433"></a><a name="en-us_topic_0020311892_p12930440111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p3718447111165"><a name="en-us_topic_0020311892_p3718447111165"></a><a name="en-us_topic_0020311892_p3718447111165"></a>ELB.6025</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p5915214911165"><a name="en-us_topic_0020311892_p5915214911165"></a><a name="en-us_topic_0020311892_p5915214911165"></a>The length of the listener name exceeds the limit.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p37032965114636"><a name="en-us_topic_0020311892_p37032965114636"></a><a name="en-us_topic_0020311892_p37032965114636"></a>Udpate request parameters error, listener len name too long.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p46880226114636"><a name="en-us_topic_0020311892_p46880226114636"></a><a name="en-us_topic_0020311892_p46880226114636"></a>Change the name and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row6260729311165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p40732691111433"><a name="en-us_topic_0020311892_p40732691111433"></a><a name="en-us_topic_0020311892_p40732691111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p3802599111165"><a name="en-us_topic_0020311892_p3802599111165"></a><a name="en-us_topic_0020311892_p3802599111165"></a>ELB.6035</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p6020642111165"><a name="en-us_topic_0020311892_p6020642111165"></a><a name="en-us_topic_0020311892_p6020642111165"></a>Invalid listener name.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p17273241114636"><a name="en-us_topic_0020311892_p17273241114636"></a><a name="en-us_topic_0020311892_p17273241114636"></a>Udpate request parameters error, listener name is not valid.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p56955274114636"><a name="en-us_topic_0020311892_p56955274114636"></a><a name="en-us_topic_0020311892_p56955274114636"></a>Change the name and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row498688111165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p11013679111433"><a name="en-us_topic_0020311892_p11013679111433"></a><a name="en-us_topic_0020311892_p11013679111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p128424111165"><a name="en-us_topic_0020311892_p128424111165"></a><a name="en-us_topic_0020311892_p128424111165"></a>ELB.6045</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p3691471411165"><a name="en-us_topic_0020311892_p3691471411165"></a><a name="en-us_topic_0020311892_p3691471411165"></a>The length of the listener description exceeds the limit.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p47116840114636"><a name="en-us_topic_0020311892_p47116840114636"></a><a name="en-us_topic_0020311892_p47116840114636"></a>Update request parameters error, listener len description too long.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p58367735114636"><a name="en-us_topic_0020311892_p58367735114636"></a><a name="en-us_topic_0020311892_p58367735114636"></a>Change the description and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row3026190411165"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p40052218111442"><a name="en-us_topic_0020311892_p40052218111442"></a><a name="en-us_topic_0020311892_p40052218111442"></a>Querying listeners</p>
</td>
<td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p19692803111433"><a name="en-us_topic_0020311892_p19692803111433"></a><a name="en-us_topic_0020311892_p19692803111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p4033726311165"><a name="en-us_topic_0020311892_p4033726311165"></a><a name="en-us_topic_0020311892_p4033726311165"></a>ELB.6003</p>
</td>
<td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p4609283411165"><a name="en-us_topic_0020311892_p4609283411165"></a><a name="en-us_topic_0020311892_p4609283411165"></a>Invalid query condition.</p>
</td>
<td class="cellrowborder" valign="top" width="24.03%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p64792380114724"><a name="en-us_topic_0020311892_p64792380114724"></a><a name="en-us_topic_0020311892_p64792380114724"></a>Listener query condition is not valid.</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0020311892_p13691414114724"><a name="en-us_topic_0020311892_p13691414114724"></a><a name="en-us_topic_0020311892_p13691414114724"></a>Change the query condition and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row1218233011165"><td class="cellrowborder" rowspan="5" valign="top" width="9%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p53348022111812"><a name="en-us_topic_0020311892_p53348022111812"></a><a name="en-us_topic_0020311892_p53348022111812"></a>Common part</p>
</td>
<td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p51613240111433"><a name="en-us_topic_0020311892_p51613240111433"></a><a name="en-us_topic_0020311892_p51613240111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p161401411165"><a name="en-us_topic_0020311892_p161401411165"></a><a name="en-us_topic_0020311892_p161401411165"></a>ELB.2000</p>
</td>
<td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p6362630311165"><a name="en-us_topic_0020311892_p6362630311165"></a><a name="en-us_topic_0020311892_p6362630311165"></a>Incorrect backend ECS URL.</p>
</td>
<td class="cellrowborder" valign="top" width="24.03%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p6395778811506"><a name="en-us_topic_0020311892_p6395778811506"></a><a name="en-us_topic_0020311892_p6395778811506"></a>Member url is not correct.</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0020311892_p1319835311506"><a name="en-us_topic_0020311892_p1319835311506"></a><a name="en-us_topic_0020311892_p1319835311506"></a>Correct the URL and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row6468897319190"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p19922934111433"><a name="en-us_topic_0020311892_p19922934111433"></a><a name="en-us_topic_0020311892_p19922934111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p4675477519199"><a name="en-us_topic_0020311892_p4675477519199"></a><a name="en-us_topic_0020311892_p4675477519199"></a>ELB.2003</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p2904040019199"><a name="en-us_topic_0020311892_p2904040019199"></a><a name="en-us_topic_0020311892_p2904040019199"></a>Failed to query the backend ECS.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p16924976"><a name="p16924976"></a><a name="p16924976"></a>Query member failed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p1432723311506"><a name="en-us_topic_0020311892_p1432723311506"></a><a name="en-us_topic_0020311892_p1432723311506"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row412186119195"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p3144932111433"><a name="en-us_topic_0020311892_p3144932111433"></a><a name="en-us_topic_0020311892_p3144932111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p3115945219199"><a name="en-us_topic_0020311892_p3115945219199"></a><a name="en-us_topic_0020311892_p3115945219199"></a>ELB.2005</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p4088770919199"><a name="en-us_topic_0020311892_p4088770919199"></a><a name="en-us_topic_0020311892_p4088770919199"></a>Failed to update the backend ECS.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p37382168"><a name="p37382168"></a><a name="p37382168"></a>Update member failed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p3445025211506"><a name="en-us_topic_0020311892_p3445025211506"></a><a name="en-us_topic_0020311892_p3445025211506"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row3576581511165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p53412906111433"><a name="en-us_topic_0020311892_p53412906111433"></a><a name="en-us_topic_0020311892_p53412906111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p1134990911165"><a name="en-us_topic_0020311892_p1134990911165"></a><a name="en-us_topic_0020311892_p1134990911165"></a>ELB.2010</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p4692747611165"><a name="en-us_topic_0020311892_p4692747611165"></a><a name="en-us_topic_0020311892_p4692747611165"></a>The length of the listener ID exceeds the limit.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p1551864111506"><a name="en-us_topic_0020311892_p1551864111506"></a><a name="en-us_topic_0020311892_p1551864111506"></a>Member listener ID length is not correct.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p4905043111506"><a name="en-us_topic_0020311892_p4905043111506"></a><a name="en-us_topic_0020311892_p4905043111506"></a>Change the listener ID and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row1969410811165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p31478129111433"><a name="en-us_topic_0020311892_p31478129111433"></a><a name="en-us_topic_0020311892_p31478129111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p5171887811165"><a name="en-us_topic_0020311892_p5171887811165"></a><a name="en-us_topic_0020311892_p5171887811165"></a>ELB.2020</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p2847960511165"><a name="en-us_topic_0020311892_p2847960511165"></a><a name="en-us_topic_0020311892_p2847960511165"></a>Incorrect listener ID.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p5584867711506"><a name="en-us_topic_0020311892_p5584867711506"></a><a name="en-us_topic_0020311892_p5584867711506"></a>Member listener ID content is not correct.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p2744900711506"><a name="en-us_topic_0020311892_p2744900711506"></a><a name="en-us_topic_0020311892_p2744900711506"></a>Change the listener ID and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row5498986011165"><td class="cellrowborder" rowspan="3" valign="top" width="9%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p54604565111442"><a name="en-us_topic_0020311892_p54604565111442"></a><a name="en-us_topic_0020311892_p54604565111442"></a>Adding a backend ECS</p>
<p id="en-us_topic_0020311892_p60893663111442"><a name="en-us_topic_0020311892_p60893663111442"></a><a name="en-us_topic_0020311892_p60893663111442"></a></p>
<p id="en-us_topic_0020311892_p33439661111442"><a name="en-us_topic_0020311892_p33439661111442"></a><a name="en-us_topic_0020311892_p33439661111442"></a></p>
</td>
<td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p66700512111433"><a name="en-us_topic_0020311892_p66700512111433"></a><a name="en-us_topic_0020311892_p66700512111433"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p1122260611165"><a name="en-us_topic_0020311892_p1122260611165"></a><a name="en-us_topic_0020311892_p1122260611165"></a>ELB.2001</p>
</td>
<td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.2.7.1.4 "><p id="p21312994"><a name="p21312994"></a><a name="p21312994"></a>Failed to add the ECS because the number of backend ECSs reaches the limit.</p>
</td>
<td class="cellrowborder" valign="top" width="24.03%" headers="mcps1.2.7.1.5 "><p id="p48630991"><a name="p48630991"></a><a name="p48630991"></a>Create member failed, the total amount of members exceeds the system setting.</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0020311892_p57022457115036"><a name="en-us_topic_0020311892_p57022457115036"></a><a name="en-us_topic_0020311892_p57022457115036"></a>Check the maximum number of ECSs that can be added and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row6110790311165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p34032416111433"><a name="en-us_topic_0020311892_p34032416111433"></a><a name="en-us_topic_0020311892_p34032416111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p5079310911165"><a name="en-us_topic_0020311892_p5079310911165"></a><a name="en-us_topic_0020311892_p5079310911165"></a>ELB.2011</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p2060113511165"><a name="en-us_topic_0020311892_p2060113511165"></a><a name="en-us_topic_0020311892_p2060113511165"></a>The listener does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p28984532115036"><a name="en-us_topic_0020311892_p28984532115036"></a><a name="en-us_topic_0020311892_p28984532115036"></a>Add member listener is not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p66045721115036"><a name="en-us_topic_0020311892_p66045721115036"></a><a name="en-us_topic_0020311892_p66045721115036"></a>Ensure that the listener exists and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row5119248911165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p5162329111433"><a name="en-us_topic_0020311892_p5162329111433"></a><a name="en-us_topic_0020311892_p5162329111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p5295094911165"><a name="en-us_topic_0020311892_p5295094911165"></a><a name="en-us_topic_0020311892_p5295094911165"></a>ELB.2021</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p61196241155329"><a name="en-us_topic_0020311892_p61196241155329"></a><a name="en-us_topic_0020311892_p61196241155329"></a>Invalid address.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p30275281115036"><a name="en-us_topic_0020311892_p30275281115036"></a><a name="en-us_topic_0020311892_p30275281115036"></a>Request parameters error, member address is null.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p36378729115036"><a name="en-us_topic_0020311892_p36378729115036"></a><a name="en-us_topic_0020311892_p36378729115036"></a>Check the address and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row1364535211165"><td class="cellrowborder" rowspan="2" valign="top" width="9%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p63602126111817"><a name="en-us_topic_0020311892_p63602126111817"></a><a name="en-us_topic_0020311892_p63602126111817"></a>Deleting a backend ECS</p>
</td>
<td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p15495474111433"><a name="en-us_topic_0020311892_p15495474111433"></a><a name="en-us_topic_0020311892_p15495474111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p393482911165"><a name="en-us_topic_0020311892_p393482911165"></a><a name="en-us_topic_0020311892_p393482911165"></a>ELB.2002</p>
</td>
<td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p64895950155341"><a name="en-us_topic_0020311892_p64895950155341"></a><a name="en-us_topic_0020311892_p64895950155341"></a>Incorrect parameters.</p>
</td>
<td class="cellrowborder" valign="top" width="24.03%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p60870587115054"><a name="en-us_topic_0020311892_p60870587115054"></a><a name="en-us_topic_0020311892_p60870587115054"></a>Delete member input param error.</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0020311892_p31570542115054"><a name="en-us_topic_0020311892_p31570542115054"></a><a name="en-us_topic_0020311892_p31570542115054"></a>Check the parameters and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row4991846411165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p47173843111433"><a name="en-us_topic_0020311892_p47173843111433"></a><a name="en-us_topic_0020311892_p47173843111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p1686378311165"><a name="en-us_topic_0020311892_p1686378311165"></a><a name="en-us_topic_0020311892_p1686378311165"></a>ELB.2012</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p2378917411165"><a name="en-us_topic_0020311892_p2378917411165"></a><a name="en-us_topic_0020311892_p2378917411165"></a>The backend ECS does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p63693802115054"><a name="en-us_topic_0020311892_p63693802115054"></a><a name="en-us_topic_0020311892_p63693802115054"></a>This member is not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p58924320115054"><a name="en-us_topic_0020311892_p58924320115054"></a><a name="en-us_topic_0020311892_p58924320115054"></a>Ensure that the backend ECS exists and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row1277598111165"><td class="cellrowborder" rowspan="3" valign="top" width="9%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p41490175111820"><a name="en-us_topic_0020311892_p41490175111820"></a><a name="en-us_topic_0020311892_p41490175111820"></a>Common part</p>
</td>
<td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p62984933111433"><a name="en-us_topic_0020311892_p62984933111433"></a><a name="en-us_topic_0020311892_p62984933111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p424144811165"><a name="en-us_topic_0020311892_p424144811165"></a><a name="en-us_topic_0020311892_p424144811165"></a>ELB.7000</p>
</td>
<td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p801296811165"><a name="en-us_topic_0020311892_p801296811165"></a><a name="en-us_topic_0020311892_p801296811165"></a>The listener ID is left blank.</p>
</td>
<td class="cellrowborder" valign="top" width="24.03%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p14833297115116"><a name="en-us_topic_0020311892_p14833297115116"></a><a name="en-us_topic_0020311892_p14833297115116"></a>Listener_id must not be null.</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0020311892_p60646393115116"><a name="en-us_topic_0020311892_p60646393115116"></a><a name="en-us_topic_0020311892_p60646393115116"></a>Change the listener ID and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row500784911165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p1505935111433"><a name="en-us_topic_0020311892_p1505935111433"></a><a name="en-us_topic_0020311892_p1505935111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p298261911165"><a name="en-us_topic_0020311892_p298261911165"></a><a name="en-us_topic_0020311892_p298261911165"></a>ELB.7010</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p4026557311165"><a name="en-us_topic_0020311892_p4026557311165"></a><a name="en-us_topic_0020311892_p4026557311165"></a>The listener with which the health check is associated does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p53588134115116"><a name="en-us_topic_0020311892_p53588134115116"></a><a name="en-us_topic_0020311892_p53588134115116"></a>Healthcheck listener is not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p45671598115116"><a name="en-us_topic_0020311892_p45671598115116"></a><a name="en-us_topic_0020311892_p45671598115116"></a>Change the listener ID and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row2684584311165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p54871930111433"><a name="en-us_topic_0020311892_p54871930111433"></a><a name="en-us_topic_0020311892_p54871930111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p2702968511165"><a name="en-us_topic_0020311892_p2702968511165"></a><a name="en-us_topic_0020311892_p2702968511165"></a>ELB.7020</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p4192090011165"><a name="en-us_topic_0020311892_p4192090011165"></a><a name="en-us_topic_0020311892_p4192090011165"></a>The health check does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p8598877115116"><a name="en-us_topic_0020311892_p8598877115116"></a><a name="en-us_topic_0020311892_p8598877115116"></a>This healthcheck is not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p25420464115116"><a name="en-us_topic_0020311892_p25420464115116"></a><a name="en-us_topic_0020311892_p25420464115116"></a>Change the health check ID and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row4174378311165"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p52862880111442"><a name="en-us_topic_0020311892_p52862880111442"></a><a name="en-us_topic_0020311892_p52862880111442"></a>Configuring a health check</p>
</td>
<td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p15441358111433"><a name="en-us_topic_0020311892_p15441358111433"></a><a name="en-us_topic_0020311892_p15441358111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p969254511165"><a name="en-us_topic_0020311892_p969254511165"></a><a name="en-us_topic_0020311892_p969254511165"></a>ELB.7001</p>
</td>
<td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p4689866211165"><a name="en-us_topic_0020311892_p4689866211165"></a><a name="en-us_topic_0020311892_p4689866211165"></a>Invalid health check interval.</p>
</td>
<td class="cellrowborder" valign="top" width="24.03%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p64797861115131"><a name="en-us_topic_0020311892_p64797861115131"></a><a name="en-us_topic_0020311892_p64797861115131"></a>Healthcheck_interval is illegal.</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0020311892_p14135422115131"><a name="en-us_topic_0020311892_p14135422115131"></a><a name="en-us_topic_0020311892_p14135422115131"></a>Change the interval and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row4275362511165"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p54034926111442"><a name="en-us_topic_0020311892_p54034926111442"></a><a name="en-us_topic_0020311892_p54034926111442"></a>Deleting a health check</p>
</td>
<td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p42790449111433"><a name="en-us_topic_0020311892_p42790449111433"></a><a name="en-us_topic_0020311892_p42790449111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p5859682511165"><a name="en-us_topic_0020311892_p5859682511165"></a><a name="en-us_topic_0020311892_p5859682511165"></a>ELB.7002</p>
</td>
<td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p4872236111165"><a name="en-us_topic_0020311892_p4872236111165"></a><a name="en-us_topic_0020311892_p4872236111165"></a>Invalid query condition.</p>
</td>
<td class="cellrowborder" valign="top" width="24.03%" headers="mcps1.2.7.1.5 "><p id="p4330799"><a name="p4330799"></a><a name="p4330799"></a>Healthcheck delete condition is not valid.</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0020311892_p41324096115214"><a name="en-us_topic_0020311892_p41324096115214"></a><a name="en-us_topic_0020311892_p41324096115214"></a>Change the query condition and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row3584807011165"><td class="cellrowborder" valign="top" width="9%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p14752896111442"><a name="en-us_topic_0020311892_p14752896111442"></a><a name="en-us_topic_0020311892_p14752896111442"></a>Modifying a health check</p>
</td>
<td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p43474382111433"><a name="en-us_topic_0020311892_p43474382111433"></a><a name="en-us_topic_0020311892_p43474382111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p4973110711165"><a name="en-us_topic_0020311892_p4973110711165"></a><a name="en-us_topic_0020311892_p4973110711165"></a>ELB.7001</p>
</td>
<td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p168785211165"><a name="en-us_topic_0020311892_p168785211165"></a><a name="en-us_topic_0020311892_p168785211165"></a>Invalid query condition.</p>
</td>
<td class="cellrowborder" valign="top" width="24.03%" headers="mcps1.2.7.1.5 "><p id="p552442"><a name="p552442"></a><a name="p552442"></a>Healthcheck update condition is not valid.</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0020311892_p1140915115214"><a name="en-us_topic_0020311892_p1140915115214"></a><a name="en-us_topic_0020311892_p1140915115214"></a>Change the query condition and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row1519067211165"><td class="cellrowborder" rowspan="2" valign="top" width="9%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p46660613111826"><a name="en-us_topic_0020311892_p46660613111826"></a><a name="en-us_topic_0020311892_p46660613111826"></a>Querying details of a health check</p>
</td>
<td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p31764043111433"><a name="en-us_topic_0020311892_p31764043111433"></a><a name="en-us_topic_0020311892_p31764043111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p933750211165"><a name="en-us_topic_0020311892_p933750211165"></a><a name="en-us_topic_0020311892_p933750211165"></a>ELB.7004</p>
</td>
<td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p1814020211165"><a name="en-us_topic_0020311892_p1814020211165"></a><a name="en-us_topic_0020311892_p1814020211165"></a>Invalid query condition.</p>
</td>
<td class="cellrowborder" valign="top" width="24.03%" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p8846562115235"><a name="en-us_topic_0020311892_p8846562115235"></a><a name="en-us_topic_0020311892_p8846562115235"></a>Healthcheck query condition is not valid.</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0020311892_p45482942115235"><a name="en-us_topic_0020311892_p45482942115235"></a><a name="en-us_topic_0020311892_p45482942115235"></a>Change the query condition and deliver the request again.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row2904409411165"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p22750672111433"><a name="en-us_topic_0020311892_p22750672111433"></a><a name="en-us_topic_0020311892_p22750672111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p376138111165"><a name="en-us_topic_0020311892_p376138111165"></a><a name="en-us_topic_0020311892_p376138111165"></a>ELB.7014</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p3623646511165"><a name="en-us_topic_0020311892_p3623646511165"></a><a name="en-us_topic_0020311892_p3623646511165"></a>The health check does not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p14106894"><a name="p14106894"></a><a name="p14106894"></a>Healthcheck configuration not exist.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p25558506115235"><a name="en-us_topic_0020311892_p25558506115235"></a><a name="en-us_topic_0020311892_p25558506115235"></a>Check the health check ID.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row16689641192927"><td class="cellrowborder" rowspan="19" valign="top" width="9%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p57207782111921"><a name="en-us_topic_0020311892_p57207782111921"></a><a name="en-us_topic_0020311892_p57207782111921"></a>Private network load balancer operations</p>
</td>
<td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p30865158111433"><a name="en-us_topic_0020311892_p30865158111433"></a><a name="en-us_topic_0020311892_p30865158111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p46178249192927"><a name="en-us_topic_0020311892_p46178249192927"></a><a name="en-us_topic_0020311892_p46178249192927"></a>ELB.8001</p>
</td>
<td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p23661500193752"><a name="en-us_topic_0020311892_p23661500193752"></a><a name="en-us_topic_0020311892_p23661500193752"></a>Failed to create the security group.</p>
</td>
<td class="cellrowborder" valign="top" width="24.03%" headers="mcps1.2.7.1.5 "><p id="p30093039"><a name="p30093039"></a><a name="p30093039"></a>Create a SG error.</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0020311892_p56701567115342"><a name="en-us_topic_0020311892_p56701567115342"></a><a name="en-us_topic_0020311892_p56701567115342"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row52566806192932"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p17049876111433"><a name="en-us_topic_0020311892_p17049876111433"></a><a name="en-us_topic_0020311892_p17049876111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p18367721192932"><a name="en-us_topic_0020311892_p18367721192932"></a><a name="en-us_topic_0020311892_p18367721192932"></a>ELB.8101</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p37372732193758"><a name="en-us_topic_0020311892_p37372732193758"></a><a name="en-us_topic_0020311892_p37372732193758"></a>Failed to create the VPC.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p30408810"><a name="p30408810"></a><a name="p30408810"></a>Create VPC error.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p66595636115344"><a name="en-us_topic_0020311892_p66595636115344"></a><a name="en-us_topic_0020311892_p66595636115344"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row22663522192937"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p38862755111433"><a name="en-us_topic_0020311892_p38862755111433"></a><a name="en-us_topic_0020311892_p38862755111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p34354835193127"><a name="en-us_topic_0020311892_p34354835193127"></a><a name="en-us_topic_0020311892_p34354835193127"></a>ELB.8102</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p11777907192949"><a name="en-us_topic_0020311892_p11777907192949"></a><a name="en-us_topic_0020311892_p11777907192949"></a>Failed to delete the VPC.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p57056514"><a name="p57056514"></a><a name="p57056514"></a>Delete VPC error.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p49177974115348"><a name="en-us_topic_0020311892_p49177974115348"></a><a name="en-us_topic_0020311892_p49177974115348"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row34339602192955"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p60875483111433"><a name="en-us_topic_0020311892_p60875483111433"></a><a name="en-us_topic_0020311892_p60875483111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p34782672193242"><a name="en-us_topic_0020311892_p34782672193242"></a><a name="en-us_topic_0020311892_p34782672193242"></a>ELB.8103</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p3157543519303"><a name="en-us_topic_0020311892_p3157543519303"></a><a name="en-us_topic_0020311892_p3157543519303"></a>Failed to query the VPC.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p32556657"><a name="p32556657"></a><a name="p32556657"></a>Query VPC error.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p56494598115350"><a name="en-us_topic_0020311892_p56494598115350"></a><a name="en-us_topic_0020311892_p56494598115350"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row413932193010"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p31967075111433"><a name="en-us_topic_0020311892_p31967075111433"></a><a name="en-us_topic_0020311892_p31967075111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p31455047193010"><a name="en-us_topic_0020311892_p31455047193010"></a><a name="en-us_topic_0020311892_p31455047193010"></a>ELB.8201</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p64830885193010"><a name="en-us_topic_0020311892_p64830885193010"></a><a name="en-us_topic_0020311892_p64830885193010"></a>Failed to create the subnet.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p6524924"><a name="p6524924"></a><a name="p6524924"></a>Create subnet error.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p41302525115353"><a name="en-us_topic_0020311892_p41302525115353"></a><a name="en-us_topic_0020311892_p41302525115353"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row26624323193015"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p39196259111433"><a name="en-us_topic_0020311892_p39196259111433"></a><a name="en-us_topic_0020311892_p39196259111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p64921548193015"><a name="en-us_topic_0020311892_p64921548193015"></a><a name="en-us_topic_0020311892_p64921548193015"></a>ELB.8202</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p24154011193015"><a name="en-us_topic_0020311892_p24154011193015"></a><a name="en-us_topic_0020311892_p24154011193015"></a>Failed to delete the subnet.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p62047021"><a name="p62047021"></a><a name="p62047021"></a>Delete subnet error.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p49982634115355"><a name="en-us_topic_0020311892_p49982634115355"></a><a name="en-us_topic_0020311892_p49982634115355"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row45505037193019"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p20780420111433"><a name="en-us_topic_0020311892_p20780420111433"></a><a name="en-us_topic_0020311892_p20780420111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p58324695193019"><a name="en-us_topic_0020311892_p58324695193019"></a><a name="en-us_topic_0020311892_p58324695193019"></a>ELB.8203</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p26679889193019"><a name="en-us_topic_0020311892_p26679889193019"></a><a name="en-us_topic_0020311892_p26679889193019"></a>Failed to query the subnet.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p65517208"><a name="p65517208"></a><a name="p65517208"></a>Query subnet error.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p35568305115358"><a name="en-us_topic_0020311892_p35568305115358"></a><a name="en-us_topic_0020311892_p35568305115358"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row3948204193024"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p5492461111433"><a name="en-us_topic_0020311892_p5492461111433"></a><a name="en-us_topic_0020311892_p5492461111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p146080193024"><a name="en-us_topic_0020311892_p146080193024"></a><a name="en-us_topic_0020311892_p146080193024"></a>ELB.9001</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p11832519193024"><a name="en-us_topic_0020311892_p11832519193024"></a><a name="en-us_topic_0020311892_p11832519193024"></a>Failed to add the ECS.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p40257174"><a name="p40257174"></a><a name="p40257174"></a>Interval ELB create VM error.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p1898233411541"><a name="en-us_topic_0020311892_p1898233411541"></a><a name="en-us_topic_0020311892_p1898233411541"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row2757160193028"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p42236231111433"><a name="en-us_topic_0020311892_p42236231111433"></a><a name="en-us_topic_0020311892_p42236231111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p37446149193028"><a name="en-us_topic_0020311892_p37446149193028"></a><a name="en-us_topic_0020311892_p37446149193028"></a>ELB.9002</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p13239261193028"><a name="en-us_topic_0020311892_p13239261193028"></a><a name="en-us_topic_0020311892_p13239261193028"></a>Failed to delete the ECS.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p44245003"><a name="p44245003"></a><a name="p44245003"></a>Internal ELB delete VM error.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p5233136011543"><a name="en-us_topic_0020311892_p5233136011543"></a><a name="en-us_topic_0020311892_p5233136011543"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row39004944193032"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p65691578111433"><a name="en-us_topic_0020311892_p65691578111433"></a><a name="en-us_topic_0020311892_p65691578111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p25343675193032"><a name="en-us_topic_0020311892_p25343675193032"></a><a name="en-us_topic_0020311892_p25343675193032"></a>ELB.9003</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p39571795193032"><a name="en-us_topic_0020311892_p39571795193032"></a><a name="en-us_topic_0020311892_p39571795193032"></a>Failed to query ECS details.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p56298787"><a name="p56298787"></a><a name="p56298787"></a>Internal ELB query VM error.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p3572574411546"><a name="en-us_topic_0020311892_p3572574411546"></a><a name="en-us_topic_0020311892_p3572574411546"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row8260346193036"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p19417581111433"><a name="en-us_topic_0020311892_p19417581111433"></a><a name="en-us_topic_0020311892_p19417581111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p39277280193036"><a name="en-us_topic_0020311892_p39277280193036"></a><a name="en-us_topic_0020311892_p39277280193036"></a>ELB.9006</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p27343143193036"><a name="en-us_topic_0020311892_p27343143193036"></a><a name="en-us_topic_0020311892_p27343143193036"></a>Failed to update the port configured on the ECS data plane.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p39023632"><a name="p39023632"></a><a name="p39023632"></a>Internal ELB update port fail.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p439789311548"><a name="en-us_topic_0020311892_p439789311548"></a><a name="en-us_topic_0020311892_p439789311548"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row31169681193040"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p29320200111433"><a name="en-us_topic_0020311892_p29320200111433"></a><a name="en-us_topic_0020311892_p29320200111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p23572238193040"><a name="en-us_topic_0020311892_p23572238193040"></a><a name="en-us_topic_0020311892_p23572238193040"></a>ELB.9007</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p30303158193040"><a name="en-us_topic_0020311892_p30303158193040"></a><a name="en-us_topic_0020311892_p30303158193040"></a>Failed to bind the port configured on the ECS data plane.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p66107340"><a name="p66107340"></a><a name="p66107340"></a>Intenal ELB bind port fail.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p46022599115420"><a name="en-us_topic_0020311892_p46022599115420"></a><a name="en-us_topic_0020311892_p46022599115420"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row57734576193439"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p26126004111433"><a name="en-us_topic_0020311892_p26126004111433"></a><a name="en-us_topic_0020311892_p26126004111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p34126578193439"><a name="en-us_topic_0020311892_p34126578193439"></a><a name="en-us_topic_0020311892_p34126578193439"></a>ELB.9061</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p12789401193439"><a name="en-us_topic_0020311892_p12789401193439"></a><a name="en-us_topic_0020311892_p12789401193439"></a>Failed to query the SMN topic.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p27241180"><a name="p27241180"></a><a name="p27241180"></a>Internal ELB query topic fail.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p48993281115424"><a name="en-us_topic_0020311892_p48993281115424"></a><a name="en-us_topic_0020311892_p48993281115424"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row42034314193453"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p35831576111433"><a name="en-us_topic_0020311892_p35831576111433"></a><a name="en-us_topic_0020311892_p35831576111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p36811990193453"><a name="en-us_topic_0020311892_p36811990193453"></a><a name="en-us_topic_0020311892_p36811990193453"></a>ELB.9062</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p28981239193453"><a name="en-us_topic_0020311892_p28981239193453"></a><a name="en-us_topic_0020311892_p28981239193453"></a>Failed to create the SMN topic.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p4965386"><a name="p4965386"></a><a name="p4965386"></a>Internal ELB create topic fail.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p44593024115427"><a name="en-us_topic_0020311892_p44593024115427"></a><a name="en-us_topic_0020311892_p44593024115427"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row27100609193457"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p16676573111433"><a name="en-us_topic_0020311892_p16676573111433"></a><a name="en-us_topic_0020311892_p16676573111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p35715028193457"><a name="en-us_topic_0020311892_p35715028193457"></a><a name="en-us_topic_0020311892_p35715028193457"></a>ELB.9063</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p7236142193457"><a name="en-us_topic_0020311892_p7236142193457"></a><a name="en-us_topic_0020311892_p7236142193457"></a>Failed to query the SMN subscription.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p279849"><a name="p279849"></a><a name="p279849"></a>Internal ELB query subscription fail.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p66446459112533"><a name="en-us_topic_0020311892_p66446459112533"></a><a name="en-us_topic_0020311892_p66446459112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row41604423193516"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p8625195111433"><a name="en-us_topic_0020311892_p8625195111433"></a><a name="en-us_topic_0020311892_p8625195111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p34875783193516"><a name="en-us_topic_0020311892_p34875783193516"></a><a name="en-us_topic_0020311892_p34875783193516"></a>ELB.9064</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p6366198193516"><a name="en-us_topic_0020311892_p6366198193516"></a><a name="en-us_topic_0020311892_p6366198193516"></a>Failed to create the SMN subscription.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p61277141"><a name="p61277141"></a><a name="p61277141"></a>Internal ELB create subscription fail.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p13454124112533"><a name="en-us_topic_0020311892_p13454124112533"></a><a name="en-us_topic_0020311892_p13454124112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row1979483419350"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p27552169111433"><a name="en-us_topic_0020311892_p27552169111433"></a><a name="en-us_topic_0020311892_p27552169111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p1825712219350"><a name="en-us_topic_0020311892_p1825712219350"></a><a name="en-us_topic_0020311892_p1825712219350"></a>ELB.9023</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p243189619350"><a name="en-us_topic_0020311892_p243189619350"></a><a name="en-us_topic_0020311892_p243189619350"></a>Failed to query the image.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p34079791"><a name="p34079791"></a><a name="p34079791"></a>Internal ELB get image error.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p16042298112533"><a name="en-us_topic_0020311892_p16042298112533"></a><a name="en-us_topic_0020311892_p16042298112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row50637398193512"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p17133183111433"><a name="en-us_topic_0020311892_p17133183111433"></a><a name="en-us_topic_0020311892_p17133183111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p43092721193512"><a name="en-us_topic_0020311892_p43092721193512"></a><a name="en-us_topic_0020311892_p43092721193512"></a>ELB.9033</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p849473193512"><a name="en-us_topic_0020311892_p849473193512"></a><a name="en-us_topic_0020311892_p849473193512"></a>Failed to query ECS specifications.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p62494116"><a name="p62494116"></a><a name="p62494116"></a>Internal ELB get flavour error.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p24357772112533"><a name="en-us_topic_0020311892_p24357772112533"></a><a name="en-us_topic_0020311892_p24357772112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row5438966019358"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p45610582111433"><a name="en-us_topic_0020311892_p45610582111433"></a><a name="en-us_topic_0020311892_p45610582111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p3273123019358"><a name="en-us_topic_0020311892_p3273123019358"></a><a name="en-us_topic_0020311892_p3273123019358"></a>ELB.9043</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p3398394119358"><a name="en-us_topic_0020311892_p3398394119358"></a><a name="en-us_topic_0020311892_p3398394119358"></a>Failed to query the API bound to the ECS.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p40968613"><a name="p40968613"></a><a name="p40968613"></a>Internal ELB get interface error.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p26822539112533"><a name="en-us_topic_0020311892_p26822539112533"></a><a name="en-us_topic_0020311892_p26822539112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row52208319201"><td class="cellrowborder" rowspan="24" valign="top" width="9%" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p50155748111930"><a name="en-us_topic_0020311892_p50155748111930"></a><a name="en-us_topic_0020311892_p50155748111930"></a>Others</p>
</td>
<td class="cellrowborder" valign="top" width="11.15%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p3469653111433"><a name="en-us_topic_0020311892_p3469653111433"></a><a name="en-us_topic_0020311892_p3469653111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="15.559999999999999%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p34374358192133"><a name="en-us_topic_0020311892_p34374358192133"></a><a name="en-us_topic_0020311892_p34374358192133"></a>ELB.1007</p>
</td>
<td class="cellrowborder" valign="top" width="21.46%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0020311892_p32859590192133"><a name="en-us_topic_0020311892_p32859590192133"></a><a name="en-us_topic_0020311892_p32859590192133"></a>Failed to query details of the private network load balancer.</p>
</td>
<td class="cellrowborder" valign="top" width="24.03%" headers="mcps1.2.7.1.5 "><p id="p35012440"><a name="p35012440"></a><a name="p35012440"></a>Query internal ELB error.</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.7.1.6 "><p id="en-us_topic_0020311892_p25142046112533"><a name="en-us_topic_0020311892_p25142046112533"></a><a name="en-us_topic_0020311892_p25142046112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row1390041119209"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p12606501111433"><a name="en-us_topic_0020311892_p12606501111433"></a><a name="en-us_topic_0020311892_p12606501111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p63885971192133"><a name="en-us_topic_0020311892_p63885971192133"></a><a name="en-us_topic_0020311892_p63885971192133"></a>ELB.1012</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p7381176192133"><a name="en-us_topic_0020311892_p7381176192133"></a><a name="en-us_topic_0020311892_p7381176192133"></a>Failed to create the relationship between resources and the tenant.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p27620662"><a name="p27620662"></a><a name="p27620662"></a>Create tenant resource relation error.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p23239854112533"><a name="en-us_topic_0020311892_p23239854112533"></a><a name="en-us_topic_0020311892_p23239854112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row29516841192012"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p14493678111433"><a name="en-us_topic_0020311892_p14493678111433"></a><a name="en-us_topic_0020311892_p14493678111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p12168413192133"><a name="en-us_topic_0020311892_p12168413192133"></a><a name="en-us_topic_0020311892_p12168413192133"></a>ELB.1013</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p46117376192133"><a name="en-us_topic_0020311892_p46117376192133"></a><a name="en-us_topic_0020311892_p46117376192133"></a>Failed to modify the quota of a resource because the quota set in the Cloud Eye alarm rule is too large.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p2055829"><a name="p2055829"></a><a name="p2055829"></a>Update resource tenant allocation failed, cloud eye warning rule exceeds.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p3380002112533"><a name="en-us_topic_0020311892_p3380002112533"></a><a name="en-us_topic_0020311892_p3380002112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row944342419205"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p33137239111433"><a name="en-us_topic_0020311892_p33137239111433"></a><a name="en-us_topic_0020311892_p33137239111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p65135207192133"><a name="en-us_topic_0020311892_p65135207192133"></a><a name="en-us_topic_0020311892_p65135207192133"></a>ELB.1014</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p41460451192133"><a name="en-us_topic_0020311892_p41460451192133"></a><a name="en-us_topic_0020311892_p41460451192133"></a>Failed to query the relationship between resources and the tenant.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p20409975"><a name="p20409975"></a><a name="p20409975"></a>Query resouce tenant relation failed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p5344739112533"><a name="en-us_topic_0020311892_p5344739112533"></a><a name="en-us_topic_0020311892_p5344739112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row41582599192028"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p66870664111433"><a name="en-us_topic_0020311892_p66870664111433"></a><a name="en-us_topic_0020311892_p66870664111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p56417596192133"><a name="en-us_topic_0020311892_p56417596192133"></a><a name="en-us_topic_0020311892_p56417596192133"></a>ELB.1102</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p6422582192133"><a name="en-us_topic_0020311892_p6422582192133"></a><a name="en-us_topic_0020311892_p6422582192133"></a>Invalid token.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p3852327"><a name="p3852327"></a><a name="p3852327"></a>Token invalid</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p30270680112533"><a name="en-us_topic_0020311892_p30270680112533"></a><a name="en-us_topic_0020311892_p30270680112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row39992894192032"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p47814698111433"><a name="en-us_topic_0020311892_p47814698111433"></a><a name="en-us_topic_0020311892_p47814698111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p51550936192133"><a name="en-us_topic_0020311892_p51550936192133"></a><a name="en-us_topic_0020311892_p51550936192133"></a>ELB.1103</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p14876312192133"><a name="en-us_topic_0020311892_p14876312192133"></a><a name="en-us_topic_0020311892_p14876312192133"></a>Invalid token.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p31360504"><a name="p31360504"></a><a name="p31360504"></a>Token invalid</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p36005993112533"><a name="en-us_topic_0020311892_p36005993112533"></a><a name="en-us_topic_0020311892_p36005993112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row23649840192036"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p47785316111433"><a name="en-us_topic_0020311892_p47785316111433"></a><a name="en-us_topic_0020311892_p47785316111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p40304858192133"><a name="en-us_topic_0020311892_p40304858192133"></a><a name="en-us_topic_0020311892_p40304858192133"></a>ELB.1104</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p43468026192133"><a name="en-us_topic_0020311892_p43468026192133"></a><a name="en-us_topic_0020311892_p43468026192133"></a>Invalid token.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p15639046"><a name="p15639046"></a><a name="p15639046"></a>Token invalid</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p30804352112533"><a name="en-us_topic_0020311892_p30804352112533"></a><a name="en-us_topic_0020311892_p30804352112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row6414857510855"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p45405407111433"><a name="en-us_topic_0020311892_p45405407111433"></a><a name="en-us_topic_0020311892_p45405407111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p4046626610855"><a name="en-us_topic_0020311892_p4046626610855"></a><a name="en-us_topic_0020311892_p4046626610855"></a>ELB.1105</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p5654209410855"><a name="en-us_topic_0020311892_p5654209410855"></a><a name="en-us_topic_0020311892_p5654209410855"></a>Invalid token.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p64794866"><a name="p64794866"></a><a name="p64794866"></a>Token invalid</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p12124546112533"><a name="en-us_topic_0020311892_p12124546112533"></a><a name="en-us_topic_0020311892_p12124546112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row26226214143752"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p53959363111433"><a name="en-us_topic_0020311892_p53959363111433"></a><a name="en-us_topic_0020311892_p53959363111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p34709336143752"><a name="en-us_topic_0020311892_p34709336143752"></a><a name="en-us_topic_0020311892_p34709336143752"></a>ELB.1109</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p59992859143752"><a name="en-us_topic_0020311892_p59992859143752"></a><a name="en-us_topic_0020311892_p59992859143752"></a>Real-name authentication failed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p60432040"><a name="p60432040"></a><a name="p60432040"></a>Authentication failed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p42564185112533"><a name="en-us_topic_0020311892_p42564185112533"></a><a name="en-us_topic_0020311892_p42564185112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row902388192042"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p8632246111433"><a name="en-us_topic_0020311892_p8632246111433"></a><a name="en-us_topic_0020311892_p8632246111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p12807261192133"><a name="en-us_topic_0020311892_p12807261192133"></a><a name="en-us_topic_0020311892_p12807261192133"></a>ELB.1201</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p30755207192133"><a name="en-us_topic_0020311892_p30755207192133"></a><a name="en-us_topic_0020311892_p30755207192133"></a>Failed to obtain the token.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p12721436"><a name="p12721436"></a><a name="p12721436"></a>Get Token failed</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p25146989112533"><a name="en-us_topic_0020311892_p25146989112533"></a><a name="en-us_topic_0020311892_p25146989112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row20162485192046"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p28123363111433"><a name="en-us_topic_0020311892_p28123363111433"></a><a name="en-us_topic_0020311892_p28123363111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p6185863192133"><a name="en-us_topic_0020311892_p6185863192133"></a><a name="en-us_topic_0020311892_p6185863192133"></a>ELB.3001</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p31292918192133"><a name="en-us_topic_0020311892_p31292918192133"></a><a name="en-us_topic_0020311892_p31292918192133"></a>Failed to assign the floating IP address.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p50066696"><a name="p50066696"></a><a name="p50066696"></a>Create floating IP failed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p23640229112533"><a name="en-us_topic_0020311892_p23640229112533"></a><a name="en-us_topic_0020311892_p23640229112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row57999194192049"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p63399920111433"><a name="en-us_topic_0020311892_p63399920111433"></a><a name="en-us_topic_0020311892_p63399920111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p62632646192133"><a name="en-us_topic_0020311892_p62632646192133"></a><a name="en-us_topic_0020311892_p62632646192133"></a>ELB.3002</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p40079555192133"><a name="en-us_topic_0020311892_p40079555192133"></a><a name="en-us_topic_0020311892_p40079555192133"></a>Failed to release the floating IP address.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p47114415"><a name="p47114415"></a><a name="p47114415"></a>Delete floating IP failed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p35810410112533"><a name="en-us_topic_0020311892_p35810410112533"></a><a name="en-us_topic_0020311892_p35810410112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row55431029192053"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p35119877111433"><a name="en-us_topic_0020311892_p35119877111433"></a><a name="en-us_topic_0020311892_p35119877111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p25639950192133"><a name="en-us_topic_0020311892_p25639950192133"></a><a name="en-us_topic_0020311892_p25639950192133"></a>ELB.3003</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p63570035192133"><a name="en-us_topic_0020311892_p63570035192133"></a><a name="en-us_topic_0020311892_p63570035192133"></a>Failed to query the floating IP address.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p33380508"><a name="p33380508"></a><a name="p33380508"></a>Query floating IP failed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p14962083112533"><a name="en-us_topic_0020311892_p14962083112533"></a><a name="en-us_topic_0020311892_p14962083112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row44822500192056"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p26137803111433"><a name="en-us_topic_0020311892_p26137803111433"></a><a name="en-us_topic_0020311892_p26137803111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p11610246192237"><a name="en-us_topic_0020311892_p11610246192237"></a><a name="en-us_topic_0020311892_p11610246192237"></a>ELB.3004</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p905839192237"><a name="en-us_topic_0020311892_p905839192237"></a><a name="en-us_topic_0020311892_p905839192237"></a>Failed to query floating IP addresses.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p50682466"><a name="p50682466"></a><a name="p50682466"></a>Query floating IP list failed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p3969209112533"><a name="en-us_topic_0020311892_p3969209112533"></a><a name="en-us_topic_0020311892_p3969209112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row58604601192157"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p36787305111433"><a name="en-us_topic_0020311892_p36787305111433"></a><a name="en-us_topic_0020311892_p36787305111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p56376867192237"><a name="en-us_topic_0020311892_p56376867192237"></a><a name="en-us_topic_0020311892_p56376867192237"></a>ELB.3005</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p3123540192237"><a name="en-us_topic_0020311892_p3123540192237"></a><a name="en-us_topic_0020311892_p3123540192237"></a>Failed to update the floating IP address.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p28930396"><a name="p28930396"></a><a name="p28930396"></a>Update floating IP failed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p53070483112533"><a name="en-us_topic_0020311892_p53070483112533"></a><a name="en-us_topic_0020311892_p53070483112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row6337268519211"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p26981768111433"><a name="en-us_topic_0020311892_p26981768111433"></a><a name="en-us_topic_0020311892_p26981768111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p62468855192237"><a name="en-us_topic_0020311892_p62468855192237"></a><a name="en-us_topic_0020311892_p62468855192237"></a>ELB.4001</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p26812507192237"><a name="en-us_topic_0020311892_p26812507192237"></a><a name="en-us_topic_0020311892_p26812507192237"></a>Failed to assign the EIP.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p2398574"><a name="p2398574"></a><a name="p2398574"></a>Create elastic IP failed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p3741849112533"><a name="en-us_topic_0020311892_p3741849112533"></a><a name="en-us_topic_0020311892_p3741849112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row6095406719215"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p38039632111433"><a name="en-us_topic_0020311892_p38039632111433"></a><a name="en-us_topic_0020311892_p38039632111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p17638214192237"><a name="en-us_topic_0020311892_p17638214192237"></a><a name="en-us_topic_0020311892_p17638214192237"></a>ELB.4002</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p19409238192237"><a name="en-us_topic_0020311892_p19409238192237"></a><a name="en-us_topic_0020311892_p19409238192237"></a>Failed to release the EIP.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p37311425"><a name="p37311425"></a><a name="p37311425"></a>Delete elastic IP failed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p34654389112533"><a name="en-us_topic_0020311892_p34654389112533"></a><a name="en-us_topic_0020311892_p34654389112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row2580187419219"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p61311336111433"><a name="en-us_topic_0020311892_p61311336111433"></a><a name="en-us_topic_0020311892_p61311336111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p56473245192237"><a name="en-us_topic_0020311892_p56473245192237"></a><a name="en-us_topic_0020311892_p56473245192237"></a>ELB.4003</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p10930147192237"><a name="en-us_topic_0020311892_p10930147192237"></a><a name="en-us_topic_0020311892_p10930147192237"></a>Failed to query the EIP.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p21226890"><a name="p21226890"></a><a name="p21226890"></a>Query elastic IP failed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p55542092112533"><a name="en-us_topic_0020311892_p55542092112533"></a><a name="en-us_topic_0020311892_p55542092112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row66703473192113"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p162296111433"><a name="en-us_topic_0020311892_p162296111433"></a><a name="en-us_topic_0020311892_p162296111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p49231633192237"><a name="en-us_topic_0020311892_p49231633192237"></a><a name="en-us_topic_0020311892_p49231633192237"></a>ELB.4004</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p28339368192237"><a name="en-us_topic_0020311892_p28339368192237"></a><a name="en-us_topic_0020311892_p28339368192237"></a>Failed to query EIPs.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p31226051"><a name="p31226051"></a><a name="p31226051"></a>Query elastic IP list failed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p2615624112533"><a name="en-us_topic_0020311892_p2615624112533"></a><a name="en-us_topic_0020311892_p2615624112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row3683168619221"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p13146025111433"><a name="en-us_topic_0020311892_p13146025111433"></a><a name="en-us_topic_0020311892_p13146025111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p56978048192237"><a name="en-us_topic_0020311892_p56978048192237"></a><a name="en-us_topic_0020311892_p56978048192237"></a>ELB.4005</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p51819152192237"><a name="en-us_topic_0020311892_p51819152192237"></a><a name="en-us_topic_0020311892_p51819152192237"></a>Failed to update the EIP.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p54939375"><a name="p54939375"></a><a name="p54939375"></a>Update elastic IP failed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p10539025112533"><a name="en-us_topic_0020311892_p10539025112533"></a><a name="en-us_topic_0020311892_p10539025112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row19773331192210"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p16183180111433"><a name="en-us_topic_0020311892_p16183180111433"></a><a name="en-us_topic_0020311892_p16183180111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p55300647192237"><a name="en-us_topic_0020311892_p55300647192237"></a><a name="en-us_topic_0020311892_p55300647192237"></a>ELB.5003</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p50167402192237"><a name="en-us_topic_0020311892_p50167402192237"></a><a name="en-us_topic_0020311892_p50167402192237"></a>Failed to query the bandwidth.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p14610004"><a name="p14610004"></a><a name="p14610004"></a>Query bandwidth failed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p24416808112533"><a name="en-us_topic_0020311892_p24416808112533"></a><a name="en-us_topic_0020311892_p24416808112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row47128773192214"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p35769231111433"><a name="en-us_topic_0020311892_p35769231111433"></a><a name="en-us_topic_0020311892_p35769231111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p64814145192237"><a name="en-us_topic_0020311892_p64814145192237"></a><a name="en-us_topic_0020311892_p64814145192237"></a>ELB.5005</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p15454429192237"><a name="en-us_topic_0020311892_p15454429192237"></a><a name="en-us_topic_0020311892_p15454429192237"></a>Failed to update the bandwidth.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p52737275"><a name="p52737275"></a><a name="p52737275"></a>Update bandwidth failed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p31604422112533"><a name="en-us_topic_0020311892_p31604422112533"></a><a name="en-us_topic_0020311892_p31604422112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row63880742192217"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p11626578111433"><a name="en-us_topic_0020311892_p11626578111433"></a><a name="en-us_topic_0020311892_p11626578111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p59098522192237"><a name="en-us_topic_0020311892_p59098522192237"></a><a name="en-us_topic_0020311892_p59098522192237"></a>ELB.6004</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p22251000192237"><a name="en-us_topic_0020311892_p22251000192237"></a><a name="en-us_topic_0020311892_p22251000192237"></a>Failed to query listeners.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p22912242"><a name="p22912242"></a><a name="p22912242"></a>Query listeners list failed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p9821393112533"><a name="en-us_topic_0020311892_p9821393112533"></a><a name="en-us_topic_0020311892_p9821393112533"></a>Contact customer service.</p>
</td>
</tr>
<tr id="en-us_topic_0020311892_row24559470192221"><td class="cellrowborder" valign="top" headers="mcps1.2.7.1.1 "><p id="en-us_topic_0020311892_p2228733111433"><a name="en-us_topic_0020311892_p2228733111433"></a><a name="en-us_topic_0020311892_p2228733111433"></a>400</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0020311892_p47742902192237"><a name="en-us_topic_0020311892_p47742902192237"></a><a name="en-us_topic_0020311892_p47742902192237"></a>ELB.6006</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0020311892_p41969872192237"><a name="en-us_topic_0020311892_p41969872192237"></a><a name="en-us_topic_0020311892_p41969872192237"></a>Failed to query the ECS.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.4 "><p id="p36957346"><a name="p36957346"></a><a name="p36957346"></a>Query ECS failed.</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.7.1.5 "><p id="en-us_topic_0020311892_p57335344112533"><a name="en-us_topic_0020311892_p57335344112533"></a><a name="en-us_topic_0020311892_p57335344112533"></a>Contact customer service.</p>
</td>
</tr>
</tbody>
</table>


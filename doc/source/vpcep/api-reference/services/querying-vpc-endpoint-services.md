# Querying VPC Endpoint Services<a name="vpcep_06_0205"></a>

## Function<a name="section11645525"></a>

This API is used to query VPC endpoint services.

## URI<a name="section37700862"></a>

Format

GET /v1/\{project\_id\}/vpc-endpoint-services?endpoint\_service\_name=\{endpoint\_service\_name\}&id=\{id\}&sort\_key=\{sort\_key\}&sort\_dir=\{sort\_dir\}&limit=\{limit\}&offset=\{offset\}&status=\{status\}

[Table 1](#table29895862)  describes the required parameters.

**Table  1**  Parameters

<a name="table29895862"></a>
<table><thead align="left"><tr id="row52794610"><th class="cellrowborder" valign="top" width="32.65%" id="mcps1.2.4.1.1"><p id="p48504985"><a name="p48504985"></a><a name="p48504985"></a><strong id="b739411332713"><a name="b739411332713"></a><a name="b739411332713"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.2"><p id="p36589733"><a name="p36589733"></a><a name="p36589733"></a><strong id="b185121834272"><a name="b185121834272"></a><a name="b185121834272"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="40.82%" id="mcps1.2.4.1.3"><p id="p10978430"><a name="p10978430"></a><a name="p10978430"></a><strong id="b2548193514715"><a name="b2548193514715"></a><a name="b2548193514715"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row16837643"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="p21671861"><a name="p21671861"></a><a name="p21671861"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p10590307"><a name="p10590307"></a><a name="p10590307"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.3 "><p id="p52508542"><a name="p52508542"></a><a name="p52508542"></a>Specifies the project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section3763446"></a>

-   Parameter description

    **Table  2**  Request parameters

    <a name="table5645742"></a>
    <table><thead align="left"><tr id="row43414540"><th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.5.1.1"><p id="p26916874"><a name="p26916874"></a><a name="p26916874"></a><strong id="b1193410431676"><a name="b1193410431676"></a><a name="b1193410431676"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.5.1.2"><p id="p32783160"><a name="p32783160"></a><a name="p32783160"></a><strong id="b1736978142"><a name="b1736978142"></a><a name="b1736978142"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.3"><p id="p38190270"><a name="p38190270"></a><a name="p38190270"></a><strong id="b1192018202817"><a name="b1192018202817"></a><a name="b1192018202817"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.46464646464647%" id="mcps1.2.5.1.4"><p id="p6404165"><a name="p6404165"></a><a name="p6404165"></a><strong id="b1785777389"><a name="b1785777389"></a><a name="b1785777389"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row48975348"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p7580276"><a name="p7580276"></a><a name="p7580276"></a>endpoint_service_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.2 "><p id="p10022637"><a name="p10022637"></a><a name="p10022637"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p6527238"><a name="p6527238"></a><a name="p6527238"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p58944231"><a name="p58944231"></a><a name="p58944231"></a>Specifies the name of the VPC endpoint service. The value is not case-sensitive and supports fuzzy match.</p>
    </td>
    </tr>
    <tr id="row60736034"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p20671747"><a name="p20671747"></a><a name="p20671747"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.2 "><p id="p63798849"><a name="p63798849"></a><a name="p63798849"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p324291"><a name="p324291"></a><a name="p324291"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p26267634"><a name="p26267634"></a><a name="p26267634"></a>Specifies the unique ID of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row35082117"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p23079266"><a name="p23079266"></a><a name="p23079266"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.2 "><p id="p57481247"><a name="p57481247"></a><a name="p57481247"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p25469412"><a name="p25469412"></a><a name="p25469412"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p49756506"><a name="p49756506"></a><a name="p49756506"></a>Specifies the status of the VPC endpoint service.</p>
    <a name="ul6347132317483"></a><a name="ul6347132317483"></a><ul id="ul6347132317483"><li><strong id="b148984611116"><a name="b148984611116"></a><a name="b148984611116"></a>creating</strong>: indicates the VPC endpoint service is being created.</li><li><strong id="b96779410228"><a name="b96779410228"></a><a name="b96779410228"></a>available</strong>: indicates the VPC endpoint service is connectable.</li><li><strong id="b15850165162214"><a name="b15850165162214"></a><a name="b15850165162214"></a>failed</strong>: indicates the creation of the VPC endpoint service failed.</li><li><strong id="b19521811171116"><a name="b19521811171116"></a><a name="b19521811171116"></a>deleting</strong>: indicates the VPC endpoint service is being deleted.</li></ul>
    </td>
    </tr>
    <tr id="row1922383593019"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p1122353518302"><a name="p1122353518302"></a><a name="p1122353518302"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.2 "><p id="p2439305315"><a name="p2439305315"></a><a name="p2439305315"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p1422315351303"><a name="p1422315351303"></a><a name="p1422315351303"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p1517010112277"><a name="p1517010112277"></a><a name="p1517010112277"></a>Specifies the sorting field of the VPC endpoint service list. The value can be:</p>
    <a name="ul248814136274"></a><a name="ul248814136274"></a><ul id="ul248814136274"><li><strong id="b91061528181018"><a name="b91061528181018"></a><a name="b91061528181018"></a>create_at</strong>: indicates that VPC endpoint services are sorted by creation time.</li><li><strong id="b10717101561115"><a name="b10717101561115"></a><a name="b10717101561115"></a>update_at</strong>: indicates that VPC endpoint services are sorted by update time.</li></ul>
    <p id="p31932603"><a name="p31932603"></a><a name="p31932603"></a>The default value is <strong id="b84581912152219"><a name="b84581912152219"></a><a name="b84581912152219"></a>create_at</strong>.</p>
    </td>
    </tr>
    <tr id="row36340727"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p57917784"><a name="p57917784"></a><a name="p57917784"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.2 "><p id="p60828929"><a name="p60828929"></a><a name="p60828929"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p28196251"><a name="p28196251"></a><a name="p28196251"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p116071347131216"><a name="p116071347131216"></a><a name="p116071347131216"></a>Specifies the sorting method of the VPC endpoint service list. The value can be:</p>
    <a name="ul18204217325"></a><a name="ul18204217325"></a><ul id="ul18204217325"><li><strong id="b842352706193046"><a name="b842352706193046"></a><a name="b842352706193046"></a>desc</strong>: indicates that VPC endpoint services are sorted in the descending order.</li><li><strong id="b84235270619316"><a name="b84235270619316"></a><a name="b84235270619316"></a>asc</strong>: indicates that VPC endpoint services are sorted in the ascending order.</li></ul>
    <p id="p3562616138"><a name="p3562616138"></a><a name="p3562616138"></a>The default value is <strong id="b84235270614202"><a name="b84235270614202"></a><a name="b84235270614202"></a>desc</strong>.</p>
    </td>
    </tr>
    <tr id="row56667338"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p26651648"><a name="p26651648"></a><a name="p26651648"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.2 "><p id="p11299916"><a name="p11299916"></a><a name="p11299916"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p42877971"><a name="p42877971"></a><a name="p42877971"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p50563647"><a name="p50563647"></a><a name="p50563647"></a>Specifies the maximum number of VPC endpoint services displayed on each page.</p>
    <p id="p52419647"><a name="p52419647"></a><a name="p52419647"></a>The value ranges from <strong id="b630941759"><a name="b630941759"></a><a name="b630941759"></a>0</strong> to <strong id="b16639174313512"><a name="b16639174313512"></a><a name="b16639174313512"></a>1000</strong> and is generally <strong id="b1913385273011"><a name="b1913385273011"></a><a name="b1913385273011"></a>10</strong>,<strong id="b191341552153016"><a name="b191341552153016"></a><a name="b191341552153016"></a> 20</strong>, or <strong id="b0135195223012"><a name="b0135195223012"></a><a name="b0135195223012"></a>50</strong>. The default value is <strong id="b63481226111015"><a name="b63481226111015"></a><a name="b63481226111015"></a>10</strong>.</p>
    </td>
    </tr>
    <tr id="row2014776"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="p28979173"><a name="p28979173"></a><a name="p28979173"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.2 "><p id="p65611695"><a name="p65611695"></a><a name="p65611695"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p12947069"><a name="p12947069"></a><a name="p12947069"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p183133831912"><a name="p183133831912"></a><a name="p183133831912"></a>Specifies the offset.</p>
    <p id="p11316385191"><a name="p11316385191"></a><a name="p11316385191"></a>All VPC endpoint services after this offset will be queried. The value must be an integer greater than 0 but less than the number of VPC endpoint services.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    GET https://{endpoint}/v1/{project_id}/vpc-endpoint-services
    ```


## Response<a name="section36403741"></a>

-   Parameter description

    **Table  3**  Response parameters

    <a name="table50811679"></a>
    <table><thead align="left"><tr id="row1443251"><th class="cellrowborder" valign="top" width="24.242424242424242%" id="mcps1.2.4.1.1"><p id="p49794519"><a name="p49794519"></a><a name="p49794519"></a><strong id="b1632542405"><a name="b1632542405"></a><a name="b1632542405"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.292929292929294%" id="mcps1.2.4.1.2"><p id="p6824202"><a name="p6824202"></a><a name="p6824202"></a><strong id="b2136747562"><a name="b2136747562"></a><a name="b2136747562"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.464646464646464%" id="mcps1.2.4.1.3"><p id="p15889527"><a name="p15889527"></a><a name="p15889527"></a><strong id="b730788209"><a name="b730788209"></a><a name="b730788209"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11983300"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p31123225"><a name="p31123225"></a><a name="p31123225"></a>endpoint_services</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p37953311"><a name="p37953311"></a><a name="p37953311"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p54319357"><a name="p54319357"></a><a name="p54319357"></a>Lists the VPC endpoint services. For details, see <a href="#table11315049">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row19112173"><td class="cellrowborder" valign="top" width="24.242424242424242%" headers="mcps1.2.4.1.1 "><p id="p4582212"><a name="p4582212"></a><a name="p4582212"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="p35614854"><a name="p35614854"></a><a name="p35614854"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.464646464646464%" headers="mcps1.2.4.1.3 "><p id="p18744171320381"><a name="p18744171320381"></a><a name="p18744171320381"></a>Specifies the total number of VPC endpoint services that meet the search criteria. The number is not affected by the limit or offset.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **endpoint\_service**  parameters

    <a name="table11315049"></a>
    <table><thead align="left"><tr id="row58655549"><th class="cellrowborder" valign="top" width="19.59%" id="mcps1.2.4.1.1"><p id="p53478999"><a name="p53478999"></a><a name="p53478999"></a><strong id="b17339161315186"><a name="b17339161315186"></a><a name="b17339161315186"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.59%" id="mcps1.2.4.1.2"><p id="p36831645"><a name="p36831645"></a><a name="p36831645"></a><strong id="b1888305494"><a name="b1888305494"></a><a name="b1888305494"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="60.81999999999999%" id="mcps1.2.4.1.3"><p id="p30573305"><a name="p30573305"></a><a name="p30573305"></a><strong id="b440422620"><a name="b440422620"></a><a name="b440422620"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60518608"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.1 "><p id="p3060236"><a name="p3060236"></a><a name="p3060236"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.2 "><p id="p46552597"><a name="p46552597"></a><a name="p46552597"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.81999999999999%" headers="mcps1.2.4.1.3 "><p id="p18497559"><a name="p18497559"></a><a name="p18497559"></a>Specifies the unique ID of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row46867304"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.1 "><p id="p38155279"><a name="p38155279"></a><a name="p38155279"></a>port_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.2 "><p id="p3569886"><a name="p3569886"></a><a name="p3569886"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.81999999999999%" headers="mcps1.2.4.1.3 "><p id="p23501288"><a name="p23501288"></a><a name="p23501288"></a>Specifies the ID for identifying the backend resource of the VPC endpoint service. The ID is in the form of the UUID. The value is as follows:</p>
    <a name="ul16432132118180"></a><a name="ul16432132118180"></a><ul id="ul16432132118180"><li>If the backend service is an enhanced load balancer, the value is the ID of the port bound to the private IP address of the load balancer.</li><li>If the backend resource is an ECS, the value is the NIC ID of the ECS where the VPC endpoint service is deployed.</li><li>If the backend resource is a virtual IP address, the value is the NIC ID of the physical server where virtual resources are created.</li></ul>
    </td>
    </tr>
    <tr id="row177242001419"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.1 "><p id="p8159433171415"><a name="p8159433171415"></a><a name="p8159433171415"></a>vip_port_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.2 "><p id="p71591433171417"><a name="p71591433171417"></a><a name="p71591433171417"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.81999999999999%" headers="mcps1.2.4.1.3 "><p id="p12742155131712"><a name="p12742155131712"></a><a name="p12742155131712"></a>Specifies the ID of the virtual NIC to which the virtual IP address is bound.</p>
    <p id="p17311725769"><a name="p17311725769"></a><a name="p17311725769"></a>This parameter is returned only when <strong id="b14305337131"><a name="b14305337131"></a><a name="b14305337131"></a>port_id</strong> is set to VIP.</p>
    </td>
    </tr>
    <tr id="row24563651"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.1 "><p id="p43498701"><a name="p43498701"></a><a name="p43498701"></a>service_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.2 "><p id="p33733912"><a name="p33733912"></a><a name="p33733912"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.81999999999999%" headers="mcps1.2.4.1.3 "><p id="p48092364"><a name="p48092364"></a><a name="p48092364"></a>Specifies the name of the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row18205265"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.1 "><p id="p65340323"><a name="p65340323"></a><a name="p65340323"></a>server_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.2 "><p id="p58074826"><a name="p58074826"></a><a name="p58074826"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.81999999999999%" headers="mcps1.2.4.1.3 "><p id="p1497382074811"><a name="p1497382074811"></a><a name="p1497382074811"></a>Specifies the resource type.</p>
    <a name="ul1417663314354"></a><a name="ul1417663314354"></a><ul id="ul1417663314354"><li><strong id="vpcep_06_0201_b111511354539"><a name="vpcep_06_0201_b111511354539"></a><a name="vpcep_06_0201_b111511354539"></a>VM</strong>: indicates the ECS.</li><li><strong id="vpcep_06_0201_b111348551533"><a name="vpcep_06_0201_b111348551533"></a><a name="vpcep_06_0201_b111348551533"></a>VIP</strong>: indicates the virtual IP address.</li><li><strong id="vpcep_06_0201_b1842415561432"><a name="vpcep_06_0201_b1842415561432"></a><a name="vpcep_06_0201_b1842415561432"></a>LB</strong>: indicates the enhanced load balancer.</li></ul>
    </td>
    </tr>
    <tr id="row202495420397"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.1 "><p id="p6282859"><a name="p6282859"></a><a name="p6282859"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.2 "><p id="p39149581"><a name="p39149581"></a><a name="p39149581"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.81999999999999%" headers="mcps1.2.4.1.3 "><p id="p16536246191512"><a name="p16536246191512"></a><a name="p16536246191512"></a>Specifies the ID of the VPC to which the backend resource of the VPC endpoint service belongs.</p>
    </td>
    </tr>
    <tr id="row64608875"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.1 "><p id="p65936421"><a name="p65936421"></a><a name="p65936421"></a>approval_enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.2 "><p id="p39249912"><a name="p39249912"></a><a name="p39249912"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.81999999999999%" headers="mcps1.2.4.1.3 "><p id="p11315182920485"><a name="p11315182920485"></a><a name="p11315182920485"></a>Specifies whether connection approval is required.</p>
    <a name="ul175221837143510"></a><a name="ul175221837143510"></a><ul id="ul175221837143510"><li><strong id="vpcep_06_0201_b1836705966"><a name="vpcep_06_0201_b1836705966"></a><a name="vpcep_06_0201_b1836705966"></a>false</strong>: indicates that connection approval is not required. The created VPC endpoint is in the <strong id="vpcep_06_0201_b15309009"><a name="vpcep_06_0201_b15309009"></a><a name="vpcep_06_0201_b15309009"></a>Accepted</strong> state.</li><li><strong id="vpcep_06_0201_b1374184052"><a name="vpcep_06_0201_b1374184052"></a><a name="vpcep_06_0201_b1374184052"></a>true</strong>: indicates that connection approval is required. The created VPC endpoint is in the <strong id="vpcep_06_0201_b724489048"><a name="vpcep_06_0201_b724489048"></a><a name="vpcep_06_0201_b724489048"></a>Pending acceptance</strong> state until the owner of the associated VPC endpoint service approves the connection.</li></ul>
    </td>
    </tr>
    <tr id="row34173714"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.1 "><p id="p16607446"><a name="p16607446"></a><a name="p16607446"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.2 "><p id="p3025915"><a name="p3025915"></a><a name="p3025915"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.81999999999999%" headers="mcps1.2.4.1.3 "><p id="p13535121115119"><a name="p13535121115119"></a><a name="p13535121115119"></a>Specifies the status of the VPC endpoint service.</p>
    <a name="ul16737041185119"></a><a name="ul16737041185119"></a><ul id="ul16737041185119"><li><strong id="b689300463"><a name="b689300463"></a><a name="b689300463"></a>creating</strong>: indicates the VPC endpoint service is being created.</li><li><strong id="b17785192602216"><a name="b17785192602216"></a><a name="b17785192602216"></a>available</strong>: indicates the VPC endpoint service is connectable.</li><li><strong id="b10839928162214"><a name="b10839928162214"></a><a name="b10839928162214"></a>failed</strong>: indicates the creation of the VPC endpoint service failed.</li><li><strong id="b992684800"><a name="b992684800"></a><a name="b992684800"></a>deleting</strong>: indicates the VPC endpoint service is being deleted.</li></ul>
    </td>
    </tr>
    <tr id="row39472279"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.1 "><p id="p43138034"><a name="p43138034"></a><a name="p43138034"></a>service_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.2 "><p id="p4519841"><a name="p4519841"></a><a name="p4519841"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.81999999999999%" headers="mcps1.2.4.1.3 "><p id="p135911520141219"><a name="p135911520141219"></a><a name="p135911520141219"></a>Specifies the type of the VPC endpoint service.</p>
    <div class="p" id="p3359114552814"><a name="p3359114552814"></a><a name="p3359114552814"></a>There are two types of VPC endpoint services: interface and gateway.<a name="vpcep_06_0201_ul87241928184613"></a><a name="vpcep_06_0201_ul87241928184613"></a><ul id="vpcep_06_0201_ul87241928184613"><li>Gateway: VPC endpoint services of this type are configured by operations people. You can use them directly without the need to create one by yourselves.</li><li>Interface: VPC endpoint services of this type include cloud services configured by operations people and private services created by yourselves. You cannot configure these cloud services, but can use them.</li></ul>
    </div>
    <p id="p941115410718"><a name="p941115410718"></a><a name="p941115410718"></a>You can perform the operations in <a href="creating-a-vpc-endpoint.md">Creating a VPC Endpoint</a> to create VPC endpoints for accessing VPC endpoints of the gateway and interface types.</p>
    </td>
    </tr>
    <tr id="row6630005"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.1 "><p id="p159494"><a name="p159494"></a><a name="p159494"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.2 "><p id="p12919048"><a name="p12919048"></a><a name="p12919048"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.81999999999999%" headers="mcps1.2.4.1.3 "><p id="p22890001"><a name="p22890001"></a><a name="p22890001"></a>Specifies the creation time of the VPC endpoint service.</p>
    <p id="p871616113394"><a name="p871616113394"></a><a name="p871616113394"></a>The UTC time format is used: YYYY-MM-DDTHH:MM:SSZ.</p>
    </td>
    </tr>
    <tr id="row22745272"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.1 "><p id="p30427754"><a name="p30427754"></a><a name="p30427754"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.2 "><p id="p48729033"><a name="p48729033"></a><a name="p48729033"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.81999999999999%" headers="mcps1.2.4.1.3 "><p id="p27321481"><a name="p27321481"></a><a name="p27321481"></a>Specifies the update time of the VPC endpoint service.</p>
    <p id="p181016810016"><a name="p181016810016"></a><a name="p181016810016"></a>The UTC time format is used: YYYY-MM-DDTHH:MM:SSZ.</p>
    </td>
    </tr>
    <tr id="row22876321"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.1 "><p id="p41042702"><a name="p41042702"></a><a name="p41042702"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.2 "><p id="p36124547"><a name="p36124547"></a><a name="p36124547"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.81999999999999%" headers="mcps1.2.4.1.3 "><p id="p40407209"><a name="p40407209"></a><a name="p40407209"></a>Specifies the project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row28120566"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.1 "><p id="p63173351"><a name="p63173351"></a><a name="p63173351"></a>ports</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.2 "><p id="p16767838"><a name="p16767838"></a><a name="p16767838"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.81999999999999%" headers="mcps1.2.4.1.3 "><p id="p5656200651"><a name="p5656200651"></a><a name="p5656200651"></a>Lists the port mappings opened to the VPC endpoint service. For details, see <a href="#table31283788">Table 5</a>.</p>
    <p id="p3651104885713"><a name="p3651104885713"></a><a name="p3651104885713"></a>Duplicate port mappings are not allowed in the same VPC endpoint service. If multiple VPC endpoint services share the same <strong id="vpcep_06_0201_b159801931141111"><a name="vpcep_06_0201_b159801931141111"></a><a name="vpcep_06_0201_b159801931141111"></a>port_id</strong> value, service ports and terminal ports of all these endpoint services cannot be duplicated when the protocol is the same.</p>
    </td>
    </tr>
    <tr id="row58021781920"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.1 "><p id="p13103244015"><a name="p13103244015"></a><a name="p13103244015"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.2 "><p id="p21037441512"><a name="p21037441512"></a><a name="p21037441512"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.81999999999999%" headers="mcps1.2.4.1.3 "><p id="p1510414411116"><a name="p1510414411116"></a><a name="p1510414411116"></a>Lists the resource tags. For details, see <a href="#table489217571060">Table 6</a>.</p>
    </td>
    </tr>
    <tr id="row5508840184111"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.1 "><p id="p185091040184118"><a name="p185091040184118"></a><a name="p185091040184118"></a>connection_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.2 "><p id="p35097402411"><a name="p35097402411"></a><a name="p35097402411"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.81999999999999%" headers="mcps1.2.4.1.3 "><p id="p1650984011411"><a name="p1650984011411"></a><a name="p1650984011411"></a>Specifies the number of <strong id="b863117258508"><a name="b863117258508"></a><a name="b863117258508"></a>Creating</strong> or <strong id="b4632122525016"><a name="b4632122525016"></a><a name="b4632122525016"></a>Accepted</strong> VPC endpoints under the VPC endpoint service.</p>
    </td>
    </tr>
    <tr id="row1794114562189"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.1 "><p id="p6679144311349"><a name="p6679144311349"></a><a name="p6679144311349"></a>tcp_proxy</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.2 "><p id="p1867920439347"><a name="p1867920439347"></a><a name="p1867920439347"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.81999999999999%" headers="mcps1.2.4.1.3 "><p id="p3988426182213"><a name="p3988426182213"></a><a name="p3988426182213"></a>Specifies whether the client IP address and port number or <strong id="vpcep_06_0201_b1340623194912"><a name="vpcep_06_0201_b1340623194912"></a><a name="vpcep_06_0201_b1340623194912"></a>marker_id</strong> information is transmitted to the server. The following methods are supported:</p>
    <a name="ul113422343220"></a><a name="ul113422343220"></a><ul id="ul113422343220"><li>TCP TOA: The client information is inserted into field <strong id="vpcep_06_0201_b1328024583915"><a name="vpcep_06_0201_b1328024583915"></a><a name="vpcep_06_0201_b1328024583915"></a>tcp option</strong> and transmitted to the server.</li><li>Proxy Protocol: The client information is inserted into field <strong id="vpcep_06_0201_b18340846124016"><a name="vpcep_06_0201_b18340846124016"></a><a name="vpcep_06_0201_b18340846124016"></a>tcp payload</strong> and transmitted to the server.</li></ul>
    <p id="p117219186296"><a name="p117219186296"></a><a name="p117219186296"></a>This parameter is available only when the server can parse fields <strong id="vpcep_06_0201_b1246063817713"><a name="vpcep_06_0201_b1246063817713"></a><a name="vpcep_06_0201_b1246063817713"></a>tcp option</strong> and <strong id="vpcep_06_0201_b832154415710"><a name="vpcep_06_0201_b832154415710"></a><a name="vpcep_06_0201_b832154415710"></a>tcp payload</strong>.</p>
    <p id="p29385542114"><a name="p29385542114"></a><a name="p29385542114"></a>The values are as follows:</p>
    <a name="ul523712223"></a><a name="ul523712223"></a><ul id="ul523712223"><li><strong id="vpcep_06_0201_b485111422"><a name="vpcep_06_0201_b485111422"></a><a name="vpcep_06_0201_b485111422"></a>close</strong>: indicates that the TOA and Proxy Protocol methods are neither used.</li><li><strong id="vpcep_06_0201_b1432825911248"><a name="vpcep_06_0201_b1432825911248"></a><a name="vpcep_06_0201_b1432825911248"></a>toa_open</strong>: indicates that the TOA method is used.</li><li><strong id="vpcep_06_0201_b1394119162519"><a name="vpcep_06_0201_b1394119162519"></a><a name="vpcep_06_0201_b1394119162519"></a>proxy_open</strong>: indicates that the Proxy Protocol method is used.</li><li><strong id="vpcep_06_0201_b123462452517"><a name="vpcep_06_0201_b123462452517"></a><a name="vpcep_06_0201_b123462452517"></a>open</strong>: indicates that the TOA and Proxy Protocol methods are both used.</li></ul>
    <p id="p1725615331720"><a name="p1725615331720"></a><a name="p1725615331720"></a>The default value is <strong id="vpcep_06_0201_b842352706144841"><a name="vpcep_06_0201_b842352706144841"></a><a name="vpcep_06_0201_b842352706144841"></a>close</strong>.</p>
    </td>
    </tr>
    <tr id="row11979515"><td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.1 "><p id="p134782274443"><a name="p134782274443"></a><a name="p134782274443"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.4.1.2 "><p id="p20478112713443"><a name="p20478112713443"></a><a name="p20478112713443"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.81999999999999%" headers="mcps1.2.4.1.3 "><p id="p12568428134419"><a name="p12568428134419"></a><a name="p12568428134419"></a>Specifies the error message.</p>
    <p id="p2478152724413"><a name="p2478152724413"></a><a name="p2478152724413"></a>This field is returned when the status of the VPC endpoint service changes to <strong id="b1015018215149"><a name="b1015018215149"></a><a name="b1015018215149"></a>failed</strong>. For details, see <a href="#table178701348456">Table 7</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  Port mapping parameters

    <a name="table31283788"></a>
    <table><thead align="left"><tr id="vpcep_06_0201_en-us_topic_0178993304_row54069340"><th class="cellrowborder" valign="top" width="17.98%" id="mcps1.2.4.1.1"><p id="vpcep_06_0201_en-us_topic_0178993304_p17540449"><a name="vpcep_06_0201_en-us_topic_0178993304_p17540449"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p17540449"></a><strong id="vpcep_06_0201_b8302057171210"><a name="vpcep_06_0201_b8302057171210"></a><a name="vpcep_06_0201_b8302057171210"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.650000000000002%" id="mcps1.2.4.1.2"><p id="vpcep_06_0201_en-us_topic_0178993304_p11490287"><a name="vpcep_06_0201_en-us_topic_0178993304_p11490287"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p11490287"></a><strong id="vpcep_06_0201_b1355134319224"><a name="vpcep_06_0201_b1355134319224"></a><a name="vpcep_06_0201_b1355134319224"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="62.370000000000005%" id="mcps1.2.4.1.3"><p id="vpcep_06_0201_en-us_topic_0178993304_p58298029"><a name="vpcep_06_0201_en-us_topic_0178993304_p58298029"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p58298029"></a><strong id="vpcep_06_0201_b735778700"><a name="vpcep_06_0201_b735778700"></a><a name="vpcep_06_0201_b735778700"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="vpcep_06_0201_en-us_topic_0178993304_row24519875"><td class="cellrowborder" valign="top" width="17.98%" headers="mcps1.2.4.1.1 "><p id="vpcep_06_0201_en-us_topic_0178993304_p39952858"><a name="vpcep_06_0201_en-us_topic_0178993304_p39952858"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p39952858"></a>client_port</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.650000000000002%" headers="mcps1.2.4.1.2 "><p id="vpcep_06_0201_p88823381809"><a name="vpcep_06_0201_p88823381809"></a><a name="vpcep_06_0201_p88823381809"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.370000000000005%" headers="mcps1.2.4.1.3 "><p id="vpcep_06_0201_en-us_topic_0178993304_p3481129"><a name="vpcep_06_0201_en-us_topic_0178993304_p3481129"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p3481129"></a>Specifies the port for accessing the VPC endpoint.</p>
    <p id="vpcep_06_0201_en-us_topic_0178993304_p209011349124811"><a name="vpcep_06_0201_en-us_topic_0178993304_p209011349124811"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p209011349124811"></a>This port is provided by the VPC endpoint, allowing you to access the VPC endpoint service. The value ranges from <strong id="vpcep_06_0201_b1871853314113"><a name="vpcep_06_0201_b1871853314113"></a><a name="vpcep_06_0201_b1871853314113"></a>1</strong> to <strong id="vpcep_06_0201_b14719173314116"><a name="vpcep_06_0201_b14719173314116"></a><a name="vpcep_06_0201_b14719173314116"></a>65535</strong>.</p>
    </td>
    </tr>
    <tr id="vpcep_06_0201_en-us_topic_0178993304_row31330167"><td class="cellrowborder" valign="top" width="17.98%" headers="mcps1.2.4.1.1 "><p id="vpcep_06_0201_en-us_topic_0178993304_p54715587"><a name="vpcep_06_0201_en-us_topic_0178993304_p54715587"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p54715587"></a>server_port</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.650000000000002%" headers="mcps1.2.4.1.2 "><p id="vpcep_06_0201_en-us_topic_0178993304_p2777523"><a name="vpcep_06_0201_en-us_topic_0178993304_p2777523"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p2777523"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.370000000000005%" headers="mcps1.2.4.1.3 "><p id="vpcep_06_0201_en-us_topic_0178993304_p23652783"><a name="vpcep_06_0201_en-us_topic_0178993304_p23652783"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p23652783"></a>Specifies the port for accessing the VPC endpoint service.</p>
    <p id="vpcep_06_0201_en-us_topic_0178993304_p1136918011496"><a name="vpcep_06_0201_en-us_topic_0178993304_p1136918011496"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p1136918011496"></a>This port is provided by the backend service to provide services. The value ranges from <strong id="vpcep_06_0201_b1141065692215"><a name="vpcep_06_0201_b1141065692215"></a><a name="vpcep_06_0201_b1141065692215"></a>1</strong> to <strong id="vpcep_06_0201_b204105566224"><a name="vpcep_06_0201_b204105566224"></a><a name="vpcep_06_0201_b204105566224"></a>65535</strong>.</p>
    </td>
    </tr>
    <tr id="vpcep_06_0201_en-us_topic_0178993304_row11548462"><td class="cellrowborder" valign="top" width="17.98%" headers="mcps1.2.4.1.1 "><p id="vpcep_06_0201_en-us_topic_0178993304_p63010216"><a name="vpcep_06_0201_en-us_topic_0178993304_p63010216"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p63010216"></a>protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.650000000000002%" headers="mcps1.2.4.1.2 "><p id="vpcep_06_0201_en-us_topic_0178993304_p3553891"><a name="vpcep_06_0201_en-us_topic_0178993304_p3553891"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p3553891"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.370000000000005%" headers="mcps1.2.4.1.3 "><p id="vpcep_06_0201_en-us_topic_0178993304_p19429767"><a name="vpcep_06_0201_en-us_topic_0178993304_p19429767"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p19429767"></a>Specifies the protocol used in port mappings. The value can be <strong id="vpcep_06_0201_b2110651230"><a name="vpcep_06_0201_b2110651230"></a><a name="vpcep_06_0201_b2110651230"></a>TCP</strong> or <strong id="vpcep_06_0201_b51117516233"><a name="vpcep_06_0201_b51117516233"></a><a name="vpcep_06_0201_b51117516233"></a>UDP</strong>. The default value is <strong id="vpcep_06_0201_b511115152312"><a name="vpcep_06_0201_b511115152312"></a><a name="vpcep_06_0201_b511115152312"></a>TCP</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **ResourceTags**  parameters

    <a name="table489217571060"></a>
    <table><thead align="left"><tr id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_row4410728"><th class="cellrowborder" valign="top" width="18.09%" id="mcps1.2.4.1.1"><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p21724664"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p21724664"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p21724664"></a><strong id="vpcep_06_0201_b1866348132314"><a name="vpcep_06_0201_b1866348132314"></a><a name="vpcep_06_0201_b1866348132314"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p63406242"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p63406242"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p63406242"></a><strong id="vpcep_06_0201_b616714104231"><a name="vpcep_06_0201_b616714104231"></a><a name="vpcep_06_0201_b616714104231"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="61.91%" id="mcps1.2.4.1.3"><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p35632012"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p35632012"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p35632012"></a><strong id="vpcep_06_0201_b163691023811"><a name="vpcep_06_0201_b163691023811"></a><a name="vpcep_06_0201_b163691023811"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_row511887"><td class="cellrowborder" valign="top" width="18.09%" headers="mcps1.2.4.1.1 "><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p41462866"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p41462866"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p41462866"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p45638969"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p45638969"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p45638969"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.91%" headers="mcps1.2.4.1.3 "><p id="vpcep_06_0201_en-us_topic_0178993304_p48921437201850"><a name="vpcep_06_0201_en-us_topic_0178993304_p48921437201850"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p48921437201850"></a>Specifies the tag key. A tag key contains a maximum of 36 Unicode characters. This parameter cannot be left empty. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_row51921052"><td class="cellrowborder" valign="top" width="18.09%" headers="mcps1.2.4.1.1 "><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p44855704"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p44855704"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p44855704"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p25911262"><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p25911262"></a><a name="vpcep_06_0201_en-us_topic_0178993304_en-us_topic_0056765542_p25911262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.91%" headers="mcps1.2.4.1.3 "><p id="vpcep_06_0201_en-us_topic_0178993304_p61714725112922"><a name="vpcep_06_0201_en-us_topic_0178993304_p61714725112922"></a><a name="vpcep_06_0201_en-us_topic_0178993304_p61714725112922"></a>Specifies the tag value. A tag value contains a maximum of 43 Unicode characters and can be left blank. It can contain only digits, letters, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7**  Error parameters

    <a name="table178701348456"></a>
    <table><thead align="left"><tr id="vpcep_06_0202_row4652255153018"><th class="cellrowborder" valign="top" width="18.34%" id="mcps1.2.4.1.1"><p id="vpcep_06_0202_p665015573309"><a name="vpcep_06_0202_p665015573309"></a><a name="vpcep_06_0202_p665015573309"></a><strong id="vpcep_06_0202_b085424117110"><a name="vpcep_06_0202_b085424117110"></a><a name="vpcep_06_0202_b085424117110"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.630000000000003%" id="mcps1.2.4.1.2"><p id="vpcep_06_0202_p865015710307"><a name="vpcep_06_0202_p865015710307"></a><a name="vpcep_06_0202_p865015710307"></a><strong id="vpcep_06_0202_b1597841565"><a name="vpcep_06_0202_b1597841565"></a><a name="vpcep_06_0202_b1597841565"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="61.029999999999994%" id="mcps1.2.4.1.3"><p id="vpcep_06_0202_p1565011575303"><a name="vpcep_06_0202_p1565011575303"></a><a name="vpcep_06_0202_p1565011575303"></a><strong id="vpcep_06_0202_b1010514442017"><a name="vpcep_06_0202_b1010514442017"></a><a name="vpcep_06_0202_b1010514442017"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="vpcep_06_0202_row865255513010"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="vpcep_06_0202_p96501057153013"><a name="vpcep_06_0202_p96501057153013"></a><a name="vpcep_06_0202_p96501057153013"></a>error_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.630000000000003%" headers="mcps1.2.4.1.2 "><p id="vpcep_06_0202_p6650155710309"><a name="vpcep_06_0202_p6650155710309"></a><a name="vpcep_06_0202_p6650155710309"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.029999999999994%" headers="mcps1.2.4.1.3 "><p id="vpcep_06_0202_p12650557133019"><a name="vpcep_06_0202_p12650557133019"></a><a name="vpcep_06_0202_p12650557133019"></a>Specifies the error code.</p>
    </td>
    </tr>
    <tr id="vpcep_06_0202_row186521755153018"><td class="cellrowborder" valign="top" width="18.34%" headers="mcps1.2.4.1.1 "><p id="vpcep_06_0202_p10650057123018"><a name="vpcep_06_0202_p10650057123018"></a><a name="vpcep_06_0202_p10650057123018"></a>error_message</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.630000000000003%" headers="mcps1.2.4.1.2 "><p id="vpcep_06_0202_p14650157113016"><a name="vpcep_06_0202_p14650157113016"></a><a name="vpcep_06_0202_p14650157113016"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.029999999999994%" headers="mcps1.2.4.1.3 "><p id="vpcep_06_0202_p156501957183013"><a name="vpcep_06_0202_p156501957183013"></a><a name="vpcep_06_0202_p156501957183013"></a>Specifies the error message.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
       "endpoint_services":[
             {
               "id":"4189d3c2-8882-4871-a3c2-d380272eed83",
               "port_id":"4189d3c2-8882-4871-a3c2-d380272eed88",
               "vpc_id":"4189d3c2-8882-4871-a3c2-d380272eed80",
               "status":"available",
               "approval_enabled":false,
               "service_name":"test123",
               "server_type":"VM",
               "service_type":"interface",
               "ports":[
                    {
                      "client_port":8080,
                      "server_port":90,
                      "protocol":"TCP"
                    },
                    {
                      "client_port":8081,
                      "server_port":80,
                      "protocol":"TCP"
                    }
                 ],
               "project_id":"6e9dfd51d1124e8d8498dce894923a0d",
               "created_at":"2018-01-30T07:42:01.174",
               "update_at":"2018-01-30T07:42:01.174"
             }
         ],
       "total_count":100
    }
    ```



# Querying Details About a BMS Flavor \(Native OpenStack API\)<a name="EN-US_TOPIC_0053158674"></a>

## Function<a name="section64833508"></a>

This API is used to query details about a BMS flavor, such as the flavor name, CPU cores, and memory.

## URI<a name="section46630661"></a>

GET /v2.1/\{project\_id\}/flavors/\{flavors\_id\}

[Table 1](#table1857156445)  lists the parameters.

**Table  1**  Parameter description

<a name="table1857156445"></a>
<table><thead align="left"><tr id="row98631534416"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p26298136"><a name="p26298136"></a><a name="p26298136"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p49774232"><a name="p49774232"></a><a name="p49774232"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p5180964"><a name="p5180964"></a><a name="p5180964"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row58681534411"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p35224963"><a name="p35224963"></a><a name="p35224963"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p34649765"><a name="p34649765"></a><a name="p34649765"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p55167604"><a name="p55167604"></a><a name="p55167604"></a>Specifies the project ID.</p>
<p id="p9141450142010"><a name="p9141450142010"></a><a name="p9141450142010"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row98691534416"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p18974100"><a name="p18974100"></a><a name="p18974100"></a>flavors_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p60507121"><a name="p60507121"></a><a name="p60507121"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p2129750"><a name="p2129750"></a><a name="p2129750"></a>Specifies the flavor ID.</p>
<p id="p1153834112450"><a name="p1153834112450"></a><a name="p1153834112450"></a>You can obtain the flavor ID from the <span id="text374914110111"><a name="text374914110111"></a><a name="text374914110111"></a>BMS</span><span id="text1749131818"><a name="text1749131818"></a><a name="text1749131818"></a></span> console or using the <a href="querying-bms-flavors-(native-openstack-api).md">Querying BMS Flavors (Native OpenStack API)</a> API.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section17022773"></a>

-   Request parameters

    None

-   Example request

    ```
    GET https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/flavors/physical.o2.medium
    ```


## Response Message<a name="section18987236"></a>

-   Response parameters

    <a name="table61695723"></a>
    <table><thead align="left"><tr id="row52977523"><th class="cellrowborder" valign="top" width="25.41%" id="mcps1.1.4.1.1"><p id="p59978491115233"><a name="p59978491115233"></a><a name="p59978491115233"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.619999999999997%" id="mcps1.1.4.1.2"><p id="p26419641115233"><a name="p26419641115233"></a><a name="p26419641115233"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.97%" id="mcps1.1.4.1.3"><p id="p64181866115233"><a name="p64181866115233"></a><a name="p64181866115233"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2794650"><td class="cellrowborder" valign="top" width="25.41%" headers="mcps1.1.4.1.1 "><p id="p25040094"><a name="p25040094"></a><a name="p25040094"></a>flavor</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.619999999999997%" headers="mcps1.1.4.1.2 "><p id="p5563313"><a name="p5563313"></a><a name="p5563313"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.97%" headers="mcps1.1.4.1.3 "><p id="p29123463"><a name="p29123463"></a><a name="p29123463"></a>Specifies the <span id="text3829312517"><a name="text3829312517"></a><a name="text3829312517"></a>BMS</span><span id="text482913122112"><a name="text482913122112"></a><a name="text482913122112"></a></span> flavor. For details, see <a href="#table20109663">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **flavor**  field description

    <a name="table20109663"></a>
    <table><thead align="left"><tr id="row50842877"><th class="cellrowborder" valign="top" width="26.169999999999998%" id="mcps1.2.4.1.1"><p id="p17447358101319"><a name="p17447358101319"></a><a name="p17447358101319"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.990000000000002%" id="mcps1.2.4.1.2"><p id="p14450195812134"><a name="p14450195812134"></a><a name="p14450195812134"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.839999999999996%" id="mcps1.2.4.1.3"><p id="p12452195881310"><a name="p12452195881310"></a><a name="p12452195881310"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37029065"><td class="cellrowborder" valign="top" width="26.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p46564252"><a name="p46564252"></a><a name="p46564252"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.990000000000002%" headers="mcps1.2.4.1.2 "><p id="p28514710"><a name="p28514710"></a><a name="p28514710"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p50584809"><a name="p50584809"></a><a name="p50584809"></a>Specifies the <span id="text115310534115"><a name="text115310534115"></a><a name="text115310534115"></a>BMS</span><span id="text153119535117"><a name="text153119535117"></a><a name="text153119535117"></a></span> flavor ID.</p>
    </td>
    </tr>
    <tr id="row52610097"><td class="cellrowborder" valign="top" width="26.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p33559471"><a name="p33559471"></a><a name="p33559471"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.990000000000002%" headers="mcps1.2.4.1.2 "><p id="p66621782"><a name="p66621782"></a><a name="p66621782"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p47570623"><a name="p47570623"></a><a name="p47570623"></a>Specifies the <span id="text1160529361"><a name="text1160529361"></a><a name="text1160529361"></a>BMS</span><span id="text196057914619"><a name="text196057914619"></a><a name="text196057914619"></a></span> flavor name.</p>
    </td>
    </tr>
    <tr id="row25482430"><td class="cellrowborder" valign="top" width="26.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p50810959"><a name="p50810959"></a><a name="p50810959"></a>vcpus</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.990000000000002%" headers="mcps1.2.4.1.2 "><p id="p40977906"><a name="p40977906"></a><a name="p40977906"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p9449599"><a name="p9449599"></a><a name="p9449599"></a>Specifies the number of CPU cores in the <span id="text19872175810116"><a name="text19872175810116"></a><a name="text19872175810116"></a>BMS</span><span id="text1587219584117"><a name="text1587219584117"></a><a name="text1587219584117"></a></span> flavor.</p>
    </td>
    </tr>
    <tr id="row2289826710437"><td class="cellrowborder" valign="top" width="26.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p6260494310453"><a name="p6260494310453"></a><a name="p6260494310453"></a>ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.990000000000002%" headers="mcps1.2.4.1.2 "><p id="p3783561810453"><a name="p3783561810453"></a><a name="p3783561810453"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p42285210453"><a name="p42285210453"></a><a name="p42285210453"></a>Specifies the memory size (MB) in the <span id="text6332134716614"><a name="text6332134716614"></a><a name="text6332134716614"></a>BMS</span><span id="text123331478611"><a name="text123331478611"></a><a name="text123331478611"></a></span> flavor.</p>
    </td>
    </tr>
    <tr id="row17937528"><td class="cellrowborder" valign="top" width="26.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p43653635"><a name="p43653635"></a><a name="p43653635"></a>disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.990000000000002%" headers="mcps1.2.4.1.2 "><p id="p57980147"><a name="p57980147"></a><a name="p57980147"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p56052334"><a name="p56052334"></a><a name="p56052334"></a>Specifies the disk size (GB) in the <span id="text5421146717"><a name="text5421146717"></a><a name="text5421146717"></a>BMS</span><span id="text1436417714"><a name="text1436417714"></a><a name="text1436417714"></a></span> flavor.</p>
    </td>
    </tr>
    <tr id="row43945239"><td class="cellrowborder" valign="top" width="26.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p2794612"><a name="p2794612"></a><a name="p2794612"></a>swap</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.990000000000002%" headers="mcps1.2.4.1.2 "><p id="p14734188"><a name="p14734188"></a><a name="p14734188"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p1160474410518"><a name="p1160474410518"></a><a name="p1160474410518"></a>This is a reserved attribute.</p>
    </td>
    </tr>
    <tr id="row34246806"><td class="cellrowborder" valign="top" width="26.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p22527890"><a name="p22527890"></a><a name="p22527890"></a>OS-FLV-EXT-DATA:ephemeral</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.990000000000002%" headers="mcps1.2.4.1.2 "><p id="p31767774"><a name="p31767774"></a><a name="p31767774"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p414192310518"><a name="p414192310518"></a><a name="p414192310518"></a>This is a reserved attribute.</p>
    </td>
    </tr>
    <tr id="row55347837"><td class="cellrowborder" valign="top" width="26.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p53989823"><a name="p53989823"></a><a name="p53989823"></a>OS-FLV-DISABLED:disabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.990000000000002%" headers="mcps1.2.4.1.2 "><p id="p26649649"><a name="p26649649"></a><a name="p26649649"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p6667220510518"><a name="p6667220510518"></a><a name="p6667220510518"></a>This is a reserved attribute.</p>
    </td>
    </tr>
    <tr id="row29760277"><td class="cellrowborder" valign="top" width="26.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p61772230"><a name="p61772230"></a><a name="p61772230"></a>rxtx_factor</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.990000000000002%" headers="mcps1.2.4.1.2 "><p id="p17171756"><a name="p17171756"></a><a name="p17171756"></a>Float</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p1722029710518"><a name="p1722029710518"></a><a name="p1722029710518"></a>This is a reserved attribute.</p>
    </td>
    </tr>
    <tr id="row5115727"><td class="cellrowborder" valign="top" width="26.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p11720763"><a name="p11720763"></a><a name="p11720763"></a>os-flavor-access:is_public</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.990000000000002%" headers="mcps1.2.4.1.2 "><p id="p60282721"><a name="p60282721"></a><a name="p60282721"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p4354924810518"><a name="p4354924810518"></a><a name="p4354924810518"></a>This is a reserved attribute.</p>
    </td>
    </tr>
    <tr id="row57014372193259"><td class="cellrowborder" valign="top" width="26.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p1587802219356"><a name="p1587802219356"></a><a name="p1587802219356"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.990000000000002%" headers="mcps1.2.4.1.2 "><p id="p1105141919356"><a name="p1105141919356"></a><a name="p1105141919356"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.839999999999996%" headers="mcps1.2.4.1.3 "><p id="p342100019356"><a name="p342100019356"></a><a name="p342100019356"></a>Specifies the shortcut link of the BMS flavor. For details, see <a href="#table35514108193545">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **links**  field data structure description

    <a name="table35514108193545"></a>
    <table><thead align="left"><tr id="row23367815193545"><th class="cellrowborder" valign="top" width="26.85%" id="mcps1.2.4.1.1"><p id="p1992228131410"><a name="p1992228131410"></a><a name="p1992228131410"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.53%" id="mcps1.2.4.1.2"><p id="p159245814143"><a name="p159245814143"></a><a name="p159245814143"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.620000000000005%" id="mcps1.2.4.1.3"><p id="p792512831417"><a name="p792512831417"></a><a name="p792512831417"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37879124193545"><td class="cellrowborder" valign="top" width="26.85%" headers="mcps1.2.4.1.1 "><p id="p48310227193545"><a name="p48310227193545"></a><a name="p48310227193545"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.53%" headers="mcps1.2.4.1.2 "><p id="p20814310193545"><a name="p20814310193545"></a><a name="p20814310193545"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.620000000000005%" headers="mcps1.2.4.1.3 "><p id="p8237558193545"><a name="p8237558193545"></a><a name="p8237558193545"></a>Specifies the shortcut link marker name.</p>
    <a name="ul207311644172510"></a><a name="ul207311644172510"></a><ul id="ul207311644172510"><li><strong id="en-us_topic_0131326852_b320113110516"><a name="en-us_topic_0131326852_b320113110516"></a><a name="en-us_topic_0131326852_b320113110516"></a>self</strong>: resource link that contains the version number. It is used when immediate tracing is required.</li><li><strong id="en-us_topic_0131326852_b84171947711"><a name="en-us_topic_0131326852_b84171947711"></a><a name="en-us_topic_0131326852_b84171947711"></a>bookmark</strong>: resource link that can be stored for a long time.</li></ul>
    </td>
    </tr>
    <tr id="row7029160193545"><td class="cellrowborder" valign="top" width="26.85%" headers="mcps1.2.4.1.1 "><p id="p32491069193545"><a name="p32491069193545"></a><a name="p32491069193545"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.53%" headers="mcps1.2.4.1.2 "><p id="p14530947193545"><a name="p14530947193545"></a><a name="p14530947193545"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.620000000000005%" headers="mcps1.2.4.1.3 "><p id="p36156065193545"><a name="p36156065193545"></a><a name="p36156065193545"></a>Specifies the corresponding shortcut link.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "flavor": {
            "name": "physical.o2.medium",
            "links": [
                {
                    "href": "https://openstack.example.com/v2/c685484a8cc2416b97260938705deb65/flavors/physical.o2.medium",
                    "rel": "self"
                },
                {
                    "href": "https://openstack.example.com/c685484a8cc2416b97260938705deb65/flavors/physical.o2.medium",
                    "rel": "bookmark"
                }
            ],
            "ram": 192705,
            "OS-FLV-DISABLED:disabled": false,
            "vcpus": 24,
            "swap": "",
            "os-flavor-access:is_public": true,
            "rxtx_factor": 1,
            "OS-FLV-EXT-DATA:ephemeral": 0,
            "disk": 1862,
            "id": "physical.o2.medium"
        }
                    }
    ```


## Returned Values<a name="section7610951"></a>

Normal values

<a name="en-us_topic_0106040941_table753804619176"></a>
<table><thead align="left"><tr id="en-us_topic_0106040941_row10735134615172"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="en-us_topic_0106040941_p19735204616177"><a name="en-us_topic_0106040941_p19735204616177"></a><a name="en-us_topic_0106040941_p19735204616177"></a>Returned Values</p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="en-us_topic_0106040941_p207355465176"><a name="en-us_topic_0106040941_p207355465176"></a><a name="en-us_topic_0106040941_p207355465176"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0106040941_row1473514621713"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0106040941_p13735144611178"><a name="en-us_topic_0106040941_p13735144611178"></a><a name="en-us_topic_0106040941_p13735144611178"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0106040941_p207351246161711"><a name="en-us_topic_0106040941_p207351246161711"></a><a name="en-us_topic_0106040941_p207351246161711"></a>The server has successfully processed the request.</p>
</td>
</tr>
</tbody>
</table>

For details about other returned values, see  [Status Codes](status-codes.md).

## Error Codes<a name="section14752650154917"></a>

See  [Error Codes](error-codes.md).


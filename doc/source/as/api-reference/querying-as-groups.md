# Querying AS Groups<a name="EN-US_TOPIC_0043063030"></a>

## Function<a name="section21821369"></a>

This interface is used to query AS groups based on search criteria. The results are displayed by page.

-   Search criteria can be the AS group name, AS configuration ID, AS group status, start line number, and number of records.
-   If no search criteria are specified, a maximum of 20 AS groups can be queried for a tenant by default.

## URI<a name="section62174594"></a>

GET /autoscaling-api/v1/\{project\_id\}/scaling\_group

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>You can type the question mark \(?\) and ampersand \(&\) at the end of the URI to define multiple search criteria. AS groups can be searched by all optional parameters in the following table. For details, see the example request.  

**Table  1**  Parameter description

<a name="table63724816"></a>
<table><thead align="left"><tr id="row58113810"><th class="cellrowborder" valign="top" width="33%" id="mcps1.2.5.1.1"><p id="p9598184"><a name="p9598184"></a><a name="p9598184"></a><strong id="b275781443110"><a name="b275781443110"></a><a name="b275781443110"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.2"><p id="p39255446"><a name="p39255446"></a><a name="p39255446"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p25574597"><a name="p25574597"></a><a name="p25574597"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="41%" id="mcps1.2.5.1.4"><p id="p58276509"><a name="p58276509"></a><a name="p58276509"></a><strong id="b1511421103111"><a name="b1511421103111"></a><a name="b1511421103111"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row22776773"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.5.1.1 "><p id="p32979301"><a name="p32979301"></a><a name="p32979301"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.2 "><p id="p54077734"><a name="p54077734"></a><a name="p54077734"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p18220335"><a name="p18220335"></a><a name="p18220335"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row62178680"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.5.1.1 "><p id="p3308318"><a name="p3308318"></a><a name="p3308318"></a>scaling_group_name</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.2 "><p id="p66647176"><a name="p66647176"></a><a name="p66647176"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p29712158"><a name="p29712158"></a><a name="p29712158"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.5.1.4 "><p id="p57874634"><a name="p57874634"></a><a name="p57874634"></a>Specifies the AS group name.</p>
<p id="p1187583819613"><a name="p1187583819613"></a><a name="p1187583819613"></a>Supports fuzzy search. </p>
</td>
</tr>
<tr id="row51109658"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.5.1.1 "><p id="p46241663"><a name="p46241663"></a><a name="p46241663"></a>scaling_configuration_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.2 "><p id="p54587245"><a name="p54587245"></a><a name="p54587245"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p59490699"><a name="p59490699"></a><a name="p59490699"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.5.1.4 "><p id="p54017281"><a name="p54017281"></a><a name="p54017281"></a>Specifies the AS configuration ID, which can be obtained using the API for querying AS configurations. For details, see <a href="querying-as-configurations.md">Querying AS Configurations</a>.</p>
</td>
</tr>
<tr id="row16393485"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.5.1.1 "><p id="p52803899"><a name="p52803899"></a><a name="p52803899"></a>scaling_group_status</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.2 "><p id="p49257430"><a name="p49257430"></a><a name="p49257430"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p30428869"><a name="p30428869"></a><a name="p30428869"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.5.1.4 "><p id="p48819313"><a name="p48819313"></a><a name="p48819313"></a>Specifies the AS group status. The options are as follows:</p>
<a name="ul1566484916389"></a><a name="ul1566484916389"></a><ul id="ul1566484916389"><li><strong id="b84235270602019"><a name="b84235270602019"></a><a name="b84235270602019"></a>INSERVICE</strong>: indicates that the AS group is functional.</li><li><strong id="b84235270602042"><a name="b84235270602042"></a><a name="b84235270602042"></a>PAUSED</strong>: indicates that the AS group is paused.</li><li><strong id="b8423527060210"><a name="b8423527060210"></a><a name="b8423527060210"></a>ERROR</strong>: indicates that the AS group malfunctions.</li><li><strong id="b84235270602120"><a name="b84235270602120"></a><a name="b84235270602120"></a>DELETING</strong>: indicates that the AS group is being deleted.</li></ul>
</td>
</tr>
<tr id="row36720633"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.5.1.1 "><p id="p21581258"><a name="p21581258"></a><a name="p21581258"></a>start_number</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.2 "><p id="p3251468"><a name="p3251468"></a><a name="p3251468"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p62042342"><a name="p62042342"></a><a name="p62042342"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.5.1.4 "><p id="p59373825"><a name="p59373825"></a><a name="p59373825"></a>Specifies the start line number. The default value is <strong id="b5876156789409"><a name="b5876156789409"></a><a name="b5876156789409"></a>0</strong>. The minimum value is <strong id="b10904131015190"><a name="b10904131015190"></a><a name="b10904131015190"></a>0</strong>, and there is no limit on the maximum value.</p>
</td>
</tr>
<tr id="row64602382"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.5.1.1 "><p id="p65410477"><a name="p65410477"></a><a name="p65410477"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.2 "><p id="p63757280"><a name="p63757280"></a><a name="p63757280"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p64066064"><a name="p64066064"></a><a name="p64066064"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.5.1.4 "><p id="p21968676"><a name="p21968676"></a><a name="p21968676"></a>Specifies the number of query records. The default value is <strong id="b68928927894017"><a name="b68928927894017"></a><a name="b68928927894017"></a>20</strong>. The value range is 0 to 100.</p>
</td>
</tr>
<tr id="row38233872164714"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.5.1.1 "><p id="p9935898164714"><a name="p9935898164714"></a><a name="p9935898164714"></a>enterprise_project_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.2 "><p id="p66610256164714"><a name="p66610256164714"></a><a name="p66610256164714"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p26721692164714"><a name="p26721692164714"></a><a name="p26721692164714"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.5.1.4 "><p id="p8897132611520"><a name="p8897132611520"></a><a name="p8897132611520"></a>Specifies the enterprise project ID. When <strong id="b2623047164411"><a name="b2623047164411"></a><a name="b2623047164411"></a>all_granted_eps</strong> is specified, AS groups of all the authorized enterprise projects of the user are to be queried.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section22700440"></a>

-   Request parameters

    None

-   Example request

    This example shows how to query AS groups with name  **as-group-test**  and AS configuration ID  **1d281494-6085-4579-b817-c1f813be835f**.

    ```
    GET https://{Endpoint}/autoscaling-api/v1/{project_id}/scaling_group?scaling_group_name=as-group-test&scaling_configuration_id=1d281494-6085-4579-b817-c1f813be835f
    ```


## Response Message<a name="section2977371"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="table5445839"></a>
    <table><thead align="left"><tr id="row5521893"><th class="cellrowborder" valign="top" width="33%" id="mcps1.2.4.1.1"><p id="p44620187"><a name="p44620187"></a><a name="p44620187"></a><strong id="b181591920183419"><a name="b181591920183419"></a><a name="b181591920183419"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.2"><p id="p57465365"><a name="p57465365"></a><a name="p57465365"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="p24182971"><a name="p24182971"></a><a name="p24182971"></a><strong id="b36301523143419"><a name="b36301523143419"></a><a name="b36301523143419"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12663671"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p19124398"><a name="p19124398"></a><a name="p19124398"></a>total_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p5572426"><a name="p5572426"></a><a name="p5572426"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p48713395"><a name="p48713395"></a><a name="p48713395"></a>Specifies the total number of query records.</p>
    </td>
    </tr>
    <tr id="row35767376"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p11476310"><a name="p11476310"></a><a name="p11476310"></a>start_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p57165917"><a name="p57165917"></a><a name="p57165917"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p67036556"><a name="p67036556"></a><a name="p67036556"></a>Specifies the start number of query records.</p>
    </td>
    </tr>
    <tr id="row66458099"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p14396914"><a name="p14396914"></a><a name="p14396914"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p25299374"><a name="p25299374"></a><a name="p25299374"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p35983374"><a name="p35983374"></a><a name="p35983374"></a>Specifies the number of query records.</p>
    </td>
    </tr>
    <tr id="row55414911"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p59422801"><a name="p59422801"></a><a name="p59422801"></a>scaling_groups</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p48517563"><a name="p48517563"></a><a name="p48517563"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p37608550"><a name="p37608550"></a><a name="p37608550"></a>Specifies the scaling group list.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **scaling\_groups**  field description

    <a name="table3818677995816"></a>
    <table><thead align="left"><tr id="row3125168495816"><th class="cellrowborder" valign="top" width="33%" id="mcps1.2.4.1.1"><p id="p4835851595816"><a name="p4835851595816"></a><a name="p4835851595816"></a><strong id="b14507125433416"><a name="b14507125433416"></a><a name="b14507125433416"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.2"><p id="p2472567595816"><a name="p2472567595816"></a><a name="p2472567595816"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="p5662264395816"><a name="p5662264395816"></a><a name="p5662264395816"></a><strong id="b966010563343"><a name="b966010563343"></a><a name="b966010563343"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2303134795816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p5359982895816"><a name="p5359982895816"></a><a name="p5359982895816"></a>scaling_group_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p4661881395816"><a name="p4661881395816"></a><a name="p4661881395816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p1802754395816"><a name="p1802754395816"></a><a name="p1802754395816"></a>Specifies the name of the AS group.</p>
    </td>
    </tr>
    <tr id="row2803016695816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p5585097295816"><a name="p5585097295816"></a><a name="p5585097295816"></a>scaling_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p2763485495816"><a name="p2763485495816"></a><a name="p2763485495816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p2383068495816"><a name="p2383068495816"></a><a name="p2383068495816"></a>Specifies the AS group ID.</p>
    </td>
    </tr>
    <tr id="row1314957295816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p5848240895816"><a name="p5848240895816"></a><a name="p5848240895816"></a>scaling_group_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p3945463795816"><a name="p3945463795816"></a><a name="p3945463795816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p4170905195816"><a name="p4170905195816"></a><a name="p4170905195816"></a>Specifies the status of the AS group.</p>
    </td>
    </tr>
    <tr id="row3983714095816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p558291395816"><a name="p558291395816"></a><a name="p558291395816"></a>scaling_configuration_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p4956282795816"><a name="p4956282795816"></a><a name="p4956282795816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p5516604195816"><a name="p5516604195816"></a><a name="p5516604195816"></a>Specifies the AS configuration ID.</p>
    </td>
    </tr>
    <tr id="row2673232595816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p1783474195816"><a name="p1783474195816"></a><a name="p1783474195816"></a>scaling_configuration_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p3532793495816"><a name="p3532793495816"></a><a name="p3532793495816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p4299037595816"><a name="p4299037595816"></a><a name="p4299037595816"></a>Specifies the AS configuration name.</p>
    </td>
    </tr>
    <tr id="row5136905595816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p14389995816"><a name="p14389995816"></a><a name="p14389995816"></a>current_instance_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p1165588495816"><a name="p1165588495816"></a><a name="p1165588495816"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p460258695816"><a name="p460258695816"></a><a name="p460258695816"></a>Specifies the number of current instances in the AS group.</p>
    </td>
    </tr>
    <tr id="row4142327995816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p6695131595816"><a name="p6695131595816"></a><a name="p6695131595816"></a>desire_instance_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p5434739895816"><a name="p5434739895816"></a><a name="p5434739895816"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p4006315595816"><a name="p4006315595816"></a><a name="p4006315595816"></a>Specifies the expected number of instances in the AS group.</p>
    </td>
    </tr>
    <tr id="row2502407895816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p1368441895816"><a name="p1368441895816"></a><a name="p1368441895816"></a>min_instance_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p3469606795816"><a name="p3469606795816"></a><a name="p3469606795816"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p5891800895816"><a name="p5891800895816"></a><a name="p5891800895816"></a>Specifies the minimum number of instances in the AS group.</p>
    </td>
    </tr>
    <tr id="row6050002595816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p155503295816"><a name="p155503295816"></a><a name="p155503295816"></a>max_instance_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p5884880095816"><a name="p5884880095816"></a><a name="p5884880095816"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p202348095816"><a name="p202348095816"></a><a name="p202348095816"></a>Specifies the maximum number of instances in the AS group.</p>
    </td>
    </tr>
    <tr id="row1821132195816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p6583092595816"><a name="p6583092595816"></a><a name="p6583092595816"></a>cool_down_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p3070470995816"><a name="p3070470995816"></a><a name="p3070470995816"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p405351495816"><a name="p405351495816"></a><a name="p405351495816"></a>Specifies the cooldown period (s).</p>
    </td>
    </tr>
    <tr id="row3648162895816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p222191995816"><a name="p222191995816"></a><a name="p222191995816"></a>lb_listener_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p4575773095816"><a name="p4575773095816"></a><a name="p4575773095816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p1538862195816"><a name="p1538862195816"></a><a name="p1538862195816"></a>Specifies the ID of a typical ELB listener. ELB listener IDs are separated using a comma (,).</p>
    </td>
    </tr>
    <tr id="row33800908174636"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p53519047174636"><a name="p53519047174636"></a><a name="p53519047174636"></a>lbaas_listeners</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p1966763821113"><a name="p1966763821113"></a><a name="p1966763821113"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p24895134174636"><a name="p24895134174636"></a><a name="p24895134174636"></a>Specifies enhanced load balancers. For details, see <a href="#table62452402171652">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row30423366112250"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p48373547112250"><a name="p48373547112250"></a><a name="p48373547112250"></a>available_zones</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p25943212112250"><a name="p25943212112250"></a><a name="p25943212112250"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p21025459112250"><a name="p21025459112250"></a><a name="p21025459112250"></a>Specifies the AZ information.</p>
    </td>
    </tr>
    <tr id="row427986595816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p1112482195816"><a name="p1112482195816"></a><a name="p1112482195816"></a>networks</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p2869527695816"><a name="p2869527695816"></a><a name="p2869527695816"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p4800004895816"><a name="p4800004895816"></a><a name="p4800004895816"></a>Specifies networks. For details, see <a href="#t67e1f67cb70d4457bab7efeb3dfeee6e">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="row2934724995816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p2831697495816"><a name="p2831697495816"></a><a name="p2831697495816"></a>security_groups</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p569719238385"><a name="p569719238385"></a><a name="p569719238385"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p458485895816"><a name="p458485895816"></a><a name="p458485895816"></a>Specifies security groups. For details, see <a href="#t3db1c8f5898a4179b5029204834c82e5">Table 7</a>.</p>
    </td>
    </tr>
    <tr id="row4126372995816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p5402772895816"><a name="p5402772895816"></a><a name="p5402772895816"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p1416983695816"><a name="p1416983695816"></a><a name="p1416983695816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p690602895816"><a name="p690602895816"></a><a name="p690602895816"></a>Specifies the time when an AS group was created. The time format complies with UTC.</p>
    </td>
    </tr>
    <tr id="row6215425395816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p132972795816"><a name="p132972795816"></a><a name="p132972795816"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p4059904995816"><a name="p4059904995816"></a><a name="p4059904995816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p18869295816"><a name="p18869295816"></a><a name="p18869295816"></a>Specifies the ID of the VPC to which the AS group belongs.</p>
    </td>
    </tr>
    <tr id="row169823395816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p333920895816"><a name="p333920895816"></a><a name="p333920895816"></a>detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p204042795816"><a name="p204042795816"></a><a name="p204042795816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p3105690795816"><a name="p3105690795816"></a><a name="p3105690795816"></a>Specifies details about the AS group. If a scaling action fails, this parameter is used to record errors.</p>
    </td>
    </tr>
    <tr id="row1107670995816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p2479821895816"><a name="p2479821895816"></a><a name="p2479821895816"></a>is_scaling</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p6249865695816"><a name="p6249865695816"></a><a name="p6249865695816"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p2922638295816"><a name="p2922638295816"></a><a name="p2922638295816"></a>Specifies the scaling flag of the AS group.</p>
    </td>
    </tr>
    <tr id="row6171085495816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p3252330995816"><a name="p3252330995816"></a><a name="p3252330995816"></a>health_periodic_audit_method</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p1714233595816"><a name="p1714233595816"></a><a name="p1714233595816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p4635191095816"><a name="p4635191095816"></a><a name="p4635191095816"></a>Specifies the health check method.</p>
    </td>
    </tr>
    <tr id="row1451401395816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p3478441495816"><a name="p3478441495816"></a><a name="p3478441495816"></a>health_periodic_audit_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p6607415195816"><a name="p6607415195816"></a><a name="p6607415195816"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p5040604995816"><a name="p5040604995816"></a><a name="p5040604995816"></a>Specifies the health check interval.</p>
    </td>
    </tr>
    <tr id="row42331571153426"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p6305198153426"><a name="p6305198153426"></a><a name="p6305198153426"></a>health_periodic_audit_grace_period</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p40959034153426"><a name="p40959034153426"></a><a name="p40959034153426"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p29347454153426"><a name="p29347454153426"></a><a name="p29347454153426"></a>Specifies the grace period for health check.</p>
    </td>
    </tr>
    <tr id="row5100126495816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p3746171895816"><a name="p3746171895816"></a><a name="p3746171895816"></a>instance_terminate_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p1450028895816"><a name="p1450028895816"></a><a name="p1450028895816"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p3367266295816"><a name="p3367266295816"></a><a name="p3367266295816"></a>Specifies the instance removal policy.</p>
    </td>
    </tr>
    <tr id="row3461851095816"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p5263592295816"><a name="p5263592295816"></a><a name="p5263592295816"></a>notifications</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p3565131995816"><a name="p3565131995816"></a><a name="p3565131995816"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p207574995816"><a name="p207574995816"></a><a name="p207574995816"></a>Specifies the notification mode.</p>
    <p id="p1868174295816"><a name="p1868174295816"></a><a name="p1868174295816"></a><strong id="b58832166171917"><a name="b58832166171917"></a><a name="b58832166171917"></a>EMAIL</strong> refers to notification by email.</p>
    </td>
    </tr>
    <tr id="row58376155111614"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p30848135111614"><a name="p30848135111614"></a><a name="p30848135111614"></a>delete_publicip</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p40568935111649"><a name="p40568935111649"></a><a name="p40568935111649"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p64858299111649"><a name="p64858299111649"></a><a name="p64858299111649"></a>Specifies whether to delete the EIP bound to the ECS when deleting the ECS.</p>
    </td>
    </tr>
    <tr id="row1666213536250"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p1585114581258"><a name="p1585114581258"></a><a name="p1585114581258"></a>delete_volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p19851458122520"><a name="p19851458122520"></a><a name="p19851458122520"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p178519586250"><a name="p178519586250"></a><a name="p178519586250"></a>Specifies whether to delete the data disks attached to the ECS when deleting the ECS.</p>
    </td>
    </tr>
    <tr id="row50398037163752"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p55709224163752"><a name="p55709224163752"></a><a name="p55709224163752"></a>cloud_location_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p16153275163752"><a name="p16153275163752"></a><a name="p16153275163752"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p33346870163752"><a name="p33346870163752"></a><a name="p33346870163752"></a>This parameter is reserved.</p>
    </td>
    </tr>
    <tr id="row529918693932"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p2658093993932"><a name="p2658093993932"></a><a name="p2658093993932"></a>enterprise_project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p557242093932"><a name="p557242093932"></a><a name="p557242093932"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p4871283793932"><a name="p4871283793932"></a><a name="p4871283793932"></a>Specifies the enterprise project ID.</p>
    </td>
    </tr>
    <tr id="row870025345713"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p67015533576"><a name="p67015533576"></a><a name="p67015533576"></a>activity_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p14701185316570"><a name="p14701185316570"></a><a name="p14701185316570"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p16701185365719"><a name="p16701185365719"></a><a name="p16701185365719"></a>Specifies the type of the AS action.</p>
    </td>
    </tr>
    <tr id="row9571105073212"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p1766414574320"><a name="p1766414574320"></a><a name="p1766414574320"></a>multi_az_priority_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p176649575326"><a name="p176649575326"></a><a name="p176649575326"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p1766565743214"><a name="p1766565743214"></a><a name="p1766565743214"></a>Specifies the priority policy used to select target AZs when adjusting the number of instances in an AS group.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **lbaas\_listeners**  field description

    <a name="table62452402171652"></a>
    <table><thead align="left"><tr id="row45038761171652"><th class="cellrowborder" valign="top" width="33%" id="mcps1.2.4.1.1"><p id="p24261034171652"><a name="p24261034171652"></a><a name="p24261034171652"></a><strong id="b1882212592346"><a name="b1882212592346"></a><a name="b1882212592346"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="p61530925171652"><a name="p61530925171652"></a><a name="p61530925171652"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.4.1.3"><p id="p17949056171652"><a name="p17949056171652"></a><a name="p17949056171652"></a><strong id="b1486304193518"><a name="b1486304193518"></a><a name="b1486304193518"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row44587411171652"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p54810510171652"><a name="p54810510171652"></a><a name="p54810510171652"></a>listener_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p42466398171652"><a name="p42466398171652"></a><a name="p42466398171652"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p17226243171652"><a name="p17226243171652"></a><a name="p17226243171652"></a>Specifies the listener ID.</p>
    </td>
    </tr>
    <tr id="row16035310115445"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p239701115447"><a name="p239701115447"></a><a name="p239701115447"></a>pool_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p19415824115447"><a name="p19415824115447"></a><a name="p19415824115447"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p14598635115447"><a name="p14598635115447"></a><a name="p14598635115447"></a>Specifies the backend ECS group ID.</p>
    </td>
    </tr>
    <tr id="row61114407171742"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p51319960171742"><a name="p51319960171742"></a><a name="p51319960171742"></a>protocol_port</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p25093240171742"><a name="p25093240171742"></a><a name="p25093240171742"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p19286583171742"><a name="p19286583171742"></a><a name="p19286583171742"></a>Specifies the backend protocol ID, which is the port on which a backend ECS listens for traffic.</p>
    </td>
    </tr>
    <tr id="row36552334171745"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p7949116171745"><a name="p7949116171745"></a><a name="p7949116171745"></a>weight</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p10566861171745"><a name="p10566861171745"></a><a name="p10566861171745"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p50609408171745"><a name="p50609408171745"></a><a name="p50609408171745"></a>Specifies the weight, which determines the portion of requests a backend ECS processes when being compared to other backend ECSs added to the same listener.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **networks**  field description

    <a name="t67e1f67cb70d4457bab7efeb3dfeee6e"></a>
    <table><thead align="left"><tr id="r38fbfd545d8b41ac9a165cb5b185293c"><th class="cellrowborder" valign="top" width="33%" id="mcps1.2.4.1.1"><p id="a25948832a6e540e4aeaf9201f17c6136"><a name="a25948832a6e540e4aeaf9201f17c6136"></a><a name="a25948832a6e540e4aeaf9201f17c6136"></a><strong id="b16850768358"><a name="b16850768358"></a><a name="b16850768358"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="a5fa8352938e048e29a2a0ae3465f8beb"><a name="a5fa8352938e048e29a2a0ae3465f8beb"></a><a name="a5fa8352938e048e29a2a0ae3465f8beb"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.4.1.3"><p id="abe4729b8fced431487d765209a10d998"><a name="abe4729b8fced431487d765209a10d998"></a><a name="abe4729b8fced431487d765209a10d998"></a><strong id="b699417913511"><a name="b699417913511"></a><a name="b699417913511"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rc7ffdcdeb84a45feb1ea195ba834fbfd"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="a7d60ed8df47c4992a324abe8c0284e98"><a name="a7d60ed8df47c4992a324abe8c0284e98"></a><a name="a7d60ed8df47c4992a324abe8c0284e98"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="a0c27097a7a204f7f8b84faf6c4ace52c"><a name="a0c27097a7a204f7f8b84faf6c4ace52c"></a><a name="a0c27097a7a204f7f8b84faf6c4ace52c"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="a449a6776950944bda68da138e6abe695"><a name="a449a6776950944bda68da138e6abe695"></a><a name="a449a6776950944bda68da138e6abe695"></a>Specifies the network ID.</p>
    </td>
    </tr>
    <tr id="row225972616103"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p168461419171814"><a name="p168461419171814"></a><a name="p168461419171814"></a>ipv6_enable</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p128463194182"><a name="p128463194182"></a><a name="p128463194182"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p1869495520194"><a name="p1869495520194"></a><a name="p1869495520194"></a>Specifies whether to support IPv6 addresses. If the value of this parameter is set to <strong id="b28331146153114"><a name="b28331146153114"></a><a name="b28331146153114"></a>true</strong>, the NIC supports IPv6 addresses. The default value is <strong id="b8423527060277"><a name="b8423527060277"></a><a name="b8423527060277"></a>false</strong>. This parameter is reserved.</p>
    </td>
    </tr>
    <tr id="row10392255147"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p205431522101813"><a name="p205431522101813"></a><a name="p205431522101813"></a>ipv6_bandwidth</p>
    </td>
    <td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p571213113810"><a name="p571213113810"></a><a name="p571213113810"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p18543162219184"><a name="p18543162219184"></a><a name="p18543162219184"></a>Specifies the shared bandwidth of an IPv6 address. This parameter is left blank by default, indicating that no IPv6 shared bandwidth is bound. This parameter is reserved.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **ipv6\_bandwidth**  field description

    <a name="table165325426371"></a>
    <table><thead align="left"><tr id="row1853319428379"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="p18442811162111"><a name="p18442811162111"></a><a name="p18442811162111"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18%" id="mcps1.2.4.1.2"><p id="p651421810389"><a name="p651421810389"></a><a name="p651421810389"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="59%" id="mcps1.2.4.1.3"><p id="p444917113212"><a name="p444917113212"></a><a name="p444917113212"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1853324213378"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="p109011143210"><a name="p109011143210"></a><a name="p109011143210"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.4.1.2 "><p id="p59010416217"><a name="p59010416217"></a><a name="p59010416217"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p18389161592217"><a name="p18389161592217"></a><a name="p18389161592217"></a>Specifies the ID of the shared bandwidth of an IPv6 address. This parameter is reserved.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7** **security\_groups**  field description

    <a name="t3db1c8f5898a4179b5029204834c82e5"></a>
    <table><thead align="left"><tr id="r64cc323b13f2470cbd5cf20531f45aad"><th class="cellrowborder" valign="top" width="23.56%" id="mcps1.2.4.1.1"><p id="ab42ad58aefab4311ac0c2507984a8107"><a name="ab42ad58aefab4311ac0c2507984a8107"></a><a name="ab42ad58aefab4311ac0c2507984a8107"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.73%" id="mcps1.2.4.1.2"><p id="abd02ac6bdeed4b159635817d455d3286"><a name="abd02ac6bdeed4b159635817d455d3286"></a><a name="abd02ac6bdeed4b159635817d455d3286"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.709999999999994%" id="mcps1.2.4.1.3"><p id="a6dc84c25ec0244e2844321a8291a9981"><a name="a6dc84c25ec0244e2844321a8291a9981"></a><a name="a6dc84c25ec0244e2844321a8291a9981"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r3650c2ffcd3d405496639de740222790"><td class="cellrowborder" valign="top" width="23.56%" headers="mcps1.2.4.1.1 "><p id="ae0d8aa75f726414f812781414bf4d87f"><a name="ae0d8aa75f726414f812781414bf4d87f"></a><a name="ae0d8aa75f726414f812781414bf4d87f"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.73%" headers="mcps1.2.4.1.2 "><p id="a0b213143b4754bf786bb0ed28229d86a"><a name="a0b213143b4754bf786bb0ed28229d86a"></a><a name="a0b213143b4754bf786bb0ed28229d86a"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.709999999999994%" headers="mcps1.2.4.1.3 "><p id="adc3054875e29415a8e5f0d3cccda9703"><a name="adc3054875e29415a8e5f0d3cccda9703"></a><a name="adc3054875e29415a8e5f0d3cccda9703"></a>Specifies the security group ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "limit": 20,
        "scaling_groups": [
            {
                "networks": [
                    {
                        "id": "a8327883-6b07-4497-9c61-68d03ee193a",
                        "ipv6_enable": false,
                        "ipv6_bandwidth":  null,
                    }
                ],
                "available_zones": [
                       "XXXa",
                       "XXXb"
                ],
                "detail": null,
                "scaling_group_name": "as-group-test",
                "scaling_group_id": "77a7a397-7d2f-4e79-9da9-6a35e2709150",
                "scaling_group_status": "INSERVICE",
                "scaling_configuration_id": "1d281494-6085-4579-b817-c1f813be835f",
                "scaling_configuration_name": "healthCheck",
                "current_instance_number": 0,
                "desire_instance_number": 1,
                "min_instance_number": 0,
                "max_instance_number": 500,
                "cool_down_time": 300,
                "lb_listener_id": "f06c0112570743b51c0e8fbe1f235bab",
                "security_groups": [
                    {
                        "id": "8a4b1d5b-0054-419f-84b1-5c8a59ebc829"
                    }
                ],
                "create_time": "2015-07-23T02:46:29Z",
                "vpc_id": "863ccae2-ee85-4d27-bc5b-3ba2a198a9e2",
                "health_periodic_audit_method": "ELB_AUDIT",
                "health_periodic_audit_time": 5,
                "health_periodic_audit_grace_period": 600,
                "instance_terminate_policy": "OLD_CONFIG_OLD_INSTANCE",
                "is_scaling": false,
                "delete_publicip": false,
                "notifications": [
                    "EMAIL"
                ]
               "enterprise_project_id": "c92b1a5d-6f20-43f2-b1b7-7ce35e58e413",
                "multi_az_priority_policy": "PICK_FIRST"
            }
        ],
        "total_number": 1,
        "start_number": 0
    }
    ```


## Returned Values<a name="section26796340"></a>

-   Normal

    200

-   Abnormal

    <a name="table31069492"></a>
    <table><thead align="left"><tr id="row334102"><th class="cellrowborder" valign="top" width="43.8%" id="mcps1.1.3.1.1"><p id="p27062312"><a name="p27062312"></a><a name="p27062312"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.2%" id="mcps1.1.3.1.2"><p id="p44563687"><a name="p44563687"></a><a name="p44563687"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row52888890"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p56141706"><a name="p56141706"></a><a name="p56141706"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p51184318"><a name="p51184318"></a><a name="p51184318"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row58005681"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p839735"><a name="p839735"></a><a name="p839735"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p909717"><a name="p909717"></a><a name="p909717"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row8187461"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p59204636"><a name="p59204636"></a><a name="p59204636"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p30846174"><a name="p30846174"></a><a name="p30846174"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row9180116"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p5391908"><a name="p5391908"></a><a name="p5391908"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p34091413"><a name="p34091413"></a><a name="p34091413"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row38387265"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p22360774"><a name="p22360774"></a><a name="p22360774"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p66392255"><a name="p66392255"></a><a name="p66392255"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row60659387"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p14463294"><a name="p14463294"></a><a name="p14463294"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p30676137"><a name="p30676137"></a><a name="p30676137"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row7649781"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p15652561"><a name="p15652561"></a><a name="p15652561"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p59897896"><a name="p59897896"></a><a name="p59897896"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row2210158"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p44805132"><a name="p44805132"></a><a name="p44805132"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p5337050"><a name="p5337050"></a><a name="p5337050"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row48033450"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p65504260"><a name="p65504260"></a><a name="p65504260"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p4244834"><a name="p4244834"></a><a name="p4244834"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row38203510"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p7476630"><a name="p7476630"></a><a name="p7476630"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p1627311"><a name="p1627311"></a><a name="p1627311"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row14645800"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p45459112"><a name="p45459112"></a><a name="p45459112"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p58309428"><a name="p58309428"></a><a name="p58309428"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row55022811"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p27662693"><a name="p27662693"></a><a name="p27662693"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p26085680"><a name="p26085680"></a><a name="p26085680"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row33444533"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p24652676"><a name="p24652676"></a><a name="p24652676"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p50709735"><a name="p50709735"></a><a name="p50709735"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row53734436"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p57522049"><a name="p57522049"></a><a name="p57522049"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p28774374"><a name="p28774374"></a><a name="p28774374"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).


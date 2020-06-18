# Querying AS Policies<a name="EN-US_TOPIC_0134002033"></a>

## Function<a name="en-us_topic_0130755740_section11355891"></a>

This interface is used to query AS policies based on search criteria. The results are displayed by page.

-   Search criteria can be the AS policy name, policy type, policy ID, start line number, and number of records.
-   If no search criteria are specified, a maximum of 20 AS policies for a specified AS group can be queried for a tenant by default.

## URI<a name="en-us_topic_0130755740_section35094160"></a>

GET /autoscaling-api/v1/\{project\_id\}/scaling\_policy/\{scaling\_group\_id\}/list

>![](/images/icon-note.gif) **NOTE:**   
>You can type the question mark \(?\) and ampersand \(&\) at the end of the URI to define multiple search criteria. AS policies can be searched by all optional parameters in the following table. For details, see the example request.  

**Table  1**  Parameter description

<a name="en-us_topic_0130755740_table53255854"></a>
<table><thead align="left"><tr id="en-us_topic_0130755740_row14242537"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.1"><p id="en-us_topic_0130755740_p12794876"><a name="en-us_topic_0130755740_p12794876"></a><a name="en-us_topic_0130755740_p12794876"></a><strong id="b685054435518"><a name="b685054435518"></a><a name="b685054435518"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="en-us_topic_0130755740_p29752015"><a name="en-us_topic_0130755740_p29752015"></a><a name="en-us_topic_0130755740_p29752015"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="en-us_topic_0130755740_p61102986"><a name="en-us_topic_0130755740_p61102986"></a><a name="en-us_topic_0130755740_p61102986"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48%" id="mcps1.2.5.1.4"><p id="en-us_topic_0130755740_p50394838"><a name="en-us_topic_0130755740_p50394838"></a><a name="en-us_topic_0130755740_p50394838"></a><strong id="b14356144516558"><a name="b14356144516558"></a><a name="b14356144516558"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0130755740_row55450074"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0130755740_p62271039"><a name="en-us_topic_0130755740_p62271039"></a><a name="en-us_topic_0130755740_p62271039"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0130755740_p10789421"><a name="en-us_topic_0130755740_p10789421"></a><a name="en-us_topic_0130755740_p10789421"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0130755740_p1527883"><a name="en-us_topic_0130755740_p1527883"></a><a name="en-us_topic_0130755740_p1527883"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0130755740_p56649665"><a name="en-us_topic_0130755740_p56649665"></a><a name="en-us_topic_0130755740_p56649665"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0130755740_row40084941"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0130755740_p25654779"><a name="en-us_topic_0130755740_p25654779"></a><a name="en-us_topic_0130755740_p25654779"></a>scaling_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0130755740_p64771222"><a name="en-us_topic_0130755740_p64771222"></a><a name="en-us_topic_0130755740_p64771222"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0130755740_p11977605"><a name="en-us_topic_0130755740_p11977605"></a><a name="en-us_topic_0130755740_p11977605"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0130755740_p30661937"><a name="en-us_topic_0130755740_p30661937"></a><a name="en-us_topic_0130755740_p30661937"></a>Specifies the AS group ID.</p>
</td>
</tr>
<tr id="en-us_topic_0130755740_row7521977"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0130755740_p5300362"><a name="en-us_topic_0130755740_p5300362"></a><a name="en-us_topic_0130755740_p5300362"></a>scaling_policy_name</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0130755740_p26676172"><a name="en-us_topic_0130755740_p26676172"></a><a name="en-us_topic_0130755740_p26676172"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0130755740_p13286310"><a name="en-us_topic_0130755740_p13286310"></a><a name="en-us_topic_0130755740_p13286310"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0130755740_p2449345"><a name="en-us_topic_0130755740_p2449345"></a><a name="en-us_topic_0130755740_p2449345"></a>Specifies the AS policy name.</p>
<p id="p1590252499"><a name="p1590252499"></a><a name="p1590252499"></a>Supports fuzzy search. </p>
</td>
</tr>
<tr id="en-us_topic_0130755740_row22044110"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0130755740_p40742509"><a name="en-us_topic_0130755740_p40742509"></a><a name="en-us_topic_0130755740_p40742509"></a>scaling_policy_type</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0130755740_p11808928"><a name="en-us_topic_0130755740_p11808928"></a><a name="en-us_topic_0130755740_p11808928"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0130755740_p16999120"><a name="en-us_topic_0130755740_p16999120"></a><a name="en-us_topic_0130755740_p16999120"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0130755740_p34751460"><a name="en-us_topic_0130755740_p34751460"></a><a name="en-us_topic_0130755740_p34751460"></a>Specifies the AS policy type.</p>
<a name="ul1459175775513"></a><a name="ul1459175775513"></a><ul id="ul1459175775513"><li><strong id="b11547175394718"><a name="b11547175394718"></a><a name="b11547175394718"></a>ALARM</strong>: alarm policy</li><li><strong id="b029219316483"><a name="b029219316483"></a><a name="b029219316483"></a>SCHEDULED</strong>: scheduled policy</li><li><strong id="b1363811419486"><a name="b1363811419486"></a><a name="b1363811419486"></a>RECURRENCE</strong>: periodic policy</li></ul>
</td>
</tr>
<tr id="en-us_topic_0130755740_row4938239411254"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0130755740_p4055096211254"><a name="en-us_topic_0130755740_p4055096211254"></a><a name="en-us_topic_0130755740_p4055096211254"></a>scaling_policy_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0130755740_p6340246611254"><a name="en-us_topic_0130755740_p6340246611254"></a><a name="en-us_topic_0130755740_p6340246611254"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0130755740_p3532613111254"><a name="en-us_topic_0130755740_p3532613111254"></a><a name="en-us_topic_0130755740_p3532613111254"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0130755740_p4284436411254"><a name="en-us_topic_0130755740_p4284436411254"></a><a name="en-us_topic_0130755740_p4284436411254"></a>Specifies the AS policy ID.</p>
</td>
</tr>
<tr id="en-us_topic_0130755740_row44327687"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0130755740_p33772909"><a name="en-us_topic_0130755740_p33772909"></a><a name="en-us_topic_0130755740_p33772909"></a>start_number</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0130755740_p51251115"><a name="en-us_topic_0130755740_p51251115"></a><a name="en-us_topic_0130755740_p51251115"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0130755740_p57699690"><a name="en-us_topic_0130755740_p57699690"></a><a name="en-us_topic_0130755740_p57699690"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.5.1.4 "><p id="p59373825"><a name="p59373825"></a><a name="p59373825"></a>Specifies the start line number. The default value is <strong id="b18683191795815"><a name="b18683191795815"></a><a name="b18683191795815"></a>0</strong>. The minimum parameter value is <strong id="b18744142621611"><a name="b18744142621611"></a><a name="b18744142621611"></a>0</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0130755740_row52925796"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0130755740_p59131099"><a name="en-us_topic_0130755740_p59131099"></a><a name="en-us_topic_0130755740_p59131099"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0130755740_p24889743"><a name="en-us_topic_0130755740_p24889743"></a><a name="en-us_topic_0130755740_p24889743"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0130755740_p2803303"><a name="en-us_topic_0130755740_p2803303"></a><a name="en-us_topic_0130755740_p2803303"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.5.1.4 "><p id="p21968676"><a name="p21968676"></a><a name="p21968676"></a>Specifies the number of query records. The default value is <strong id="b168447885495335"><a name="b168447885495335"></a><a name="b168447885495335"></a>20</strong>. The value range is 0 to 100.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="en-us_topic_0130755740_section47411987"></a>

-   Request parameters

    None

-   Example request

    This example shows how to query scheduled AS policies named  **as-policy-test**  in the AS group with ID  **e5d27f5c-dd76-4a61-b4bc-a67c5686719a**.

    ```
    GET https://{Endpoint}/autoscaling-api/v1/{project_id}/scaling_policy/e5d27f5c-dd76-4a61-b4bc-a67c5686719a/list?scaling_policy_name=as-policy-test&scaling_policy_type=SCHEDULED
    ```


## Response Message<a name="en-us_topic_0130755740_section24054701"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="en-us_topic_0130755740_table59665636"></a>
    <table><thead align="left"><tr id="en-us_topic_0130755740_row28755990"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.1"><p id="en-us_topic_0130755740_p47533853"><a name="en-us_topic_0130755740_p47533853"></a><a name="en-us_topic_0130755740_p47533853"></a><strong id="b1411617463554"><a name="b1411617463554"></a><a name="b1411617463554"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.2"><p id="en-us_topic_0130755740_p25036876"><a name="en-us_topic_0130755740_p25036876"></a><a name="en-us_topic_0130755740_p25036876"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="62%" id="mcps1.2.4.1.3"><p id="en-us_topic_0130755740_p14721100"><a name="en-us_topic_0130755740_p14721100"></a><a name="en-us_topic_0130755740_p14721100"></a><strong id="b0541647115519"><a name="b0541647115519"></a><a name="b0541647115519"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0130755740_row51558469"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0130755740_p15486430"><a name="en-us_topic_0130755740_p15486430"></a><a name="en-us_topic_0130755740_p15486430"></a>total_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0130755740_p46441279"><a name="en-us_topic_0130755740_p46441279"></a><a name="en-us_topic_0130755740_p46441279"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0130755740_p3647249"><a name="en-us_topic_0130755740_p3647249"></a><a name="en-us_topic_0130755740_p3647249"></a>Specifies the total number of query records.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_row32825243"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0130755740_p41599065"><a name="en-us_topic_0130755740_p41599065"></a><a name="en-us_topic_0130755740_p41599065"></a>start_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0130755740_p14081115"><a name="en-us_topic_0130755740_p14081115"></a><a name="en-us_topic_0130755740_p14081115"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0130755740_p66828554"><a name="en-us_topic_0130755740_p66828554"></a><a name="en-us_topic_0130755740_p66828554"></a>Specifies the start line number.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_row64586077"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0130755740_p64089786"><a name="en-us_topic_0130755740_p64089786"></a><a name="en-us_topic_0130755740_p64089786"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0130755740_p23890167"><a name="en-us_topic_0130755740_p23890167"></a><a name="en-us_topic_0130755740_p23890167"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0130755740_p56055356"><a name="en-us_topic_0130755740_p56055356"></a><a name="en-us_topic_0130755740_p56055356"></a>Specifies the maximum number of resources to be queried.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_row34736162"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0130755740_p62165703"><a name="en-us_topic_0130755740_p62165703"></a><a name="en-us_topic_0130755740_p62165703"></a>scaling_policies</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p1361671412425"><a name="p1361671412425"></a><a name="p1361671412425"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="62%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0130755740_p48612303"><a name="en-us_topic_0130755740_p48612303"></a><a name="en-us_topic_0130755740_p48612303"></a>Specifies scaling policies. For details, see <a href="#en-us_topic_0130755740_table5036780310489">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **scaling\_policies**  field description

    <a name="en-us_topic_0130755740_table5036780310489"></a>
    <table><thead align="left"><tr id="en-us_topic_0130755740_r1f3f90a6acc94015acc80b9d6b53f072"><th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.2.4.1.1"><p id="en-us_topic_0130755740_ad0d15c1370cb450fb7e6011b8baff160"><a name="en-us_topic_0130755740_ad0d15c1370cb450fb7e6011b8baff160"></a><a name="en-us_topic_0130755740_ad0d15c1370cb450fb7e6011b8baff160"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.2"><p id="en-us_topic_0130755740_a2273dfb9dd3341b0b5cbf801a0aa70fc"><a name="en-us_topic_0130755740_a2273dfb9dd3341b0b5cbf801a0aa70fc"></a><a name="en-us_topic_0130755740_a2273dfb9dd3341b0b5cbf801a0aa70fc"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.4.1.3"><p id="en-us_topic_0130755740_a479b45e1fbfc44118151c43b5ecb82f1"><a name="en-us_topic_0130755740_a479b45e1fbfc44118151c43b5ecb82f1"></a><a name="en-us_topic_0130755740_a479b45e1fbfc44118151c43b5ecb82f1"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0130755740_rdd24623b54f94a86b0f655ec659180e9"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0130755740_ab9c8eb8b964943509fca83cc70a4e489"><a name="en-us_topic_0130755740_ab9c8eb8b964943509fca83cc70a4e489"></a><a name="en-us_topic_0130755740_ab9c8eb8b964943509fca83cc70a4e489"></a>scaling_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0130755740_a43cc5f338c7e429c861f7dbb2dcb3229"><a name="en-us_topic_0130755740_a43cc5f338c7e429c861f7dbb2dcb3229"></a><a name="en-us_topic_0130755740_a43cc5f338c7e429c861f7dbb2dcb3229"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0130755740_a5c153a8f0b8d4f26af1405cdcbcec1cc"><a name="en-us_topic_0130755740_a5c153a8f0b8d4f26af1405cdcbcec1cc"></a><a name="en-us_topic_0130755740_a5c153a8f0b8d4f26af1405cdcbcec1cc"></a>Specifies the AS group ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_r784e679e20ef42c7b5f0d9caebb3d506"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0130755740_af5650be6710143e49d288b78f41a9c9d"><a name="en-us_topic_0130755740_af5650be6710143e49d288b78f41a9c9d"></a><a name="en-us_topic_0130755740_af5650be6710143e49d288b78f41a9c9d"></a>scaling_policy_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0130755740_aa41878c3fbc74f52be50c47e0dd26a46"><a name="en-us_topic_0130755740_aa41878c3fbc74f52be50c47e0dd26a46"></a><a name="en-us_topic_0130755740_aa41878c3fbc74f52be50c47e0dd26a46"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0130755740_a37d79d061a9f47c5beee1f98f4c4611b"><a name="en-us_topic_0130755740_a37d79d061a9f47c5beee1f98f4c4611b"></a><a name="en-us_topic_0130755740_a37d79d061a9f47c5beee1f98f4c4611b"></a>Specifies the AS policy name.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_r28ff2dd5c492496191a531a728a81d07"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0130755740_en-us_topic_0021400638_p861939155558"><a name="en-us_topic_0130755740_en-us_topic_0021400638_p861939155558"></a><a name="en-us_topic_0130755740_en-us_topic_0021400638_p861939155558"></a>scaling_policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0130755740_a62f65a9bf723409c94d67ac591947e49"><a name="en-us_topic_0130755740_a62f65a9bf723409c94d67ac591947e49"></a><a name="en-us_topic_0130755740_a62f65a9bf723409c94d67ac591947e49"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0130755740_ab6a47799a67f44dfb76306dd45488f59"><a name="en-us_topic_0130755740_ab6a47799a67f44dfb76306dd45488f59"></a><a name="en-us_topic_0130755740_ab6a47799a67f44dfb76306dd45488f59"></a>Specifies the AS policy ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_r06fe5129bbc1493289f623afe4a4f1a2"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0130755740_a49f38aeff8914592ba6b8d9e46c40e5c"><a name="en-us_topic_0130755740_a49f38aeff8914592ba6b8d9e46c40e5c"></a><a name="en-us_topic_0130755740_a49f38aeff8914592ba6b8d9e46c40e5c"></a>policy_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0130755740_a89734c8a12d44d69ab229cf5857bdf05"><a name="en-us_topic_0130755740_a89734c8a12d44d69ab229cf5857bdf05"></a><a name="en-us_topic_0130755740_a89734c8a12d44d69ab229cf5857bdf05"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0130755740_aebd2fb9cfe76474d8ff66349fef14fc9"><a name="en-us_topic_0130755740_aebd2fb9cfe76474d8ff66349fef14fc9"></a><a name="en-us_topic_0130755740_aebd2fb9cfe76474d8ff66349fef14fc9"></a>Specifies the AS policy status.</p>
    <a name="en-us_topic_0130755740_u52aa276809d74817884d905b6a93c8bc"></a><a name="en-us_topic_0130755740_u52aa276809d74817884d905b6a93c8bc"></a><ul id="en-us_topic_0130755740_u52aa276809d74817884d905b6a93c8bc"><li><strong id="b7576229175212"><a name="b7576229175212"></a><a name="b7576229175212"></a>INSERVICE</strong>: The AS policy is enabled.</li><li><strong id="b84235270612734"><a name="b84235270612734"></a><a name="b84235270612734"></a>PAUSED</strong>: The AS policy is disabled.</li><li><strong id="b842352706171746"><a name="b842352706171746"></a><a name="b842352706171746"></a>EXECUTING</strong>: The AS policy is being executed.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_rac189e8b65c5430eb4503bf1d1bbb4d7"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0130755740_ab5c5c2b93a134f18a2455224014556e9"><a name="en-us_topic_0130755740_ab5c5c2b93a134f18a2455224014556e9"></a><a name="en-us_topic_0130755740_ab5c5c2b93a134f18a2455224014556e9"></a>scaling_policy_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0130755740_a2de7247f99c143e09e698f0ef82f62bc"><a name="en-us_topic_0130755740_a2de7247f99c143e09e698f0ef82f62bc"></a><a name="en-us_topic_0130755740_a2de7247f99c143e09e698f0ef82f62bc"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0130755740_a65ce06cd4813480498062e1de2541bd3"><a name="en-us_topic_0130755740_a65ce06cd4813480498062e1de2541bd3"></a><a name="en-us_topic_0130755740_a65ce06cd4813480498062e1de2541bd3"></a>Specifies the AS policy type.</p>
    <a name="en-us_topic_0130755740_ud3dc362d60f54fc08039ec57e921e5a6"></a><a name="en-us_topic_0130755740_ud3dc362d60f54fc08039ec57e921e5a6"></a><ul id="en-us_topic_0130755740_ud3dc362d60f54fc08039ec57e921e5a6"><li><strong>ALARM</strong>: indicates that the scaling action is triggered by an alarm. A value is returned for <strong>alarm_id</strong>, and no value is returned for <strong>scheduled_policy</strong>.</li><li><strong>SCHEDULED</strong>: indicates that the scaling action is triggered as scheduled. A value is returned for <strong>scheduled_policy</strong>, and no value is returned for <strong>alarm_id</strong>, <strong>recurrence_type</strong>, <strong>recurrence_value</strong>, <strong>start_time</strong>, or <strong>end_time</strong>.</li><li><strong>RECURRENCE</strong>: indicates that the scaling action is triggered periodically. Values are returned for <strong>scheduled_policy</strong>, <strong>recurrence_type</strong>, <strong>recurrence_value</strong>, <strong>start_time</strong>, and <strong>end_time</strong>, and no value is returned for <strong>alarm_id</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_r4dfedc0bd4ff45f2ac05364f99f01708"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0130755740_a306f2c2ef05e47f78c5e0fc5440cea3c"><a name="en-us_topic_0130755740_a306f2c2ef05e47f78c5e0fc5440cea3c"></a><a name="en-us_topic_0130755740_a306f2c2ef05e47f78c5e0fc5440cea3c"></a>alarm_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0130755740_a979f525a997c4d1e8808195ca9d7f53e"><a name="en-us_topic_0130755740_a979f525a997c4d1e8808195ca9d7f53e"></a><a name="en-us_topic_0130755740_a979f525a997c4d1e8808195ca9d7f53e"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0130755740_a6b68b50e9d6b4676bc2495467cfd4012"><a name="en-us_topic_0130755740_a6b68b50e9d6b4676bc2495467cfd4012"></a><a name="en-us_topic_0130755740_a6b68b50e9d6b4676bc2495467cfd4012"></a>Specifies the alarm ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_r45a3cc4c3f6943639ac3843c688f6865"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0130755740_a52a9f640ec724f40a4829ddf066e0837"><a name="en-us_topic_0130755740_a52a9f640ec724f40a4829ddf066e0837"></a><a name="en-us_topic_0130755740_a52a9f640ec724f40a4829ddf066e0837"></a>scheduled_policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="a4c03d226ca78442f99e13b8d363cd51d"><a name="a4c03d226ca78442f99e13b8d363cd51d"></a><a name="a4c03d226ca78442f99e13b8d363cd51d"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0130755740_adefe07f521ca4e0aab9007ea28bebc7d"><a name="en-us_topic_0130755740_adefe07f521ca4e0aab9007ea28bebc7d"></a><a name="en-us_topic_0130755740_adefe07f521ca4e0aab9007ea28bebc7d"></a>Specifies the periodic or scheduled AS policy. For details, see <a href="#en-us_topic_0130755740_t759e6d15d244474e8f286185ede143fb">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_r3adc5e99c0394bb09b88bfd7836e5929"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0130755740_a4019097cbec84816b539b0064cf28e6f"><a name="en-us_topic_0130755740_a4019097cbec84816b539b0064cf28e6f"></a><a name="en-us_topic_0130755740_a4019097cbec84816b539b0064cf28e6f"></a>scaling_policy_action</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="p16641921104212"><a name="p16641921104212"></a><a name="p16641921104212"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0130755740_a465f6bd6f7314632914ffbcd580db294"><a name="en-us_topic_0130755740_a465f6bd6f7314632914ffbcd580db294"></a><a name="en-us_topic_0130755740_a465f6bd6f7314632914ffbcd580db294"></a>Specifies the scaling action of the AS policy. For details, see <a href="#en-us_topic_0130755740_t34390832ab524bcc8123c0f9a056064f">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_rfbf6d02ab13a45c4b20a3933009721c5"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0130755740_a05d1d794494e401b8c880ccd61a16ae0"><a name="en-us_topic_0130755740_a05d1d794494e401b8c880ccd61a16ae0"></a><a name="en-us_topic_0130755740_a05d1d794494e401b8c880ccd61a16ae0"></a>cool_down_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0130755740_a7b0e63a0ece54ea9a446dce1c73d2d4c"><a name="en-us_topic_0130755740_a7b0e63a0ece54ea9a446dce1c73d2d4c"></a><a name="en-us_topic_0130755740_a7b0e63a0ece54ea9a446dce1c73d2d4c"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0130755740_a888589d12ffb4e7687ae04d2d501165f"><a name="en-us_topic_0130755740_a888589d12ffb4e7687ae04d2d501165f"></a><a name="en-us_topic_0130755740_a888589d12ffb4e7687ae04d2d501165f"></a>Specifies the cooldown period (s).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_rfeeb99d66bb548f68bf214af05f7ded7"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0130755740_aca42d34a1ca749ac886051c797503641"><a name="en-us_topic_0130755740_aca42d34a1ca749ac886051c797503641"></a><a name="en-us_topic_0130755740_aca42d34a1ca749ac886051c797503641"></a>create_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0130755740_a3415b0578ab545f9b4eefe023761a215"><a name="en-us_topic_0130755740_a3415b0578ab545f9b4eefe023761a215"></a><a name="en-us_topic_0130755740_a3415b0578ab545f9b4eefe023761a215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0130755740_a3e6b9790a8504e11b63b6a20ebe50817"><a name="en-us_topic_0130755740_a3e6b9790a8504e11b63b6a20ebe50817"></a><a name="en-us_topic_0130755740_a3e6b9790a8504e11b63b6a20ebe50817"></a>Specifies the time when an AS policy was created. The time format complies with UTC.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **scheduled\_policy**  field description

    <a name="en-us_topic_0130755740_t759e6d15d244474e8f286185ede143fb"></a>
    <table><thead align="left"><tr id="en-us_topic_0130755740_rce98b9668cd747c88039421afe5ce935"><th class="cellrowborder" valign="top" width="26.57%" id="mcps1.2.4.1.1"><p id="en-us_topic_0130755740_ad9ac3007570a4752b2b2dbc0fb04dadc"><a name="en-us_topic_0130755740_ad9ac3007570a4752b2b2dbc0fb04dadc"></a><a name="en-us_topic_0130755740_ad9ac3007570a4752b2b2dbc0fb04dadc"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.3%" id="mcps1.2.4.1.2"><p id="en-us_topic_0130755740_a602246198adf4a79a13bc4317d4c0d4f"><a name="en-us_topic_0130755740_a602246198adf4a79a13bc4317d4c0d4f"></a><a name="en-us_topic_0130755740_a602246198adf4a79a13bc4317d4c0d4f"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.13%" id="mcps1.2.4.1.3"><p id="en-us_topic_0130755740_a8cbfa8dcb0b943ff8e789755123fec83"><a name="en-us_topic_0130755740_a8cbfa8dcb0b943ff8e789755123fec83"></a><a name="en-us_topic_0130755740_a8cbfa8dcb0b943ff8e789755123fec83"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0130755740_r43de461181294c56b28da56a1f604b09"><td class="cellrowborder" valign="top" width="26.57%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0130755740_abc19a41a8f594f1ba6701e10da50a078"><a name="en-us_topic_0130755740_abc19a41a8f594f1ba6701e10da50a078"></a><a name="en-us_topic_0130755740_abc19a41a8f594f1ba6701e10da50a078"></a>launch_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0130755740_a15ae7b8585d24e48abc6b9bf45636fda"><a name="en-us_topic_0130755740_a15ae7b8585d24e48abc6b9bf45636fda"></a><a name="en-us_topic_0130755740_a15ae7b8585d24e48abc6b9bf45636fda"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.13%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0130755740_a61510df8f8ad43319d6df7c903934e43"><a name="en-us_topic_0130755740_a61510df8f8ad43319d6df7c903934e43"></a><a name="en-us_topic_0130755740_a61510df8f8ad43319d6df7c903934e43"></a>Specifies the time when the scaling action is triggered. The time format complies with UTC.</p>
    <a name="en-us_topic_0130755740_uf00af89403894ffc8ec87c36bc988668"></a><a name="en-us_topic_0130755740_uf00af89403894ffc8ec87c36bc988668"></a><ul id="en-us_topic_0130755740_uf00af89403894ffc8ec87c36bc988668"><li>If <strong>scaling_policy_type</strong> is set to <strong>SCHEDULED</strong>, the time format is <strong>YYYY-MM-DDThh:mmZ</strong>.</li><li>If <strong>scaling_policy_type</strong> is set to <strong>RECURRENCE</strong>, the time format is <strong>hh:mm</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_rbd5ec7242fef4c03b21636ac14160d9e"><td class="cellrowborder" valign="top" width="26.57%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0130755740_a18479f6b70b34f29b2b90d754f59282a"><a name="en-us_topic_0130755740_a18479f6b70b34f29b2b90d754f59282a"></a><a name="en-us_topic_0130755740_a18479f6b70b34f29b2b90d754f59282a"></a>recurrence_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0130755740_ae1f14fa2e6a54531aeffd26874fea267"><a name="en-us_topic_0130755740_ae1f14fa2e6a54531aeffd26874fea267"></a><a name="en-us_topic_0130755740_ae1f14fa2e6a54531aeffd26874fea267"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.13%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0130755740_aec06182f642543c6b455c58bfdaffadd"><a name="en-us_topic_0130755740_aec06182f642543c6b455c58bfdaffadd"></a><a name="en-us_topic_0130755740_aec06182f642543c6b455c58bfdaffadd"></a>Specifies the type of a periodically triggered scaling action.</p>
    <a name="ul323885205718"></a><a name="ul323885205718"></a><ul id="ul323885205718"><li><strong>Daily</strong>: indicates that the scaling action is triggered once a day.</li><li><strong>Weekly</strong>: indicates that the scaling action is triggered once a week.</li><li><strong>Monthly</strong>: indicates that the scaling action is triggered once a month.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_r0a62cf7acbad402386b6375b0d8b1353"><td class="cellrowborder" valign="top" width="26.57%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0130755740_a36de9ca6c86e45a3b06fa24eedf584ad"><a name="en-us_topic_0130755740_a36de9ca6c86e45a3b06fa24eedf584ad"></a><a name="en-us_topic_0130755740_a36de9ca6c86e45a3b06fa24eedf584ad"></a>recurrence_value</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0130755740_ad2c0647319f843e0a6c26a2fe1e57172"><a name="en-us_topic_0130755740_ad2c0647319f843e0a6c26a2fe1e57172"></a><a name="en-us_topic_0130755740_ad2c0647319f843e0a6c26a2fe1e57172"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.13%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0130755740_a0fddaf89726a4b13849e706e60be5708"><a name="en-us_topic_0130755740_a0fddaf89726a4b13849e706e60be5708"></a><a name="en-us_topic_0130755740_a0fddaf89726a4b13849e706e60be5708"></a>Specifies the frequency at which scaling actions are triggered.</p>
    <a name="en-us_topic_0130755740_u339136fb44714869865eb1ccb9d659cd"></a><a name="en-us_topic_0130755740_u339136fb44714869865eb1ccb9d659cd"></a><ul id="en-us_topic_0130755740_u339136fb44714869865eb1ccb9d659cd"><li>If <strong>recurrence_type</strong> is set to <strong>Daily</strong>, the value is <strong>null</strong>, indicating that the scaling action is triggered once a day.</li><li>If <strong>recurrence_type</strong> is set to <strong>Weekly</strong>, the value ranges from <strong>1</strong> (Sunday) to <strong>7</strong> (Saturday). The digits refer to dates in each week and separated by a comma, such as <strong>1,3,5</strong>.</li><li>If <strong>recurrence_type</strong> is set to <strong>Monthly</strong>, the value ranges from <strong>1</strong> to <strong>31</strong>. The digits refer to the dates in each month and separated by a comma, such as <strong>1,10,13,28</strong>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_r4c08c4f22c3b4df1a3a5403eeddc4354"><td class="cellrowborder" valign="top" width="26.57%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0130755740_a0c2c51e444dd4e29ba2b60d5461e12c2"><a name="en-us_topic_0130755740_a0c2c51e444dd4e29ba2b60d5461e12c2"></a><a name="en-us_topic_0130755740_a0c2c51e444dd4e29ba2b60d5461e12c2"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0130755740_a615a9f0c0305423db2f2ddf584c93d4b"><a name="en-us_topic_0130755740_a615a9f0c0305423db2f2ddf584c93d4b"></a><a name="en-us_topic_0130755740_a615a9f0c0305423db2f2ddf584c93d4b"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.13%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0130755740_a9fd1aed571e0410681f98248360eb0e0"><a name="en-us_topic_0130755740_a9fd1aed571e0410681f98248360eb0e0"></a><a name="en-us_topic_0130755740_a9fd1aed571e0410681f98248360eb0e0"></a>Specifies the start time of the scaling action triggered periodically. The time format complies with UTC.</p>
    <p id="en-us_topic_0130755740_aea18ea5bcc1d42469166346b0e654f95"><a name="en-us_topic_0130755740_aea18ea5bcc1d42469166346b0e654f95"></a><a name="en-us_topic_0130755740_aea18ea5bcc1d42469166346b0e654f95"></a>The time format is <strong>YYYY-MM-DDThh:mmZ</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_r2ca2a0e358dc475ca68e9d3916d479c5"><td class="cellrowborder" valign="top" width="26.57%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0130755740_ad750922d2cc94d0d9be7f5cfa9629ad0"><a name="en-us_topic_0130755740_ad750922d2cc94d0d9be7f5cfa9629ad0"></a><a name="en-us_topic_0130755740_ad750922d2cc94d0d9be7f5cfa9629ad0"></a>end_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0130755740_adfb428f0abfd4adc9ea6b4ac94f5357a"><a name="en-us_topic_0130755740_adfb428f0abfd4adc9ea6b4ac94f5357a"></a><a name="en-us_topic_0130755740_adfb428f0abfd4adc9ea6b4ac94f5357a"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.13%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0130755740_p16222223105153"><a name="en-us_topic_0130755740_p16222223105153"></a><a name="en-us_topic_0130755740_p16222223105153"></a>Specifies the end time of the scaling action triggered periodically. The time format complies with UTC.</p>
    <p id="en-us_topic_0130755740_ad0f134288f51466e8329969670b77dd3"><a name="en-us_topic_0130755740_ad0f134288f51466e8329969670b77dd3"></a><a name="en-us_topic_0130755740_ad0f134288f51466e8329969670b77dd3"></a>The time format is <strong>YYYY-MM-DDThh:mmZ</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **scaling\_policy\_action**  field description

    <a name="en-us_topic_0130755740_t34390832ab524bcc8123c0f9a056064f"></a>
    <table><thead align="left"><tr id="en-us_topic_0130755740_r60aefe7e3567494189e88990879b9f9d"><th class="cellrowborder" valign="top" width="26.57%" id="mcps1.2.4.1.1"><p id="en-us_topic_0130755740_adddb39856ec84c28bc88ed54a4dfbac7"><a name="en-us_topic_0130755740_adddb39856ec84c28bc88ed54a4dfbac7"></a><a name="en-us_topic_0130755740_adddb39856ec84c28bc88ed54a4dfbac7"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.3%" id="mcps1.2.4.1.2"><p id="en-us_topic_0130755740_ae247601bc48c49498bd0af9cf8617de0"><a name="en-us_topic_0130755740_ae247601bc48c49498bd0af9cf8617de0"></a><a name="en-us_topic_0130755740_ae247601bc48c49498bd0af9cf8617de0"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.13%" id="mcps1.2.4.1.3"><p id="en-us_topic_0130755740_acb5b03b96a6946d79776f9ca4febd68f"><a name="en-us_topic_0130755740_acb5b03b96a6946d79776f9ca4febd68f"></a><a name="en-us_topic_0130755740_acb5b03b96a6946d79776f9ca4febd68f"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0130755740_rdcec146dd2b449beb8e387195da7689d"><td class="cellrowborder" valign="top" width="26.57%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0130755740_a4b8c581b6cdf4fa697bf88b211db4182"><a name="en-us_topic_0130755740_a4b8c581b6cdf4fa697bf88b211db4182"></a><a name="en-us_topic_0130755740_a4b8c581b6cdf4fa697bf88b211db4182"></a>operation</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0130755740_a05d72e6b4cee47d7b26b01d4f9b192dd"><a name="en-us_topic_0130755740_a05d72e6b4cee47d7b26b01d4f9b192dd"></a><a name="en-us_topic_0130755740_a05d72e6b4cee47d7b26b01d4f9b192dd"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.13%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0130755740_a515de00bcdbf499c9d337ad8649a8c17"><a name="en-us_topic_0130755740_a515de00bcdbf499c9d337ad8649a8c17"></a><a name="en-us_topic_0130755740_a515de00bcdbf499c9d337ad8649a8c17"></a>Specifies the scaling action.</p>
    <a name="ul19640134512573"></a><a name="ul19640134512573"></a><ul id="ul19640134512573"><li><strong id="b65676466494"><a name="b65676466494"></a><a name="b65676466494"></a>ADD</strong>: adds specified number of instances to the AS group.</li><li><strong id="b87631211133919"><a name="b87631211133919"></a><a name="b87631211133919"></a>REMOVE</strong>: removes specified number of instances from the AS group.</li><li><strong>SET</strong>: sets the number of instances in the AS group.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_re4b949df938b4369b59c0a5061d8e292"><td class="cellrowborder" valign="top" width="26.57%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0130755740_a9420e7cdbd4f4e2d8c8a5acc3cb52c56"><a name="en-us_topic_0130755740_a9420e7cdbd4f4e2d8c8a5acc3cb52c56"></a><a name="en-us_topic_0130755740_a9420e7cdbd4f4e2d8c8a5acc3cb52c56"></a>instance_number</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0130755740_a0a73f34ebc41475897926a2991096ac0"><a name="en-us_topic_0130755740_a0a73f34ebc41475897926a2991096ac0"></a><a name="en-us_topic_0130755740_a0a73f34ebc41475897926a2991096ac0"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.13%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0130755740_afaf87464277d4a4b9061631559cb97c7"><a name="en-us_topic_0130755740_afaf87464277d4a4b9061631559cb97c7"></a><a name="en-us_topic_0130755740_afaf87464277d4a4b9061631559cb97c7"></a>Specifies the number of instances to be operated.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_row6642680173028"><td class="cellrowborder" valign="top" width="26.57%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0130755740_p34524434173032"><a name="en-us_topic_0130755740_p34524434173032"></a><a name="en-us_topic_0130755740_p34524434173032"></a>instance_percentage</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0130755740_p45015732173032"><a name="en-us_topic_0130755740_p45015732173032"></a><a name="en-us_topic_0130755740_p45015732173032"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.13%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0130755740_p22395691173032"><a name="en-us_topic_0130755740_p22395691173032"></a><a name="en-us_topic_0130755740_p22395691173032"></a>Specifies the percentage of instances to be operated.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "limit": 20,
        "total_number": 1,
        "start_number": 0,
        "scaling_policies": [
            {
                "scaling_policy_id": "fd7d63ce-8f5c-443e-b9a0-bef9386b23b3",
                "scaling_group_id": "e5d27f5c-dd76-4a61-b4bc-a67c5686719a",
                "scaling_policy_name": "as-policy-test",
                "scaling_policy_type": "SCHEDULED",
                "scheduled_policy": {
                    "launch_time": "2015-07-24T01:21Z"
                },
                "cool_down_time": 300,
                "scaling_policy_action": {
                    "operation": "REMOVE",
                    "instance_number": 1
                },
                "policy_status": "INSERVICE",
                "create_time": "2015-07-24T01:09:30Z"
            }
        ]
    }
    ```


## Returned Value<a name="en-us_topic_0130755740_section15165719"></a>

-   Normal

    200

-   Abnormal

    <a name="en-us_topic_0130755740_table5908907"></a>
    <table><thead align="left"><tr id="en-us_topic_0130755740_row16065622"><th class="cellrowborder" valign="top" width="44.17%" id="mcps1.1.3.1.1"><p id="en-us_topic_0130755740_p26246992"><a name="en-us_topic_0130755740_p26246992"></a><a name="en-us_topic_0130755740_p26246992"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.83%" id="mcps1.1.3.1.2"><p id="en-us_topic_0130755740_p45631627"><a name="en-us_topic_0130755740_p45631627"></a><a name="en-us_topic_0130755740_p45631627"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0130755740_row5174319"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0130755740_p16466658"><a name="en-us_topic_0130755740_p16466658"></a><a name="en-us_topic_0130755740_p16466658"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0130755740_p58730959"><a name="en-us_topic_0130755740_p58730959"></a><a name="en-us_topic_0130755740_p58730959"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_row58816586"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0130755740_p66523006"><a name="en-us_topic_0130755740_p66523006"></a><a name="en-us_topic_0130755740_p66523006"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0130755740_p19654399"><a name="en-us_topic_0130755740_p19654399"></a><a name="en-us_topic_0130755740_p19654399"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_row42671863"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0130755740_p33868885"><a name="en-us_topic_0130755740_p33868885"></a><a name="en-us_topic_0130755740_p33868885"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0130755740_p59025204"><a name="en-us_topic_0130755740_p59025204"></a><a name="en-us_topic_0130755740_p59025204"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_row61464796"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0130755740_p12592542"><a name="en-us_topic_0130755740_p12592542"></a><a name="en-us_topic_0130755740_p12592542"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0130755740_p13362997"><a name="en-us_topic_0130755740_p13362997"></a><a name="en-us_topic_0130755740_p13362997"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_row53158116"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0130755740_p10840149"><a name="en-us_topic_0130755740_p10840149"></a><a name="en-us_topic_0130755740_p10840149"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0130755740_p5636878"><a name="en-us_topic_0130755740_p5636878"></a><a name="en-us_topic_0130755740_p5636878"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_row50731910"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0130755740_p15644031"><a name="en-us_topic_0130755740_p15644031"></a><a name="en-us_topic_0130755740_p15644031"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0130755740_p59206997"><a name="en-us_topic_0130755740_p59206997"></a><a name="en-us_topic_0130755740_p59206997"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_row63100926"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0130755740_p10901353"><a name="en-us_topic_0130755740_p10901353"></a><a name="en-us_topic_0130755740_p10901353"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0130755740_p10594405"><a name="en-us_topic_0130755740_p10594405"></a><a name="en-us_topic_0130755740_p10594405"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_row28240785"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0130755740_p5802216"><a name="en-us_topic_0130755740_p5802216"></a><a name="en-us_topic_0130755740_p5802216"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0130755740_p217508"><a name="en-us_topic_0130755740_p217508"></a><a name="en-us_topic_0130755740_p217508"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_row1957580"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0130755740_p24346266"><a name="en-us_topic_0130755740_p24346266"></a><a name="en-us_topic_0130755740_p24346266"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0130755740_p25890496"><a name="en-us_topic_0130755740_p25890496"></a><a name="en-us_topic_0130755740_p25890496"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_row31687876"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0130755740_p16581154"><a name="en-us_topic_0130755740_p16581154"></a><a name="en-us_topic_0130755740_p16581154"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0130755740_p896237"><a name="en-us_topic_0130755740_p896237"></a><a name="en-us_topic_0130755740_p896237"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_row8066134"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0130755740_p49377135"><a name="en-us_topic_0130755740_p49377135"></a><a name="en-us_topic_0130755740_p49377135"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0130755740_p40124968"><a name="en-us_topic_0130755740_p40124968"></a><a name="en-us_topic_0130755740_p40124968"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_row25580392"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0130755740_p58745844"><a name="en-us_topic_0130755740_p58745844"></a><a name="en-us_topic_0130755740_p58745844"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0130755740_p60792949"><a name="en-us_topic_0130755740_p60792949"></a><a name="en-us_topic_0130755740_p60792949"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_row10265637"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0130755740_p26210288"><a name="en-us_topic_0130755740_p26210288"></a><a name="en-us_topic_0130755740_p26210288"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0130755740_p42658596"><a name="en-us_topic_0130755740_p42658596"></a><a name="en-us_topic_0130755740_p42658596"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0130755740_row48383044"><td class="cellrowborder" valign="top" width="44.17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0130755740_p26712487"><a name="en-us_topic_0130755740_p26712487"></a><a name="en-us_topic_0130755740_p26712487"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0130755740_p16227847"><a name="en-us_topic_0130755740_p16227847"></a><a name="en-us_topic_0130755740_p16227847"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).


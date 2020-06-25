# Querying the Information About a CMK<a name="kms_02_0018"></a>

## Function<a name="en-us_topic_0112992343_s1731a14fb0144c79bf0fa90c694f34f7"></a>

This API allows you to query the details about a CMK.

## URI<a name="en-us_topic_0112992343_se70c3e5518a04f60b06032524dddfef4"></a>

-   URI format

    POST /v1.0/\{project\_id\}/kms/describe-key

-   Parameter description

    **Table  1**  Parameters

    <a name="en-us_topic_0112992343_t982da1e0196d4ec1a28d1fbff2cc8191"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992343_r6e963322c1e740d181726d2f0e91df5a"><th class="cellrowborder" valign="top" width="22.74%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992343_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"><a name="en-us_topic_0112992343_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"></a><a name="en-us_topic_0112992343_a3b5bbe5a7f644fd3a74cecbfb3f7ed60"></a><strong id="en-us_topic_0112992343_b842352706173823"><a name="en-us_topic_0112992343_b842352706173823"></a><a name="en-us_topic_0112992343_b842352706173823"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.36%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992343_ad98d2f62bd064b4e96ea922645197c24"><a name="en-us_topic_0112992343_ad98d2f62bd064b4e96ea922645197c24"></a><a name="en-us_topic_0112992343_ad98d2f62bd064b4e96ea922645197c24"></a><strong id="en-us_topic_0112992343_b842352706173832"><a name="en-us_topic_0112992343_b842352706173832"></a><a name="en-us_topic_0112992343_b842352706173832"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.05%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992343_a3becf0b3aec9468984c2efc8d5abbea5"><a name="en-us_topic_0112992343_a3becf0b3aec9468984c2efc8d5abbea5"></a><a name="en-us_topic_0112992343_a3becf0b3aec9468984c2efc8d5abbea5"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="36.85%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992343_a6bb6f1fe56a2454982832e8d56d354d8"><a name="en-us_topic_0112992343_a6bb6f1fe56a2454982832e8d56d354d8"></a><a name="en-us_topic_0112992343_a6bb6f1fe56a2454982832e8d56d354d8"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992343_r69bf37b65d3f446eab7b3f4d1b2fcec0"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992343_ae42d73592f58424ea93a11e52d2478dd"><a name="en-us_topic_0112992343_ae42d73592f58424ea93a11e52d2478dd"></a><a name="en-us_topic_0112992343_ae42d73592f58424ea93a11e52d2478dd"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992343_a56440c0f0ae34ba3b8033d1247673984"><a name="en-us_topic_0112992343_a56440c0f0ae34ba3b8033d1247673984"></a><a name="en-us_topic_0112992343_a56440c0f0ae34ba3b8033d1247673984"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992343_a1a4a71c11a4a45a58d0de2fbe009e9d9"><a name="en-us_topic_0112992343_a1a4a71c11a4a45a58d0de2fbe009e9d9"></a><a name="en-us_topic_0112992343_a1a4a71c11a4a45a58d0de2fbe009e9d9"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="36.85%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992343_a1314869d2dc147b38461e037d622f7b4"><a name="en-us_topic_0112992343_a1314869d2dc147b38461e037d622f7b4"></a><a name="en-us_topic_0112992343_a1314869d2dc147b38461e037d622f7b4"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992343_seb7b7901701247fab30a59b76f1c7f93"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0112992343_table46221022101230"></a>
<table><thead align="left"><tr id="en-us_topic_0112992343_row1239210313121"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992343_p93922314127"><a name="en-us_topic_0112992343_p93922314127"></a><a name="en-us_topic_0112992343_p93922314127"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992343_p63928351216"><a name="en-us_topic_0112992343_p63928351216"></a><a name="en-us_topic_0112992343_p63928351216"></a><strong id="en-us_topic_0112992343_b842352706173926_1"><a name="en-us_topic_0112992343_b842352706173926_1"></a><a name="en-us_topic_0112992343_b842352706173926_1"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992343_p2039263171212"><a name="en-us_topic_0112992343_p2039263171212"></a><a name="en-us_topic_0112992343_p2039263171212"></a><strong id="en-us_topic_0112992343_b842352706173922"><a name="en-us_topic_0112992343_b842352706173922"></a><a name="en-us_topic_0112992343_b842352706173922"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992343_p1739363151218"><a name="en-us_topic_0112992343_p1739363151218"></a><a name="en-us_topic_0112992343_p1739363151218"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992343_row139316391219"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992343_p839318315126"><a name="en-us_topic_0112992343_p839318315126"></a><a name="en-us_topic_0112992343_p839318315126"></a>key_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992343_p6393153101218"><a name="en-us_topic_0112992343_p6393153101218"></a><a name="en-us_topic_0112992343_p6393153101218"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992343_p439315391210"><a name="en-us_topic_0112992343_p439315391210"></a><a name="en-us_topic_0112992343_p439315391210"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992343_p139363101219"><a name="en-us_topic_0112992343_p139363101219"></a><a name="en-us_topic_0112992343_p139363101219"></a>36-byte ID of a CMK that matches the regular expression <span class="parmvalue" id="en-us_topic_0112992343_parmvalue80435593163333"><a name="en-us_topic_0112992343_parmvalue80435593163333"></a><a name="en-us_topic_0112992343_parmvalue80435593163333"></a><b>^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$</b></span></p>
<p id="en-us_topic_0112992343_p1039323161219"><a name="en-us_topic_0112992343_p1039323161219"></a><a name="en-us_topic_0112992343_p1039323161219"></a>Example: 0d0466b0-e727-4d9c-b35d-f84bb474a37f</p>
</td>
</tr>
<tr id="en-us_topic_0112992343_row1839312391218"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992343_p1639317391213"><a name="en-us_topic_0112992343_p1639317391213"></a><a name="en-us_topic_0112992343_p1639317391213"></a>sequence</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992343_p839310318127"><a name="en-us_topic_0112992343_p839310318127"></a><a name="en-us_topic_0112992343_p839310318127"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992343_p10393535125"><a name="en-us_topic_0112992343_p10393535125"></a><a name="en-us_topic_0112992343_p10393535125"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992343_p143931034125"><a name="en-us_topic_0112992343_p143931034125"></a><a name="en-us_topic_0112992343_p143931034125"></a>36-byte serial number of a request message</p>
<p id="en-us_topic_0112992343_p133931230121"><a name="en-us_topic_0112992343_p133931230121"></a><a name="en-us_topic_0112992343_p133931230121"></a>Example: 919c82d4-8046-4722-9094-35c3c6524cff</p>
</td>
</tr>
</tbody>
</table>

## Responses<a name="en-us_topic_0112992343_sfadd53a5f4714e8f87811818d62d0296"></a>

**Table  3**  Response parameters

<a name="en-us_topic_0112992343_t98d238e10953421e84a073707024c329"></a>
<table><thead align="left"><tr id="en-us_topic_0112992343_row842320371212"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992343_p2042319314123"><a name="en-us_topic_0112992343_p2042319314123"></a><a name="en-us_topic_0112992343_p2042319314123"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992343_p194231638123"><a name="en-us_topic_0112992343_p194231638123"></a><a name="en-us_topic_0112992343_p194231638123"></a><strong id="en-us_topic_0112992343_b842352706173926_3"><a name="en-us_topic_0112992343_b842352706173926_3"></a><a name="en-us_topic_0112992343_b842352706173926_3"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992343_p44231391216"><a name="en-us_topic_0112992343_p44231391216"></a><a name="en-us_topic_0112992343_p44231391216"></a><strong id="en-us_topic_0112992343_b84235270617406"><a name="en-us_topic_0112992343_b84235270617406"></a><a name="en-us_topic_0112992343_b84235270617406"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992343_p3423123131211"><a name="en-us_topic_0112992343_p3423123131211"></a><a name="en-us_topic_0112992343_p3423123131211"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992343_row9423631125"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992343_p34231838129"><a name="en-us_topic_0112992343_p34231838129"></a><a name="en-us_topic_0112992343_p34231838129"></a>key_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992343_p1342393181210"><a name="en-us_topic_0112992343_p1342393181210"></a><a name="en-us_topic_0112992343_p1342393181210"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992343_p164231238124"><a name="en-us_topic_0112992343_p164231238124"></a><a name="en-us_topic_0112992343_p164231238124"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992343_p34238381219"><a name="en-us_topic_0112992343_p34238381219"></a><a name="en-us_topic_0112992343_p34238381219"></a>CMK ID</p>
</td>
</tr>
<tr id="en-us_topic_0112992343_row1423113121213"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992343_p0423133111211"><a name="en-us_topic_0112992343_p0423133111211"></a><a name="en-us_topic_0112992343_p0423133111211"></a>domain_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992343_p042317320129"><a name="en-us_topic_0112992343_p042317320129"></a><a name="en-us_topic_0112992343_p042317320129"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992343_p194231832126"><a name="en-us_topic_0112992343_p194231832126"></a><a name="en-us_topic_0112992343_p194231832126"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992343_p54241034126"><a name="en-us_topic_0112992343_p54241034126"></a><a name="en-us_topic_0112992343_p54241034126"></a>User domain ID</p>
</td>
</tr>
<tr id="en-us_topic_0112992343_row442410313125"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992343_p184243311213"><a name="en-us_topic_0112992343_p184243311213"></a><a name="en-us_topic_0112992343_p184243311213"></a>key_alias</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992343_p2042413310129"><a name="en-us_topic_0112992343_p2042413310129"></a><a name="en-us_topic_0112992343_p2042413310129"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992343_p84249361217"><a name="en-us_topic_0112992343_p84249361217"></a><a name="en-us_topic_0112992343_p84249361217"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992343_p142412310128"><a name="en-us_topic_0112992343_p142412310128"></a><a name="en-us_topic_0112992343_p142412310128"></a>Alias of a CMK</p>
</td>
</tr>
<tr id="en-us_topic_0112992343_row14240331218"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992343_p1342453121214"><a name="en-us_topic_0112992343_p1342453121214"></a><a name="en-us_topic_0112992343_p1342453121214"></a>realm</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992343_p1442433171215"><a name="en-us_topic_0112992343_p1442433171215"></a><a name="en-us_topic_0112992343_p1442433171215"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992343_p4424183131218"><a name="en-us_topic_0112992343_p4424183131218"></a><a name="en-us_topic_0112992343_p4424183131218"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992343_p5424731127"><a name="en-us_topic_0112992343_p5424731127"></a><a name="en-us_topic_0112992343_p5424731127"></a>Region where a CMK resides</p>
</td>
</tr>
<tr id="en-us_topic_0112992343_row12424134129"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992343_p1242443191217"><a name="en-us_topic_0112992343_p1242443191217"></a><a name="en-us_topic_0112992343_p1242443191217"></a>key_description</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992343_p64241537126"><a name="en-us_topic_0112992343_p64241537126"></a><a name="en-us_topic_0112992343_p64241537126"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992343_p164242036121"><a name="en-us_topic_0112992343_p164242036121"></a><a name="en-us_topic_0112992343_p164242036121"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992343_p11424133101212"><a name="en-us_topic_0112992343_p11424133101212"></a><a name="en-us_topic_0112992343_p11424133101212"></a>Description of a CMK</p>
</td>
</tr>
<tr id="en-us_topic_0112992343_row1424123171213"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992343_p1142418316124"><a name="en-us_topic_0112992343_p1142418316124"></a><a name="en-us_topic_0112992343_p1142418316124"></a>creation_date</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992343_p1742433101212"><a name="en-us_topic_0112992343_p1742433101212"></a><a name="en-us_topic_0112992343_p1742433101212"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992343_p54241631124"><a name="en-us_topic_0112992343_p54241631124"></a><a name="en-us_topic_0112992343_p54241631124"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992343_p442412311128"><a name="en-us_topic_0112992343_p442412311128"></a><a name="en-us_topic_0112992343_p442412311128"></a>Time when a key is created. The value is a timestamp expressed in the number of seconds since 00:00:00 UTC on January 1, 1970.</p>
</td>
</tr>
<tr id="en-us_topic_0112992343_row13424203111217"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992343_p5424133131216"><a name="en-us_topic_0112992343_p5424133131216"></a><a name="en-us_topic_0112992343_p5424133131216"></a>scheduled_deletion_date</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992343_p1442411341219"><a name="en-us_topic_0112992343_p1442411341219"></a><a name="en-us_topic_0112992343_p1442411341219"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992343_p104243318128"><a name="en-us_topic_0112992343_p104243318128"></a><a name="en-us_topic_0112992343_p104243318128"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992343_p1442417391215"><a name="en-us_topic_0112992343_p1442417391215"></a><a name="en-us_topic_0112992343_p1442417391215"></a>Time when a key will be deleted as scheduled. The value is a timestamp expressed in the number of seconds since 00:00:00 UTC on January 1, 1970.</p>
</td>
</tr>
<tr id="en-us_topic_0112992343_row1242543111216"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992343_p104253316124"><a name="en-us_topic_0112992343_p104253316124"></a><a name="en-us_topic_0112992343_p104253316124"></a>key_state</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992343_p2042511341218"><a name="en-us_topic_0112992343_p2042511341218"></a><a name="en-us_topic_0112992343_p2042511341218"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992343_p1742518312125"><a name="en-us_topic_0112992343_p1742518312125"></a><a name="en-us_topic_0112992343_p1742518312125"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><div class="p" id="en-us_topic_0112992343_p542593151215"><a name="en-us_topic_0112992343_p542593151215"></a><a name="en-us_topic_0112992343_p542593151215"></a>State of a CMK:<a name="en-us_topic_0112992343_ul184931831124"></a><a name="en-us_topic_0112992343_ul184931831124"></a><ul id="en-us_topic_0112992343_ul184931831124"><li><span class="parmvalue" id="en-us_topic_0112992343_parmvalue63632845104232"><a name="en-us_topic_0112992343_parmvalue63632845104232"></a><a name="en-us_topic_0112992343_parmvalue63632845104232"></a><b>1</b></span> indicates that the CMK is waiting to be activated.</li><li><span class="parmvalue" id="en-us_topic_0112992343_parmvalue27931731104241"><a name="en-us_topic_0112992343_parmvalue27931731104241"></a><a name="en-us_topic_0112992343_parmvalue27931731104241"></a><b>2</b></span> indicates that the CMK is enabled.</li><li><span class="parmvalue" id="en-us_topic_0112992343_parmvalue49067618104244"><a name="en-us_topic_0112992343_parmvalue49067618104244"></a><a name="en-us_topic_0112992343_parmvalue49067618104244"></a><b>3</b></span> indicates that the CMK is disabled.</li><li><span class="parmvalue" id="en-us_topic_0112992343_parmvalue28113363104247"><a name="en-us_topic_0112992343_parmvalue28113363104247"></a><a name="en-us_topic_0112992343_parmvalue28113363104247"></a><b>4</b></span> indicates that the CMK is scheduled for deletion.</li><li><span class="parmvalue" id="en-us_topic_0112992343_parmvalue18075000104250"><a name="en-us_topic_0112992343_parmvalue18075000104250"></a><a name="en-us_topic_0112992343_parmvalue18075000104250"></a><b>5</b></span> indicates that the CMK is waiting to be imported.</li></ul>
</div>
</td>
</tr>
<tr id="en-us_topic_0112992343_row124257381216"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992343_p11425633128"><a name="en-us_topic_0112992343_p11425633128"></a><a name="en-us_topic_0112992343_p11425633128"></a>default_key_flag</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992343_p15425338126"><a name="en-us_topic_0112992343_p15425338126"></a><a name="en-us_topic_0112992343_p15425338126"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992343_p6425183151210"><a name="en-us_topic_0112992343_p6425183151210"></a><a name="en-us_topic_0112992343_p6425183151210"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992343_p1042510391215"><a name="en-us_topic_0112992343_p1042510391215"></a><a name="en-us_topic_0112992343_p1042510391215"></a>Identification of a Master Key. The value <strong id="en-us_topic_0112992343_b84235270615132"><a name="en-us_topic_0112992343_b84235270615132"></a><a name="en-us_topic_0112992343_b84235270615132"></a>1</strong> indicates a Default Master Key, and the value <strong id="en-us_topic_0112992343_b84235270615136"><a name="en-us_topic_0112992343_b84235270615136"></a><a name="en-us_topic_0112992343_b84235270615136"></a>0</strong> indicates a CMK.</p>
</td>
</tr>
<tr id="en-us_topic_0112992343_row342512381214"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992343_p142512317121"><a name="en-us_topic_0112992343_p142512317121"></a><a name="en-us_topic_0112992343_p142512317121"></a>key_type</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992343_p542518341212"><a name="en-us_topic_0112992343_p542518341212"></a><a name="en-us_topic_0112992343_p542518341212"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992343_p842518341220"><a name="en-us_topic_0112992343_p842518341220"></a><a name="en-us_topic_0112992343_p842518341220"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992343_p8425236126"><a name="en-us_topic_0112992343_p8425236126"></a><a name="en-us_topic_0112992343_p8425236126"></a>Type of a CMK</p>
</td>
</tr>
<tr id="en-us_topic_0112992343_row144251930121"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992343_p642533161216"><a name="en-us_topic_0112992343_p642533161216"></a><a name="en-us_topic_0112992343_p642533161216"></a>expiration_time</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992343_p042619351214"><a name="en-us_topic_0112992343_p042619351214"></a><a name="en-us_topic_0112992343_p042619351214"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992343_p4426932124"><a name="en-us_topic_0112992343_p4426932124"></a><a name="en-us_topic_0112992343_p4426932124"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992343_p173691125119"><a name="en-us_topic_0112992343_p173691125119"></a><a name="en-us_topic_0112992343_p173691125119"></a>Expiration time of the key material. It is expressed in the form of a time stamp, the total number of seconds since January 1, 1970.</p>
</td>
</tr>
<tr id="en-us_topic_0112992343_row1542614361215"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992343_p74261938127"><a name="en-us_topic_0112992343_p74261938127"></a><a name="en-us_topic_0112992343_p74261938127"></a>origin</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992343_p1242611315120"><a name="en-us_topic_0112992343_p1242611315120"></a><a name="en-us_topic_0112992343_p1242611315120"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992343_p54261339122"><a name="en-us_topic_0112992343_p54261339122"></a><a name="en-us_topic_0112992343_p54261339122"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992343_p9426533128"><a name="en-us_topic_0112992343_p9426533128"></a><a name="en-us_topic_0112992343_p9426533128"></a>Origin of a CMK. The default value is <span class="parmvalue" id="en-us_topic_0112992343_parmvalue5237346195350"><a name="en-us_topic_0112992343_parmvalue5237346195350"></a><a name="en-us_topic_0112992343_parmvalue5237346195350"></a><b>kms</b></span>. The following values are enumerated:</p>
<a name="en-us_topic_0112992343_ul94267314129"></a><a name="en-us_topic_0112992343_ul94267314129"></a><ul id="en-us_topic_0112992343_ul94267314129"><li><span class="parmvalue" id="en-us_topic_0112992343_parmvalue1011124252141313_3"><a name="en-us_topic_0112992343_parmvalue1011124252141313_3"></a><a name="en-us_topic_0112992343_parmvalue1011124252141313_3"></a><b>kms</b></span> indicates that the CMK material is generated by KMS.</li><li><span class="parmvalue" id="en-us_topic_0112992343_parmvalue501259129141335"><a name="en-us_topic_0112992343_parmvalue501259129141335"></a><a name="en-us_topic_0112992343_parmvalue501259129141335"></a><b>external</b></span> indicates that the CMK material is imported.</li></ul>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0112992343_section17883719132515"></a>

The following example describes how to query the information of a CMK whose ID is  **0d0466b0-e727-4d9c-b35d-f84bb474a37f**.

-   Example request

    ```
    {
        "key_id": "0d0466b0-e727-4d9c-b35d-f84bb474a37f"
    }
    ```

-   Example response

    ```
    {
        "key_info": {
            "key_id": "0d0466b0-e727-4d9c-b35d-f84bb474a37f",
            "domain_id": "b168fe00ff56492495a7d22974df2d0b",
            "key_alias": "kms_test",
            "realm": "aaa",
            "key_description": "",
            "creation_date": "1472442386000",
            "scheduled_deletion_date": "",
            "key_state": "2",
            "default_key_flag": "0",
            "key_type": "1",
            "expiration_time":"1501578672000",
            "origin":"kms"
            
        }
    }
    ```

    or

    ```
    {
        "error": {
            "error_code": "KMS.XXXX",
            "error_msg": "XXX"
        }
    }
    ```


## Status Codes<a name="en-us_topic_0112992343_section3454223421"></a>

[Table 4](#en-us_topic_0112992343_en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  4**  Status codes

<a name="en-us_topic_0112992343_en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0112992343_en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992343_en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0112992343_en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0112992343_en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992343_en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0112992343_en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0112992343_en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992343_en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0112992343_en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0112992343_en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992343_en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992343_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0112992343_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0112992343_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992343_en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0112992343_en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0112992343_en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992343_en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0112992343_en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0112992343_en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).


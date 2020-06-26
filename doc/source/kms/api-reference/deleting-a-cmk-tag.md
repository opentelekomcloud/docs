# Deleting a CMK Tag<a name="kms_02_0047"></a>

## Function<a name="en-us_topic_0112992314_section193641144611"></a>

This API enables you to delete a CMK tag.

## URI<a name="en-us_topic_0112992314_section6472103664610"></a>

-   URI format

    DELETE /v1.0/\{project\_id\}/kms/\{key\_id\}/tags/\{key\}

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0112992314_table3777142984717"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992314_row1077710299477"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992314_p1577110425210"><a name="en-us_topic_0112992314_p1577110425210"></a><a name="en-us_topic_0112992314_p1577110425210"></a><strong id="en-us_topic_0112992314_b842352706202545"><a name="en-us_topic_0112992314_b842352706202545"></a><a name="en-us_topic_0112992314_b842352706202545"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992314_p167751142326"><a name="en-us_topic_0112992314_p167751142326"></a><a name="en-us_topic_0112992314_p167751142326"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992314_p157711420214"><a name="en-us_topic_0112992314_p157711420214"></a><a name="en-us_topic_0112992314_p157711420214"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992314_p1877644212217"><a name="en-us_topic_0112992314_p1877644212217"></a><a name="en-us_topic_0112992314_p1877644212217"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992314_row17777142912470"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992314_p1277782954712"><a name="en-us_topic_0112992314_p1277782954712"></a><a name="en-us_topic_0112992314_p1277782954712"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992314_p577711293474"><a name="en-us_topic_0112992314_p577711293474"></a><a name="en-us_topic_0112992314_p577711293474"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992314_p988536101020"><a name="en-us_topic_0112992314_p988536101020"></a><a name="en-us_topic_0112992314_p988536101020"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992314_p177771729114715"><a name="en-us_topic_0112992314_p177771729114715"></a><a name="en-us_topic_0112992314_p177771729114715"></a>Project ID</p>
    </td>
    </tr>
    <tr id="en-us_topic_0112992314_row9777132904717"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992314_p18777192911477"><a name="en-us_topic_0112992314_p18777192911477"></a><a name="en-us_topic_0112992314_p18777192911477"></a>key_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992314_p27774293475"><a name="en-us_topic_0112992314_p27774293475"></a><a name="en-us_topic_0112992314_p27774293475"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992314_p208879615108"><a name="en-us_topic_0112992314_p208879615108"></a><a name="en-us_topic_0112992314_p208879615108"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992314_p17777122912478"><a name="en-us_topic_0112992314_p17777122912478"></a><a name="en-us_topic_0112992314_p17777122912478"></a>36-byte ID of a CMK that matches the regular expression <span class="parmvalue" id="en-us_topic_0112992314_parmvalue80435593163333"><a name="en-us_topic_0112992314_parmvalue80435593163333"></a><a name="en-us_topic_0112992314_parmvalue80435593163333"></a><b>^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$</b></span></p>
    <p id="en-us_topic_0112992314_p1777762912477"><a name="en-us_topic_0112992314_p1777762912477"></a><a name="en-us_topic_0112992314_p1777762912477"></a>Example: 0d0466b0-e727-4d9c-b35d-f84bb474a37f</p>
    </td>
    </tr>
    <tr id="en-us_topic_0112992314_row477712296472"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992314_p1077718295475"><a name="en-us_topic_0112992314_p1077718295475"></a><a name="en-us_topic_0112992314_p1077718295475"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992314_p6777202934712"><a name="en-us_topic_0112992314_p6777202934712"></a><a name="en-us_topic_0112992314_p6777202934712"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992314_p48901667103"><a name="en-us_topic_0112992314_p48901667103"></a><a name="en-us_topic_0112992314_p48901667103"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992314_p3777429154716"><a name="en-us_topic_0112992314_p3777429154716"></a><a name="en-us_topic_0112992314_p3777429154716"></a>Tag key</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992314_section2156440194715"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0112992314_table1916151124817"></a>
<table><thead align="left"><tr id="en-us_topic_0112992314_row12161010481"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992314_p5871637557"><a name="en-us_topic_0112992314_p5871637557"></a><a name="en-us_topic_0112992314_p5871637557"></a><strong id="en-us_topic_0112992314_b1932779048"><a name="en-us_topic_0112992314_b1932779048"></a><a name="en-us_topic_0112992314_b1932779048"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992314_p1087537152"><a name="en-us_topic_0112992314_p1087537152"></a><a name="en-us_topic_0112992314_p1087537152"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992314_p2087337858"><a name="en-us_topic_0112992314_p2087337858"></a><a name="en-us_topic_0112992314_p2087337858"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992314_p1687193712516"><a name="en-us_topic_0112992314_p1687193712516"></a><a name="en-us_topic_0112992314_p1687193712516"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992314_row71613116485"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992314_p196201876489"><a name="en-us_topic_0112992314_p196201876489"></a><a name="en-us_topic_0112992314_p196201876489"></a>sequence</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992314_p1662057164815"><a name="en-us_topic_0112992314_p1662057164815"></a><a name="en-us_topic_0112992314_p1662057164815"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992314_p4386100291125"><a name="en-us_topic_0112992314_p4386100291125"></a><a name="en-us_topic_0112992314_p4386100291125"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992314_p26209724811"><a name="en-us_topic_0112992314_p26209724811"></a><a name="en-us_topic_0112992314_p26209724811"></a>36-byte serial number of a request message</p>
<p id="en-us_topic_0112992314_p1162010716486"><a name="en-us_topic_0112992314_p1162010716486"></a><a name="en-us_topic_0112992314_p1162010716486"></a>Example: 919c82d4-8046-4722-9094-35c3c6524cff</p>
</td>
</tr>
</tbody>
</table>

## Responses<a name="en-us_topic_0112992314_section7456133764811"></a>

None

## Examples<a name="en-us_topic_0112992314_section1482722615177"></a>

Example response

```
{ 
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

## Status Codes<a name="en-us_topic_0112992314_section192111133389"></a>

[Table 3](#en-us_topic_0112992314_en-us_topic_0112992301_table3885195311010)  lists the normal status code returned by the response.

**Table  3**  Status codes

<a name="en-us_topic_0112992314_en-us_topic_0112992301_table3885195311010"></a>
<table><thead align="left"><tr id="en-us_topic_0112992314_en-us_topic_0112992301_row08858533011"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992314_en-us_topic_0112992301_p18885105310016"><a name="en-us_topic_0112992314_en-us_topic_0112992301_p18885105310016"></a><a name="en-us_topic_0112992314_en-us_topic_0112992301_p18885105310016"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992314_en-us_topic_0112992301_p488513536011"><a name="en-us_topic_0112992314_en-us_topic_0112992301_p488513536011"></a><a name="en-us_topic_0112992314_en-us_topic_0112992301_p488513536011"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992314_en-us_topic_0112992301_p188852531708"><a name="en-us_topic_0112992314_en-us_topic_0112992301_p188852531708"></a><a name="en-us_topic_0112992314_en-us_topic_0112992301_p188852531708"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992314_en-us_topic_0112992301_row6885125316018"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992314_en-us_topic_0112992301_p188851853102"><a name="en-us_topic_0112992314_en-us_topic_0112992301_p188851853102"></a><a name="en-us_topic_0112992314_en-us_topic_0112992301_p188851853102"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992314_en-us_topic_0112992301_p2123920113816"><a name="en-us_topic_0112992314_en-us_topic_0112992301_p2123920113816"></a><a name="en-us_topic_0112992314_en-us_topic_0112992301_p2123920113816"></a>No Content</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992314_en-us_topic_0112992301_p151239205384"><a name="en-us_topic_0112992314_en-us_topic_0112992301_p151239205384"></a><a name="en-us_topic_0112992314_en-us_topic_0112992301_p151239205384"></a>The request is processed successfully and no content is returned.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).


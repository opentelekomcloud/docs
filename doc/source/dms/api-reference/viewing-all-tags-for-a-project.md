# Viewing All Tags for a Project<a name="EN-US_TOPIC_0128036919"></a>

## Function<a name="section512706204818"></a>

This API is used to view all tags of a project.

## URI<a name="section15128156174813"></a>

GET /v1.0/\{project\_id\}/queue/tags

**Table  1**  Request header

<a name="table4132146134813"></a>
<table><thead align="left"><tr id="row1035176104818"><th class="cellrowborder" valign="top" width="20.62%" id="mcps1.2.5.1.1"><p id="p18351126194813"><a name="p18351126194813"></a><a name="p18351126194813"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.77%" id="mcps1.2.5.1.2"><p id="p113517654816"><a name="p113517654816"></a><a name="p113517654816"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="19.59%" id="mcps1.2.5.1.3"><p id="p935111694811"><a name="p935111694811"></a><a name="p935111694811"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="34.02%" id="mcps1.2.5.1.4"><p id="p53517674816"><a name="p53517674816"></a><a name="p53517674816"></a>Example</p>
</th>
</tr>
</thead>
<tbody><tr id="row18351196184813"><td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.1 "><p id="p153525624816"><a name="p153525624816"></a><a name="p153525624816"></a>Content-type</p>
</td>
<td class="cellrowborder" valign="top" width="25.77%" headers="mcps1.2.5.1.2 "><p id="p1135219618480"><a name="p1135219618480"></a><a name="p1135219618480"></a>Indicates the MIME types of a request body.</p>
</td>
<td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.5.1.3 "><p id="p1635296114820"><a name="p1635296114820"></a><a name="p1635296114820"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p93529618488"><a name="p93529618488"></a><a name="p93529618488"></a>application/json</p>
</td>
</tr>
<tr id="row335210664814"><td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.1 "><p id="p83521561484"><a name="p83521561484"></a><a name="p83521561484"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="25.77%" headers="mcps1.2.5.1.2 "><p id="p1335216684818"><a name="p1335216684818"></a><a name="p1335216684818"></a>Indicates the user token.</p>
</td>
<td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.5.1.3 "><p id="p17352186124810"><a name="p17352186124810"></a><a name="p17352186124810"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p103524620486"><a name="p103524620486"></a><a name="p103524620486"></a>-</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Parameters

<a name="table133021944127"></a>
<table><thead align="left"><tr id="row46004449215"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p5600144921"><a name="p5600144921"></a><a name="p5600144921"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p196006448220"><a name="p196006448220"></a><a name="p196006448220"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p146001744224"><a name="p146001744224"></a><a name="p146001744224"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p16600144414211"><a name="p16600144414211"></a><a name="p16600144414211"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row36020326116"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p2060273214111"><a name="p2060273214111"></a><a name="p2060273214111"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p80124841117"><a name="p80124841117"></a><a name="p80124841117"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p4311481117"><a name="p4311481117"></a><a name="p4311481117"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p1560303261110"><a name="p1560303261110"></a><a name="p1560303261110"></a>Indicates the ID of a project.</p>
</td>
</tr>
</tbody>
</table>

**Example**

```
 /v1.0/67c01b92944144a19d2da968ef34a912/queue/tags
```

## Request<a name="section35307513"></a>

**Request parameters**

None.

**Example request**

None.

## Response<a name="section10160116154818"></a>

**Response parameters**

**Table  3**  Response parameters

<a name="table121631612486"></a>
<table><thead align="left"><tr id="row435686194817"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.4.1.1"><p id="p435612664810"><a name="p435612664810"></a><a name="p435612664810"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="28.282828282828287%" id="mcps1.2.4.1.2"><p id="p193561867484"><a name="p193561867484"></a><a name="p193561867484"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="51.515151515151516%" id="mcps1.2.4.1.3"><p id="p2356126174813"><a name="p2356126174813"></a><a name="p2356126174813"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1835615615481"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.1 "><p id="p135676184817"><a name="p135676184817"></a><a name="p135676184817"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="28.282828282828287%" headers="mcps1.2.4.1.2 "><p id="p9356186174814"><a name="p9356186174814"></a><a name="p9356186174814"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.2.4.1.3 "><p id="p73566624813"><a name="p73566624813"></a><a name="p73566624813"></a>Indicates a list of tags.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  tags parameter description

<a name="table121701616482"></a>
<table><thead align="left"><tr id="row123561624819"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p63566604810"><a name="p63566604810"></a><a name="p63566604810"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.2"><p id="p17356116154813"><a name="p17356116154813"></a><a name="p17356116154813"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.4.1.3"><p id="p23561565488"><a name="p23561565488"></a><a name="p23561565488"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13356196194815"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p143562067483"><a name="p143562067483"></a><a name="p143562067483"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.2 "><p id="p63561684814"><a name="p63561684814"></a><a name="p63561684814"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p1135613654814"><a name="p1135613654814"></a><a name="p1135613654814"></a>Indicates the tag key, which can contain a maximum of 36 Unicode characters. It cannot be left blank, and cannot contain the following characters: ASCII (0-31), asterisks (*), left angle brackets (&lt;), right angle brackets (&gt;), backslashes (\), and equal signs (=).</p>
</td>
</tr>
<tr id="row23567684813"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p11356762485"><a name="p11356762485"></a><a name="p11356762485"></a>values</p>
</td>
<td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.2 "><p id="p121681849203915"><a name="p121681849203915"></a><a name="p121681849203915"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.4.1.3 "><p id="p635719634816"><a name="p635719634816"></a><a name="p635719634816"></a>Indicates a tag value, which can contain a maximum of 43 Unicode characters. It can be empty, but cannot contain the following characters: ASCII (0-31), asterisks (*), left angle brackets (&lt;), right angle brackets (&gt;), backslashes (\), and equal signs (=).</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
  "tags" : [{
      "key" : "key1",
      "values" : ["value1", "value2"]
    }, {
      "key" : "key2",
      "values" : ["value3", "value4"]
    }
  ]
}
```

## Status Code<a name="section91891164484"></a>

<a name="table18195567480"></a>
<table><thead align="left"><tr id="row133595616486"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p735936134813"><a name="p735936134813"></a><a name="p735936134813"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p335913694814"><a name="p335913694814"></a><a name="p335913694814"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1943231911364"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p01121125153614"><a name="p01121125153614"></a><a name="p01121125153614"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p151121525153615"><a name="p151121525153615"></a><a name="p151121525153615"></a>OK</p>
</td>
</tr>
<tr id="row1635996114819"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p335936174813"><a name="p335936174813"></a><a name="p335936174813"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p14359196124812"><a name="p14359196124812"></a><a name="p14359196124812"></a>Invalid parameter.</p>
</td>
</tr>
<tr id="row1735917644815"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p11359868489"><a name="p11359868489"></a><a name="p11359868489"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p03598620487"><a name="p03598620487"></a><a name="p03598620487"></a>Authentication failed.</p>
</td>
</tr>
<tr id="row143591566481"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p13359146184810"><a name="p13359146184810"></a><a name="p13359146184810"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p1535914624813"><a name="p1535914624813"></a><a name="p1535914624813"></a>Insufficient permission.</p>
</td>
</tr>
<tr id="row835946134819"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p1359116104817"><a name="p1359116104817"></a><a name="p1359116104817"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p7359196154812"><a name="p7359196154812"></a><a name="p7359196154812"></a>No queue found.</p>
</td>
</tr>
<tr id="row135915614480"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p17359106194819"><a name="p17359106194819"></a><a name="p17359106194819"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p1135918612483"><a name="p1135918612483"></a><a name="p1135918612483"></a>System error.</p>
</td>
</tr>
</tbody>
</table>


# Creating a Security Group \(Discarded\)<a name="EN-US_TOPIC_0090187680"></a>

## Function<a name="en-us_topic_0057972662_section27950026"></a>

This API is used to create a security group.

## Constraints<a name="en-us_topic_0057972662_section49359659"></a>

This API will be discarded. 

You are advised to use the desired network API. For details, see "Security Group \(Native OpenStack API\) \> Creating a Security Group" in  _Virtual Private Network API Reference_.

## URI<a name="en-us_topic_0057972662_section50223649"></a>

POST /v2/\{project\_id\}/os-security-groups

POST /v2.1/\{project\_id\}/os-security-groups

[Table 1](#en-us_topic_0057972662_table55945983)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057972662_table55945983"></a>
<table><thead align="left"><tr id="en-us_topic_0057972662_row11302482"><th class="cellrowborder" valign="top" width="33%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972662_row49888896"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972662_p14468758"><a name="en-us_topic_0057972662_p14468758"></a><a name="en-us_topic_0057972662_p14468758"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972662_p31118786"><a name="en-us_topic_0057972662_p31118786"></a><a name="en-us_topic_0057972662_p31118786"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057972662_section41583755"></a>

[Table 2](#en-us_topic_0057972662_table63943666)  describes the request parameters.

**Table  2**  Request parameters

<a name="en-us_topic_0057972662_table63943666"></a>
<table><thead align="left"><tr id="en-us_topic_0057972662_row46071449"><th class="cellrowborder" valign="top" width="21.587841215878413%" id="mcps1.2.5.1.1"><p id="en-us_topic_0058745339_p39560242204918"><a name="en-us_topic_0058745339_p39560242204918"></a><a name="en-us_topic_0058745339_p39560242204918"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.588541145885412%" id="mcps1.2.5.1.2"><p id="p776915317295"><a name="p776915317295"></a><a name="p776915317295"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="21.347865213478652%" id="mcps1.2.5.1.3"><p id="en-us_topic_0058745339_p50263001204918"><a name="en-us_topic_0058745339_p50263001204918"></a><a name="en-us_topic_0058745339_p50263001204918"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="42.47575242475752%" id="mcps1.2.5.1.4"><p id="en-us_topic_0058745339_p2596798204918"><a name="en-us_topic_0058745339_p2596798204918"></a><a name="en-us_topic_0058745339_p2596798204918"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972662_row10655236"><td class="cellrowborder" valign="top" width="21.587841215878413%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972662_p57767782"><a name="en-us_topic_0057972662_p57767782"></a><a name="en-us_topic_0057972662_p57767782"></a>security_group</p>
</td>
<td class="cellrowborder" valign="top" width="14.588541145885412%" headers="mcps1.2.5.1.2 "><p id="p776919314292"><a name="p776919314292"></a><a name="p776919314292"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.347865213478652%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972662_p48678752"><a name="en-us_topic_0057972662_p48678752"></a><a name="en-us_topic_0057972662_p48678752"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="42.47575242475752%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972662_p10212927"><a name="en-us_topic_0057972662_p10212927"></a><a name="en-us_topic_0057972662_p10212927"></a>Specifies the security group, which is configured in the message body. For details, see <a href="#en-us_topic_0057972662_table21940722">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Objects of request parameter  **security\_group**

<a name="en-us_topic_0057972662_table21940722"></a>
<table><thead align="left"><tr id="en-us_topic_0057972662_row43216271"><th class="cellrowborder" valign="top" width="22.157784221577842%" id="mcps1.2.5.1.1"><p id="p1485183101118"><a name="p1485183101118"></a><a name="p1485183101118"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.018598140185981%" id="mcps1.2.5.1.2"><p id="p987214010294"><a name="p987214010294"></a><a name="p987214010294"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="21.347865213478652%" id="mcps1.2.5.1.3"><p id="p18485336113"><a name="p18485336113"></a><a name="p18485336113"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="42.47575242475752%" id="mcps1.2.5.1.4"><p id="p1648517315115"><a name="p1648517315115"></a><a name="p1648517315115"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972662_row57557412"><td class="cellrowborder" valign="top" width="22.157784221577842%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972662_p31638772"><a name="en-us_topic_0057972662_p31638772"></a><a name="en-us_topic_0057972662_p31638772"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.018598140185981%" headers="mcps1.2.5.1.2 "><p id="p13872104052910"><a name="p13872104052910"></a><a name="p13872104052910"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.347865213478652%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972662_p415393471693"><a name="en-us_topic_0057972662_p415393471693"></a><a name="en-us_topic_0057972662_p415393471693"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.47575242475752%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972662_p15080136"><a name="en-us_topic_0057972662_p15080136"></a><a name="en-us_topic_0057972662_p15080136"></a>Specifies the security group name. It is a string of 0 to 255 characters.</p>
</td>
</tr>
<tr id="en-us_topic_0057972662_row1503503"><td class="cellrowborder" valign="top" width="22.157784221577842%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972662_p54674917"><a name="en-us_topic_0057972662_p54674917"></a><a name="en-us_topic_0057972662_p54674917"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.018598140185981%" headers="mcps1.2.5.1.2 "><p id="p087214408298"><a name="p087214408298"></a><a name="p087214408298"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="21.347865213478652%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972662_p449516831693"><a name="en-us_topic_0057972662_p449516831693"></a><a name="en-us_topic_0057972662_p449516831693"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.47575242475752%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972662_p32242465"><a name="en-us_topic_0057972662_p32242465"></a><a name="en-us_topic_0057972662_p32242465"></a>Specifies information about a security group. It is a string of 0 to 255 characters.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0057972662_section38709481"></a>

[Table 4](#en-us_topic_0057972662_table61502840)  describes the response parameters.

**Table  4**  Response parameters

<a name="en-us_topic_0057972662_table61502840"></a>
<table><thead align="left"><tr id="en-us_topic_0057972662_row45420240"><th class="cellrowborder" valign="top" width="29.95299529952995%" id="mcps1.2.4.1.1"><p id="p17521191015112"><a name="p17521191015112"></a><a name="p17521191015112"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="23.65236523652365%" id="mcps1.2.4.1.2"><p id="p35211110111112"><a name="p35211110111112"></a><a name="p35211110111112"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46.39463946394639%" id="mcps1.2.4.1.3"><p id="p105377109114"><a name="p105377109114"></a><a name="p105377109114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972662_row49282936"><td class="cellrowborder" valign="top" width="29.95299529952995%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972662_p32494840"><a name="en-us_topic_0057972662_p32494840"></a><a name="en-us_topic_0057972662_p32494840"></a>security_group</p>
</td>
<td class="cellrowborder" valign="top" width="23.65236523652365%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972662_p14836356"><a name="en-us_topic_0057972662_p14836356"></a><a name="en-us_topic_0057972662_p14836356"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="46.39463946394639%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972662_p33484259"><a name="en-us_topic_0057972662_p33484259"></a><a name="en-us_topic_0057972662_p33484259"></a>Specifies the security group. For details, see <a href="#en-us_topic_0057972662_table27870469">Table 5</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5**  Objects of response parameter  **security\_group**

<a name="en-us_topic_0057972662_table27870469"></a>
<table><thead align="left"><tr id="en-us_topic_0057972662_row21933905"><th class="cellrowborder" valign="top" width="30.023002300230022%" id="mcps1.2.4.1.1"><p id="p11189161310116"><a name="p11189161310116"></a><a name="p11189161310116"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="30.023002300230022%" id="mcps1.2.4.1.2"><p id="p1118951313111"><a name="p1118951313111"></a><a name="p1118951313111"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="39.953995399539956%" id="mcps1.2.4.1.3"><p id="p181891413161115"><a name="p181891413161115"></a><a name="p181891413161115"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972662_row36810105"><td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972662_p28828491"><a name="en-us_topic_0057972662_p28828491"></a><a name="en-us_topic_0057972662_p28828491"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972662_p6329693416937"><a name="en-us_topic_0057972662_p6329693416937"></a><a name="en-us_topic_0057972662_p6329693416937"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.953995399539956%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972662_p24345054"><a name="en-us_topic_0057972662_p24345054"></a><a name="en-us_topic_0057972662_p24345054"></a>Provides supplementary information about the security group.</p>
</td>
</tr>
<tr id="en-us_topic_0057972662_row17778899"><td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972662_p30804749"><a name="en-us_topic_0057972662_p30804749"></a><a name="en-us_topic_0057972662_p30804749"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972662_p5717066816937"><a name="en-us_topic_0057972662_p5717066816937"></a><a name="en-us_topic_0057972662_p5717066816937"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.953995399539956%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972662_p35225966"><a name="en-us_topic_0057972662_p35225966"></a><a name="en-us_topic_0057972662_p35225966"></a>Specifies the security group ID in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0057972662_row48598242"><td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972662_p44143566"><a name="en-us_topic_0057972662_p44143566"></a><a name="en-us_topic_0057972662_p44143566"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972662_p4300522616937"><a name="en-us_topic_0057972662_p4300522616937"></a><a name="en-us_topic_0057972662_p4300522616937"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.953995399539956%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972662_p52667802"><a name="en-us_topic_0057972662_p52667802"></a><a name="en-us_topic_0057972662_p52667802"></a>Specifies the security group name.</p>
</td>
</tr>
<tr id="en-us_topic_0057972662_row4248175"><td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972662_p8557861"><a name="en-us_topic_0057972662_p8557861"></a><a name="en-us_topic_0057972662_p8557861"></a>rules</p>
</td>
<td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972662_p4177153616937"><a name="en-us_topic_0057972662_p4177153616937"></a><a name="en-us_topic_0057972662_p4177153616937"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="39.953995399539956%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972662_p30752875"><a name="en-us_topic_0057972662_p30752875"></a><a name="en-us_topic_0057972662_p30752875"></a>Specifies the rules of the security group. The list is empty.</p>
</td>
</tr>
<tr id="en-us_topic_0057972662_row8340425"><td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972662_p4485813"><a name="en-us_topic_0057972662_p4485813"></a><a name="en-us_topic_0057972662_p4485813"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972662_p5835901916937"><a name="en-us_topic_0057972662_p5835901916937"></a><a name="en-us_topic_0057972662_p5835901916937"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.953995399539956%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972662_p36771698"><a name="en-us_topic_0057972662_p36771698"></a><a name="en-us_topic_0057972662_p36771698"></a>Specifies the tenant or project ID.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057972662_section12841014"></a>

```
POST https://{endpoint}/v2/bb1118612ba64af3a6ea63a1bdcaa5ae/os-security-groups
POST https://{endpoint}/v2.1/bb1118612ba64af3a6ea63a1bdcaa5ae/os-security-groups
```

```
{
    "security_group": {
        "name": "test",
        "description": "description"
    }
}
```

## Example Response<a name="section817065572614"></a>

```
{
    "security_group": {
        "rules": [],
        "tenant_id": "bb1118612ba64af3a6ea63a1bdcaa5ae",
        "description": "desc-sg",
        "id": "81f1d23b-b1e2-42cd-bdee-359b4a065a42",
        "name": "test-sg"
    }
}
```

## Returned Values<a name="en-us_topic_0057972662_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


# Querying Top N Attack Source IP Addresses<a name="EN-US_TOPIC_0193631116"></a>

## Function Description<a name="section56466498"></a>

This API is used to query the top N attack source IP addresses.

## URI<a name="section10383651"></a>

-   URI format

    GET  /v1/\{project\_id\}/waf/event/attack/source?top=\{top\}&from=\{from\}&to=\{to\}&hosts=\{hostids\}

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >An example of a URI is as follows:  
    >GET  /v1/3ac26c59e15a4a11bb680a103a29ddb6/waf/event/attack/type?from=1543976973635&to=1563976973635&hosts=3211757cafa3437aae24d760022e79ba&hosts=93029844064b43739b51ca63036fbc4b&hosts=34fe5f5c60ef4e43a9975296765d1217  

-   Parameter description

    **Table  1**  Path parameters

    <a name="table39180367"></a>
    <table><thead align="left"><tr id="row66112983"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p53551383"><a name="p53551383"></a><a name="p53551383"></a><strong id="b14104181815194"><a name="b14104181815194"></a><a name="b14104181815194"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.2"><p id="p42694776"><a name="p42694776"></a><a name="p42694776"></a><strong id="b7514161951920"><a name="b7514161951920"></a><a name="b7514161951920"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p35724833"><a name="p35724833"></a><a name="p35724833"></a><strong id="b3967152016195"><a name="b3967152016195"></a><a name="b3967152016195"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.5.1.4"><p id="p8030395"><a name="p8030395"></a><a name="p8030395"></a><strong id="b159011022111919"><a name="b159011022111919"></a><a name="b159011022111919"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46482286"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p6968801"><a name="p6968801"></a><a name="p6968801"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p27601980"><a name="p27601980"></a><a name="p27601980"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p21167912"><a name="p21167912"></a><a name="p21167912"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p36879308"><a name="p36879308"></a><a name="p36879308"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row63478323"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p41470559"><a name="p41470559"></a><a name="p41470559"></a>top</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p3672152"><a name="p3672152"></a><a name="p3672152"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p29008901"><a name="p29008901"></a><a name="p29008901"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p910799"><a name="p910799"></a><a name="p910799"></a>Specifies the top <em id="i351184685015"><a name="i351184685015"></a><a name="i351184685015"></a>n</em> attack source IP addresses to be queried. The default value is <strong id="b17640195710122"><a name="b17640195710122"></a><a name="b17640195710122"></a>5</strong>.</p>
    </td>
    </tr>
    <tr id="row8197194"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p59992969"><a name="p59992969"></a><a name="p59992969"></a>from</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p27592345"><a name="p27592345"></a><a name="p27592345"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p20387490"><a name="p20387490"></a><a name="p20387490"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p18857034"><a name="p18857034"></a><a name="p18857034"></a>Specifies the start time (UTC) in milliseconds. For example, <strong id="b181534323509"><a name="b181534323509"></a><a name="b181534323509"></a>1548172800000</strong>.</p>
    </td>
    </tr>
    <tr id="row12564727728"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p1556417274219"><a name="p1556417274219"></a><a name="p1556417274219"></a>to</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p1256410276220"><a name="p1256410276220"></a><a name="p1256410276220"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p145642274213"><a name="p145642274213"></a><a name="p145642274213"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p676211156578"><a name="p676211156578"></a><a name="p676211156578"></a>Specifies the end time (UTC) in milliseconds. For example, <strong id="b29251034135013"><a name="b29251034135013"></a><a name="b29251034135013"></a>1548431999000</strong>.</p>
    </td>
    </tr>
    <tr id="row31421347"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p62101151"><a name="p62101151"></a><a name="p62101151"></a>hosts</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.2 "><p id="p64137360"><a name="p64137360"></a><a name="p64137360"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p27743710"><a name="p27743710"></a><a name="p27743710"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.5.1.4 "><p id="p32648048"><a name="p32648048"></a><a name="p32648048"></a>Specifies the domain IDs.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section26344003"></a>

Request parameters

None

## Response<a name="section35769441"></a>

Response parameters

**Table  2**  Parameter description

<a name="table29324718"></a>
<table><thead align="left"><tr id="row1824515"><th class="cellrowborder" valign="top" width="24.490000000000002%" id="mcps1.2.4.1.1"><p id="p13568011"><a name="p13568011"></a><a name="p13568011"></a><strong id="b895919219282"><a name="b895919219282"></a><a name="b895919219282"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.23%" id="mcps1.2.4.1.2"><p id="p25267083"><a name="p25267083"></a><a name="p25267083"></a><strong id="b124461023172819"><a name="b124461023172819"></a><a name="b124461023172819"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="58.28%" id="mcps1.2.4.1.3"><p id="p33367852"><a name="p33367852"></a><a name="p33367852"></a><strong id="b466122410285"><a name="b466122410285"></a><a name="b466122410285"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row31875216"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p31755717"><a name="p31755717"></a><a name="p31755717"></a>total</p>
</td>
<td class="cellrowborder" valign="top" width="17.23%" headers="mcps1.2.4.1.2 "><p id="p22076270"><a name="p22076270"></a><a name="p22076270"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="58.28%" headers="mcps1.2.4.1.3 "><p id="p43347444"><a name="p43347444"></a><a name="p43347444"></a>Specifies the total number of attack source IP addresses.</p>
</td>
</tr>
<tr id="row54582677"><td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.1 "><p id="p59120688"><a name="p59120688"></a><a name="p59120688"></a>items</p>
</td>
<td class="cellrowborder" valign="top" width="17.23%" headers="mcps1.2.4.1.2 "><p id="p24046428"><a name="p24046428"></a><a name="p24046428"></a><a href="#table1441245463618">Table 3</a></p>
</td>
<td class="cellrowborder" valign="top" width="58.28%" headers="mcps1.2.4.1.3 "><p id="p1603648"><a name="p1603648"></a><a name="p1603648"></a>Specifies the array of items.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **items**

<a name="table1441245463618"></a>
<table><thead align="left"><tr id="row1241695410366"><th class="cellrowborder" valign="top" width="32.46675332466753%" id="mcps1.2.4.1.1"><p id="p641715493612"><a name="p641715493612"></a><a name="p641715493612"></a><strong id="b960546539"><a name="b960546539"></a><a name="b960546539"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.73722627737226%" id="mcps1.2.4.1.2"><p id="p14419115433618"><a name="p14419115433618"></a><a name="p14419115433618"></a><strong id="b1784478650"><a name="b1784478650"></a><a name="b1784478650"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.796020397960206%" id="mcps1.2.4.1.3"><p id="p942015493613"><a name="p942015493613"></a><a name="p942015493613"></a><strong id="b509122604"><a name="b509122604"></a><a name="b509122604"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row7105349114410"><td class="cellrowborder" valign="top" width="32.46675332466753%" headers="mcps1.2.4.1.1 "><p id="p1860154844412"><a name="p1860154844412"></a><a name="p1860154844412"></a>ip</p>
</td>
<td class="cellrowborder" valign="top" width="27.73722627737226%" headers="mcps1.2.4.1.2 "><p id="p96216488441"><a name="p96216488441"></a><a name="p96216488441"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p26464817444"><a name="p26464817444"></a><a name="p26464817444"></a>Specifies the attack source IP addresses.</p>
</td>
</tr>
<tr id="row18105114920444"><td class="cellrowborder" valign="top" width="32.46675332466753%" headers="mcps1.2.4.1.1 "><p id="p1267134834416"><a name="p1267134834416"></a><a name="p1267134834416"></a>num</p>
</td>
<td class="cellrowborder" valign="top" width="27.73722627737226%" headers="mcps1.2.4.1.2 "><p id="p168184818440"><a name="p168184818440"></a><a name="p168184818440"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.796020397960206%" headers="mcps1.2.4.1.3 "><p id="p37184894413"><a name="p37184894413"></a><a name="p37184894413"></a>Specifies the number of attacks came from the attack source IP addresses.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section973562631310"></a>

Response example

```
{
  "total": 4,
  "items": [
     {"ip": "X.X.1.1", "num": 1000},
     {"ip": "X.X.1.2", "num": 1000},
     {"ip": "X.X.1.3", "num": 1000},
     {"ip": "X.X.1.4", "num": 1000}
   ]
}
```

## Status Code<a name="section53489518"></a>

[Table 4](#en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0)  describes the normal status code returned by the API.

**Table  4**  Status code

<a name="en-us_topic_0193631139_t82c3440f3efb42a38b9d4dc4011a33d0"></a>
<table><thead align="left"><tr id="en-us_topic_0193631139_r3d6e2f205c444705bdbb9daaac74e575"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0193631139_af3c4073076f24eca88d94e3fa1effdc6"><a name="en-us_topic_0193631139_af3c4073076f24eca88d94e3fa1effdc6"></a><a name="en-us_topic_0193631139_af3c4073076f24eca88d94e3fa1effdc6"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="19.41%" id="mcps1.2.4.1.2"><p id="en-us_topic_0193631139_en-us_topic_0144911667_p4531342288"><a name="en-us_topic_0193631139_en-us_topic_0144911667_p4531342288"></a><a name="en-us_topic_0193631139_en-us_topic_0144911667_p4531342288"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="58.589999999999996%" id="mcps1.2.4.1.3"><p id="en-us_topic_0193631139_ada185614bba24140995b8123b3e9faa8"><a name="en-us_topic_0193631139_ada185614bba24140995b8123b3e9faa8"></a><a name="en-us_topic_0193631139_ada185614bba24140995b8123b3e9faa8"></a>Meaning</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0193631139_rc7b2adc390904a1ba79e303017797786"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0193631139_a93f3895d44bb4226934cc626ac50e37b"><a name="en-us_topic_0193631139_a93f3895d44bb4226934cc626ac50e37b"></a><a name="en-us_topic_0193631139_a93f3895d44bb4226934cc626ac50e37b"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="19.41%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0193631139_en-us_topic_0144911667_p7538425819"><a name="en-us_topic_0193631139_en-us_topic_0144911667_p7538425819"></a><a name="en-us_topic_0193631139_en-us_topic_0144911667_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0193631139_en-us_topic_0144911667_p369874114414"><a name="en-us_topic_0193631139_en-us_topic_0144911667_p369874114414"></a><a name="en-us_topic_0193631139_en-us_topic_0144911667_p369874114414"></a>The request has succeeded.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Codes](status-codes.md).


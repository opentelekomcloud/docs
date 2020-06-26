# Querying Detailed Information About Disks \(Discarded\)<a name="EN-US_TOPIC_0065817710"></a>

## Function<a name="en-us_topic_0057973210_section28902385"></a>

This API is used to query detailed information about disks.

## Constraints<a name="en-us_topic_0057973210_section53828184"></a>

-   This API will be discarded. You are advised to use the EVS API "Querying Details About All EVS Disks \(Native OpenStack API V2\)".

## URI<a name="en-us_topic_0057973210_section58794873"></a>

GET /v2/\{project\_id\}/os-volumes/detail

GET /v2.1/\{project\_id\}/os-volumes/detail

[Table 1](#en-us_topic_0057973210_table2814978410562)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973210_table2814978410562"></a>
<table><thead align="left"><tr id="en-us_topic_0057973210_row4149654710562"><th class="cellrowborder" valign="top" width="33%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="44%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973210_row3491217610562"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973210_p931403110562"><a name="en-us_topic_0057973210_p931403110562"></a><a name="en-us_topic_0057973210_p931403110562"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973210_p1623904210562"><a name="en-us_topic_0057973210_p1623904210562"></a><a name="en-us_topic_0057973210_p1623904210562"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057973210_section46007812"></a>

N/A

## Response<a name="en-us_topic_0057973210_section11417132"></a>

[Table 2](#en-us_topic_0057973210_table20675657)  describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0057973210_table20675657"></a>
<table><thead align="left"><tr id="en-us_topic_0057973210_row8633818"><th class="cellrowborder" valign="top" width="30.023002300230022%" id="mcps1.2.4.1.1"><p id="p62404314"><a name="p62404314"></a><a name="p62404314"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="30.023002300230022%" id="mcps1.2.4.1.2"><p id="p3528183"><a name="p3528183"></a><a name="p3528183"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="39.953995399539956%" id="mcps1.2.4.1.3"><p id="p17347392"><a name="p17347392"></a><a name="p17347392"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973210_row10702812"><td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973210_p61621426"><a name="en-us_topic_0057973210_p61621426"></a><a name="en-us_topic_0057973210_p61621426"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973210_p25279646"><a name="en-us_topic_0057973210_p25279646"></a><a name="en-us_topic_0057973210_p25279646"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.953995399539956%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973210_p33755089"><a name="en-us_topic_0057973210_p33755089"></a><a name="en-us_topic_0057973210_p33755089"></a>Specifies the disk ID in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0057973210_row35360353"><td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973210_p45616319"><a name="en-us_topic_0057973210_p45616319"></a><a name="en-us_topic_0057973210_p45616319"></a>displayName</p>
</td>
<td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973210_p3934325"><a name="en-us_topic_0057973210_p3934325"></a><a name="en-us_topic_0057973210_p3934325"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.953995399539956%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973210_p43305739"><a name="en-us_topic_0057973210_p43305739"></a><a name="en-us_topic_0057973210_p43305739"></a>Specifies the disk name.</p>
</td>
</tr>
<tr id="en-us_topic_0057973210_row54207338"><td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973210_p28718233"><a name="en-us_topic_0057973210_p28718233"></a><a name="en-us_topic_0057973210_p28718233"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973210_p44475525"><a name="en-us_topic_0057973210_p44475525"></a><a name="en-us_topic_0057973210_p44475525"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.953995399539956%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973210_p14578865"><a name="en-us_topic_0057973210_p14578865"></a><a name="en-us_topic_0057973210_p14578865"></a>Specifies the disk status.</p>
</td>
</tr>
<tr id="en-us_topic_0057973210_row64100928"><td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973210_p24792666"><a name="en-us_topic_0057973210_p24792666"></a><a name="en-us_topic_0057973210_p24792666"></a>attachments</p>
</td>
<td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973210_p62048949"><a name="en-us_topic_0057973210_p62048949"></a><a name="en-us_topic_0057973210_p62048949"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="39.953995399539956%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973210_p20789580"><a name="en-us_topic_0057973210_p20789580"></a><a name="en-us_topic_0057973210_p20789580"></a>Specifies the attachment information about a disk.</p>
</td>
</tr>
<tr id="en-us_topic_0057973210_row52888500"><td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973210_p56110116"><a name="en-us_topic_0057973210_p56110116"></a><a name="en-us_topic_0057973210_p56110116"></a>availabilityZone</p>
</td>
<td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973210_p48625528"><a name="en-us_topic_0057973210_p48625528"></a><a name="en-us_topic_0057973210_p48625528"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.953995399539956%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973210_p63661294"><a name="en-us_topic_0057973210_p63661294"></a><a name="en-us_topic_0057973210_p63661294"></a>Specifies the AZ to which the disk belongs.</p>
</td>
</tr>
<tr id="en-us_topic_0057973210_row36080735"><td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973210_p36858462"><a name="en-us_topic_0057973210_p36858462"></a><a name="en-us_topic_0057973210_p36858462"></a>createdAt</p>
</td>
<td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973210_p32745478"><a name="en-us_topic_0057973210_p32745478"></a><a name="en-us_topic_0057973210_p32745478"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.953995399539956%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973210_p27609454"><a name="en-us_topic_0057973210_p27609454"></a><a name="en-us_topic_0057973210_p27609454"></a>Specifies the time when the disk was created.</p>
</td>
</tr>
<tr id="en-us_topic_0057973210_row47158499"><td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973210_p61742075"><a name="en-us_topic_0057973210_p61742075"></a><a name="en-us_topic_0057973210_p61742075"></a>displayDescription</p>
</td>
<td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973210_p35052192"><a name="en-us_topic_0057973210_p35052192"></a><a name="en-us_topic_0057973210_p35052192"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.953995399539956%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973210_p62465711"><a name="en-us_topic_0057973210_p62465711"></a><a name="en-us_topic_0057973210_p62465711"></a>Specifies the disk description.</p>
</td>
</tr>
<tr id="en-us_topic_0057973210_row25320488"><td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973210_p37693619"><a name="en-us_topic_0057973210_p37693619"></a><a name="en-us_topic_0057973210_p37693619"></a>volumeType</p>
</td>
<td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973210_p33284303"><a name="en-us_topic_0057973210_p33284303"></a><a name="en-us_topic_0057973210_p33284303"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.953995399539956%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973210_p6071512"><a name="en-us_topic_0057973210_p6071512"></a><a name="en-us_topic_0057973210_p6071512"></a>Specifies the disk type.</p>
</td>
</tr>
<tr id="en-us_topic_0057973210_row54643614"><td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973210_p64056647"><a name="en-us_topic_0057973210_p64056647"></a><a name="en-us_topic_0057973210_p64056647"></a>snapshotId</p>
</td>
<td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973210_p21205924"><a name="en-us_topic_0057973210_p21205924"></a><a name="en-us_topic_0057973210_p21205924"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.953995399539956%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973210_p15397020"><a name="en-us_topic_0057973210_p15397020"></a><a name="en-us_topic_0057973210_p15397020"></a>Specifies the snapshot ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973210_row4355456"><td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973210_p17247680"><a name="en-us_topic_0057973210_p17247680"></a><a name="en-us_topic_0057973210_p17247680"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973210_p54884857"><a name="en-us_topic_0057973210_p54884857"></a><a name="en-us_topic_0057973210_p54884857"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="39.953995399539956%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973210_p60492147"><a name="en-us_topic_0057973210_p60492147"></a><a name="en-us_topic_0057973210_p60492147"></a>Specifies the disk metadata.</p>
</td>
</tr>
<tr id="en-us_topic_0057973210_row7558414"><td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973210_p8251823"><a name="en-us_topic_0057973210_p8251823"></a><a name="en-us_topic_0057973210_p8251823"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="30.023002300230022%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973210_p64417965"><a name="en-us_topic_0057973210_p64417965"></a><a name="en-us_topic_0057973210_p64417965"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="39.953995399539956%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973210_p61755870"><a name="en-us_topic_0057973210_p61755870"></a><a name="en-us_topic_0057973210_p61755870"></a>Specifies the disk size.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **attachments**  field description

<a name="en-us_topic_0057973210_table10694153118228"></a>
<table><thead align="left"><tr id="en-us_topic_0057973210_row1770213111229"><th class="cellrowborder" valign="top" width="26.502650265026507%" id="mcps1.2.4.1.1"><p id="p928012114918"><a name="p928012114918"></a><a name="p928012114918"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="24.81248124812481%" id="mcps1.2.4.1.2"><p id="p142801315498"><a name="p142801315498"></a><a name="p142801315498"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.684868486848686%" id="mcps1.2.4.1.3"><p id="p4295171184915"><a name="p4295171184915"></a><a name="p4295171184915"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973210_row17709183112211"><td class="cellrowborder" valign="top" width="26.502650265026507%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973210_p5711203142219"><a name="en-us_topic_0057973210_p5711203142219"></a><a name="en-us_topic_0057973210_p5711203142219"></a>device</p>
</td>
<td class="cellrowborder" valign="top" width="24.81248124812481%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973210_p371215313222"><a name="en-us_topic_0057973210_p371215313222"></a><a name="en-us_topic_0057973210_p371215313222"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.684868486848686%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973210_p87146313224"><a name="en-us_topic_0057973210_p87146313224"></a><a name="en-us_topic_0057973210_p87146313224"></a>Specifies the directory to which the disk is mounted.</p>
</td>
</tr>
<tr id="en-us_topic_0057973210_row11715153182215"><td class="cellrowborder" valign="top" width="26.502650265026507%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973210_p197177319224"><a name="en-us_topic_0057973210_p197177319224"></a><a name="en-us_topic_0057973210_p197177319224"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="24.81248124812481%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973210_p1719183182216"><a name="en-us_topic_0057973210_p1719183182216"></a><a name="en-us_topic_0057973210_p1719183182216"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.684868486848686%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973210_p97211331142215"><a name="en-us_topic_0057973210_p97211331142215"></a><a name="en-us_topic_0057973210_p97211331142215"></a>Specifies the ID of the attached resource.</p>
</td>
</tr>
<tr id="en-us_topic_0057973210_row117221431132216"><td class="cellrowborder" valign="top" width="26.502650265026507%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973210_p37244312222"><a name="en-us_topic_0057973210_p37244312222"></a><a name="en-us_topic_0057973210_p37244312222"></a>serverId</p>
</td>
<td class="cellrowborder" valign="top" width="24.81248124812481%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973210_p11726103113222"><a name="en-us_topic_0057973210_p11726103113222"></a><a name="en-us_topic_0057973210_p11726103113222"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.684868486848686%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973210_p18728731122219"><a name="en-us_topic_0057973210_p18728731122219"></a><a name="en-us_topic_0057973210_p18728731122219"></a>Specifies the ECS ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973210_row1729193182219"><td class="cellrowborder" valign="top" width="26.502650265026507%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973210_p673013122218"><a name="en-us_topic_0057973210_p673013122218"></a><a name="en-us_topic_0057973210_p673013122218"></a>volumeId</p>
</td>
<td class="cellrowborder" valign="top" width="24.81248124812481%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973210_p1573210319222"><a name="en-us_topic_0057973210_p1573210319222"></a><a name="en-us_topic_0057973210_p1573210319222"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.684868486848686%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973210_p97342312223"><a name="en-us_topic_0057973210_p97342312223"></a><a name="en-us_topic_0057973210_p97342312223"></a>Specifies the ID of the attached disk.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057973210_section35645325"></a>

```
GET https://{endpoint}/v2/b84c367e4d1047fc9b54f28b400ddbc2/os-volumes/detail
GET https://{endpoint}/v2.1/b84c367e4d1047fc9b54f28b400ddbc2/os-volumes/detail
```

## Example Response<a name="section1142813459392"></a>

```
{
    "volumes": [
        {
        "status": "available",
        "attachments": [{}],
        "availabilityZone": "nova",
        "createdAt": "2016-05-20T07:57:56.299000",
        "displayDescription": null,
        "volumeType": null,
        "dispalyName": "test",
        "snapshotId": null,
        "metadata": {},
        "id": "70b14513-faad-4646-b7ab-a065cef282b4",
        "size": 1    
        }
    ]
}
```

## Returned Values<a name="en-us_topic_0057973210_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


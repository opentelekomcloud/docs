# Querying Details About a Floating IP Address \(Discarded\)<a name="EN-US_TOPIC_0065820818"></a>

## Function<a name="en-us_topic_0057972673_section10293088"></a>

This API is used to query the details about a floating IP address based on the ID of the IP address.

## Constraints<a name="en-us_topic_0057972673_section28433766"></a>

-   This API will be discarded. You are advised to use the VPC API "Querying a Floating IP Address".

## URI<a name="en-us_topic_0057972673_section25528928"></a>

GET /v2/\{project\_id\}/os-floating-ips/\{floating\_ip\_id\}

GET /v2.1/\{project\_id\}/os-floating-ips/\{floating\_ip\_id\}

[Table 1](#en-us_topic_0057972673_table32475667)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057972673_table32475667"></a>
<table><thead align="left"><tr id="en-us_topic_0057972673_row44937496"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972673_row1664874"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972673_p637140"><a name="en-us_topic_0057972673_p637140"></a><a name="en-us_topic_0057972673_p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972673_p51608407"><a name="en-us_topic_0057972673_p51608407"></a><a name="en-us_topic_0057972673_p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057972673_row102094505165"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972673_p620919503165"><a name="en-us_topic_0057972673_p620919503165"></a><a name="en-us_topic_0057972673_p620919503165"></a>floating_ip_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972673_p32091350111612"><a name="en-us_topic_0057972673_p32091350111612"></a><a name="en-us_topic_0057972673_p32091350111612"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972673_p2209205020164"><a name="en-us_topic_0057972673_p2209205020164"></a><a name="en-us_topic_0057972673_p2209205020164"></a>Specifies the ID of the floating IP address.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057972673_section54577306"></a>

None

## Response<a name="en-us_topic_0057972673_section21433709"></a>

[Table 2](#en-us_topic_0057972673_table38246063)  describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0057972673_table38246063"></a>
<table><thead align="left"><tr id="en-us_topic_0057972673_row31787174"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p1810134211253"><a name="p1810134211253"></a><a name="p1810134211253"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="p1076878152910"><a name="p1076878152910"></a><a name="p1076878152910"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p88251842102518"><a name="p88251842102518"></a><a name="p88251842102518"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44%" id="mcps1.2.5.1.4"><p id="p16825942112519"><a name="p16825942112519"></a><a name="p16825942112519"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972673_row12502218"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972673_p6046746"><a name="en-us_topic_0057972673_p6046746"></a><a name="en-us_topic_0057972673_p6046746"></a>floating_ip</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p137691832912"><a name="p137691832912"></a><a name="p137691832912"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972673_p20024398"><a name="en-us_topic_0057972673_p20024398"></a><a name="en-us_topic_0057972673_p20024398"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972673_p48031108"><a name="en-us_topic_0057972673_p48031108"></a><a name="en-us_topic_0057972673_p48031108"></a>Specifies the floating IP address. For details, see <a href="#en-us_topic_0057972673_table65314517">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **floating\_ip**  objects

<a name="en-us_topic_0057972673_table65314517"></a>
<table><thead align="left"><tr id="en-us_topic_0057972673_row49408564"><th class="cellrowborder" valign="top" width="21.782178217821784%" id="mcps1.2.5.1.1"><p id="p83352466258"><a name="p83352466258"></a><a name="p83352466258"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.2.5.1.2"><p id="p41947234295"><a name="p41947234295"></a><a name="p41947234295"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.5.1.3"><p id="p103351946192513"><a name="p103351946192513"></a><a name="p103351946192513"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="42.57425742574257%" id="mcps1.2.5.1.4"><p id="p15335144615253"><a name="p15335144615253"></a><a name="p15335144615253"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972673_row23930149"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972673_p59293887"><a name="en-us_topic_0057972673_p59293887"></a><a name="en-us_topic_0057972673_p59293887"></a>fixed_ip</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.2 "><p id="p1719422320291"><a name="p1719422320291"></a><a name="p1719422320291"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972673_p38075525"><a name="en-us_topic_0057972673_p38075525"></a><a name="en-us_topic_0057972673_p38075525"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.57425742574257%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972673_p34333880"><a name="en-us_topic_0057972673_p34333880"></a><a name="en-us_topic_0057972673_p34333880"></a>Specifies a private IP address.</p>
</td>
</tr>
<tr id="en-us_topic_0057972673_row40569470"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972673_p64901660"><a name="en-us_topic_0057972673_p64901660"></a><a name="en-us_topic_0057972673_p64901660"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.2 "><p id="p151941523162915"><a name="p151941523162915"></a><a name="p151941523162915"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972673_p22543082"><a name="en-us_topic_0057972673_p22543082"></a><a name="en-us_topic_0057972673_p22543082"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.57425742574257%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972673_p64334135"><a name="en-us_topic_0057972673_p64334135"></a><a name="en-us_topic_0057972673_p64334135"></a>Specifies the floating IP address ID in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0057972673_row42136306"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972673_p57597629"><a name="en-us_topic_0057972673_p57597629"></a><a name="en-us_topic_0057972673_p57597629"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.2 "><p id="p019418233294"><a name="p019418233294"></a><a name="p019418233294"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972673_p34896348"><a name="en-us_topic_0057972673_p34896348"></a><a name="en-us_topic_0057972673_p34896348"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.57425742574257%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972673_p46606392"><a name="en-us_topic_0057972673_p46606392"></a><a name="en-us_topic_0057972673_p46606392"></a>Specifies the ID of a bound ECS in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0057972673_row16804345"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972673_p18974699"><a name="en-us_topic_0057972673_p18974699"></a><a name="en-us_topic_0057972673_p18974699"></a>ip</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.2 "><p id="p1819419236299"><a name="p1819419236299"></a><a name="p1819419236299"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972673_p60555637"><a name="en-us_topic_0057972673_p60555637"></a><a name="en-us_topic_0057972673_p60555637"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.57425742574257%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972673_p21064308"><a name="en-us_topic_0057972673_p21064308"></a><a name="en-us_topic_0057972673_p21064308"></a>Specifies the floating IP address.</p>
</td>
</tr>
<tr id="en-us_topic_0057972673_row55361044"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972673_p55059575"><a name="en-us_topic_0057972673_p55059575"></a><a name="en-us_topic_0057972673_p55059575"></a>pool</p>
</td>
<td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.2.5.1.2 "><p id="p151941923122917"><a name="p151941923122917"></a><a name="p151941923122917"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972673_p30640599"><a name="en-us_topic_0057972673_p30640599"></a><a name="en-us_topic_0057972673_p30640599"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.57425742574257%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972673_p41924012"><a name="en-us_topic_0057972673_p41924012"></a><a name="en-us_topic_0057972673_p41924012"></a>Specifies the name of a network resource pool that provides floating IP addresses.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057972673_section58685656"></a>

```
GET https://{endpoint}/v2/e73621affb8f44e1bc01898747ca09d4/os-floating-ips/05f71f43-f3c9-47ef-ac8d-9f02aef66418
GET https://{endpoint}/v2.1/e73621affb8f44e1bc01898747ca09d4/os-floating-ips/05f71f43-f3c9-47ef-ac8d-9f02aef66418
```

## Example Response<a name="section138011021164918"></a>

```
{
  "floating_ip":{
      "id": "05f71f43-f3c9-47ef-ac8d-9f02aef66418",
      "pool": "external",
      "ip": "10.154.51.235",
      "fixed_ip": "192.168.1.2",
      "instance_id": "8b380f68-5057-4aa2-a33a-170b37218fa8"
    }
}
```

## Returned Values<a name="en-us_topic_0057972673_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


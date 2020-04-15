# Releasing a Floating IP Address \(Discarded\)<a name="EN-US_TOPIC_0065820819"></a>

## Function<a name="en-us_topic_0057972674_section41330139"></a>

This API is used to release a floating IP address.

## Constraints<a name="en-us_topic_0057972674_section59406944"></a>

-   This API will be discarded. You are advised to use the VPC API "Deleting a Floating IP Address".

## URI<a name="en-us_topic_0057972674_section36426933"></a>

DELETE /v2/\{project\_id\}/os-floating-ips/\{floating\_ip\_id\}

DELETE /v2.1/\{project\_id\}/os-floating-ips/\{floating\_ip\_id\}

[Table 1](#en-us_topic_0057972674_table32475667)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057972674_table32475667"></a>
<table><thead align="left"><tr id="en-us_topic_0057972674_row44937496"><th class="cellrowborder" valign="top" width="22.24%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.87%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="55.88999999999999%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972674_row1664874"><td class="cellrowborder" valign="top" width="22.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972674_p637140"><a name="en-us_topic_0057972674_p637140"></a><a name="en-us_topic_0057972674_p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972674_p51608407"><a name="en-us_topic_0057972674_p51608407"></a><a name="en-us_topic_0057972674_p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="55.88999999999999%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057972674_row102094505165"><td class="cellrowborder" valign="top" width="22.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972674_p620919503165"><a name="en-us_topic_0057972674_p620919503165"></a><a name="en-us_topic_0057972674_p620919503165"></a>floating_ip_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972674_p32091350111612"><a name="en-us_topic_0057972674_p32091350111612"></a><a name="en-us_topic_0057972674_p32091350111612"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="55.88999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972674_p2209205020164"><a name="en-us_topic_0057972674_p2209205020164"></a><a name="en-us_topic_0057972674_p2209205020164"></a>Specifies the ID of the floating IP address.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057972674_section64900454"></a>

None

## Response<a name="en-us_topic_0057972674_section47233174"></a>

None

## Example Request<a name="en-us_topic_0057972674_section22445387"></a>

```
DELETE https://{endpoint}/v2/e73621affb8f44e1bc01898747ca09d4/os-floating-ips/05f71f43-f3c9-47ef-ac8d-9f02aef66418
DELETE https://{endpoint}/v2.1/e73621affb8f44e1bc01898747ca09d4/os-floating-ips/05f71f43-f3c9-47ef-ac8d-9f02aef66418
```

## Example Response<a name="section38161942204920"></a>

None

## Returned Values<a name="en-us_topic_0092803065_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


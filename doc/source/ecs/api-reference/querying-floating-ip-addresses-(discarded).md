# Querying Floating IP Addresses \(Discarded\)<a name="EN-US_TOPIC_0065820817"></a>

## Function<a name="en-us_topic_0057972671_section8117"></a>

This API is used to query floating IP addresses.

## Constraints<a name="en-us_topic_0057972671_section657479"></a>

-   This API will be discarded. You are advised to use the VPC API "Querying Floating IP Addresses".

## URI<a name="en-us_topic_0057972671_section73053"></a>

GET /v2/\{project\_id\}/os-floating-ips

GET /v2.1/\{project\_id\}/os-floating-ips

[Table 1](#en-us_topic_0057972671_table32475667)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057972671_table32475667"></a>
<table><thead align="left"><tr id="en-us_topic_0057972671_row44937496"><th class="cellrowborder" valign="top" width="22.24%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.87%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="55.88999999999999%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972671_row1664874"><td class="cellrowborder" valign="top" width="22.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972671_p637140"><a name="en-us_topic_0057972671_p637140"></a><a name="en-us_topic_0057972671_p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972671_p51608407"><a name="en-us_topic_0057972671_p51608407"></a><a name="en-us_topic_0057972671_p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="55.88999999999999%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057972671_section5917317"></a>

None

## Response<a name="en-us_topic_0057972671_section53255854"></a>

[Table 2](#en-us_topic_0057972671_table49535170)  describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0057972671_table49535170"></a>
<table><thead align="left"><tr id="en-us_topic_0057972671_row22681099"><th class="cellrowborder" valign="top" width="18.408159184081594%" id="mcps1.2.5.1.1"><p id="p84761026162512"><a name="p84761026162512"></a><a name="p84761026162512"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.61833816618338%" id="mcps1.2.5.1.2"><p id="p4188171582412"><a name="p4188171582412"></a><a name="p4188171582412"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="20.86791320867913%" id="mcps1.2.5.1.3"><p id="p4476126202510"><a name="p4476126202510"></a><a name="p4476126202510"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44.10558944105589%" id="mcps1.2.5.1.4"><p id="p1347632672516"><a name="p1347632672516"></a><a name="p1347632672516"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972671_row18691797"><td class="cellrowborder" valign="top" width="18.408159184081594%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972671_p37640571"><a name="en-us_topic_0057972671_p37640571"></a><a name="en-us_topic_0057972671_p37640571"></a>floating_ips</p>
</td>
<td class="cellrowborder" valign="top" width="16.61833816618338%" headers="mcps1.2.5.1.2 "><p id="p3188111515242"><a name="p3188111515242"></a><a name="p3188111515242"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20.86791320867913%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972671_p28987447"><a name="en-us_topic_0057972671_p28987447"></a><a name="en-us_topic_0057972671_p28987447"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="44.10558944105589%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972671_p119818"><a name="en-us_topic_0057972671_p119818"></a><a name="en-us_topic_0057972671_p119818"></a>Specifies the floating IP addresses.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **floating\_ip**  objects

<a name="en-us_topic_0057972671_table9705331"></a>
<table><thead align="left"><tr id="en-us_topic_0057972671_row25036876"><th class="cellrowborder" valign="top" width="18.608139186081388%" id="mcps1.2.5.1.1"><p id="p1319062962517"><a name="p1319062962517"></a><a name="p1319062962517"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.34836516348365%" id="mcps1.2.5.1.2"><p id="p155231117162412"><a name="p155231117162412"></a><a name="p155231117162412"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="21.017898210178977%" id="mcps1.2.5.1.3"><p id="p141906290254"><a name="p141906290254"></a><a name="p141906290254"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44.02559744025597%" id="mcps1.2.5.1.4"><p id="p920632913255"><a name="p920632913255"></a><a name="p920632913255"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972671_row15318330"><td class="cellrowborder" valign="top" width="18.608139186081388%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972671_p32825243"><a name="en-us_topic_0057972671_p32825243"></a><a name="en-us_topic_0057972671_p32825243"></a>floating_ip</p>
</td>
<td class="cellrowborder" valign="top" width="16.34836516348365%" headers="mcps1.2.5.1.2 "><p id="p1452361742413"><a name="p1452361742413"></a><a name="p1452361742413"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.017898210178977%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972671_p41599065"><a name="en-us_topic_0057972671_p41599065"></a><a name="en-us_topic_0057972671_p41599065"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="44.02559744025597%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972671_p66828554"><a name="en-us_topic_0057972671_p66828554"></a><a name="en-us_topic_0057972671_p66828554"></a>Specifies the floating IP address.</p>
</td>
</tr>
</tbody>
</table>

**Table  4** **floating\_ip**  attributes

<a name="en-us_topic_0057972671_table44403789"></a>
<table><thead align="left"><tr id="en-us_topic_0057972671_row44190002"><th class="cellrowborder" valign="top" width="18.59%" id="mcps1.2.5.1.1"><p id="p59042316256"><a name="p59042316256"></a><a name="p59042316256"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.43%" id="mcps1.2.5.1.2"><p id="p1734022619251"><a name="p1734022619251"></a><a name="p1734022619251"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="20.87%" id="mcps1.2.5.1.3"><p id="p12904193113252"><a name="p12904193113252"></a><a name="p12904193113252"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44.11%" id="mcps1.2.5.1.4"><p id="p16904123192516"><a name="p16904123192516"></a><a name="p16904123192516"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972671_row43998472"><td class="cellrowborder" valign="top" width="18.59%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972671_p7106508"><a name="en-us_topic_0057972671_p7106508"></a><a name="en-us_topic_0057972671_p7106508"></a>fixed_ip</p>
</td>
<td class="cellrowborder" valign="top" width="16.43%" headers="mcps1.2.5.1.2 "><p id="p2034092611256"><a name="p2034092611256"></a><a name="p2034092611256"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972671_p38756276"><a name="en-us_topic_0057972671_p38756276"></a><a name="en-us_topic_0057972671_p38756276"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.11%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972671_p4445458"><a name="en-us_topic_0057972671_p4445458"></a><a name="en-us_topic_0057972671_p4445458"></a>Specifies a private IP address.</p>
</td>
</tr>
<tr id="en-us_topic_0057972671_row40009126"><td class="cellrowborder" valign="top" width="18.59%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972671_p19513753"><a name="en-us_topic_0057972671_p19513753"></a><a name="en-us_topic_0057972671_p19513753"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="16.43%" headers="mcps1.2.5.1.2 "><p id="p73401126182514"><a name="p73401126182514"></a><a name="p73401126182514"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972671_p37110132"><a name="en-us_topic_0057972671_p37110132"></a><a name="en-us_topic_0057972671_p37110132"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.11%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972671_p8621060"><a name="en-us_topic_0057972671_p8621060"></a><a name="en-us_topic_0057972671_p8621060"></a>Specifies the floating IP address ID in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0057972671_row10480683"><td class="cellrowborder" valign="top" width="18.59%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972671_p43629015"><a name="en-us_topic_0057972671_p43629015"></a><a name="en-us_topic_0057972671_p43629015"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.43%" headers="mcps1.2.5.1.2 "><p id="p7341102662519"><a name="p7341102662519"></a><a name="p7341102662519"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972671_p44289360"><a name="en-us_topic_0057972671_p44289360"></a><a name="en-us_topic_0057972671_p44289360"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.11%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972671_p1113543"><a name="en-us_topic_0057972671_p1113543"></a><a name="en-us_topic_0057972671_p1113543"></a>Specifies the ID of a bound ECS in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0057972671_row10021890"><td class="cellrowborder" valign="top" width="18.59%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972671_p6466753"><a name="en-us_topic_0057972671_p6466753"></a><a name="en-us_topic_0057972671_p6466753"></a>ip</p>
</td>
<td class="cellrowborder" valign="top" width="16.43%" headers="mcps1.2.5.1.2 "><p id="p1534132622515"><a name="p1534132622515"></a><a name="p1534132622515"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972671_p54045009"><a name="en-us_topic_0057972671_p54045009"></a><a name="en-us_topic_0057972671_p54045009"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.11%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972671_p53180163"><a name="en-us_topic_0057972671_p53180163"></a><a name="en-us_topic_0057972671_p53180163"></a>Specifies the floating IP address.</p>
</td>
</tr>
<tr id="en-us_topic_0057972671_row8859419"><td class="cellrowborder" valign="top" width="18.59%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972671_p46524311"><a name="en-us_topic_0057972671_p46524311"></a><a name="en-us_topic_0057972671_p46524311"></a>pool</p>
</td>
<td class="cellrowborder" valign="top" width="16.43%" headers="mcps1.2.5.1.2 "><p id="p43419267251"><a name="p43419267251"></a><a name="p43419267251"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20.87%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972671_p10372872"><a name="en-us_topic_0057972671_p10372872"></a><a name="en-us_topic_0057972671_p10372872"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.11%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972671_p8031464"><a name="en-us_topic_0057972671_p8031464"></a><a name="en-us_topic_0057972671_p8031464"></a>Specifies the name of a network resource pool that provides floating IP addresses.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057972671_section9540645"></a>

```
GET https://{endpoint}/v2/e73621affb8f44e1bc01898747ca09d4/os-floating-ips
GET https://{endpoint}/v2.1/e73621affb8f44e1bc01898747ca09d4/os-floating-ips
```

## Example Response<a name="section716714585484"></a>

```
{
  "floating_ips": [
    {
      "id": "05f71f43-f3c9-47ef-ac8d-9f02aef66418",
      "pool": "external",
      "ip": "10.154.51.235",
      "fixed_ip": "192.168.1.2",
      "instance_id": "8b380f68-5057-4aa2-a33a-170b37218fa8"
    },
    {
      "id": "a25236cf-dd76-4adc-916a-f0b4a24048d3",
      "pool": "external",
      "ip": "10.154.51.237",
      "fixed_ip": null,
      "instance_id": null
    }
  ]
}
```

## Returned Values<a name="en-us_topic_0057972671_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


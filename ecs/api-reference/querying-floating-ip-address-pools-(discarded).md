# Querying Floating IP Address Pools \(Discarded\)<a name="EN-US_TOPIC_0065820820"></a>

## Function<a name="en-us_topic_0057972835_section7554882"></a>

This API is used to query floating IP address pools.

There is only one network resource pool that can be queried through this API by tenants in Open Telekom Cloud live network environment.

## Constraints<a name="en-us_topic_0057972835_section7965739"></a>

This API will be discarded. You are advised to use the VPC API "Querying Networks".

The API parameter is as follows: router:external=True

```
GET /networks?router:external=True //Name in the result is returned.
```

## URI<a name="en-us_topic_0057972835_section885082"></a>

GET /v2/\{project\_id\}/os-floating-ip-pools

GET /v2.1/\{project\_id\}/os-floating-ip-pools

[Table 1](#en-us_topic_0057972835_table32475667)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057972835_table32475667"></a>
<table><thead align="left"><tr id="en-us_topic_0057972835_row44937496"><th class="cellrowborder" valign="top" width="22.24%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.87%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="55.88999999999999%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972835_row1664874"><td class="cellrowborder" valign="top" width="22.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972835_p637140"><a name="en-us_topic_0057972835_p637140"></a><a name="en-us_topic_0057972835_p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972835_p51608407"><a name="en-us_topic_0057972835_p51608407"></a><a name="en-us_topic_0057972835_p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="55.88999999999999%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057972835_section4582792"></a>

None

## Response<a name="en-us_topic_0057972835_section41245128"></a>

[Table 2](#en-us_topic_0057972835_table54779151)  describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0057972835_table54779151"></a>
<table><thead align="left"><tr id="en-us_topic_0057972835_row21723514"><th class="cellrowborder" valign="top" width="19.18808119188081%" id="mcps1.2.5.1.1"><p id="p2181159142617"><a name="p2181159142617"></a><a name="p2181159142617"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.13828617138286%" id="mcps1.2.5.1.2"><p id="p20648171253016"><a name="p20648171253016"></a><a name="p20648171253016"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="27.407259274072594%" id="mcps1.2.5.1.3"><p id="p1418119982619"><a name="p1418119982619"></a><a name="p1418119982619"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="36.266373362663735%" id="mcps1.2.5.1.4"><p id="p1218116952619"><a name="p1218116952619"></a><a name="p1218116952619"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972835_row56262227"><td class="cellrowborder" valign="top" width="19.18808119188081%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972835_p60946511"><a name="en-us_topic_0057972835_p60946511"></a><a name="en-us_topic_0057972835_p60946511"></a>floating_ip_pools</p>
</td>
<td class="cellrowborder" valign="top" width="17.13828617138286%" headers="mcps1.2.5.1.2 "><p id="p264811215307"><a name="p264811215307"></a><a name="p264811215307"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="27.407259274072594%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972835_p37720384"><a name="en-us_topic_0057972835_p37720384"></a><a name="en-us_topic_0057972835_p37720384"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="36.266373362663735%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972835_p53064224"><a name="en-us_topic_0057972835_p53064224"></a><a name="en-us_topic_0057972835_p53064224"></a>Specifies the floating IP address pool.</p>
</td>
</tr>
<tr id="en-us_topic_0057972835_row7815975"><td class="cellrowborder" valign="top" width="19.18808119188081%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972835_p29114202"><a name="en-us_topic_0057972835_p29114202"></a><a name="en-us_topic_0057972835_p29114202"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.13828617138286%" headers="mcps1.2.5.1.2 "><p id="p764815127301"><a name="p764815127301"></a><a name="p764815127301"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="27.407259274072594%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972835_p9440199"><a name="en-us_topic_0057972835_p9440199"></a><a name="en-us_topic_0057972835_p9440199"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.266373362663735%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972835_p62775401"><a name="en-us_topic_0057972835_p62775401"></a><a name="en-us_topic_0057972835_p62775401"></a>Specifies the name of the floating IP address pool.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057972835_section35661838"></a>

```
GET https://{endpoint}/v2/e73621affb8f44e1bc01898747ca09d4/os-floating-ip-pools
GET https://{endpoint}/v2.1/e73621affb8f44e1bc01898747ca09d4/os-floating-ip-pools
```

## Example Response<a name="section96791312115012"></a>

```
{
    "floating_ip_pools": [
        {
            "name": "pool1"
        },
        {
            "name": "pool2"
        }
    ]
}
```

## Returned Values<a name="en-us_topic_0057972835_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


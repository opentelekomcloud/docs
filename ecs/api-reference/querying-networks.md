# Querying Networks<a name="EN-US_TOPIC_0031169828"></a>

## Function<a name="section53922917165259"></a>

This API is used to query the networks available to a tenant.

## Constraints<a name="section64211377173223"></a>

You can query only the network ID and label \(network name\). Other fields are all null.

## URI<a name="section51121191165259"></a>

GET /v2/\{project\_id\}/os-networks

GET /v2.1/\{project\_id\}/os-networks

[Table 1](#table60562285165259)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table60562285165259"></a>
<table><thead align="left"><tr id="row4861884165259"><th class="cellrowborder" valign="top" width="16.79%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.18%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.03%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row63809876165259"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="p1217433165259"><a name="p1217433165259"></a><a name="p1217433165259"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.18%" headers="mcps1.2.4.1.2 "><p id="p31503226165259"><a name="p31503226165259"></a><a name="p31503226165259"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.03%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section8194118165259"></a>

None

## Response<a name="section58140617165259"></a>

[Table 2](#table50321718145545)  describes the response parameters.

**Table  2**  Response parameters

<a name="table50321718145545"></a>
<table><thead align="left"><tr id="row4713958145545"><th class="cellrowborder" valign="top" width="18.5%" id="mcps1.2.5.1.1"><p id="p46286352145545"><a name="p46286352145545"></a><a name="p46286352145545"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.8%" id="mcps1.2.5.1.2"><p id="p1721837202111"><a name="p1721837202111"></a><a name="p1721837202111"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.94%" id="mcps1.2.5.1.3"><p id="p58207059145545"><a name="p58207059145545"></a><a name="p58207059145545"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="43.76%" id="mcps1.2.5.1.4"><p id="p47079489145545"><a name="p47079489145545"></a><a name="p47079489145545"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row21062221145545"><td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.2.5.1.1 "><p id="p28318377145545"><a name="p28318377145545"></a><a name="p28318377145545"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.5.1.2 "><p id="p921203715216"><a name="p921203715216"></a><a name="p921203715216"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.94%" headers="mcps1.2.5.1.3 "><p id="p12087168145545"><a name="p12087168145545"></a><a name="p12087168145545"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.5.1.4 "><p id="p48345797145545"><a name="p48345797145545"></a><a name="p48345797145545"></a>Specifies the network ID in UUID format.</p>
</td>
</tr>
<tr id="row32458994145545"><td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.2.5.1.1 "><p id="p11932824145545"><a name="p11932824145545"></a><a name="p11932824145545"></a>label</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.5.1.2 "><p id="p1321337152117"><a name="p1321337152117"></a><a name="p1321337152117"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.94%" headers="mcps1.2.5.1.3 "><p id="p27034687145545"><a name="p27034687145545"></a><a name="p27034687145545"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.5.1.4 "><p id="p5856430145545"><a name="p5856430145545"></a><a name="p5856430145545"></a>Specifies the network name.</p>
</td>
</tr>
<tr id="row52707876145545"><td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.2.5.1.1 "><p id="p41479552145545"><a name="p41479552145545"></a><a name="p41479552145545"></a>broadcast</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.5.1.2 "><p id="p421837132116"><a name="p421837132116"></a><a name="p421837132116"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.94%" headers="mcps1.2.5.1.3 "><p id="p4400512145545"><a name="p4400512145545"></a><a name="p4400512145545"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.5.1.4 "><p id="p14948749145545"><a name="p14948749145545"></a><a name="p14948749145545"></a>The value can only be null.</p>
</td>
</tr>
<tr id="row321021145545"><td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.2.5.1.1 "><p id="p26002760145545"><a name="p26002760145545"></a><a name="p26002760145545"></a>cidr</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.5.1.2 "><p id="p182183792112"><a name="p182183792112"></a><a name="p182183792112"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.94%" headers="mcps1.2.5.1.3 "><p id="p25848828145545"><a name="p25848828145545"></a><a name="p25848828145545"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.5.1.4 "><p id="p10061500145545"><a name="p10061500145545"></a><a name="p10061500145545"></a>The value can only be null.</p>
</td>
</tr>
<tr id="row23444639145545"><td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.2.5.1.1 "><p id="p19967587145545"><a name="p19967587145545"></a><a name="p19967587145545"></a>cidr_v6</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.5.1.2 "><p id="p9211337162114"><a name="p9211337162114"></a><a name="p9211337162114"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.94%" headers="mcps1.2.5.1.3 "><p id="p6761844145545"><a name="p6761844145545"></a><a name="p6761844145545"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.5.1.4 "><p id="p5499802145545"><a name="p5499802145545"></a><a name="p5499802145545"></a>The value can only be null.</p>
</td>
</tr>
<tr id="row49498225145545"><td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.2.5.1.1 "><p id="p49933321145545"><a name="p49933321145545"></a><a name="p49933321145545"></a>dns1</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.5.1.2 "><p id="p162117374210"><a name="p162117374210"></a><a name="p162117374210"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.94%" headers="mcps1.2.5.1.3 "><p id="p18067185145545"><a name="p18067185145545"></a><a name="p18067185145545"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.5.1.4 "><p id="p24548306145545"><a name="p24548306145545"></a><a name="p24548306145545"></a>The value can only be null.</p>
</td>
</tr>
<tr id="row19608166145545"><td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.2.5.1.1 "><p id="p44757627145545"><a name="p44757627145545"></a><a name="p44757627145545"></a>dns2</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.5.1.2 "><p id="p521153713218"><a name="p521153713218"></a><a name="p521153713218"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.94%" headers="mcps1.2.5.1.3 "><p id="p1489156145545"><a name="p1489156145545"></a><a name="p1489156145545"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.5.1.4 "><p id="p39570324145545"><a name="p39570324145545"></a><a name="p39570324145545"></a>The value can only be null.</p>
</td>
</tr>
<tr id="row20588598145545"><td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.2.5.1.1 "><p id="p57063746145545"><a name="p57063746145545"></a><a name="p57063746145545"></a>gateway</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.5.1.2 "><p id="p1221203792116"><a name="p1221203792116"></a><a name="p1221203792116"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.94%" headers="mcps1.2.5.1.3 "><p id="p58760710145545"><a name="p58760710145545"></a><a name="p58760710145545"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.5.1.4 "><p id="p55709145145545"><a name="p55709145145545"></a><a name="p55709145145545"></a>The value can only be null.</p>
</td>
</tr>
<tr id="row31620258145545"><td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.2.5.1.1 "><p id="p11104111145545"><a name="p11104111145545"></a><a name="p11104111145545"></a>gateway_v6</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.5.1.2 "><p id="p2211837112119"><a name="p2211837112119"></a><a name="p2211837112119"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.94%" headers="mcps1.2.5.1.3 "><p id="p27017817145545"><a name="p27017817145545"></a><a name="p27017817145545"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.5.1.4 "><p id="p29389986145545"><a name="p29389986145545"></a><a name="p29389986145545"></a>The value can only be null.</p>
</td>
</tr>
<tr id="row63183283145545"><td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.2.5.1.1 "><p id="p17572316145545"><a name="p17572316145545"></a><a name="p17572316145545"></a>netmask</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.5.1.2 "><p id="p13215379215"><a name="p13215379215"></a><a name="p13215379215"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.94%" headers="mcps1.2.5.1.3 "><p id="p14071461145545"><a name="p14071461145545"></a><a name="p14071461145545"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.5.1.4 "><p id="p48167736145545"><a name="p48167736145545"></a><a name="p48167736145545"></a>The value can only be null.</p>
</td>
</tr>
<tr id="row30856442145545"><td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.2.5.1.1 "><p id="p16343912145545"><a name="p16343912145545"></a><a name="p16343912145545"></a>netmask_v6</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.5.1.2 "><p id="p192143713217"><a name="p192143713217"></a><a name="p192143713217"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.94%" headers="mcps1.2.5.1.3 "><p id="p48788506145545"><a name="p48788506145545"></a><a name="p48788506145545"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.5.1.4 "><p id="p59220588145545"><a name="p59220588145545"></a><a name="p59220588145545"></a>The value can only be null.</p>
</td>
</tr>
<tr id="row63223249145545"><td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.2.5.1.1 "><p id="p20809534145545"><a name="p20809534145545"></a><a name="p20809534145545"></a>bridge</p>
</td>
<td class="cellrowborder" valign="top" width="18.8%" headers="mcps1.2.5.1.2 "><p id="p1621237102117"><a name="p1621237102117"></a><a name="p1621237102117"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.94%" headers="mcps1.2.5.1.3 "><p id="p7850675145545"><a name="p7850675145545"></a><a name="p7850675145545"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.76%" headers="mcps1.2.5.1.4 "><p id="p35784407145545"><a name="p35784407145545"></a><a name="p35784407145545"></a>The value is fixed to be null and is in UUID format.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section187060519134"></a>

```
GET https://{endpoint}/v2/{project_id}/os-networks
GET https://{endpoint}/v2.1/{project_id}/os-networks
```

## Example Response<a name="section391213571394"></a>

```
{
    "networks": [
        {
            "id": "04468f37-500a-4a80-88da-af823e7a1d6c",
            "cidr_v6": null,
            "gateway": null,
            "label": "network_demo1",
            "broadcast": null,
            "netmask": null,
            "cidr": null,
            "dns2": null,
            "gateway_v6": null,
            "netmask_v6": null,
            "dns1": null
        },
        {
            "id": "1fcff959-21d0-4ba8-976a-974cb564c977",
            "cidr_v6": null,
            "gateway": null,
            "label": "network_demo2",
            "broadcast": null,
            "netmask": null,
            "cidr": null,
            "dns2": null,
            "gateway_v6": null,
            "netmask_v6": null,
            "dns1": null
        }
    ]
}
```

## Returned Values<a name="section38817202165259"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


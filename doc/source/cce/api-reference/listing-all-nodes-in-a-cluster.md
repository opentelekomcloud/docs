# Listing All Nodes in a Cluster<a name="cce_02_0244"></a>

## Function<a name="section1686113493165"></a>

This API is used to obtain details about all nodes in a cluster with a specified cluster ID.

## URI<a name="section8403243161416"></a>

GET /api/v3/projects/\{project\_id\}/clusters/\{cluster\_id\}/nodes

[Table 1](#table2027961241820)  describes the parameters of the API.

**Table  1**  Parameter description

<a name="table2027961241820"></a>
<table><thead align="left"><tr id="row122809120186"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p91421758131813"><a name="p91421758131813"></a><a name="p91421758131813"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.97%" id="mcps1.2.4.1.2"><p id="p101421758131816"><a name="p101421758131816"></a><a name="p101421758131816"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="63.029999999999994%" id="mcps1.2.4.1.3"><p id="p19143115818187"><a name="p19143115818187"></a><a name="p19143115818187"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row32801312121810"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p1714415589184"><a name="p1714415589184"></a><a name="p1714415589184"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.97%" headers="mcps1.2.4.1.2 "><p id="p814518580186"><a name="p814518580186"></a><a name="p814518580186"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="63.029999999999994%" headers="mcps1.2.4.1.3 "><p id="p5145175891811"><a name="p5145175891811"></a><a name="p5145175891811"></a>Project ID. For details about how to obtain the project ID, see <a href="how-to-obtain-parameters-in-the-api-uri.md">How to Obtain Parameters in the API URI</a>.</p>
</td>
</tr>
<tr id="row1649094164612"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p749015414462"><a name="p749015414462"></a><a name="p749015414462"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.97%" headers="mcps1.2.4.1.2 "><p id="p1849084134615"><a name="p1849084134615"></a><a name="p1849084134615"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="63.029999999999994%" headers="mcps1.2.4.1.3 "><p id="p8491141114617"><a name="p8491141114617"></a><a name="p8491141114617"></a>Cluster ID. For details about how to obtain the cluster ID, see <a href="how-to-obtain-parameters-in-the-api-uri.md">How to Obtain Parameters in the API URI</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section947084713911"></a>

**Request parameters**:

[Table 2](#table13638079467)  describes the request parameters.

**Table  2**  Parameters in the request header

<a name="table13638079467"></a>
<table><thead align="left"><tr id="en-us_topic_0102499074_row55001954122614"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="en-us_topic_0102499074_p115009545264"><a name="en-us_topic_0102499074_p115009545264"></a><a name="en-us_topic_0102499074_p115009545264"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="en-us_topic_0102499074_p175001547265"><a name="en-us_topic_0102499074_p175001547265"></a><a name="en-us_topic_0102499074_p175001547265"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.2.4.1.3"><p id="en-us_topic_0102499074_p16500154162611"><a name="en-us_topic_0102499074_p16500154162611"></a><a name="en-us_topic_0102499074_p16500154162611"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0102499074_row199801811203412"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0102499074_p69808112344"><a name="en-us_topic_0102499074_p69808112344"></a><a name="en-us_topic_0102499074_p69808112344"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0102499074_p3980111103414"><a name="en-us_topic_0102499074_p3980111103414"></a><a name="en-us_topic_0102499074_p3980111103414"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0102499074_p169801011203416"><a name="en-us_topic_0102499074_p169801011203416"></a><a name="en-us_topic_0102499074_p169801011203416"></a>Message body type (format). Possible values:</p>
<a name="en-us_topic_0102499074_ul7385444163617"></a><a name="en-us_topic_0102499074_ul7385444163617"></a><ul id="en-us_topic_0102499074_ul7385444163617"><li>application/json;charset=utf-8</li><li>application/json</li></ul>
</td>
</tr>
<tr id="en-us_topic_0102499074_row3500125412260"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0102499074_p105001654202618"><a name="en-us_topic_0102499074_p105001654202618"></a><a name="en-us_topic_0102499074_p105001654202618"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0102499074_p20500954182618"><a name="en-us_topic_0102499074_p20500954182618"></a><a name="en-us_topic_0102499074_p20500954182618"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="p18824197845"><a name="p18824197845"></a><a name="p18824197845"></a>Requests for calling an API can be authenticated using either a token or AK/SK. If token-based authentication is used, this parameter is mandatory and must be set to a user token. For details on how to obtain a user token, see <a href="api-usage-guidelines.md">API Usage Guidelines</a>.</p>
</td>
</tr>
</tbody>
</table>

**Example request**:

N/A

## Response<a name="section61819725020"></a>

**Response parameters**:

[Table 3](#en-us_topic_0079616779_en-us_topic_0079614912_ref458774242)  describes the response parameters.

**Table  3**  Response parameters

<a name="en-us_topic_0079616779_en-us_topic_0079614912_ref458774242"></a>
<table><thead align="left"><tr id="en-us_topic_0079616779_en-us_topic_0079614912_row38450714"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="en-us_topic_0079616779_en-us_topic_0079614912_p27500114"><a name="en-us_topic_0079616779_en-us_topic_0079614912_p27500114"></a><a name="en-us_topic_0079616779_en-us_topic_0079614912_p27500114"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p1654581422214"><a name="p1654581422214"></a><a name="p1654581422214"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.4.1.3"><p id="p125451914132219"><a name="p125451914132219"></a><a name="p125451914132219"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079616779_en-us_topic_0079614912_row48220637"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p44731858185518"><a name="p44731858185518"></a><a name="p44731858185518"></a>kind</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p57145269553"><a name="p57145269553"></a><a name="p57145269553"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p12712326175517"><a name="p12712326175517"></a><a name="p12712326175517"></a>API type. The value is fixed to <strong id="b1228811372347"><a name="b1228811372347"></a><a name="b1228811372347"></a>List</strong>.</p>
</td>
</tr>
<tr id="row1698782994313"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p144741580551"><a name="p144741580551"></a><a name="p144741580551"></a>apiVersion</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p6707526185513"><a name="p6707526185513"></a><a name="p6707526185513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p1770492695518"><a name="p1770492695518"></a><a name="p1770492695518"></a>API version. The value is fixed at <strong id="b2014526754165210"><a name="b2014526754165210"></a><a name="b2014526754165210"></a>v3</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0079616779_en-us_topic_0079614912_row28135397"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p9274125074915"><a name="p9274125074915"></a><a name="p9274125074915"></a>items</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p861959163213"><a name="p861959163213"></a><a name="p861959163213"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p256924217343"><a name="p256924217343"></a><a name="p256924217343"></a>A list of details for all nodes in the current cluster. You can filter nodes by <strong id="b1799063512516"><a name="b1799063512516"></a><a name="b1799063512516"></a>items.metadata.name</strong>. For more information, see <a href="reading-a-specified-node.md#en-us_topic_0079616779_en-us_topic_0079614912_ref458774242">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Example response**:

```
{
  "kind": "List",
  "apiVersion": "v3",
  "items": [
    {
      "kind": "Node",
      "apiversion": "v3",
      "metadata": {
        "name": "myhost",
        "uid": "4d1ecb2c-229a-11e8-9c75-0255ac100ceb",
        "creationTimestamp": "2018-08-02 07:37:24.005071325 +0000 UTC",
        "updateTimestamp": "2018-08-02 07:44:04.965500815 +0000 UTC",
        "annotations": {
         "kubernetes.io/node-pool.id": "eu-de-01#s1.medium#EulerOS 2.5"        
        }
      },
      "spec": {
        "flavor": "s1.medium",
        "az": "eu-de-01",
        "os": "EulerOS 2.5",
        "login": {
          "sshKey": "KeyPair-demo"
        },
        "rootVolume": {
          "volumetype": "SATA",
          "size": 40
        },
        "dataVolumes": [
          {
            "volumetype": "SATA",
            "size": 100
          }
        ],
        "publicIP": {
          "eip": {
            "bandwidth": {}
          }
        }
      },
      "status": {
        "phase": "Active",
        "serverId": "456789abc-9368-46f3-8f29-d1a95622a568",
        "publicIP": "10.34.56.78",
        "privateIP": "192.168.1.23"
      }
    }
  ]
}
```

## Status Code<a name="s50f1049a6a4d404c895cf636eb8f3bf1"></a>

[Table 4](#en-us_topic_0079614900_table46761928)  describes the status code of this API.

**Table  4**  Status code

<a name="en-us_topic_0079614900_table46761928"></a>
<table><thead align="left"><tr id="en-us_topic_0079614900_row33254664"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p55616028205955"><a name="p55616028205955"></a><a name="p55616028205955"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p8604418205955"><a name="p8604418205955"></a><a name="p8604418205955"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079614900_row41084259"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0079614900_p39490674"><a name="en-us_topic_0079614900_p39490674"></a><a name="en-us_topic_0079614900_p39490674"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0079614900_p44628050"><a name="en-us_topic_0079614900_p44628050"></a><a name="en-us_topic_0079614900_p44628050"></a>Information about all the nodes in the specified cluster is successfully obtained.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Code](status-code.md).


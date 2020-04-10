# Updating a Specified Node<a name="cce_02_0245"></a>

## Function<a name="section1686113493165"></a>

This API is used to update information about a specified node.

## URI<a name="section8403243161416"></a>

PUT /api/v3/projects/\{project\_id\}/clusters/\{cluster\_id\}/nodes/\{node\_id\}

[Table 1](#table2027961241820)  describes the parameters of the API.

**Table  1**  Parameter description

<a name="table2027961241820"></a>
<table><thead align="left"><tr id="row122809120186"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p91421758131813"><a name="p91421758131813"></a><a name="p91421758131813"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.53%" id="mcps1.2.4.1.2"><p id="p101421758131816"><a name="p101421758131816"></a><a name="p101421758131816"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="64.47%" id="mcps1.2.4.1.3"><p id="p19143115818187"><a name="p19143115818187"></a><a name="p19143115818187"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row32801312121810"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p1714415589184"><a name="p1714415589184"></a><a name="p1714415589184"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.53%" headers="mcps1.2.4.1.2 "><p id="p814518580186"><a name="p814518580186"></a><a name="p814518580186"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="64.47%" headers="mcps1.2.4.1.3 "><p id="p5145175891811"><a name="p5145175891811"></a><a name="p5145175891811"></a>Project ID. For details about how to obtain the project ID, see <a href="how-to-obtain-parameters-in-the-api-uri.md">How to Obtain Parameters in the API URI</a>.</p>
</td>
</tr>
<tr id="row1649094164612"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p749015414462"><a name="p749015414462"></a><a name="p749015414462"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.53%" headers="mcps1.2.4.1.2 "><p id="p1849084134615"><a name="p1849084134615"></a><a name="p1849084134615"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="64.47%" headers="mcps1.2.4.1.3 "><p id="p8491141114617"><a name="p8491141114617"></a><a name="p8491141114617"></a>Cluster ID. For details about how to obtain the cluster ID, see <a href="how-to-obtain-parameters-in-the-api-uri.md">How to Obtain Parameters in the API URI</a>.</p>
</td>
</tr>
<tr id="row256414484464"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p1856454818463"><a name="p1856454818463"></a><a name="p1856454818463"></a>node_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.53%" headers="mcps1.2.4.1.2 "><p id="p2564134816468"><a name="p2564134816468"></a><a name="p2564134816468"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="64.47%" headers="mcps1.2.4.1.3 "><p id="p0564048184619"><a name="p0564048184619"></a><a name="p0564048184619"></a>Cluster ID. For details about how to obtain the cluster ID, see <a href="how-to-obtain-parameters-in-the-api-uri.md">How to Obtain Parameters in the API URI</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section947084713911"></a>

**Request parameters**:

[Table 2](#table34821245101211)  and  [Table 3](#table185578532300)  describe the request parameters.

**Table  2**  Parameters in the request header

<a name="table34821245101211"></a>
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

**Table  3**  Parameters in the request body

<a name="table185578532300"></a>
<table><thead align="left"><tr id="row16557175343012"><th class="cellrowborder" valign="top" width="19.607843137254903%" id="mcps1.2.5.1.1"><p id="p125571753143013"><a name="p125571753143013"></a><a name="p125571753143013"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.313725490196077%" id="mcps1.2.5.1.2"><p id="p12512124873118"><a name="p12512124873118"></a><a name="p12512124873118"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="19.921568627450977%" id="mcps1.2.5.1.3"><p id="p15574534307"><a name="p15574534307"></a><a name="p15574534307"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="42.15686274509804%" id="mcps1.2.5.1.4"><p id="p15557653163010"><a name="p15557653163010"></a><a name="p15557653163010"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row10557135318308"><td class="cellrowborder" valign="top" width="19.607843137254903%" headers="mcps1.2.5.1.1 "><p id="p1655795323010"><a name="p1655795323010"></a><a name="p1655795323010"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="18.313725490196077%" headers="mcps1.2.5.1.2 "><p id="p6512184811310"><a name="p6512184811310"></a><a name="p6512184811310"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="19.921568627450977%" headers="mcps1.2.5.1.3 "><p id="p845414161333"><a name="p845414161333"></a><a name="p845414161333"></a><a href="#table915314146321">metadata</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="42.15686274509804%" headers="mcps1.2.5.1.4 "><p id="p555711530309"><a name="p555711530309"></a><a name="p555711530309"></a>Node's metadata, which is a collection of attributes.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Data structure of the  **metadata**  field

<a name="table915314146321"></a>
<table><thead align="left"><tr id="row8168191414320"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="p2168121417329"><a name="p2168121417329"></a><a name="p2168121417329"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.68%" id="mcps1.2.5.1.2"><p id="p13168181463219"><a name="p13168181463219"></a><a name="p13168181463219"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.32%" id="mcps1.2.5.1.3"><p id="p31681148326"><a name="p31681148326"></a><a name="p31681148326"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="43%" id="mcps1.2.5.1.4"><p id="p1116811148325"><a name="p1116811148325"></a><a name="p1116811148325"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row11168614103217"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="p161689145326"><a name="p161689145326"></a><a name="p161689145326"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="18.68%" headers="mcps1.2.5.1.2 "><p id="p17168131415329"><a name="p17168131415329"></a><a name="p17168131415329"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.32%" headers="mcps1.2.5.1.3 "><p id="p111689149323"><a name="p111689149323"></a><a name="p111689149323"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.4 "><p id="p8168181423215"><a name="p8168181423215"></a><a name="p8168181423215"></a>Node name. After the node name is changed, the ECS name (VM name) is changed accordingly.</p>
</td>
</tr>
</tbody>
</table>

**Example request**:

```
{
    "metadata": {
        "name": "new-hostname"
    }
}
```

## Response<a name="section61819725020"></a>

**Response parameters**:

For the description of the response parameters, see  [Table 3](reading-a-specified-node.md#en-us_topic_0079616779_en-us_topic_0079614912_ref458774242).

**Example response**:

```
{
  "kind": "Node",
  "apiVersion": "v3",
  "metadata": {
    "name": "new-hostname",
    "uid": "4d1ecb2c-229a-11e8-9c75-0255ac100ceb",
    "creationTimestamp": " 2017-08-20T21:11:09Z",
    "updateTimestamp": "2017-08-20T21:11:09Z",
    "annotations": {
      "kubernetes.io/node-pool.id": "eu-de-01#s1.medium#EulerOS 2.5"
    }
  },
  "spec": {
    "flavor": "s1.medium",
    "az": "eu-de-01",
    "os": "EulerOS 2.5",
    "login": {
      "sshKey": "KeyPair-demo",
    },
    "rootVolume": {
      "volumeType": "SATA",
      "diskSize": 40
    },
    "dataVolumes": [
      {
        "volumeType": "SATA",
        "diskSize": 100
      }
    ],
    "publicIP": {
      "eip": {
      }
    },
      "nodeNicSpec": {
          "primaryNic": {
              "subnetId": "1756f773-5389-4c55-b94f-9ba933f678f6"
          }
      },
      "billingMode": 0
  },
  "status": {
    "phase": "Active",
    "serverId": "456789abc-9368-46f3-8f29-d1a95622a568",
    "publicIP": "10.34.56.78",
    "privateIP": "192.168.1.23"
  }
}
```

## Status Code<a name="s50f1049a6a4d404c895cf636eb8f3bf1"></a>

[Table 5](#en-us_topic_0079614900_table46761928)  describes the status code of this API.

**Table  5**  Status code

<a name="en-us_topic_0079614900_table46761928"></a>
<table><thead align="left"><tr id="en-us_topic_0079614900_row33254664"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p55616028205955"><a name="p55616028205955"></a><a name="p55616028205955"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p8604418205955"><a name="p8604418205955"></a><a name="p8604418205955"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079614900_row41084259"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0079614900_p39490674"><a name="en-us_topic_0079614900_p39490674"></a><a name="en-us_topic_0079614900_p39490674"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0079614900_p44628050"><a name="en-us_topic_0079614900_p44628050"></a><a name="en-us_topic_0079614900_p44628050"></a>Information about the specified node is successfully updated.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Code](status-code.md).


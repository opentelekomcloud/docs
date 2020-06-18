# Deleting a Node<a name="cce_02_0246"></a>

## Function<a name="section1686113493165"></a>

This API is used to delete a specified node.

## URI<a name="section8403243161416"></a>

DELETE /api/v3/projects/\{project\_id\}/clusters/\{cluster\_id\}/nodes/\{node\_id\}

[Table 1](#table2027961241820)  describes the parameters of the API.

**Table  1**  Description

<a name="table2027961241820"></a>
<table><thead align="left"><tr id="row122809120186"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p91421758131813"><a name="p91421758131813"></a><a name="p91421758131813"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p101421758131816"><a name="p101421758131816"></a><a name="p101421758131816"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.2.4.1.3"><p id="p19143115818187"><a name="p19143115818187"></a><a name="p19143115818187"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row32801312121810"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p1714415589184"><a name="p1714415589184"></a><a name="p1714415589184"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p814518580186"><a name="p814518580186"></a><a name="p814518580186"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p5145175891811"><a name="p5145175891811"></a><a name="p5145175891811"></a>Project ID. For details about how to obtain the project ID, see <a href="how-to-obtain-parameters-in-the-api-uri.md">How to Obtain Parameters in the API URI</a>.</p>
</td>
</tr>
<tr id="row1649094164612"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p749015414462"><a name="p749015414462"></a><a name="p749015414462"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p1849084134615"><a name="p1849084134615"></a><a name="p1849084134615"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p8491141114617"><a name="p8491141114617"></a><a name="p8491141114617"></a>Cluster ID. For details about how to obtain the cluster ID, see <a href="how-to-obtain-parameters-in-the-api-uri.md">How to Obtain Parameters in the API URI</a>.</p>
</td>
</tr>
<tr id="row256414484464"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p1856454818463"><a name="p1856454818463"></a><a name="p1856454818463"></a>node_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p2564134816468"><a name="p2564134816468"></a><a name="p2564134816468"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.2.4.1.3 "><p id="p0564048184619"><a name="p0564048184619"></a><a name="p0564048184619"></a>Cluster ID. For details about how to obtain the cluster ID, see <a href="how-to-obtain-parameters-in-the-api-uri.md">How to Obtain Parameters in the API URI</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section947084713911"></a>

**Request parameters**:

[Table 2](#table7347141814502)  describes the request parameters.

**Table  2**  Parameters in the request header

<a name="table7347141814502"></a>
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
<tbody><tr id="en-us_topic_0079616779_en-us_topic_0079614912_row48220637"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p108391536181311"><a name="p108391536181311"></a><a name="p108391536181311"></a>kind</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p1056311621716"><a name="p1056311621716"></a><a name="p1056311621716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p75781816181715"><a name="p75781816181715"></a><a name="p75781816181715"></a>API type. The value is fixed at <strong id="b64991835135317"><a name="b64991835135317"></a><a name="b64991835135317"></a>Node</strong> and cannot be changed.</p>
</td>
</tr>
<tr id="row1698782994313"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1785493610136"><a name="p1785493610136"></a><a name="p1785493610136"></a>apiVersion</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p757801610179"><a name="p757801610179"></a><a name="p757801610179"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p12578616151718"><a name="p12578616151718"></a><a name="p12578616151718"></a>API version. The value is fixed at <strong id="b462065805314"><a name="b462065805314"></a><a name="b462065805314"></a>v3</strong> and cannot be changed.</p>
</td>
</tr>
<tr id="en-us_topic_0079616779_en-us_topic_0079614912_row28135397"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1185493615135"><a name="p1185493615135"></a><a name="p1185493615135"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p2023911312345"><a name="p2023911312345"></a><a name="p2023911312345"></a><a href="reading-a-specified-node.md#table669019286188">metadata</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p10343195011177"><a name="p10343195011177"></a><a name="p10343195011177"></a>Node's metadata, which is a collection of attributes.</p>
</td>
</tr>
<tr id="row066718152447"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p6532732161518"><a name="p6532732161518"></a><a name="p6532732161518"></a>spec</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p5359350141715"><a name="p5359350141715"></a><a name="p5359350141715"></a><a href="creating-a-node.md#table13949117115810">spec</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p173598507179"><a name="p173598507179"></a><a name="p173598507179"></a>Detailed description of the node targeted by this API. CCE creates or updates objects by defining or updating its spec.</p>
</td>
</tr>
<tr id="row3542719114415"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p15204203610152"><a name="p15204203610152"></a><a name="p15204203610152"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p1920413611513"><a name="p1920413611513"></a><a name="p1920413611513"></a><a href="#table1741714540447">status</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p9204133661512"><a name="p9204133661512"></a><a name="p9204133661512"></a>Node status and jobID of the node deletion job.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Data structure of the  **status**  field

<a name="table1741714540447"></a>
<table><thead align="left"><tr id="row541718548449"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p9996145924411"><a name="p9996145924411"></a><a name="p9996145924411"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p1996175915440"><a name="p1996175915440"></a><a name="p1996175915440"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.4.1.3"><p id="p19961459194419"><a name="p19961459194419"></a><a name="p19961459194419"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3417125410440"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p16749153410220"><a name="p16749153410220"></a><a name="p16749153410220"></a>phase</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p4749193482216"><a name="p4749193482216"></a><a name="p4749193482216"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p18842161515251"><a name="p18842161515251"></a><a name="p18842161515251"></a>Node status.</p>
<a name="ul1920482010251"></a><a name="ul1920482010251"></a><ul id="ul1920482010251"><li><strong id="b17438244165615"><a name="b17438244165615"></a><a name="b17438244165615"></a>Build</strong>: The VM that hosts the node is being created.</li><li><strong id="b1734015477560"><a name="b1734015477560"></a><a name="b1734015477560"></a>Active</strong>: The node is ready for use.</li><li><strong id="b169471348175615"><a name="b169471348175615"></a><a name="b169471348175615"></a>Abnormal</strong>: The node is unready for use.</li><li><strong id="b734412542561"><a name="b734412542561"></a><a name="b734412542561"></a>Deleting</strong>: The node is being deleted.</li><li><strong id="b1877845645616"><a name="b1877845645616"></a><a name="b1877845645616"></a>Installing</strong>: The node is being installed.</li><li><strong id="b7232759145619"><a name="b7232759145619"></a><a name="b7232759145619"></a>Upgrading</strong>: The node is being upgraded.</li></ul>
</td>
</tr>
<tr id="row51175493251"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p18117104902515"><a name="p18117104902515"></a><a name="p18117104902515"></a>jobID</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p111718498256"><a name="p111718498256"></a><a name="p111718498256"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p1774918349229"><a name="p1774918349229"></a><a name="p1774918349229"></a>ID of the node deletion job. You can query job progress by job ID to keep updated on node deletion progress.</p>
</td>
</tr>
<tr id="row7404113715584"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p114042037165812"><a name="p114042037165812"></a><a name="p114042037165812"></a>serverId</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p7404237155818"><a name="p7404237155818"></a><a name="p7404237155818"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p11404237185813"><a name="p11404237185813"></a><a name="p11404237185813"></a>ID of the ECS where the node resides.</p>
</td>
</tr>
<tr id="row19497124014586"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p18497104035812"><a name="p18497104035812"></a><a name="p18497104035812"></a>publicIP</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p449719407586"><a name="p449719407586"></a><a name="p449719407586"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p12497204035815"><a name="p12497204035815"></a><a name="p12497204035815"></a>EIP used by the node to access public networks.</p>
</td>
</tr>
<tr id="row122016432582"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1020154375816"><a name="p1020154375816"></a><a name="p1020154375816"></a>privateIP</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p1220134320585"><a name="p1220134320585"></a><a name="p1220134320585"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p17201143195812"><a name="p17201143195812"></a><a name="p17201143195812"></a>Private IP address used by the node to communicate with other nodes in the same VPC as the current cluster.</p>
</td>
</tr>
</tbody>
</table>

**Example response**:

```
{
    "kind": "Node",
    "apiVersion": "v3",
    "metadata": {
        "name": "new-hostname",
        "uid": "cc697ad9-9563-11e8-8ea7-0255ac106311",
        "creationTimestamp": "2018-08-01 08:20:49.944664515 +0000 UTC",
        "updateTimestamp": "2018-08-01 09:20:05.644032347 +0000 UTC",
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
        "jobID": "661f6f7d-956c-11e8-a916-0255ac10575d",
        "serverId": "5b504f8d-33f1-4ab7-a600-b62dac967d72",
        "privateIP": "192.168.0.69",
        "publicIP": "10.154.194.59"
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
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0079614900_p44628050"><a name="en-us_topic_0079614900_p44628050"></a><a name="en-us_topic_0079614900_p44628050"></a>The job for deleting the node is successfully delivered.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Code](status-code.md).


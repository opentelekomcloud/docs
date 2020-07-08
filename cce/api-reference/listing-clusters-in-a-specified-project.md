# Listing Clusters in a Specified Project<a name="cce_02_0239"></a>

## Function<a name="section1686113493165"></a>

This API is used to obtain details about all clusters in a specified project.

## URI<a name="section8403243161416"></a>

GET /api/v3/projects/\{project\_id\}/clusters

[Table 1](#table2027961241820)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="table2027961241820"></a>
<table><thead align="left"><tr id="row122809120186"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p91421758131813"><a name="p91421758131813"></a><a name="p91421758131813"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.4.1.2"><p id="p101421758131816"><a name="p101421758131816"></a><a name="p101421758131816"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.2.4.1.3"><p id="p19143115818187"><a name="p19143115818187"></a><a name="p19143115818187"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row32801312121810"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p1714415589184"><a name="p1714415589184"></a><a name="p1714415589184"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p814518580186"><a name="p814518580186"></a><a name="p814518580186"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.4.1.3 "><p id="p5145175891811"><a name="p5145175891811"></a><a name="p5145175891811"></a>Project ID. For details on how to obtain the project ID, see <a href="how-to-obtain-parameters-in-the-api-uri.md">How to Obtain Parameters in the API URI</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section947084713911"></a>

**Request parameters**:

[Table 2](#table538113720514)  lists the request parameters.

**Table  2**  Parameters in the request header

<a name="table538113720514"></a>
<table><thead align="left"><tr id="en-us_topic_0199164459_row55001954122614"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="en-us_topic_0199164459_p115009545264"><a name="en-us_topic_0199164459_p115009545264"></a><a name="en-us_topic_0199164459_p115009545264"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="en-us_topic_0199164459_p175001547265"><a name="en-us_topic_0199164459_p175001547265"></a><a name="en-us_topic_0199164459_p175001547265"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.2.4.1.3"><p id="en-us_topic_0199164459_p16500154162611"><a name="en-us_topic_0199164459_p16500154162611"></a><a name="en-us_topic_0199164459_p16500154162611"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0199164459_row199801811203412"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0199164459_p69808112344"><a name="en-us_topic_0199164459_p69808112344"></a><a name="en-us_topic_0199164459_p69808112344"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0199164459_p3980111103414"><a name="en-us_topic_0199164459_p3980111103414"></a><a name="en-us_topic_0199164459_p3980111103414"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0199164459_p169801011203416"><a name="en-us_topic_0199164459_p169801011203416"></a><a name="en-us_topic_0199164459_p169801011203416"></a>Message body type (format). Possible values:</p>
<a name="en-us_topic_0199164459_ul7385444163617"></a><a name="en-us_topic_0199164459_ul7385444163617"></a><ul id="en-us_topic_0199164459_ul7385444163617"><li>application/json;charset=utf-8</li><li>application/json</li></ul>
</td>
</tr>
<tr id="en-us_topic_0199164459_row3500125412260"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0199164459_p105001654202618"><a name="en-us_topic_0199164459_p105001654202618"></a><a name="en-us_topic_0199164459_p105001654202618"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0199164459_p20500954182618"><a name="en-us_topic_0199164459_p20500954182618"></a><a name="en-us_topic_0199164459_p20500954182618"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0199164459_p18824197845"><a name="en-us_topic_0199164459_p18824197845"></a><a name="en-us_topic_0199164459_p18824197845"></a>Requests for calling an API can be authenticated using either a token or AK/SK. If token-based authentication is used, this parameter is mandatory and must be set to a user token. For details on how to obtain a user token, see <a href="api-usage-guidelines.md">API Usage Guidelines</a>.</p>
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
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p12712326175517"><a name="p12712326175517"></a><a name="p12712326175517"></a>API type. The value is fixed at <strong id="b465594618519"><a name="b465594618519"></a><a name="b465594618519"></a>Cluster</strong> and cannot be changed.</p>
</td>
</tr>
<tr id="row1698782994313"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p144741580551"><a name="p144741580551"></a><a name="p144741580551"></a>apiVersion</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p6707526185513"><a name="p6707526185513"></a><a name="p6707526185513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p1770492695518"><a name="p1770492695518"></a><a name="p1770492695518"></a>API version. The value is fixed at <strong id="b1230117563513"><a name="b1230117563513"></a><a name="b1230117563513"></a>v3</strong> and cannot be changed.</p>
</td>
</tr>
<tr id="en-us_topic_0079616779_en-us_topic_0079614912_row28135397"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p92203252379"><a name="p92203252379"></a><a name="p92203252379"></a>items</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p121914251378"><a name="p121914251378"></a><a name="p121914251378"></a><a href="#table34052983203655">items</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p2955204118263"><a name="p2955204118263"></a><a name="p2955204118263"></a>A list of details for all clusters in the current project. You can filter clusters by <strong id="b396819375714"><a name="b396819375714"></a><a name="b396819375714"></a>items.metadata.name</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Data structure of the  **items**  field

<a name="table34052983203655"></a>
<table><thead align="left"><tr id="row73461713174118"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p183483137415"><a name="p183483137415"></a><a name="p183483137415"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="p935016137414"><a name="p935016137414"></a><a name="p935016137414"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47%" id="mcps1.2.4.1.3"><p id="p6353181334117"><a name="p6353181334117"></a><a name="p6353181334117"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row83577139411"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1236111131411"><a name="p1236111131411"></a><a name="p1236111131411"></a>kind</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p1536211364111"><a name="p1536211364111"></a><a name="p1536211364111"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p id="p83669139412"><a name="p83669139412"></a><a name="p83669139412"></a>API type. The value is fixed at <strong id="b195770401172"><a name="b195770401172"></a><a name="b195770401172"></a>Cluster</strong> and cannot be changed.</p>
</td>
</tr>
<tr id="row2367713184120"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p12369151310411"><a name="p12369151310411"></a><a name="p12369151310411"></a>apiVersion</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p93719131417"><a name="p93719131417"></a><a name="p93719131417"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p id="p19374121364119"><a name="p19374121364119"></a><a name="p19374121364119"></a>API version. The value is fixed at <strong id="b058785212714"><a name="b058785212714"></a><a name="b058785212714"></a>v3</strong> and cannot be changed.</p>
</td>
</tr>
<tr id="row13375413164113"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p73771813134111"><a name="p73771813134111"></a><a name="p73771813134111"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p2085818323259"><a name="p2085818323259"></a><a name="p2085818323259"></a><a href="creating-a-cluster.md#table669019286188">metadata</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p id="p8382151374115"><a name="p8382151374115"></a><a name="p8382151374115"></a>Cluster metadata, which is a collection of attributes.</p>
</td>
</tr>
<tr id="row5383813194112"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p1038501314417"><a name="p1038501314417"></a><a name="p1038501314417"></a>spec</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p28797454259"><a name="p28797454259"></a><a name="p28797454259"></a><a href="reading-a-specified-cluster.md#table1034041612134">spec</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p id="p19125441228"><a name="p19125441228"></a><a name="p19125441228"></a>Detailed description of the cluster targeted by this API. CCE creates or updates objects by defining or updating its spec.</p>
</td>
</tr>
<tr id="row2039216132419"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p203945139415"><a name="p203945139415"></a><a name="p203945139415"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p4469647122516"><a name="p4469647122516"></a><a name="p4469647122516"></a><a href="reading-a-specified-cluster.md#table6749834132215">status</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.3 "><p id="p339891394117"><a name="p339891394117"></a><a name="p339891394117"></a>Cluster status and jobID of the job that lists clusters in a specified project.</p>
</td>
</tr>
</tbody>
</table>

**Response example**:

```
{
    "kind": "Cluster",
    "apiVersion": "v3",
    "items": [
        {
            "kind": "Cluster",
            "apiVersion": "v3",
            "metadata": {
                "name": "mycluster",
                "uid": "4d1ecb2c-229a-11e8-9c75-0255ac100ceb",
                "creationTimestamp": "2020-02-02 03:48:58.968214406 +0000 UTC",
                "updateTimestamp": "2020-02-02 04:05:29.386391813 +0000 UTC"
            },
            "spec": {
                "type": "VirtualMachine",
                "flavor": "cce.s1.small",
                "version": "v1.15.6-r1",
                "description": "awesome cluster",
                "ipv6enable": false,
                "supportIstio": true,
                "hostNetwork": {
                    "vpc": "f0c12911-4fdb-4284-9230-7ffb0860826a",
                    "subnet": "ac274229-fd2e-4695-9f01-a0c1372b8006",
                    "SecurityGroup": "5da0b181-e0a2-4981-87ac-1681545cd666"
                },
                "containerNetwork": {
                    "mode": "overlay_l2",
                    "cidr": "172.16.0.0/16"
                },
                "eniNetwork": {},
                "authentication": {
                    "mode": "rbac",
                    "authenticatingProxy": {}
                },
                "billingMode": 0,
                "extendParam": {
                    "alpha.cce/fixPoolMask": "",
                    "kubernetes.io/cpuManagerPolicy": "",
                    "patchVersion": "",
                    "upgradefrom": ""
                },
                "kubernetesSvcIpRange": "10.247.0.0/16",
                "kubeProxyMode": "iptables"
            },
            "status": {
                "phase": "Available",
                "endpoints": [
                    {
                        "url": "https://192.168.0.61:5443",
                        "type": "Internal"
                    }
                ]
            }
        }
    ]
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
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0079614900_p44628050"><a name="en-us_topic_0079614900_p44628050"></a><a name="en-us_topic_0079614900_p44628050"></a>Information about clusters in the specified project is successfully obtained.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Code](status-code.md).


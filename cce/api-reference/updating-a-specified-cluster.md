# Updating a Specified Cluster<a name="cce_02_0240"></a>

## Function<a name="section1686113493165"></a>

This API is used to update information about a specified cluster.

## URI<a name="section8403243161416"></a>

PUT /api/v3/projects/\{project\_id\}/clusters/\{cluster\_id\}

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
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.4.1.3 "><p id="p5145175891811"><a name="p5145175891811"></a><a name="p5145175891811"></a>Project ID. For details about how to obtain the project ID, see <a href="how-to-obtain-parameters-in-the-api-uri.md">How to Obtain Parameters in the API URI</a>.</p>
</td>
</tr>
<tr id="row126417469411"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p5642046194113"><a name="p5642046194113"></a><a name="p5642046194113"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.4.1.2 "><p id="p146484634113"><a name="p146484634113"></a><a name="p146484634113"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.4.1.3 "><p id="p664164613418"><a name="p664164613418"></a><a name="p664164613418"></a>Cluster ID. For details about how to obtain the cluster ID, see <a href="how-to-obtain-parameters-in-the-api-uri.md">How to Obtain Parameters in the API URI</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section947084713911"></a>

**Request parameters**:

[Table 2](#table172831182919)  and  [Table 3](#table34052983203655)  describe the request parameters.

**Table  2**  Parameters in the request header

<a name="table172831182919"></a>
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

**Table  3**  Parameters in the request body

<a name="table34052983203655"></a>
<table><thead align="left"><tr id="row30254333203655"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.1"><p id="p34681881203655"><a name="p34681881203655"></a><a name="p34681881203655"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.2"><p id="p333122111014"><a name="p333122111014"></a><a name="p333122111014"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.5.1.3"><p id="p57769002203655"><a name="p57769002203655"></a><a name="p57769002203655"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.484848484848484%" id="mcps1.2.5.1.4"><p id="p58673482203655"><a name="p58673482203655"></a><a name="p58673482203655"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9619511127"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p4785161212"><a name="p4785161212"></a><a name="p4785161212"></a>spec</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p97205171219"><a name="p97205171219"></a><a name="p97205171219"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.3 "><p id="p32441816164615"><a name="p32441816164615"></a><a name="p32441816164615"></a><a href="#table1034041612134">spec</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p10785112129"><a name="p10785112129"></a><a name="p10785112129"></a>Detailed description of the cluster targeted by this API. CCE creates or updates objects by defining or updating its spec.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Data structure of the  **spec**  field

<a name="table1034041612134"></a>
<table><thead align="left"><tr id="row14348121616132"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.1"><p id="p133505167139"><a name="p133505167139"></a><a name="p133505167139"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.2"><p id="p6353201611319"><a name="p6353201611319"></a><a name="p6353201611319"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.5.1.3"><p id="p735501615139"><a name="p735501615139"></a><a name="p735501615139"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.484848484848484%" id="mcps1.2.5.1.4"><p id="p15357151631311"><a name="p15357151631311"></a><a name="p15357151631311"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row438141651319"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p1653144010196"><a name="p1653144010196"></a><a name="p1653144010196"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p9485133718193"><a name="p9485133718193"></a><a name="p9485133718193"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.3 "><p id="p65261417142217"><a name="p65261417142217"></a><a name="p65261417142217"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.484848484848484%" headers="mcps1.2.5.1.4 "><p id="p1318113472302"><a name="p1318113472302"></a><a name="p1318113472302"></a>Cluster description.</p>
</td>
</tr>
</tbody>
</table>

**Example request**:

```
{
    "spec": {
        "description": "new description"
    }
}
```

## Response<a name="section61819725020"></a>

**Response parameters:**

For details about the response parameters, see  [Table 5](#table111553952019).

**Table  5**  Parameters in the response body

<a name="table111553952019"></a>
<table><thead align="left"><tr id="row215439202012"><th class="cellrowborder" valign="top" width="23.26%" id="mcps1.2.4.1.1"><p id="p1216133992018"><a name="p1216133992018"></a><a name="p1216133992018"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.93%" id="mcps1.2.4.1.2"><p id="p1316153982018"><a name="p1316153982018"></a><a name="p1316153982018"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.81%" id="mcps1.2.4.1.3"><p id="p111663913204"><a name="p111663913204"></a><a name="p111663913204"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row54931625203655"><td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.4.1.1 "><p id="p16164395205"><a name="p16164395205"></a><a name="p16164395205"></a>kind</p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p11673972012"><a name="p11673972012"></a><a name="p11673972012"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.81%" headers="mcps1.2.4.1.3 "><p id="p016239162015"><a name="p016239162015"></a><a name="p016239162015"></a>API type. For a cluster management API, the parameter must be set to <strong id="b8304143918315"><a name="b8304143918315"></a><a name="b8304143918315"></a>Cluster</strong> and cannot be changed.</p>
</td>
</tr>
<tr id="row15234185203655"><td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.4.1.1 "><p id="p4168391206"><a name="p4168391206"></a><a name="p4168391206"></a>apiVersion</p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p101616395202"><a name="p101616395202"></a><a name="p101616395202"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.81%" headers="mcps1.2.4.1.3 "><p id="p1416173919201"><a name="p1416173919201"></a><a name="p1416173919201"></a>API version. The value is fixed at <strong id="b95215361854"><a name="b95215361854"></a><a name="b95215361854"></a>v3</strong> and cannot be changed.</p>
</td>
</tr>
<tr id="row1122635417553"><td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.4.1.1 "><p id="p144741558135518"><a name="p144741558135518"></a><a name="p144741558135518"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p16227554165511"><a name="p16227554165511"></a><a name="p16227554165511"></a><a href="creating-a-cluster.md#table669019286188">metadata</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="55.81%" headers="mcps1.2.4.1.3 "><p id="p102271654195515"><a name="p102271654195515"></a><a name="p102271654195515"></a>Basic information about a cluster. metadata is a collection of attributes.</p>
</td>
</tr>
<tr id="row3161391200"><td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.4.1.1 "><p id="p1016239102012"><a name="p1016239102012"></a><a name="p1016239102012"></a>spec</p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p67105119126"><a name="p67105119126"></a><a name="p67105119126"></a><a href="reading-a-specified-cluster.md#table1034041612134">spec</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="55.81%" headers="mcps1.2.4.1.3 "><p id="p16166398201"><a name="p16166398201"></a><a name="p16166398201"></a>Detailed description of the cluster to be created. CCE creates or updates objects by defining or updating its spec.</p>
</td>
</tr>
<tr id="row98251185230"><td class="cellrowborder" valign="top" width="23.26%" headers="mcps1.2.4.1.1 "><p id="p118251118192315"><a name="p118251118192315"></a><a name="p118251118192315"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p148261618142315"><a name="p148261618142315"></a><a name="p148261618142315"></a><a href="creating-a-cluster.md#table6749834132215">status</a> object</p>
</td>
<td class="cellrowborder" valign="top" width="55.81%" headers="mcps1.2.4.1.3 "><p id="p188261618172317"><a name="p188261618172317"></a><a name="p188261618172317"></a>Cluster status and jobID of the job that reads a specified cluster.</p>
</td>
</tr>
</tbody>
</table>

**Example response:**

```
{
    "kind": "Cluster",
    "apiVersion": "v3",
    "metadata": {
        "name": "mycluster",
        "uid": "4d1ecb2c-229a-11e8-9c75-0255ac100ceb",
        "creationTimestamp": "2020-02-02 03:48:58.968214406 +0000 UTC",
        "updateTimestamp": "2020-02-02 06:39:36.844676088 +0000 UTC"
    },
    "spec": {
        "type": "VirtualMachine",
        "flavor": "cce.s1.small",
        "version": "v1.15.6-r1",
        "description": "new description",
        "az": "eu-de-01",
        "ipv6enable": false,
        "supportIstio": true,
        "hostNetwork": {
            "vpc": "4d1ecb2c-229a-11e8-9c75-0255ac100ceb",
            "subnet": "4d1ecb2c-229a-11e8-9c75-0255ac100ceb",
            "SecurityGroup": "5da0b181-e0a2-4981-87ac-1681545cd666"
        },
        "containerNetwork": {
            "mode": "overlay_l2",
            "cidr": "172.17.0.0/16"
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
```

## Status Code<a name="s50f1049a6a4d404c895cf636eb8f3bf1"></a>

[Table 6](#en-us_topic_0079614900_table46761928)  describes the status code of this API.

**Table  6**  Status code

<a name="en-us_topic_0079614900_table46761928"></a>
<table><thead align="left"><tr id="en-us_topic_0079614900_row33254664"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p55616028205955"><a name="p55616028205955"></a><a name="p55616028205955"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p8604418205955"><a name="p8604418205955"></a><a name="p8604418205955"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079614900_row41084259"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0079614900_p39490674"><a name="en-us_topic_0079614900_p39490674"></a><a name="en-us_topic_0079614900_p39490674"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0079614900_p44628050"><a name="en-us_topic_0079614900_p44628050"></a><a name="en-us_topic_0079614900_p44628050"></a>Information about the specified cluster is successfully updated.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Code](status-code.md).


# Querying Maintenance Time Window<a name="dcs-api-0312041"></a>

## Function<a name="section51971645131316"></a>

The API is used to query the start time and end time of the maintenance time window.

## URI<a name="section64622449235"></a>

GET /v1.0/instances/maintain-windows

## Request<a name="section240851911242"></a>

**Request parameters**

None.

**Example request**

None.

## Response<a name="section17914193911241"></a>

**Response parameters**

[Table 1](#table615617458391)  describes the response parameters.

**Table  1**  Parameter description

<a name="table615617458391"></a>
<table><thead align="left"><tr id="row1215694553917"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.1"><p id="p1115617457395"><a name="p1115617457395"></a><a name="p1115617457395"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.2.4.1.2"><p id="p11561345123918"><a name="p11561345123918"></a><a name="p11561345123918"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.2.4.1.3"><p id="p6156194512396"><a name="p6156194512396"></a><a name="p6156194512396"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row415615459392"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.1 "><p id="p471315247"><a name="p471315247"></a><a name="p471315247"></a>maintain_windows</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.4.1.2 "><p id="p172015145"><a name="p172015145"></a><a name="p172015145"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p171115441"><a name="p171115441"></a><a name="p171115441"></a>List of supported maintenance time windows.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  maintain\_windows parameter description

<a name="table910362216139"></a>
<table><thead align="left"><tr id="row16103322121317"><th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.1"><p id="p10104022111310"><a name="p10104022111310"></a><a name="p10104022111310"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.4.1.2"><p id="p161041122171313"><a name="p161041122171313"></a><a name="p161041122171313"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.2.4.1.3"><p id="p4104722171313"><a name="p4104722171313"></a><a name="p4104722171313"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row151043224130"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.1 "><p id="p1259242341"><a name="p1259242341"></a><a name="p1259242341"></a>seq</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p159042743"><a name="p159042743"></a><a name="p159042743"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p659194219418"><a name="p659194219418"></a><a name="p659194219418"></a>Sequence number of the maintenance time window.</p>
</td>
</tr>
<tr id="row81044225134"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.1 "><p id="p8599427416"><a name="p8599427416"></a><a name="p8599427416"></a>begin</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p165974212414"><a name="p165974212414"></a><a name="p165974212414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p15917421341"><a name="p15917421341"></a><a name="p15917421341"></a>Start time of the maintenance time window.</p>
</td>
</tr>
<tr id="row81049226139"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.1 "><p id="p45917421844"><a name="p45917421844"></a><a name="p45917421844"></a>end</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p659042541"><a name="p659042541"></a><a name="p659042541"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p175919421044"><a name="p175919421044"></a><a name="p175919421044"></a>End time of the maintenance time window.</p>
</td>
</tr>
<tr id="row7105132241314"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.1 "><p id="p959842643"><a name="p959842643"></a><a name="p959842643"></a>default</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.4.1.2 "><p id="p85984210414"><a name="p85984210414"></a><a name="p85984210414"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p65910421645"><a name="p65910421645"></a><a name="p65910421645"></a>An indicator of whether the maintenance time window is set to the default time segment.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
    "maintain_windows": [
        {
            "seq": 1,
            "begin": "22",
            "end": "02",
            "default": false
        },
        {
            "seq": 2,
            "begin": "02",
            "end": "06",
            "default": true
        },
        {
            "seq": 3,
            "begin": "06",
            "end": "10",
            "default": false
        },
        {
            "seq": 4,
            "begin": "10",
            "end": "14",
            "default": false
        },
        {
            "seq": 5,
            "begin": "14",
            "end": "18",
            "default": false
        },
        {
            "seq": 6,
            "begin": "18",
            "end": "22",
            "default": false
        }
    ]
}
```

## Status Code<a name="section15118192111410"></a>

[Table 3](#table611872191420)  describes the status code of successful operations. For details about other status codes, see  [Table 1](status-codes.md#table5210141351517).

**Table  3**  Status code

<a name="table611872191420"></a>
<table><thead align="left"><tr id="row1411932101418"><th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.3.1.1"><p id="p81194271410"><a name="p81194271410"></a><a name="p81194271410"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.02%" id="mcps1.2.3.1.2"><p id="p91199217144"><a name="p91199217144"></a><a name="p91199217144"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1011932151411"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.3.1.1 "><p id="p21194210147"><a name="p21194210147"></a><a name="p21194210147"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.02%" headers="mcps1.2.3.1.2 "><p id="p10119626142"><a name="p10119626142"></a><a name="p10119626142"></a>Successfully queried the maintenance time window.</p>
</td>
</tr>
</tbody>
</table>


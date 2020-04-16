# Abnormal Request Results<a name="en-us_topic_0032488197"></a>

## v3 APIs<a name="section41121247572"></a>

**Abnormal response description**

**Table  1**  Abnormal response description

<a name="table7745218464"></a>
<table><thead align="left"><tr id="row879102194619"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p38113217464"><a name="p38113217464"></a><a name="p38113217464"></a><strong id="b84235270691445"><a name="b84235270691445"></a><a name="b84235270691445"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.200000000000003%" id="mcps1.2.4.1.2"><p id="p581192104614"><a name="p581192104614"></a><a name="p581192104614"></a><strong id="b842352706164541"><a name="b842352706164541"></a><a name="b842352706164541"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="56.57%" id="mcps1.2.4.1.3"><p id="p883152154610"><a name="p883152154610"></a><a name="p883152154610"></a><strong>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1485152113462"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p12851213469"><a name="p12851213469"></a><a name="p12851213469"></a>error_code</p>
</td>
<td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.2 "><p id="p487192112463"><a name="p487192112463"></a><a name="p487192112463"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.4.1.3 "><p id="p088221154617"><a name="p088221154617"></a><a name="p088221154617"></a>Specifies the error code returned when a task submission exception occurs. For details, see <a href="error-codes.md#td93aca0e44834bb3939478d798feb72e">Table 2</a>.</p>
</td>
</tr>
<tr id="row788132114618"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p29082164616"><a name="p29082164616"></a><a name="p29082164616"></a>error_msg</p>
</td>
<td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.2 "><p id="p1290102116462"><a name="p1290102116462"></a><a name="p1290102116462"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.4.1.3 "><p id="p1592121204615"><a name="p1592121204615"></a><a name="p1592121204615"></a>Specifies the description of the error returned when a task submission exception occurs.</p>
</td>
</tr>
</tbody>
</table>

**Response example**

```
{
    "error_code": "DBS.200022",
    "error_msg": "The DB instance name already exists."
}
```

## v1 APIs<a name="section15334153219015"></a>

**Abnormal response description**

**Table  2**  Abnormal response description

<a name="t1600a24cde73446fadb04fa4fd4176c9"></a>
<table><thead align="left"><tr id="rd8bc4cbf15874672964a2f6155ff619b"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="ae933c42bba744097bb871e1e47a3d811"><a name="ae933c42bba744097bb871e1e47a3d811"></a><a name="ae933c42bba744097bb871e1e47a3d811"></a><strong id="b84235270691445_1"><a name="b84235270691445_1"></a><a name="b84235270691445_1"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.200000000000003%" id="mcps1.2.4.1.2"><p id="a70dcf20d1f394d3886396b45ae4ed9e9"><a name="a70dcf20d1f394d3886396b45ae4ed9e9"></a><a name="a70dcf20d1f394d3886396b45ae4ed9e9"></a><strong id="b842352706164541_1"><a name="b842352706164541_1"></a><a name="b842352706164541_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="56.57%" id="mcps1.2.4.1.3"><p id="aab87d22c016b458fbf47a74f2c84238b"><a name="aab87d22c016b458fbf47a74f2c84238b"></a><a name="aab87d22c016b458fbf47a74f2c84238b"></a><strong id="b842352706163417"><a name="b842352706163417"></a><a name="b842352706163417"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r3a83848174a44b2499a0b79476a18366"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="ace78946dd7914bdc9051d696003e3d6f"><a name="ace78946dd7914bdc9051d696003e3d6f"></a><a name="ace78946dd7914bdc9051d696003e3d6f"></a>errCode</p>
</td>
<td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.2 "><p id="a70943c58d7524abcb12b87181c64e2a5"><a name="a70943c58d7524abcb12b87181c64e2a5"></a><a name="a70943c58d7524abcb12b87181c64e2a5"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.4.1.3 "><p id="ac399032b44cd41cd82fc0a0c3e083886"><a name="ac399032b44cd41cd82fc0a0c3e083886"></a><a name="ac399032b44cd41cd82fc0a0c3e083886"></a>Specifies the error code returned when a task submission exception occurs. For details, see <a href="error-codes.md#td93aca0e44834bb3939478d798feb72e">Table 2</a>.</p>
</td>
</tr>
<tr id="r406296b9b2bf4aafb5e79cf9da8fb201"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="aa97ccde9ddfc4aa0823d82c4a22f6962"><a name="aa97ccde9ddfc4aa0823d82c4a22f6962"></a><a name="aa97ccde9ddfc4aa0823d82c4a22f6962"></a>externalMessage</p>
</td>
<td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.2 "><p id="a1ef067712a0141029c3dd10e0df28ab9"><a name="a1ef067712a0141029c3dd10e0df28ab9"></a><a name="a1ef067712a0141029c3dd10e0df28ab9"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.4.1.3 "><p id="a0994d9a70c8241ba8a2b1fc9b0757e6e"><a name="a0994d9a70c8241ba8a2b1fc9b0757e6e"></a><a name="a0994d9a70c8241ba8a2b1fc9b0757e6e"></a>Specifies the description of the error returned when a task submission exception occurs.</p>
</td>
</tr>
</tbody>
</table>

**Response example**

```
{
    "errCode": "RDS.1102",
    "externalMessage": "The DB instance name already exists."
}
```

## OpenStack Trove API v1.0 APIs<a name="section146347505020"></a>

**Abnormal response description**

**Table  3**  Abnormal response description \(using itemNotFound as an example\)

<a name="table2531689118519"></a>
<table><thead align="left"><tr id="row4651182318519"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p936128918519"><a name="p936128918519"></a><a name="p936128918519"></a><strong id="b84235270618498"><a name="b84235270618498"></a><a name="b84235270618498"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.200000000000003%" id="mcps1.2.4.1.2"><p id="p2006692718519"><a name="p2006692718519"></a><a name="p2006692718519"></a><strong id="b842352706164541_2"><a name="b842352706164541_2"></a><a name="b842352706164541_2"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="56.57%" id="mcps1.2.4.1.3"><p id="p1480842718519"><a name="p1480842718519"></a><a name="p1480842718519"></a><strong id="b842352706163417_1"><a name="b842352706163417_1"></a><a name="b842352706163417_1"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row274094101879"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p55697501879"><a name="p55697501879"></a><a name="p55697501879"></a>itemNotFound</p>
</td>
<td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.2 "><p id="p484965691879"><a name="p484965691879"></a><a name="p484965691879"></a>List data structure. For details, see <a href="#table6204277318822">Table 4</a>.</p>
</td>
<td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.4.1.3 "><p id="p359080541879"><a name="p359080541879"></a><a name="p359080541879"></a>Specifies the error type when a task submission exception occurs. For details, see <a href="error-codes.md#table57182163211057">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Error type parameter data structure description

<a name="table6204277318822"></a>
<table><thead align="left"><tr id="row1241408818822"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p6601708518822"><a name="p6601708518822"></a><a name="p6601708518822"></a><strong id="b84235270691445_2"><a name="b84235270691445_2"></a><a name="b84235270691445_2"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.200000000000003%" id="mcps1.2.4.1.2"><p id="p4578365418822"><a name="p4578365418822"></a><a name="p4578365418822"></a><strong id="b842352706164541_3"><a name="b842352706164541_3"></a><a name="b842352706164541_3"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="56.57%" id="mcps1.2.4.1.3"><p id="p1748849218822"><a name="p1748849218822"></a><a name="p1748849218822"></a><strong id="b842352706163417_2"><a name="b842352706163417_2"></a><a name="b842352706163417_2"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row728171818822"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p5294826818822"><a name="p5294826818822"></a><a name="p5294826818822"></a>code</p>
</td>
<td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.2 "><p id="p6095135218822"><a name="p6095135218822"></a><a name="p6095135218822"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.4.1.3 "><p id="p3811244718822"><a name="p3811244718822"></a><a name="p3811244718822"></a>Specifies the response code returned when a task submission exception occurs.</p>
</td>
</tr>
<tr id="row10052318822"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p814243618822"><a name="p814243618822"></a><a name="p814243618822"></a>message</p>
</td>
<td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.2 "><p id="p5555758518822"><a name="p5555758518822"></a><a name="p5555758518822"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.2.4.1.3 "><p id="p387055518822"><a name="p387055518822"></a><a name="p387055518822"></a>Specifies the description of the error returned when a task submission exception occurs.</p>
</td>
</tr>
</tbody>
</table>

**Response example**

```
{
  "itemNotFound": {
    "code": 404,
    "message": "The resource could not be found."
  }
}
```


# About CarbonData Table<a name="EN-US_TOPIC_0125375879"></a>

## Overview<a name="sb0c4662f9ae54d7490fa271fc80bce63"></a>

CarbonData tables are similar to tables in the relational database management system \(RDBMS\). RDBMS tables consist of rows and columns to store data. CarbonData tables have fixed columns and also store structured data. In CarbonData, data is saved in entity files.

## Data Types Supported<a name="sc02995aee3204685ba8a7b4f8ffb60b9"></a>

CarbonData tables support the following data types:

-   Int
-   String
-   BigInt
-   Decimal
-   Double
-   TimeStamp

[Table 1](#t3cf77e4c0be04f3aac5116acd8e18aa1)  describes the details about the data types.

**Table  1**  CarbonData data types

<a name="t3cf77e4c0be04f3aac5116acd8e18aa1"></a>
<table><thead align="left"><tr id="r0046c6b5a22c449f8b1068eb60799712"><th class="cellrowborder" valign="top" width="17.86%" id="mcps1.2.3.1.1"><p id="ae1032d88ea874d9d9fbecbd8834730a8"><a name="ae1032d88ea874d9d9fbecbd8834730a8"></a><a name="ae1032d88ea874d9d9fbecbd8834730a8"></a><strong id="aa28193ecd37b4761913ae1d5c476ed91"><a name="aa28193ecd37b4761913ae1d5c476ed91"></a><a name="aa28193ecd37b4761913ae1d5c476ed91"></a>Data Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="82.14%" id="mcps1.2.3.1.2"><p id="a1a0e217529774341bce6fc2b261e260f"><a name="a1a0e217529774341bce6fc2b261e260f"></a><a name="a1a0e217529774341bce6fc2b261e260f"></a><strong id="a1e4b7a949f424b0bb56c208c5a5f06a6"><a name="a1e4b7a949f424b0bb56c208c5a5f06a6"></a><a name="a1e4b7a949f424b0bb56c208c5a5f06a6"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rb6b4d0c480514f629f4e28414bcaf099"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.2.3.1.1 "><p id="a1b82ca5dafb64828b87b60e8a8bb2852"><a name="a1b82ca5dafb64828b87b60e8a8bb2852"></a><a name="a1b82ca5dafb64828b87b60e8a8bb2852"></a>Int</p>
</td>
<td class="cellrowborder" valign="top" width="82.14%" headers="mcps1.2.3.1.2 "><p id="ab40285fcf0b045db8f0586577040bd90"><a name="ab40285fcf0b045db8f0586577040bd90"></a><a name="ab40285fcf0b045db8f0586577040bd90"></a>4-byte signed integer ranging from -2,147,483,648 to 2,147,483,647</p>
<div class="note" id="n6961f57f09f649629e2fa96b137c54b0"><a name="n6961f57f09f649629e2fa96b137c54b0"></a><a name="n6961f57f09f649629e2fa96b137c54b0"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a64d4a57f256d4757bfeb335ed0f0e099"><a name="a64d4a57f256d4757bfeb335ed0f0e099"></a><a name="a64d4a57f256d4757bfeb335ed0f0e099"></a>If non-dictionary columns have Int data, the data is saved as BigInt data in the table.</p>
</div></div>
</td>
</tr>
<tr id="r35431b58f5f3478ebe89b74de145bfc6"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.2.3.1.1 "><p id="a028182a6e1d340a3ac2f3e814bb6fdfe"><a name="a028182a6e1d340a3ac2f3e814bb6fdfe"></a><a name="a028182a6e1d340a3ac2f3e814bb6fdfe"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="82.14%" headers="mcps1.2.3.1.2 "><p id="af32decac5d324eb5a6bb6478fbef2e78"><a name="af32decac5d324eb5a6bb6478fbef2e78"></a><a name="af32decac5d324eb5a6bb6478fbef2e78"></a>The maximum character string length is 100,000.</p>
</td>
</tr>
<tr id="rcd0ec2ba7112438dac2f3d347cf2ab13"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.2.3.1.1 "><p id="a5dbcea75821d4d6e8fe1c47ea6b2dee4"><a name="a5dbcea75821d4d6e8fe1c47ea6b2dee4"></a><a name="a5dbcea75821d4d6e8fe1c47ea6b2dee4"></a>BigInt</p>
</td>
<td class="cellrowborder" valign="top" width="82.14%" headers="mcps1.2.3.1.2 "><p id="aae3e29f715164a5182b70e9965432a37"><a name="aae3e29f715164a5182b70e9965432a37"></a><a name="aae3e29f715164a5182b70e9965432a37"></a>Data is saved using the 64-bit technology. The value ranges from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807.</p>
</td>
</tr>
<tr id="r597a9fa374454f949882bcd4d64a4dcc"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.2.3.1.1 "><p id="a28db669d5089413ea281544b8912a19d"><a name="a28db669d5089413ea281544b8912a19d"></a><a name="a28db669d5089413ea281544b8912a19d"></a>Decimal</p>
</td>
<td class="cellrowborder" valign="top" width="82.14%" headers="mcps1.2.3.1.2 "><p id="a288bc753f23a4eceb3deeac909101c8b"><a name="a288bc753f23a4eceb3deeac909101c8b"></a><a name="a288bc753f23a4eceb3deeac909101c8b"></a>The default value is (10,0) and maximum value is (38,38).</p>
<div class="note" id="n26f72a8b5ae142b394a131593d446b5d"><a name="n26f72a8b5ae142b394a131593d446b5d"></a><a name="n26f72a8b5ae142b394a131593d446b5d"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a20b0712a5b21425dbcb74c8a34435d22"><a name="a20b0712a5b21425dbcb74c8a34435d22"></a><a name="a20b0712a5b21425dbcb74c8a34435d22"></a>If a query condition is used, users can add <strong id="ac10c7e05c30f473daa24d457513ebf66"><a name="ac10c7e05c30f473daa24d457513ebf66"></a><a name="ac10c7e05c30f473daa24d457513ebf66"></a>BD</strong>&nbsp;after the number to obtain accurate results. For example,&nbsp;<strong id="a10a60007f4c7474abf2264c1d7b16618"><a name="a10a60007f4c7474abf2264c1d7b16618"></a><a name="a10a60007f4c7474abf2264c1d7b16618"></a>select * from carbon_table where num = 1234567890123456.22BD</strong>.</p>
</div></div>
</td>
</tr>
<tr id="r47eb2f358f4d43298440d6790b22a519"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.2.3.1.1 "><p id="a04a502499ab340a197655bbfc959b296"><a name="a04a502499ab340a197655bbfc959b296"></a><a name="a04a502499ab340a197655bbfc959b296"></a>Double</p>
</td>
<td class="cellrowborder" valign="top" width="82.14%" headers="mcps1.2.3.1.2 "><p id="a877414a8cbb149a79c873546c4f5c7b7"><a name="a877414a8cbb149a79c873546c4f5c7b7"></a><a name="a877414a8cbb149a79c873546c4f5c7b7"></a>Data is saved using the 64-bit technology. The value ranges from 4.9E-324 to 1.7976931348623157E308.</p>
</td>
</tr>
<tr id="re53a6a346929418fbddd0116fd15dfe2"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.2.3.1.1 "><p id="ac36f96f81b53449099a6edfaa553644a"><a name="ac36f96f81b53449099a6edfaa553644a"></a><a name="ac36f96f81b53449099a6edfaa553644a"></a>TimeStamp</p>
</td>
<td class="cellrowborder" valign="top" width="82.14%" headers="mcps1.2.3.1.2 "><p id="a1fd91eda1d6f41efa367baa2a57e7905"><a name="a1fd91eda1d6f41efa367baa2a57e7905"></a><a name="a1fd91eda1d6f41efa367baa2a57e7905"></a>The default format is yyyy-MM-dd HH:mm:ss.</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>Measurement of all Int data is processed and displayed using the BigInt data type.  


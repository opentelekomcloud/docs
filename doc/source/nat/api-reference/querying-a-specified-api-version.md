# Querying a Specified API Version<a name="nat_api_0026"></a>

## Function<a name="section66578044"></a>

This API is used to query a specified API version of NAT Gateway.

## URI<a name="section42428029"></a>

GET/\{api\_version\}

**Table  1**  Parameter description

<a name="table23820074175412"></a>
<table><thead align="left"><tr id="row17704405175412"><th class="cellrowborder" valign="top" width="19.99%" id="mcps1.2.4.1.1"><p id="p24770673175412"><a name="p24770673175412"></a><a name="p24770673175412"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.93%" id="mcps1.2.4.1.2"><p id="p60267522175412"><a name="p60267522175412"></a><a name="p60267522175412"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="59.08%" id="mcps1.2.4.1.3"><p id="p49831152175412"><a name="p49831152175412"></a><a name="p49831152175412"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9791522175412"><td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.2.4.1.1 "><p id="p54915841175412"><a name="p54915841175412"></a><a name="p54915841175412"></a>api_version</p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="p18998132175412"><a name="p18998132175412"></a><a name="p18998132175412"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59.08%" headers="mcps1.2.4.1.3 "><p id="p62453732175412"><a name="p62453732175412"></a><a name="p62453732175412"></a>Specifies the API version.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section24112512"></a>

None

## Response<a name="section15686020"></a>

[Table 2](#table26246518152631)  lists response parameters.

**Table  2**  Response parameters

<a name="table26246518152631"></a>
<table><thead align="left"><tr id="row29602547152631"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.1"><p id="p1143665616354"><a name="p1143665616354"></a><a name="p1143665616354"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.2.5.1.2"><p id="p543845610355"><a name="p543845610355"></a><a name="p543845610355"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.3"><p id="p11440156143517"><a name="p11440156143517"></a><a name="p11440156143517"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46.46464646464647%" id="mcps1.2.5.1.4"><p id="p244212561357"><a name="p244212561357"></a><a name="p244212561357"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row56174697152631"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p4445556153516"><a name="p4445556153516"></a><a name="p4445556153516"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p1044685612352"><a name="p1044685612352"></a><a name="p1044685612352"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p1165613153517"><a name="p1165613153517"></a><a name="p1165613153517"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p344911569354"><a name="p344911569354"></a><a name="p344911569354"></a>Specifies the API version.</p>
</td>
</tr>
<tr id="row4615503152631"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p8452756123518"><a name="p8452756123518"></a><a name="p8452756123518"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p1045395620354"><a name="p1045395620354"></a><a name="p1045395620354"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p3312552203413"><a name="p3312552203413"></a><a name="p3312552203413"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p045585620357"><a name="p045585620357"></a><a name="p045585620357"></a>Specifies the version ID, for example, <strong id="b132119521229"><a name="b132119521229"></a><a name="b132119521229"></a>v1</strong>.</p>
</td>
</tr>
<tr id="row9239644152631"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p9460175653518"><a name="p9460175653518"></a><a name="p9460175653518"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p44601856133514"><a name="p44601856133514"></a><a name="p44601856133514"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p1784101818342"><a name="p1784101818342"></a><a name="p1784101818342"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p746525619351"><a name="p746525619351"></a><a name="p746525619351"></a>Specifies the API URL.</p>
</td>
</tr>
<tr id="row419672501413"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p16283354130"><a name="p16283354130"></a><a name="p16283354130"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p139117297139"><a name="p139117297139"></a><a name="p139117297139"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p13242332181317"><a name="p13242332181317"></a><a name="p13242332181317"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p2269104581219"><a name="p2269104581219"></a><a name="p2269104581219"></a>Specifies the reference address of the current API version.</p>
</td>
</tr>
<tr id="row154810286148"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p2139956101218"><a name="p2139956101218"></a><a name="p2139956101218"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p1994102917139"><a name="p1994102917139"></a><a name="p1994102917139"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p824653211138"><a name="p824653211138"></a><a name="p824653211138"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p513917563125"><a name="p513917563125"></a><a name="p513917563125"></a>Specifies the relationship between the current API version and the referenced address.</p>
</td>
</tr>
<tr id="row12929787152631"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p13468556113518"><a name="p13468556113518"></a><a name="p13468556113518"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p164706561359"><a name="p164706561359"></a><a name="p164706561359"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p15130115893410"><a name="p15130115893410"></a><a name="p15130115893410"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p11474856173511"><a name="p11474856173511"></a><a name="p11474856173511"></a>Specifies the version. If APIs of this version support minor versions, set this parameter to the supported maximum minor version. If the minor versions are not supported, leave this parameter blank.</p>
</td>
</tr>
<tr id="row39341340152631"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p647516561358"><a name="p647516561358"></a><a name="p647516561358"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p447812565352"><a name="p447812565352"></a><a name="p447812565352"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p143925911344"><a name="p143925911344"></a><a name="p143925911344"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p104811756113517"><a name="p104811756113517"></a><a name="p104811756113517"></a>Specifies the version status. Possible values are as follows:</p>
<a name="ul148328408213"></a><a name="ul148328408213"></a><ul id="ul148328408213"><li><strong id="b779063413315"><a name="b779063413315"></a><a name="b779063413315"></a>CURRENT</strong>: indicates that the version is the primary version.</li><li><strong id="b1977663518320"><a name="b1977663518320"></a><a name="b1977663518320"></a>SUPPORTED</strong>: indicates that the version is an old version, but it is still supported.</li><li><strong id="b447020371131"><a name="b447020371131"></a><a name="b447020371131"></a>DEPRECATED</strong>: indicates a deprecated version which may be deleted later.</li></ul>
</td>
</tr>
<tr id="row398200152631"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p7486145617358"><a name="p7486145617358"></a><a name="p7486145617358"></a>updated</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p1487135693517"><a name="p1487135693517"></a><a name="p1487135693517"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p167918023512"><a name="p167918023512"></a><a name="p167918023512"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p24932056163517"><a name="p24932056163517"></a><a name="p24932056163517"></a>Specifies the version release time, which must be the UTC time. For example, the release time of v1 is 2014-06-28T12:20:21Z.</p>
</td>
</tr>
<tr id="row61549520152631"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p2495115693510"><a name="p2495115693510"></a><a name="p2495115693510"></a>min_version</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p14966566355"><a name="p14966566355"></a><a name="p14966566355"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p134991256203512"><a name="p134991256203512"></a><a name="p134991256203512"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p205014565351"><a name="p205014565351"></a><a name="p205014565351"></a>If APIs of this version support minor versions, set this parameter to the supported minimum minor version. If not, leave this parameter blank.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section33573539387"></a>

-   Example response

```
{ 
  "version": { 
      "id": "v2.0", 
      "links": [ 
        { 
          "href": "https://x.x.x.x/v2.0/", 
          "rel": "self" 
        } 
      ], 
      "min_version": "", 
      "status": "CURRENT", 
      "updated": "2018-09-30T00:00:00Z", 
      "version": "" 
    } 
}
```

## Status Code<a name="section11326181114390"></a>

See  [Status Codes](status-codes.md).


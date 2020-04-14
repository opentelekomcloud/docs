# Show Container Metadata<a name="obs_03_0045"></a>

Users can send requests to obtain container metadata.

## Method<a name="section42203044114811"></a>

**Table  1**  Method description

<a name="table63003397114811"></a>
<table><thead align="left"><tr id="row958610114811"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p10538570114811"><a name="p10538570114811"></a><a name="p10538570114811"></a>Method</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p32207183114811"><a name="p32207183114811"></a><a name="p32207183114811"></a><strong id="b21429195114811"><a name="b21429195114811"></a><a name="b21429195114811"></a>URI</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p58043236114811"><a name="p58043236114811"></a><a name="p58043236114811"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row34935397114811"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p11194907114811"><a name="p11194907114811"></a><a name="p11194907114811"></a>HEAD</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p34372245114811"><a name="p34372245114811"></a><a name="p34372245114811"></a>/v1/{account}/{container}</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p32688443114811"><a name="p32688443114811"></a><a name="p32688443114811"></a>Shows container metadata, including the number of objects and the total bytes of all objects stored in the container.</p>
</td>
</tr>
</tbody>
</table>

**\{account\}**  indicates the name of an account.

**\{container\}**  indicates the name of a container.

This operation does not involve a request body.

## Example Request<a name="section56060206114811"></a>

Show metadata of container  **marktwain**:

```
curl -i $publicURL/marktwain -X HEAD -H "X-Auth-Token:$token"
```

## Request Query Parameters<a name="section47707984114811"></a>

This request does not include query parameters.

## Request Headers<a name="section16729309114811"></a>

Request URI parameters

<a name="table57616674111612"></a>
<table><thead align="left"><tr id="row34860353111612"><th class="cellrowborder" valign="top" width="20.66%" id="mcps1.1.4.1.1"><p id="p5116378111612"><a name="p5116378111612"></a><a name="p5116378111612"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="14.399999999999999%" id="mcps1.1.4.1.2"><p id="p38852453111612"><a name="p38852453111612"></a><a name="p38852453111612"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.94%" id="mcps1.1.4.1.3"><p id="p3497983111612"><a name="p3497983111612"></a><a name="p3497983111612"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row67002027111612"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p58455124111612"><a name="p58455124111612"></a><a name="p58455124111612"></a>{account}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p37244573111612"><a name="p37244573111612"></a><a name="p37244573111612"></a>String</p>
<p id="p66765701111612"><a name="p66765701111612"></a><a name="p66765701111612"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p39312673111612"><a name="p39312673111612"></a><a name="p39312673111612"></a>Unique name of the account. In the current version, it indicates the unique ID of the account.</p>
</td>
</tr>
<tr id="row18269744111612"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p3454282111612"><a name="p3454282111612"></a><a name="p3454282111612"></a>{container}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p11361445111612"><a name="p11361445111612"></a><a name="p11361445111612"></a>String</p>
<p id="p35144146111612"><a name="p35144146111612"></a><a name="p35144146111612"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p28103601111612"><a name="p28103601111612"></a><a name="p28103601111612"></a>Unique name of the container.</p>
<p id="p51605820111612"><a name="p51605820111612"></a><a name="p51605820111612"></a>For details about container naming rules, see <a href="naming-rules.md">Naming Rules</a>.</p>
</td>
</tr>
</tbody>
</table>

Request header parameters

<a name="table65258011111612"></a>
<table><thead align="left"><tr id="row62776274111612"><th class="cellrowborder" valign="top" width="20.66%" id="mcps1.1.4.1.1"><p id="p51713465111612"><a name="p51713465111612"></a><a name="p51713465111612"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.399999999999999%" id="mcps1.1.4.1.2"><p id="p51043305111612"><a name="p51043305111612"></a><a name="p51043305111612"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.94%" id="mcps1.1.4.1.3"><p id="p32258838111612"><a name="p32258838111612"></a><a name="p32258838111612"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row28590867111612"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p34158925111612"><a name="p34158925111612"></a><a name="p34158925111612"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p15409568111612"><a name="p15409568111612"></a><a name="p15409568111612"></a>String</p>
<p id="p4468386111612"><a name="p4468386111612"></a><a name="p4468386111612"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p26394956111612"><a name="p26394956111612"></a><a name="p26394956111612"></a>Authentication token.</p>
</td>
</tr>
</tbody>
</table>

## Response Headers<a name="section84586421267"></a>

The following table describes the response headers:

**Table  2**  Response header parameters

<a name="table501912211267"></a>
<table><thead align="left"><tr id="row186862111267"><th class="cellrowborder" valign="top" width="36.41%" id="mcps1.2.4.1.1"><p id="p371881261267"><a name="p371881261267"></a><a name="p371881261267"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="17.380000000000003%" id="mcps1.2.4.1.2"><p id="p652718001267"><a name="p652718001267"></a><a name="p652718001267"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46.21%" id="mcps1.2.4.1.3"><p id="p29577051267"><a name="p29577051267"></a><a name="p29577051267"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row86834121267"><td class="cellrowborder" valign="top" width="36.41%" headers="mcps1.2.4.1.1 "><p id="p322677581267"><a name="p322677581267"></a><a name="p322677581267"></a>Accept-Ranges</p>
</td>
<td class="cellrowborder" valign="top" width="17.380000000000003%" headers="mcps1.2.4.1.2 "><p id="p635516251267"><a name="p635516251267"></a><a name="p635516251267"></a>String</p>
<p id="p14552320111713"><a name="p14552320111713"></a><a name="p14552320111713"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p474080131267"><a name="p474080131267"></a><a name="p474080131267"></a>Type of ranges that the object accepts.</p>
</td>
</tr>
<tr id="row240189331267"><td class="cellrowborder" valign="top" width="36.41%" headers="mcps1.2.4.1.1 "><p id="p664854161267"><a name="p664854161267"></a><a name="p664854161267"></a>X-Container-Bytes-Used</p>
</td>
<td class="cellrowborder" valign="top" width="17.380000000000003%" headers="mcps1.2.4.1.2 "><p id="p166096241267"><a name="p166096241267"></a><a name="p166096241267"></a>Int</p>
<p id="p56989345111751"><a name="p56989345111751"></a><a name="p56989345111751"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p32022841267"><a name="p32022841267"></a><a name="p32022841267"></a>Total number of bytes that are stored in OBS for the container.</p>
</td>
</tr>
<tr id="row288205591267"><td class="cellrowborder" valign="top" width="36.41%" headers="mcps1.2.4.1.1 "><p id="p527639571267"><a name="p527639571267"></a><a name="p527639571267"></a>X-Container-Object-Count</p>
</td>
<td class="cellrowborder" valign="top" width="17.380000000000003%" headers="mcps1.2.4.1.2 "><p id="p460221311267"><a name="p460221311267"></a><a name="p460221311267"></a>Int</p>
<p id="p58445763111755"><a name="p58445763111755"></a><a name="p58445763111755"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p368051701267"><a name="p368051701267"></a><a name="p368051701267"></a>Number of objects in the container.</p>
</td>
</tr>
<tr id="row628110821267"><td class="cellrowborder" valign="top" width="36.41%" headers="mcps1.2.4.1.1 "><p id="p545328441267"><a name="p545328441267"></a><a name="p545328441267"></a>X-Container-Meta-name</p>
</td>
<td class="cellrowborder" valign="top" width="17.380000000000003%" headers="mcps1.2.4.1.2 "><p id="p550842591267"><a name="p550842591267"></a><a name="p550842591267"></a>String</p>
<p id="p1211158111181"><a name="p1211158111181"></a><a name="p1211158111181"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p326400231267"><a name="p326400231267"></a><a name="p326400231267"></a>Custom container metadata item, where <strong id="b41932174"><a name="b41932174"></a><a name="b41932174"></a>{name}</strong> is the name of the metadata item.</p>
</td>
</tr>
<tr id="row43429524121311"><td class="cellrowborder" valign="top" width="36.41%" headers="mcps1.2.4.1.1 "><p id="p24291112121317"><a name="p24291112121317"></a><a name="p24291112121317"></a>X-Container-Read</p>
</td>
<td class="cellrowborder" valign="top" width="17.380000000000003%" headers="mcps1.2.4.1.2 "><p id="p63985345121311"><a name="p63985345121311"></a><a name="p63985345121311"></a>String</p>
<p id="p57441639111817"><a name="p57441639111817"></a><a name="p57441639111817"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p15430436121311"><a name="p15430436121311"></a><a name="p15430436121311"></a>ACL that grants read access.</p>
</td>
</tr>
<tr id="row62377012121314"><td class="cellrowborder" valign="top" width="36.41%" headers="mcps1.2.4.1.1 "><p id="p45766562121321"><a name="p45766562121321"></a><a name="p45766562121321"></a>X-Container-Write</p>
</td>
<td class="cellrowborder" valign="top" width="17.380000000000003%" headers="mcps1.2.4.1.2 "><p id="p25723072121314"><a name="p25723072121314"></a><a name="p25723072121314"></a>String</p>
<p id="p10880947111825"><a name="p10880947111825"></a><a name="p10880947111825"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p3194113121314"><a name="p3194113121314"></a><a name="p3194113121314"></a>ACL that grants write access.</p>
</td>
</tr>
<tr id="row545197882027"><td class="cellrowborder" valign="top" width="36.41%" headers="mcps1.2.4.1.1 "><p id="p4889422520231"><a name="p4889422520231"></a><a name="p4889422520231"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="17.380000000000003%" headers="mcps1.2.4.1.2 "><p id="p100927520231"><a name="p100927520231"></a><a name="p100927520231"></a>String</p>
<p id="p908348120231"><a name="p908348120231"></a><a name="p908348120231"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p6467337120231"><a name="p6467337120231"></a><a name="p6467337120231"></a>If the operation succeeds, this value is 0.</p>
<p id="p4518943420231"><a name="p4518943420231"></a><a name="p4518943420231"></a>If the operation fails, this value is the length of the error text in the response body.</p>
</td>
</tr>
<tr id="row10360342028"><td class="cellrowborder" valign="top" width="36.41%" headers="mcps1.2.4.1.1 "><p id="p5975406120231"><a name="p5975406120231"></a><a name="p5975406120231"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="17.380000000000003%" headers="mcps1.2.4.1.2 "><p id="p824078120231"><a name="p824078120231"></a><a name="p824078120231"></a>String</p>
<p id="p705816720231"><a name="p705816720231"></a><a name="p705816720231"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p3484063620231"><a name="p3484063620231"></a><a name="p3484063620231"></a>MIME type of the object.</p>
</td>
</tr>
<tr id="row375166852029"><td class="cellrowborder" valign="top" width="36.41%" headers="mcps1.2.4.1.1 "><p id="p3167354320231"><a name="p3167354320231"></a><a name="p3167354320231"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="17.380000000000003%" headers="mcps1.2.4.1.2 "><p id="p1542016820231"><a name="p1542016820231"></a><a name="p1542016820231"></a>Datetime</p>
<p id="p456379120231"><a name="p456379120231"></a><a name="p456379120231"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p3412282320231"><a name="p3412282320231"></a><a name="p3412282320231"></a>Transaction date and time.</p>
</td>
</tr>
<tr id="row79682512029"><td class="cellrowborder" valign="top" width="36.41%" headers="mcps1.2.4.1.1 "><p id="p4525850420231"><a name="p4525850420231"></a><a name="p4525850420231"></a>X-Trans-Id</p>
</td>
<td class="cellrowborder" valign="top" width="17.380000000000003%" headers="mcps1.2.4.1.2 "><p id="p4206023620231"><a name="p4206023620231"></a><a name="p4206023620231"></a>Uuid</p>
<p id="p4299780820231"><a name="p4299780820231"></a><a name="p4299780820231"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p6027042520231"><a name="p6027042520231"></a><a name="p6027042520231"></a>Unique transaction identifier.</p>
<p id="p556292120231"><a name="p556292120231"></a><a name="p556292120231"></a></p>
</td>
</tr>
<tr id="row2248688120211"><td class="cellrowborder" valign="top" width="36.41%" headers="mcps1.2.4.1.1 "><p id="p2883779820231"><a name="p2883779820231"></a><a name="p2883779820231"></a>X-Timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="17.380000000000003%" headers="mcps1.2.4.1.2 "><p id="p5416028120231"><a name="p5416028120231"></a><a name="p5416028120231"></a>Datetime</p>
<p id="p1768048220231"><a name="p1768048220231"></a><a name="p1768048220231"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.21%" headers="mcps1.2.4.1.3 "><p id="p416969620231"><a name="p416969620231"></a><a name="p416969620231"></a>Object creation time and date, in UNIX Epoch timestamp format.</p>
</td>
</tr>
</tbody>
</table>

## Show Container Metadata<a name="section42277158"></a>

Show metadata of container  **marktwain**:

```
curl -i -H "X-auth-token:b85044aa87eb46b88552f1dcbae411e3" http://172.28.5.31:80/v1/AUTH_09ijuyhgt675432wert56yt789i0o98u/marktwain -X HEAD
```

```
HTTP/1.1 204 No Content
X-Trans-Id: tx0e8b58d90e74b1b043db5-15554c1c1a
Accept-Ranges: bytes
Content-Type: text/plain;charset=UTF-8
Date: Sat, 19 Sep 2015 04:35:29 GMT
X-Container-Bytes-Used: 27
X-Container-Meta-Author: Other
X-Container-Object-Count: 1
X-Timestamp: 1442632853817
Content-Length: 0
```


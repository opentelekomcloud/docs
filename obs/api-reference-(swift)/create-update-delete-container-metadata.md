# Create/Update/Delete Container Metadata<a name="obs_03_0041"></a>

Users can send requests to create, update, or delete container metadata.

For details about metadata rules, see  [Naming Rules](naming-rules.md).

## Method<a name="section2546628103434"></a>

**Table  1**  Method description

<a name="table4950298103434"></a>
<table><thead align="left"><tr id="row45407113103434"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p54097511103434"><a name="p54097511103434"></a><a name="p54097511103434"></a>Method</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p44182409103434"><a name="p44182409103434"></a><a name="p44182409103434"></a><strong id="b62097364103434"><a name="b62097364103434"></a><a name="b62097364103434"></a>URI</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p63830579103434"><a name="p63830579103434"></a><a name="p63830579103434"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row26049921103434"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p29668845103434"><a name="p29668845103434"></a><a name="p29668845103434"></a>POST</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p54366205103434"><a name="p54366205103434"></a><a name="p54366205103434"></a>/v1/{account}/{container}</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p41586457103434"><a name="p41586457103434"></a><a name="p41586457103434"></a>Creates, updates, or deletes container metadata.</p>
</td>
</tr>
</tbody>
</table>

**\{account\}**  indicates the name of an account.  **\{container\}**  indicates the name of a container.

Metadata creation or update depends on whether the specified metadata exists. Metadata is created if it does not exist. Metadata is updated if it exists.

This operation does not involve a request body.

## Example Request<a name="section5807786810479"></a>

Create or update metadata:

```
curl -i $publicURL/marktwain -X POST -H "X-Auth-Token:$token" -H "X-Container-Meta-name:value"
```

Delete metadata:

```
curl -i $publicURL/marktwain -X POST -H "X-Auth-Token:$token" -H "X-Remove-Container-Meta-name:x"
```

## Request Query Parameters<a name="section5058163010479"></a>

<a name="table13066390143824"></a>
<table><thead align="left"><tr id="row60050431143824"><th class="cellrowborder" valign="top" width="20.66%" id="mcps1.1.4.1.1"><p id="p32246725143824"><a name="p32246725143824"></a><a name="p32246725143824"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.399999999999999%" id="mcps1.1.4.1.2"><p id="p19760809143824"><a name="p19760809143824"></a><a name="p19760809143824"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.94%" id="mcps1.1.4.1.3"><p id="p44333492143824"><a name="p44333492143824"></a><a name="p44333492143824"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row39752746143824"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p65855824143824"><a name="p65855824143824"></a><a name="p65855824143824"></a>bulk-delete</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p32721527143824"><a name="p32721527143824"></a><a name="p32721527143824"></a>String</p>
<p id="p26058290143824"><a name="p26058290143824"></a><a name="p26058290143824"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p30346749143824"><a name="p30346749143824"></a><a name="p30346749143824"></a>Bulk-deletes objects. This parameter is used with the deletion list file.</p>
<p id="p4685286143824"><a name="p4685286143824"></a><a name="p4685286143824"></a>A maximum of 10,000 objects can be deleted.</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section3124263010479"></a>

Request URI parameters

<a name="table4114798105553"></a>
<table><thead align="left"><tr id="row30330451105553"><th class="cellrowborder" valign="top" width="20.66%" id="mcps1.1.4.1.1"><p id="p40847470105553"><a name="p40847470105553"></a><a name="p40847470105553"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.399999999999999%" id="mcps1.1.4.1.2"><p id="p48579016105553"><a name="p48579016105553"></a><a name="p48579016105553"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.94%" id="mcps1.1.4.1.3"><p id="p47731417105553"><a name="p47731417105553"></a><a name="p47731417105553"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row33811556105553"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p54381502105553"><a name="p54381502105553"></a><a name="p54381502105553"></a>{account}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p42825561105553"><a name="p42825561105553"></a><a name="p42825561105553"></a>String</p>
<p id="p49885734105553"><a name="p49885734105553"></a><a name="p49885734105553"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p14212677105553"><a name="p14212677105553"></a><a name="p14212677105553"></a>Unique name of the account. In the current version, it indicates the unique ID of the account.</p>
</td>
</tr>
<tr id="row60805232105553"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p26276797105553"><a name="p26276797105553"></a><a name="p26276797105553"></a>{container}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p48045802105553"><a name="p48045802105553"></a><a name="p48045802105553"></a>String</p>
<p id="p29759036105553"><a name="p29759036105553"></a><a name="p29759036105553"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p61671709105553"><a name="p61671709105553"></a><a name="p61671709105553"></a>Unique name of the container.</p>
<p id="p18174469105553"><a name="p18174469105553"></a><a name="p18174469105553"></a>For details about container naming rules, see <a href="naming-rules.md">Naming Rules</a>.</p>
</td>
</tr>
</tbody>
</table>

[Table 2](#table15259407105955)  describes the request header parameters.

**Table  2**  Request header parameters

<a name="table15259407105955"></a>
<table><thead align="left"><tr id="row1038926105955"><th class="cellrowborder" valign="top" width="36.54%" id="mcps1.2.4.1.1"><p id="p17044171105955"><a name="p17044171105955"></a><a name="p17044171105955"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="16.939999999999998%" id="mcps1.2.4.1.2"><p id="p10061014105955"><a name="p10061014105955"></a><a name="p10061014105955"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46.52%" id="mcps1.2.4.1.3"><p id="p19613076105955"><a name="p19613076105955"></a><a name="p19613076105955"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1286149195840"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p22279653195855"><a name="p22279653195855"></a><a name="p22279653195855"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p59821436195855"><a name="p59821436195855"></a><a name="p59821436195855"></a>String</p>
<p id="p1522018195855"><a name="p1522018195855"></a><a name="p1522018195855"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p56174656195855"><a name="p56174656195855"></a><a name="p56174656195855"></a>Authentication token.</p>
</td>
</tr>
<tr id="row45816803105955"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p20173539105955"><a name="p20173539105955"></a><a name="p20173539105955"></a>X-Container-Read</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p23443972105955"><a name="p23443972105955"></a><a name="p23443972105955"></a>String</p>
<p id="p37011763105457"><a name="p37011763105457"></a><a name="p37011763105457"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p19913581105955"><a name="p19913581105955"></a><a name="p19913581105955"></a>Sets a container ACL that grants read access. For details about the ACL rules, see <a href="create-container.md#section1003248895852">Container Read ACL Rules (X-Container-Read)</a>.</p>
</td>
</tr>
<tr id="row21486598105955"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p62692876105955"><a name="p62692876105955"></a><a name="p62692876105955"></a>X-Container-Write</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p44958166105955"><a name="p44958166105955"></a><a name="p44958166105955"></a>String</p>
<p id="p316752410558"><a name="p316752410558"></a><a name="p316752410558"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p17732812105955"><a name="p17732812105955"></a><a name="p17732812105955"></a>Sets a container ACL that grants write access. For details about the ACL rules, see <a href="create-container.md#section39003754101721">Container Write ACL Rules (X-Container-Write)</a>.</p>
</td>
</tr>
<tr id="row63267932105955"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p24428891105955"><a name="p24428891105955"></a><a name="p24428891105955"></a>X-Container-Meta-name</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p32583150105955"><a name="p32583150105955"></a><a name="p32583150105955"></a>String</p>
<p id="p40086891105510"><a name="p40086891105510"></a><a name="p40086891105510"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p21989502105955"><a name="p21989502105955"></a><a name="p21989502105955"></a>Container metadata. <strong id="b27380479"><a name="b27380479"></a><a name="b27380479"></a>{name}</strong> is the name of metadata item that you want to add, update, or delete. To delete this item, send an empty value in this header. You must specify an <strong id="b1958652481102620"><a name="b1958652481102620"></a><a name="b1958652481102620"></a>X-Container-Meta-{name}</strong> header for each metadata item (for each <strong id="b1279392657102620"><a name="b1279392657102620"></a><a name="b1279392657102620"></a>{name}</strong>) that you want to add, update, or delete.</p>
</td>
</tr>
<tr id="row458779151141"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p1484652511410"><a name="p1484652511410"></a><a name="p1484652511410"></a>X-Remove-Container-Meta-name</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p217504131141"><a name="p217504131141"></a><a name="p217504131141"></a>String</p>
<p id="p49410157105512"><a name="p49410157105512"></a><a name="p49410157105512"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p169530371141"><a name="p169530371141"></a><a name="p169530371141"></a>Deletes container metadata. <strong id="b30495700"><a name="b30495700"></a><a name="b30495700"></a>{name}</strong> is the name of metadata item that you want to add, update, or delete. Metadata deletion requires the <strong id="b2028005442102633"><a name="b2028005442102633"></a><a name="b2028005442102633"></a>X-Remove-Container-Meta-{name}</strong> parameter, and the value can be set to any non-empty character string.</p>
</td>
</tr>
<tr id="row62788344111830"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p37854186111832"><a name="p37854186111832"></a><a name="p37854186111832"></a>X-Container-Meta-Web-Directory-Type</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p46290239111832"><a name="p46290239111832"></a><a name="p46290239111832"></a>String</p>
<p id="p58330641105513"><a name="p58330641105513"></a><a name="p58330641105513"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p19683931161050"><a name="p19683931161050"></a><a name="p19683931161050"></a>Type of the object shown as a folder.</p>
</td>
</tr>
<tr id="row24556019161111"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p50637782161123"><a name="p50637782161123"></a><a name="p50637782161123"></a>X-Container-Meta-Web-Index</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p46349110161130"><a name="p46349110161130"></a><a name="p46349110161130"></a>String</p>
<p id="p8019660161123"><a name="p8019660161123"></a><a name="p8019660161123"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p45612760161123"><a name="p45612760161123"></a><a name="p45612760161123"></a>Name of the specified index page.</p>
</td>
</tr>
<tr id="row16061118161137"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p23515956161212"><a name="p23515956161212"></a><a name="p23515956161212"></a>X-Container-Meta-Web-Error</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p34640194161518"><a name="p34640194161518"></a><a name="p34640194161518"></a>String</p>
<p id="p25744254161212"><a name="p25744254161212"></a><a name="p25744254161212"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p4909812161212"><a name="p4909812161212"></a><a name="p4909812161212"></a>Name of the page shown in the error information, only 401 and 404 errors supported.</p>
</td>
</tr>
<tr id="row5880191161217"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p27288609161225"><a name="p27288609161225"></a><a name="p27288609161225"></a>X-Container-Meta-Web-Listings</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p37362349161516"><a name="p37362349161516"></a><a name="p37362349161516"></a>boolean</p>
<p id="p62893743161225"><a name="p62893743161225"></a><a name="p62893743161225"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p61228397161225"><a name="p61228397161225"></a><a name="p61228397161225"></a>Indicates whether to show the object list when no index page is configured. The value <strong id="b84235270614579"><a name="b84235270614579"></a><a name="b84235270614579"></a>true</strong> indicates to show and <strong id="b842352706145723"><a name="b842352706145723"></a><a name="b842352706145723"></a>false</strong> (default) not to show.</p>
</td>
</tr>
<tr id="row2720846161153"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p27061310161235"><a name="p27061310161235"></a><a name="p27061310161235"></a>X-Container-Meta-Web-Listings-CSS</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p3225886316152"><a name="p3225886316152"></a><a name="p3225886316152"></a>String</p>
<p id="p44482467161235"><a name="p44482467161235"></a><a name="p44482467161235"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p46310052161235"><a name="p46310052161235"></a><a name="p46310052161235"></a>Type of the CSS loaded when showing the object list.</p>
</td>
</tr>
<tr id="row40940633161157"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p38235690161419"><a name="p38235690161419"></a><a name="p38235690161419"></a>X-Web-Mode</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p46741775161423"><a name="p46741775161423"></a><a name="p46741775161423"></a>boolean</p>
<p id="p10083176161419"><a name="p10083176161419"></a><a name="p10083176161419"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p11430931161419"><a name="p11430931161419"></a><a name="p11430931161419"></a>Indicates whether to enable static website for authorized users. The value <strong id="b84235270615315"><a name="b84235270615315"></a><a name="b84235270615315"></a>true</strong> indicates to enable and <strong id="b84235270615319"><a name="b84235270615319"></a><a name="b84235270615319"></a>false</strong> (default) not to enable.</p>
</td>
</tr>
<tr id="row31362913162035"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p64891499162047"><a name="p64891499162047"></a><a name="p64891499162047"></a>X-Container-Meta-Access-Control-Allow-Origin</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p21720103162047"><a name="p21720103162047"></a><a name="p21720103162047"></a>String</p>
<p id="p61263199162047"><a name="p61263199162047"></a><a name="p61263199162047"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p63372116162047"><a name="p63372116162047"></a><a name="p63372116162047"></a>Website addresses whose CORS-based access requests are allowed, which are separated from each other with commas (,).</p>
</td>
</tr>
<tr id="row41697949162033"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p27374691162047"><a name="p27374691162047"></a><a name="p27374691162047"></a>X-Container-Meta-Access-Control-Max-Age</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p2757504162047"><a name="p2757504162047"></a><a name="p2757504162047"></a>Int</p>
<p id="p24817542162047"><a name="p24817542162047"></a><a name="p24817542162047"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p64063885162047"><a name="p64063885162047"></a><a name="p64063885162047"></a>Maximum duration during which clients can keep CORS access results (clients' browsers cache CORS access results).</p>
</td>
</tr>
<tr id="row22086053162031"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p61911971162047"><a name="p61911971162047"></a><a name="p61911971162047"></a>X-Container-Meta-Access-Control-Expose-Headers</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p48813730162047"><a name="p48813730162047"></a><a name="p48813730162047"></a>String</p>
<p id="p36670389162047"><a name="p36670389162047"></a><a name="p36670389162047"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p17511502162047"><a name="p17511502162047"></a><a name="p17511502162047"></a>Headers that can be exposed to clients (for example browsers), separated from each other with spaces.</p>
</td>
</tr>
<tr id="row57255603142420"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p45538384142420"><a name="p45538384142420"></a><a name="p45538384142420"></a>X-Container-Meta-Temp-URL-Key</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p18376640142520"><a name="p18376640142520"></a><a name="p18376640142520"></a>String</p>
<p id="p31172033142520"><a name="p31172033142520"></a><a name="p31172033142520"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p8679111142420"><a name="p8679111142420"></a><a name="p8679111142420"></a>Secret key value for container-layer TempURL.</p>
</td>
</tr>
<tr id="row54539534142428"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p21093759142428"><a name="p21093759142428"></a><a name="p21093759142428"></a>X-Container-Meta-Temp-URL-Key-2</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p1040367142521"><a name="p1040367142521"></a><a name="p1040367142521"></a>String</p>
<p id="p9363310142521"><a name="p9363310142521"></a><a name="p9363310142521"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p17676166142428"><a name="p17676166142428"></a><a name="p17676166142428"></a>A second secret key value for container-layer TempURL.</p>
</td>
</tr>
</tbody>
</table>

## Response Headers<a name="section59311107103522"></a>

<a name="table8662222195940"></a>
<table><thead align="left"><tr id="row60478982195940"><th class="cellrowborder" valign="top" width="23.43%" id="mcps1.1.4.1.1"><p id="p66959380195940"><a name="p66959380195940"></a><a name="p66959380195940"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="20.11%" id="mcps1.1.4.1.2"><p id="p55000739195940"><a name="p55000739195940"></a><a name="p55000739195940"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.46%" id="mcps1.1.4.1.3"><p id="p25874907195940"><a name="p25874907195940"></a><a name="p25874907195940"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15492707195940"><td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.1 "><p id="p46949731195940"><a name="p46949731195940"></a><a name="p46949731195940"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.1.4.1.2 "><p id="p44831876195940"><a name="p44831876195940"></a><a name="p44831876195940"></a>String</p>
<p id="p833704195940"><a name="p833704195940"></a><a name="p833704195940"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="56.46%" headers="mcps1.1.4.1.3 "><p id="p421213195940"><a name="p421213195940"></a><a name="p421213195940"></a>If the operation succeeds, this value is 0.</p>
<p id="p3790919195940"><a name="p3790919195940"></a><a name="p3790919195940"></a>If the operation fails, this value is the length of the error text in the response body.</p>
</td>
</tr>
<tr id="row34118278195940"><td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.1 "><p id="p12117132195940"><a name="p12117132195940"></a><a name="p12117132195940"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.1.4.1.2 "><p id="p41963606195940"><a name="p41963606195940"></a><a name="p41963606195940"></a>String</p>
<p id="p42128136195940"><a name="p42128136195940"></a><a name="p42128136195940"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="56.46%" headers="mcps1.1.4.1.3 "><p id="p56935860195940"><a name="p56935860195940"></a><a name="p56935860195940"></a>MIME type of the object.</p>
</td>
</tr>
<tr id="row42660696195940"><td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.1 "><p id="p32964319195940"><a name="p32964319195940"></a><a name="p32964319195940"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.1.4.1.2 "><p id="p52864203195940"><a name="p52864203195940"></a><a name="p52864203195940"></a>Datetime</p>
<p id="p6015787195940"><a name="p6015787195940"></a><a name="p6015787195940"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="56.46%" headers="mcps1.1.4.1.3 "><p id="p17516713195940"><a name="p17516713195940"></a><a name="p17516713195940"></a>Transaction date and time.</p>
</td>
</tr>
<tr id="row23432689195940"><td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.1 "><p id="p18999675195940"><a name="p18999675195940"></a><a name="p18999675195940"></a>X-Trans-Id</p>
</td>
<td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.1.4.1.2 "><p id="p62578697195940"><a name="p62578697195940"></a><a name="p62578697195940"></a>Uuid</p>
<p id="p26337365195940"><a name="p26337365195940"></a><a name="p26337365195940"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="56.46%" headers="mcps1.1.4.1.3 "><p id="p52951845195940"><a name="p52951845195940"></a><a name="p52951845195940"></a>Unique transaction identifier.</p>
<p id="p6804563195940"><a name="p6804563195940"></a><a name="p6804563195940"></a></p>
</td>
</tr>
<tr id="row61241070195940"><td class="cellrowborder" valign="top" width="23.43%" headers="mcps1.1.4.1.1 "><p id="p61579607195940"><a name="p61579607195940"></a><a name="p61579607195940"></a>X-Timestamp</p>
</td>
<td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.1.4.1.2 "><p id="p21892232195940"><a name="p21892232195940"></a><a name="p21892232195940"></a>Datetime</p>
<p id="p62812363195940"><a name="p62812363195940"></a><a name="p62812363195940"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="56.46%" headers="mcps1.1.4.1.3 "><p id="p21967972195940"><a name="p21967972195940"></a><a name="p21967972195940"></a>Object creation time and date, in UNIX Epoch timestamp format.</p>
</td>
</tr>
</tbody>
</table>

## Create Container Metadata<a name="section63148656103541"></a>

Create container metadata  **Author**  with the value set to  **MarkTwain**:

```
curl -i -H "X-auth-token:b85044aa87eb46b88552f1dcbae411e3" http://172.28.5.31:80/v1/AUTH_09ijuyhgt675432wert56yt789i0o98u/marktwain -X POST -H "X-Container-Meta-Author:MarkTwain"
```

```
HTTP/1.1 204 No Content
X-Trans-Id: tx756aafaa7d2725f407980-172957b1a5
Content-Type: text/html;charset=UTF-8
Date: Sat, 19 Sep 2015 03:53:50 GMT
Content-Length: 0
```

## Update Container Metadata<a name="section59441921103541"></a>

Update container metadata  **Author**  with the value set to  **Other**:

```
curl -i -H "X-auth-token:b85044aa87eb46b88552f1dcbae411e3" http://172.28.5.31:80/v1/AUTH_09ijuyhgt675432wert56yt789i0o98u/marktwain -X POST -H "X-Container-Meta-Author:Other"
```

```
HTTP/1.1 204 No Content
X-Trans-Id: tx78195a4320339a358ef6b-7d910daaf2
Content-Type: text/html;charset=UTF-8
Date: Sat, 19 Sep 2015 03:54:07 GMT
Content-Length: 0
```

## Delete Container Metadata<a name="section54329679114246"></a>

Delete container metadata  **Author**  with the value set to any non-empty character string:

```
curl -i -H "X-auth-token:b85044aa87eb46b88552f1dcbae411e3" http://172.28.5.31:80/v1/AUTH_09ijuyhgt675432wert56yt789i0o98u/marktwain -X POST -H "X-Remove-Container-Meta-Author:x"
```

```
HTTP/1.1 204 No Content
X-Trans-Id: txd55ee251c5c4eb7747016-84b51a54c0
Content-Type: text/html;charset=UTF-8
Date: Sat, 19 Sep 2015 03:54:30 GMT
Content-Length: 0
```


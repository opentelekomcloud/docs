# Delete Container<a name="obs_03_0037"></a>

This operation deletes a container from a specified account.

Only empty containers can be deleted.

## Method<a name="section39869956112928"></a>

**Table  1**  Method description

<a name="table36630378113016"></a>
<table><thead align="left"><tr id="row48730343113016"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p5336715811413"><a name="p5336715811413"></a><a name="p5336715811413"></a>Method</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p51296332113016"><a name="p51296332113016"></a><a name="p51296332113016"></a><strong id="b39273688114629"><a name="b39273688114629"></a><a name="b39273688114629"></a>URI</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p61362190113016"><a name="p61362190113016"></a><a name="p61362190113016"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15388804113016"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p38533588113016"><a name="p38533588113016"></a><a name="p38533588113016"></a>DELETE</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p52757727113245"><a name="p52757727113245"></a><a name="p52757727113245"></a>/v1/{account}/{container}</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p19784190113016"><a name="p19784190113016"></a><a name="p19784190113016"></a>Deletes a container in a specified account. Only empty containers can be deleted.</p>
</td>
</tr>
</tbody>
</table>

**\{account\}**  indicates the name of an account.  **\{container\}**  indicates the name of a container.

This operation does not involve a request body.

## Example Request<a name="section16623225"></a>

Delete the empty containers from the specified account:

```
curl -i $publicURL/steven -X DELETE -H "X-Auth-Token:$token"
```

## Request Query Parameters<a name="section5103708"></a>

<a name="table3465011514345"></a>
<table><thead align="left"><tr id="row2112728814345"><th class="cellrowborder" valign="top" width="20.66%" id="mcps1.1.4.1.1"><p id="p3358873314345"><a name="p3358873314345"></a><a name="p3358873314345"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.399999999999999%" id="mcps1.1.4.1.2"><p id="p5856002114345"><a name="p5856002114345"></a><a name="p5856002114345"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.94%" id="mcps1.1.4.1.3"><p id="p901845514345"><a name="p901845514345"></a><a name="p901845514345"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6489438914345"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p2195416614345"><a name="p2195416614345"></a><a name="p2195416614345"></a>bulk-delete</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p37892681143424"><a name="p37892681143424"></a><a name="p37892681143424"></a>String</p>
<p id="p5489809143424"><a name="p5489809143424"></a><a name="p5489809143424"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p2965280814345"><a name="p2965280814345"></a><a name="p2965280814345"></a>Bulk-deletes objects. This parameter is used with the deletion list file.</p>
<p id="p3129015814377"><a name="p3129015814377"></a><a name="p3129015814377"></a>A maximum of 10,000 objects can be deleted.</p>
</td>
</tr>
</tbody>
</table>

## Request Headers<a name="section2186955"></a>

Request URI parameters

<a name="table47942484104315"></a>
<table><thead align="left"><tr id="row50384064104315"><th class="cellrowborder" valign="top" width="20.66%" id="mcps1.1.4.1.1"><p id="p54577389104315"><a name="p54577389104315"></a><a name="p54577389104315"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.399999999999999%" id="mcps1.1.4.1.2"><p id="p58469618104315"><a name="p58469618104315"></a><a name="p58469618104315"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.94%" id="mcps1.1.4.1.3"><p id="p10223168104315"><a name="p10223168104315"></a><a name="p10223168104315"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3605706104315"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p23626739104315"><a name="p23626739104315"></a><a name="p23626739104315"></a>{account}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p34717668104315"><a name="p34717668104315"></a><a name="p34717668104315"></a>String</p>
<p id="p44023559104315"><a name="p44023559104315"></a><a name="p44023559104315"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p9138552104315"><a name="p9138552104315"></a><a name="p9138552104315"></a>Unique name of the account. In the current version, it indicates the unique ID of the account.</p>
</td>
</tr>
<tr id="row15138112104315"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p18227579104315"><a name="p18227579104315"></a><a name="p18227579104315"></a>{container}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p38943104315"><a name="p38943104315"></a><a name="p38943104315"></a>String</p>
<p id="p350487104315"><a name="p350487104315"></a><a name="p350487104315"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p28389482104315"><a name="p28389482104315"></a><a name="p28389482104315"></a>Unique name of the container.</p>
<p id="p54178751104315"><a name="p54178751104315"></a><a name="p54178751104315"></a>For details about container naming rules, see <a href="naming-rules.md">Naming Rules</a>.</p>
</td>
</tr>
</tbody>
</table>

Request header parameters

<a name="table61429650104315"></a>
<table><thead align="left"><tr id="row54025279104315"><th class="cellrowborder" valign="top" width="20.66%" id="mcps1.1.4.1.1"><p id="p13971441104315"><a name="p13971441104315"></a><a name="p13971441104315"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.399999999999999%" id="mcps1.1.4.1.2"><p id="p51742527104315"><a name="p51742527104315"></a><a name="p51742527104315"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.94%" id="mcps1.1.4.1.3"><p id="p5121060104315"><a name="p5121060104315"></a><a name="p5121060104315"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row42265699104315"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p969622104315"><a name="p969622104315"></a><a name="p969622104315"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p11430537104315"><a name="p11430537104315"></a><a name="p11430537104315"></a>String</p>
<p id="p35765970104315"><a name="p35765970104315"></a><a name="p35765970104315"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p11362440104315"><a name="p11362440104315"></a><a name="p11362440104315"></a>Authentication token.</p>
</td>
</tr>
</tbody>
</table>

## Response Headers<a name="section30570743"></a>

<a name="table3295090919581"></a>
<table><thead align="left"><tr id="row1039828619581"><th class="cellrowborder" valign="top" width="24.177582241775823%" id="mcps1.1.4.1.1"><p id="p3695482319581"><a name="p3695482319581"></a><a name="p3695482319581"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="17.858214178582145%" id="mcps1.1.4.1.2"><p id="p4055068519581"><a name="p4055068519581"></a><a name="p4055068519581"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="57.96420357964204%" id="mcps1.1.4.1.3"><p id="p6338002319581"><a name="p6338002319581"></a><a name="p6338002319581"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3350822119581"><td class="cellrowborder" valign="top" width="24.177582241775823%" headers="mcps1.1.4.1.1 "><p id="p2981141719581"><a name="p2981141719581"></a><a name="p2981141719581"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.4.1.2 "><p id="p6591454419581"><a name="p6591454419581"></a><a name="p6591454419581"></a>String</p>
<p id="p5635999019581"><a name="p5635999019581"></a><a name="p5635999019581"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="57.96420357964204%" headers="mcps1.1.4.1.3 "><p id="p175650019581"><a name="p175650019581"></a><a name="p175650019581"></a>If the operation succeeds, this value is 0.</p>
<p id="p1580850119581"><a name="p1580850119581"></a><a name="p1580850119581"></a>If the operation fails, this value is the length of the error text in the response body.</p>
</td>
</tr>
<tr id="row805878619581"><td class="cellrowborder" valign="top" width="24.177582241775823%" headers="mcps1.1.4.1.1 "><p id="p4878189619581"><a name="p4878189619581"></a><a name="p4878189619581"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.4.1.2 "><p id="p5901950319581"><a name="p5901950319581"></a><a name="p5901950319581"></a>String</p>
<p id="p6141348219581"><a name="p6141348219581"></a><a name="p6141348219581"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="57.96420357964204%" headers="mcps1.1.4.1.3 "><p id="p843614919581"><a name="p843614919581"></a><a name="p843614919581"></a>MIME type of the object.</p>
</td>
</tr>
<tr id="row881647819581"><td class="cellrowborder" valign="top" width="24.177582241775823%" headers="mcps1.1.4.1.1 "><p id="p4304613519581"><a name="p4304613519581"></a><a name="p4304613519581"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.4.1.2 "><p id="p6418488019581"><a name="p6418488019581"></a><a name="p6418488019581"></a>Datetime</p>
<p id="p4079300819581"><a name="p4079300819581"></a><a name="p4079300819581"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="57.96420357964204%" headers="mcps1.1.4.1.3 "><p id="p1589932419581"><a name="p1589932419581"></a><a name="p1589932419581"></a>Transaction date and time.</p>
</td>
</tr>
<tr id="row887619519581"><td class="cellrowborder" valign="top" width="24.177582241775823%" headers="mcps1.1.4.1.1 "><p id="p4788318119581"><a name="p4788318119581"></a><a name="p4788318119581"></a>X-Trans-Id</p>
</td>
<td class="cellrowborder" valign="top" width="17.858214178582145%" headers="mcps1.1.4.1.2 "><p id="p5333247219581"><a name="p5333247219581"></a><a name="p5333247219581"></a>Uuid</p>
<p id="p1023020519581"><a name="p1023020519581"></a><a name="p1023020519581"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="57.96420357964204%" headers="mcps1.1.4.1.3 "><p id="p2334030019581"><a name="p2334030019581"></a><a name="p2334030019581"></a>Unique transaction identifier.</p>
<p id="p873611119581"><a name="p873611119581"></a><a name="p873611119581"></a></p>
</td>
</tr>
</tbody>
</table>

## Delete Empty Container<a name="section2201390"></a>

Delete an empty  **steven**  container:

```
curl -i -H "X-auth-token:b85044aa87eb46b88552f1dcbae411e3" http://172.28.5.31:80/v1/AUTH_09ijuyhgt675432wert56yt789i0o98u/steven -X DELETE
```

```
HTTP/1.1 204 No Content
X-Trans-Id: tx3d3e55d11af10dd917cdd-b205cb56e6
Content-Length: 0
Content-Type: text/html;charset=UTF-8
Date: Sat, 19 Sep 2015 02:37:34 GMT
```

## Delete Non-Existing Container<a name="section60098234144536"></a>

Delete the non-existing  **steve**  container:

```
curl -i -H "X-auth-token:b85044aa87eb46b88552f1dcbae411e3" http://172.28.5.31:80/v1/AUTH_09ijuyhgt675432wert56yt789i0o98u/steve -X DELETE
```

```
HTTP/1.1 404 Not Found
X-Trans-Id: txbfb5fe049899729a00e6d-e304231475
Content-Type: text/html;charset=UTF-8
Date: Sat, 19 Sep 2015 02:37:04 GMT
Content-Length: 70

<html><h1>Not Found</h1><p>The resource could not be found.</p></html> 
```

## Delete Non-Empty Container<a name="section35141195103039"></a>

Delete the non-empty  **CONTAINER**  container:

```
curl -i -H "X-auth-token:b85044aa87eb46b88552f1dcbae411e3" http://172.28.5.31:80/v1/AUTH_09ijuyhgt675432wert56yt789i0o98u/CONTAINER -X DELETE
```

```
HTTP/1.1 409 Conflict
X-Trans-Id: tx920280c22ff4ec5f733a5-74a61c1cb9
Content-Type: text/html;charset=UTF-8
Date: Sat, 19 Sep 2015 02:33:28 GMT
Content-Length: 95

<html><h1>Conflict</h1><p>There was a conflict when trying to complete your request.</p></html>
```


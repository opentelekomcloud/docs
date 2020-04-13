# Create Container<a name="obs_03_0033"></a>

This operation creates a container under a specified account. Under an account, each container must have a unique name. However, containers under different accounts can have the same name.

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
<tbody><tr id="row15388804113016"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p38533588113016"><a name="p38533588113016"></a><a name="p38533588113016"></a>PUT</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p52757727113245"><a name="p52757727113245"></a><a name="p52757727113245"></a>/v1/{account}/{container}</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p19784190113016"><a name="p19784190113016"></a><a name="p19784190113016"></a>Creates a container in a specified account.</p>
</td>
</tr>
</tbody>
</table>

**\{account\}**  indicates the name of an account.

**\{container\}**  indicates the name of a container.

This operation does not involve a request body.

## Example Request<a name="section16623225"></a>

Create a container named  **marktwain**:

```
curl -i $publicURL/marktwain -X PUT -H "X-Auth-Token:$token"
```

## Request Query Parameters<a name="section5103708"></a>

This operation does not include request query parameters.

## Request Headers<a name="section2186955"></a>

Request URI parameters

<a name="table6094619095136"></a>
<table><thead align="left"><tr id="row1674751895136"><th class="cellrowborder" valign="top" width="20.66%" id="mcps1.1.4.1.1"><p id="p1437168995136"><a name="p1437168995136"></a><a name="p1437168995136"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.399999999999999%" id="mcps1.1.4.1.2"><p id="p797889795136"><a name="p797889795136"></a><a name="p797889795136"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.94%" id="mcps1.1.4.1.3"><p id="p4525367895136"><a name="p4525367895136"></a><a name="p4525367895136"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3947959795136"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p4373079495136"><a name="p4373079495136"></a><a name="p4373079495136"></a>{account}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p5253344495136"><a name="p5253344495136"></a><a name="p5253344495136"></a>String</p>
<p id="p303895195136"><a name="p303895195136"></a><a name="p303895195136"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p4482847095136"><a name="p4482847095136"></a><a name="p4482847095136"></a>Unique name of the account. In the current version, it indicates the unique ID of the account.</p>
</td>
</tr>
<tr id="row80305395136"><td class="cellrowborder" valign="top" width="20.66%" headers="mcps1.1.4.1.1 "><p id="p6504730895136"><a name="p6504730895136"></a><a name="p6504730895136"></a>{container}</p>
</td>
<td class="cellrowborder" valign="top" width="14.399999999999999%" headers="mcps1.1.4.1.2 "><p id="p3434058495136"><a name="p3434058495136"></a><a name="p3434058495136"></a>String</p>
<p id="p4062980095136"><a name="p4062980095136"></a><a name="p4062980095136"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="64.94%" headers="mcps1.1.4.1.3 "><p id="p267946595136"><a name="p267946595136"></a><a name="p267946595136"></a>Unique name of the container.</p>
<p id="p2411518895136"><a name="p2411518895136"></a><a name="p2411518895136"></a>For details about container naming rules, see <a href="naming-rules.md">Naming Rules</a>.</p>
</td>
</tr>
</tbody>
</table>

[Table 2](#table2213898993436)  describes the request header parameters.

**Table  2**  Request header parameters

<a name="table2213898993436"></a>
<table><thead align="left"><tr id="row2383841493436"><th class="cellrowborder" valign="top" width="36.54%" id="mcps1.2.4.1.1"><p id="p5186338393436"><a name="p5186338393436"></a><a name="p5186338393436"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="16.939999999999998%" id="mcps1.2.4.1.2"><p id="p2611644893436"><a name="p2611644893436"></a><a name="p2611644893436"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46.52%" id="mcps1.2.4.1.3"><p id="p4708242393436"><a name="p4708242393436"></a><a name="p4708242393436"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row38652360195336"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p65236216195345"><a name="p65236216195345"></a><a name="p65236216195345"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p49642148195345"><a name="p49642148195345"></a><a name="p49642148195345"></a>String</p>
<p id="p44126152195345"><a name="p44126152195345"></a><a name="p44126152195345"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p17448527195345"><a name="p17448527195345"></a><a name="p17448527195345"></a>Authentication token.</p>
</td>
</tr>
<tr id="row5720377893436"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p299447193436"><a name="p299447193436"></a><a name="p299447193436"></a>X-Container-Read</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p4122562193436"><a name="p4122562193436"></a><a name="p4122562193436"></a>String</p>
<p id="p344567579536"><a name="p344567579536"></a><a name="p344567579536"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p5094097993436"><a name="p5094097993436"></a><a name="p5094097993436"></a>Sets a container access control list (ACL) that grants read access.</p>
<p id="p699305295556"><a name="p699305295556"></a><a name="p699305295556"></a>To set the container read ACL:</p>
<p id="p5743548095618"><a name="p5743548095618"></a><a name="p5743548095618"></a>curl -X {PUT|POST} -i -H "X-Auth-Token: $token" -H \</p>
<p id="p4715727595618"><a name="p4715727595618"></a><a name="p4715727595618"></a>"X-Container-Read: ACL" $publicURL/Container</p>
<p id="p2291626110164"><a name="p2291626110164"></a><a name="p2291626110164"></a>For details about ACL format rules, see the next section.</p>
</td>
</tr>
<tr id="row2477195793436"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p6037149193436"><a name="p6037149193436"></a><a name="p6037149193436"></a>X-Container-Write</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p5825260693436"><a name="p5825260693436"></a><a name="p5825260693436"></a>String</p>
<p id="p5945820095322"><a name="p5945820095322"></a><a name="p5945820095322"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p2084062193436"><a name="p2084062193436"></a><a name="p2084062193436"></a>Sets a container ACL that grants write access.</p>
<p id="p1703297195632"><a name="p1703297195632"></a><a name="p1703297195632"></a>To set the container write ACL:</p>
<p id="p1907901195632"><a name="p1907901195632"></a><a name="p1907901195632"></a>curl -X {PUT|POST} -i -H "X-Auth-Token: $token" -H \</p>
<p id="p3749337395632"><a name="p3749337395632"></a><a name="p3749337395632"></a>"X-Container-Write: ACL" $publicURL/Container</p>
<p id="p52656914101624"><a name="p52656914101624"></a><a name="p52656914101624"></a>For details about ACL format rules, see the next section.</p>
</td>
</tr>
<tr id="row4968641311486"><td class="cellrowborder" valign="top" width="36.54%" headers="mcps1.2.4.1.1 "><p id="p6517651711486"><a name="p6517651711486"></a><a name="p6517651711486"></a>X-Container-Meta-name</p>
</td>
<td class="cellrowborder" valign="top" width="16.939999999999998%" headers="mcps1.2.4.1.2 "><p id="p4480653811486"><a name="p4480653811486"></a><a name="p4480653811486"></a>String</p>
<p id="p4105006895324"><a name="p4105006895324"></a><a name="p4105006895324"></a>(Optional)</p>
</td>
<td class="cellrowborder" valign="top" width="46.52%" headers="mcps1.2.4.1.3 "><p id="p545094711486"><a name="p545094711486"></a><a name="p545094711486"></a>Container metadata. <strong id="b34632325"><a name="b34632325"></a><a name="b34632325"></a>{name}</strong> is the name of metadata item that you want to add, update, or delete. To delete this item, send an empty value in this header. You must specify an <strong id="b2119073566101717"><a name="b2119073566101717"></a><a name="b2119073566101717"></a>X-Container-Meta-{name}</strong> header for each metadata item (for each <strong id="b1507413363102042"><a name="b1507413363102042"></a><a name="b1507413363102042"></a>{name}</strong>) that you want to add, update, or delete.</p>
</td>
</tr>
</tbody>
</table>

## Container Read ACL Rules \(X-Container-Read\)<a name="section1003248895852"></a>

Container read ACL rules are as follows:

-   **.r:\*\#**: All referrers.
-   **.r:example.com,swift.example.com\#**: Comma-separated list of referrers.
-   **.rlistings\#**: Container listing access, always combined with  **.r:**.
-   **.r:-example.com\#**: Comma-separated list of inaccessible addresses.
-   **\{account:user\} \#**:  **account**  is  **projectid**  and  **user**  is  **userid**.

## Container Write ACL Rules \(X-Container-Write\)<a name="section39003754101721"></a>

Container write ACL rules are as follows:

-   **\{account:user\} \#**: Only this format is supported.  **account**  is  **projectid**  and  **user**  is  **userid**.

## Response Headers<a name="section30570743"></a>

<a name="table60070351195511"></a>
<table><thead align="left"><tr id="row26800198195511"><th class="cellrowborder" valign="top" width="23.62%" id="mcps1.1.4.1.1"><p id="p23332461195511"><a name="p23332461195511"></a><a name="p23332461195511"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="21.61%" id="mcps1.1.4.1.2"><p id="p10881151195511"><a name="p10881151195511"></a><a name="p10881151195511"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.769999999999996%" id="mcps1.1.4.1.3"><p id="p8958054195511"><a name="p8958054195511"></a><a name="p8958054195511"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row54513802195511"><td class="cellrowborder" valign="top" width="23.62%" headers="mcps1.1.4.1.1 "><p id="p53541842195511"><a name="p53541842195511"></a><a name="p53541842195511"></a>Content-Length</p>
</td>
<td class="cellrowborder" valign="top" width="21.61%" headers="mcps1.1.4.1.2 "><p id="p41921959195511"><a name="p41921959195511"></a><a name="p41921959195511"></a>String</p>
<p id="p41753313195511"><a name="p41753313195511"></a><a name="p41753313195511"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="54.769999999999996%" headers="mcps1.1.4.1.3 "><p id="p37850390195511"><a name="p37850390195511"></a><a name="p37850390195511"></a>Length of a response body.</p>
</td>
</tr>
<tr id="row8515749195511"><td class="cellrowborder" valign="top" width="23.62%" headers="mcps1.1.4.1.1 "><p id="p18687043195511"><a name="p18687043195511"></a><a name="p18687043195511"></a>Content-Type</p>
</td>
<td class="cellrowborder" valign="top" width="21.61%" headers="mcps1.1.4.1.2 "><p id="p37255481195511"><a name="p37255481195511"></a><a name="p37255481195511"></a>String</p>
<p id="p66863877195511"><a name="p66863877195511"></a><a name="p66863877195511"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="54.769999999999996%" headers="mcps1.1.4.1.3 "><p id="p47264947195511"><a name="p47264947195511"></a><a name="p47264947195511"></a>MIME type of the object.</p>
</td>
</tr>
<tr id="row22731343195511"><td class="cellrowborder" valign="top" width="23.62%" headers="mcps1.1.4.1.1 "><p id="p29299519195511"><a name="p29299519195511"></a><a name="p29299519195511"></a>Date</p>
</td>
<td class="cellrowborder" valign="top" width="21.61%" headers="mcps1.1.4.1.2 "><p id="p24450856195511"><a name="p24450856195511"></a><a name="p24450856195511"></a>Datetime</p>
<p id="p18731113195511"><a name="p18731113195511"></a><a name="p18731113195511"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="54.769999999999996%" headers="mcps1.1.4.1.3 "><p id="p40825145195511"><a name="p40825145195511"></a><a name="p40825145195511"></a>Transaction date and time.</p>
</td>
</tr>
<tr id="row31881986195511"><td class="cellrowborder" valign="top" width="23.62%" headers="mcps1.1.4.1.1 "><p id="p32304068195511"><a name="p32304068195511"></a><a name="p32304068195511"></a>X-Trans-Id</p>
</td>
<td class="cellrowborder" valign="top" width="21.61%" headers="mcps1.1.4.1.2 "><p id="p66492702195511"><a name="p66492702195511"></a><a name="p66492702195511"></a>Uuid</p>
<p id="p61563412195511"><a name="p61563412195511"></a><a name="p61563412195511"></a>(Required)</p>
</td>
<td class="cellrowborder" valign="top" width="54.769999999999996%" headers="mcps1.1.4.1.3 "><p id="p20580486195511"><a name="p20580486195511"></a><a name="p20580486195511"></a>Unique transaction identifier.</p>
<p id="p51006653195511"><a name="p51006653195511"></a><a name="p51006653195511"></a></p>
</td>
</tr>
</tbody>
</table>

## Response Body Parameters<a name="section29255058162616"></a>

The request does not include response body parameters.

## Error Responses<a name="section6388915"></a>

All the error responses are contained in  [Table 1](error-code-list.md#table30733758).

## Create Container<a name="section2201390"></a>

Create a container named  **marktwain**:

```
curl -i -H "X-Auth-token:caf12eeaae6b45b1afcb7ad1d6588a4f" "http://172.28.5.30:80/v1/AUTH_0ce042a9be6140769b12c1001d41bcf9/marktwain" -X PUT
```

```
HTTP/1.1 201 Created
X-Trans-Id: tx568a5d33add18d5f73757-b6dc185e91
Content-Type: text/html;charset=UTF-8
Date: Fri, 18 Sep 2015 01:58:51 GMT
Content-Length: 0
```

## Create Existing Container<a name="section60098234144536"></a>

Container  **marktwain**  exists. Create it again.

```
curl -i -H "X-Auth-token:caf12eeaae6b45b1afcb7ad1d6588a4f" "http://172.28.5.30:80/v1/AUTH_0ce042a9be6140769b12c1001d41bcf9/marktwain" -X PUT
```

```
HTTP/1.1 202 Accepted
X-Trans-Id: txed4fe8ffb3219cd0db230-cbe125775d
Content-Type: text/html;charset=UTF-8
Date: Fri, 18 Sep 2015 01:59:01 GMT
Content-Length: 76
<html><h1>Accepted</h1><p>The request is accepted for processing.</p></html>
```

## Create Container \(with a Read ACL Specified\)<a name="section55269209103042"></a>

Create a container and specify the  **X-Container-Read**  metadata.

```
curl -i http://172.28.54.10:80/v1/AUTH_4b34aa268d8c45879cf4da16443d3f95/ruanman -H"x-auth-token:c1f21a34cce442efbd4957018263cc2c" -H"x-container-read:.r:*" -X PUT
```

```
HTTP/1.1 201 Created
X-Trans-Id: tx000001513752eba4370a5-4f8cd5e885
Content-Length: 0
Content-Type: text/html;charset=UTF-8
Date: Tue, 24 Nov 2015 02:29:24 GMT
```


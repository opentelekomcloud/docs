# Deleting a Queue Tag<a name="EN-US_TOPIC_0128036915"></a>

## Function<a name="section3104571857"></a>

This API is used to delete a queue tag. If the key of the tag to be deleted is empty or an empty string, status code 400 is returned. If the key of the tag to be deleted does not exist, status code 404 is returned.

This API is idempotent.

## URI<a name="section15171657259"></a>

DELETE /v1.0/\{project\_id\}/queue/\{queue\_id\}/tags/\{key\}

**Table  1**  Request header

<a name="table82718572053"></a>
<table><thead align="left"><tr id="row1732913571155"><th class="cellrowborder" valign="top" width="20.62%" id="mcps1.2.5.1.1"><p id="p632914574519"><a name="p632914574519"></a><a name="p632914574519"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.77%" id="mcps1.2.5.1.2"><p id="p143299574518"><a name="p143299574518"></a><a name="p143299574518"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="19.59%" id="mcps1.2.5.1.3"><p id="p7329757359"><a name="p7329757359"></a><a name="p7329757359"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="34.02%" id="mcps1.2.5.1.4"><p id="p183292571156"><a name="p183292571156"></a><a name="p183292571156"></a>Example</p>
</th>
</tr>
</thead>
<tbody><tr id="row17329357354"><td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.1 "><p id="p6329155719511"><a name="p6329155719511"></a><a name="p6329155719511"></a>Content-type</p>
</td>
<td class="cellrowborder" valign="top" width="25.77%" headers="mcps1.2.5.1.2 "><p id="p19329957255"><a name="p19329957255"></a><a name="p19329957255"></a>Indicates the MIME types of a request body.</p>
</td>
<td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.5.1.3 "><p id="p033015713512"><a name="p033015713512"></a><a name="p033015713512"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p1833020571514"><a name="p1833020571514"></a><a name="p1833020571514"></a>application/json</p>
</td>
</tr>
<tr id="row13307573511"><td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.2.5.1.1 "><p id="p43309571255"><a name="p43309571255"></a><a name="p43309571255"></a>X-Auth-Token</p>
</td>
<td class="cellrowborder" valign="top" width="25.77%" headers="mcps1.2.5.1.2 "><p id="p1133015577519"><a name="p1133015577519"></a><a name="p1133015577519"></a>Indicates the user token.</p>
</td>
<td class="cellrowborder" valign="top" width="19.59%" headers="mcps1.2.5.1.3 "><p id="p16330155713517"><a name="p16330155713517"></a><a name="p16330155713517"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="34.02%" headers="mcps1.2.5.1.4 "><p id="p133302571518"><a name="p133302571518"></a><a name="p133302571518"></a>-</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Parameters

<a name="table165513571154"></a>
<table><thead align="left"><tr id="row33303579510"><th class="cellrowborder" valign="top" width="21.782178217821784%" id="mcps1.2.5.1.1"><p id="p20330257959"><a name="p20330257959"></a><a name="p20330257959"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.742574257425744%" id="mcps1.2.5.1.2"><p id="p133316575514"><a name="p133316575514"></a><a name="p133316575514"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="27.722772277227726%" id="mcps1.2.5.1.3"><p id="p233118570511"><a name="p233118570511"></a><a name="p233118570511"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="24.752475247524753%" id="mcps1.2.5.1.4"><p id="p133319573520"><a name="p133319573520"></a><a name="p133319573520"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row143313579519"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.5.1.1 "><p id="p1933116571056"><a name="p1933116571056"></a><a name="p1933116571056"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.5.1.2 "><p id="p33328571356"><a name="p33328571356"></a><a name="p33328571356"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="27.722772277227726%" headers="mcps1.2.5.1.3 "><p id="p0332185715519"><a name="p0332185715519"></a><a name="p0332185715519"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.5.1.4 "><p id="p73321357353"><a name="p73321357353"></a><a name="p73321357353"></a>Indicates the ID of a project.</p>
</td>
</tr>
<tr id="row1833235715519"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.5.1.1 "><p id="p1533285716511"><a name="p1533285716511"></a><a name="p1533285716511"></a>queue_id</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.5.1.2 "><p id="p11332157652"><a name="p11332157652"></a><a name="p11332157652"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="27.722772277227726%" headers="mcps1.2.5.1.3 "><p id="p43321257753"><a name="p43321257753"></a><a name="p43321257753"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.5.1.4 "><p id="p19332115717511"><a name="p19332115717511"></a><a name="p19332115717511"></a>Indicates the queue ID.</p>
</td>
</tr>
<tr id="row53321057353"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.5.1.1 "><p id="p1833212578514"><a name="p1833212578514"></a><a name="p1833212578514"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="25.742574257425744%" headers="mcps1.2.5.1.2 "><p id="p33329571954"><a name="p33329571954"></a><a name="p33329571954"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="27.722772277227726%" headers="mcps1.2.5.1.3 "><p id="p1333255716517"><a name="p1333255716517"></a><a name="p1333255716517"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.752475247524753%" headers="mcps1.2.5.1.4 "><p id="p233213571553"><a name="p233213571553"></a><a name="p233213571553"></a>Indicates a tag key.</p>
</td>
</tr>
</tbody>
</table>

**Example**

```
 /v1.0/67c01b92944144a19d2da968ef34a912/queue/dd713484-e0b6-4e70-9942-4250e773d17c/tags/T123
```

## Request<a name="section35307513"></a>

**Request parameters**

None.

**Example request**

None.

## Response<a name="section49332166"></a>

**Response parameters**

None.

**Example response**

None.

## Status Code<a name="section499257955"></a>

<a name="table61091457454"></a>
<table><thead align="left"><tr id="row203334579515"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p43331157752"><a name="p43331157752"></a><a name="p43331157752"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p143337574518"><a name="p143337574518"></a><a name="p143337574518"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2821192317357"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p48621628173514"><a name="p48621628173514"></a><a name="p48621628173514"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p28621028123510"><a name="p28621028123510"></a><a name="p28621028123510"></a>No content.</p>
</td>
</tr>
<tr id="row153335576514"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p8333557155"><a name="p8333557155"></a><a name="p8333557155"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p16334165710516"><a name="p16334165710516"></a><a name="p16334165710516"></a>Invalid parameter.</p>
</td>
</tr>
<tr id="row633419571156"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p1533415576511"><a name="p1533415576511"></a><a name="p1533415576511"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p2334165719519"><a name="p2334165719519"></a><a name="p2334165719519"></a>Authentication failed.</p>
</td>
</tr>
<tr id="row1533417577519"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p1633413571512"><a name="p1633413571512"></a><a name="p1633413571512"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p183343571454"><a name="p183343571454"></a><a name="p183343571454"></a>Insufficient permission.</p>
</td>
</tr>
<tr id="row43347571557"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p123347577513"><a name="p123347577513"></a><a name="p123347577513"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p153341857352"><a name="p153341857352"></a><a name="p153341857352"></a>No queue is found or the key does not exist.</p>
</td>
</tr>
<tr id="row193341557751"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p933415577510"><a name="p933415577510"></a><a name="p933415577510"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p1833410571353"><a name="p1833410571353"></a><a name="p1833410571353"></a>System error.</p>
</td>
</tr>
</tbody>
</table>


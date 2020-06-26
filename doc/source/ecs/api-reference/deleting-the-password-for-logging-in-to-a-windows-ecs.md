# Deleting the Password for Logging In to a Windows ECS<a name="EN-US_TOPIC_0031176554"></a>

## Function<a name="section57769674"></a>

This API is used to delete the recorded random password generated during initial Windows ECS installation. After the password is deleted, you can still use your password to log in to your ECS. However, you cannot use the Get Password function to recover the ECS initial password.

## URI<a name="section50165025"></a>

DELETE /v2/\{project\_id\}/servers/\{server\_id\}/os-server-password

DELETE /v2.1/\{project\_id\}/servers/\{server\_id\}/os-server-password

[Table 1](#table46110007)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table46110007"></a>
<table><thead align="left"><tr id="row14148614"><th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.66%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17201924"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p51178607"><a name="p51178607"></a><a name="p51178607"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p51826478"><a name="p51826478"></a><a name="p51826478"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row615338831654"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.1 "><p id="p519996316521"><a name="p519996316521"></a><a name="p519996316521"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p5588153816521"><a name="p5588153816521"></a><a name="p5588153816521"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.4.1.3 "><p id="p1719074216521"><a name="p1719074216521"></a><a name="p1719074216521"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section48832041"></a>

None

## Response<a name="section1927776"></a>

None

## Example Request<a name="section118665219435"></a>

```
DELETE https://{endpoint}/v2/{project_id}/servers/{server_id}/os-server-password
DELETE https://{endpoint}/v2.1/{project_id}/servers/{server_id}/os-server-password
```

## Example Response<a name="section19716123044320"></a>

None

## Returned Values<a name="section17349988"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


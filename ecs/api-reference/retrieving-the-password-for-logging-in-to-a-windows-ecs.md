# Retrieving the Password for Logging In to a Windows ECS<a name="EN-US_TOPIC_0031176553"></a>

## Function<a name="section57769674"></a>

This API is used to obtain the random password generated during initial Windows ECS installation for user  **Administrator**  or the configured  **Cloudbase-init**  user when you use an image that supports Cloudbase-Init to create a Windows ECS.

After starting an ECS, wait for 5 to 10 minutes and ensure that the password is injected. Then, you can use this API to query the password.

## URI<a name="section50165025"></a>

GET /v2/\{project\_id\}/servers/\{server\_id\}/os-server-password

GET /v2.1/\{project\_id\}/servers/\{server\_id\}/os-server-password

[Table 1](#table46110007)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table46110007"></a>
<table><thead align="left"><tr id="row14148614"><th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.36%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.66%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17201924"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p51178607"><a name="p51178607"></a><a name="p51178607"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p51826478"><a name="p51826478"></a><a name="p51826478"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row615338831654"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p519996316521"><a name="p519996316521"></a><a name="p519996316521"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p5588153816521"><a name="p5588153816521"></a><a name="p5588153816521"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.4.1.3 "><p id="p1719074216521"><a name="p1719074216521"></a><a name="p1719074216521"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section48832041"></a>

None

## Response<a name="section36835188"></a>

[Table 2](#table23477058)  describes the response parameters.

**Table  2**  Response parameters

<a name="table23477058"></a>
<table><thead align="left"><tr id="row2792905"><th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.4.1.1"><p id="p24898733"><a name="p24898733"></a><a name="p24898733"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.4.1.2"><p id="p17614915"><a name="p17614915"></a><a name="p17614915"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65.67%" id="mcps1.2.4.1.3"><p id="p17521988"><a name="p17521988"></a><a name="p17521988"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9994955"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p4284989"><a name="p4284989"></a><a name="p4284989"></a>password</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p62312200"><a name="p62312200"></a><a name="p62312200"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.67%" headers="mcps1.2.4.1.3 "><p id="p60002101"><a name="p60002101"></a><a name="p60002101"></a>Specifies the password in ciphertext.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section10960125004315"></a>

```
GET https://{endpoint}/v2/{project_id}/servers/{server_id}/os-server-password
GET https://{endpoint}/v2.1/{project_id}/servers/{server_id}/os-server-password
```

## Example Response<a name="section15240205325510"></a>

```
{
    "password": "UHC9+YW1xDC1Yu8Mg9n+tnOp7euEO/cW//9KgdJKWhr5w=="
}
```

## Returned Values<a name="section63081244"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


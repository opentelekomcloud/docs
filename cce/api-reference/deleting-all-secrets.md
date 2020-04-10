# Deleting All Secrets<a name="cce_02_0114"></a>

## Function<a name="section44856736"></a>

This API is used to delete secrets in batches.

## URI<a name="section1057444"></a>

DELETE /api/v1/namespaces/\{namespace\}/secrets

[Table 1](#table891810242912)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="table891810242912"></a>
<table><thead align="left"><tr id="row179181214298"><th class="cellrowborder" valign="top" width="22.45%" id="mcps1.2.4.1.1"><p id="p1791819211292"><a name="p1791819211292"></a><a name="p1791819211292"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.33%" id="mcps1.2.4.1.2"><p id="p10918192162916"><a name="p10918192162916"></a><a name="p10918192162916"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="61.22%" id="mcps1.2.4.1.3"><p id="p791832162913"><a name="p791832162913"></a><a name="p791832162913"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row99181520293"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p1691815211296"><a name="p1691815211296"></a><a name="p1691815211296"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.4.1.2 "><p id="p1791817211297"><a name="p1791817211297"></a><a name="p1791817211297"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61.22%" headers="mcps1.2.4.1.3 "><p id="p35456838"><a name="p35456838"></a><a name="p35456838"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="row091816242917"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p1891815212913"><a name="p1891815212913"></a><a name="p1891815212913"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.4.1.2 "><p id="p1991811242919"><a name="p1991811242919"></a><a name="p1991811242919"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61.22%" headers="mcps1.2.4.1.3 "><p id="p159181023297"><a name="p159181023297"></a><a name="p159181023297"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="row15918322299"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p2919028297"><a name="p2919028297"></a><a name="p2919028297"></a>fieldSelector</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.4.1.2 "><p id="p7919182152913"><a name="p7919182152913"></a><a name="p7919182152913"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61.22%" headers="mcps1.2.4.1.3 "><p id="p149194242915"><a name="p149194242915"></a><a name="p149194242915"></a>A selector to restrict the list of returned objects by their fields. Defaults to everything.</p>
</td>
</tr>
<tr id="row5919720298"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p109199217294"><a name="p109199217294"></a><a name="p109199217294"></a>includeUninitialized</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.4.1.2 "><p id="p791952152916"><a name="p791952152916"></a><a name="p791952152916"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61.22%" headers="mcps1.2.4.1.3 "><p id="p99198222912"><a name="p99198222912"></a><a name="p99198222912"></a>If true, partially initialized resources are included in the response.</p>
</td>
</tr>
<tr id="row169191272918"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p1791912219294"><a name="p1791912219294"></a><a name="p1791912219294"></a>labelSelector</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.4.1.2 "><p id="p79199212297"><a name="p79199212297"></a><a name="p79199212297"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61.22%" headers="mcps1.2.4.1.3 "><p id="p61527483"><a name="p61527483"></a><a name="p61527483"></a>A selector to restrict the list of returned objects by their labels. Defaults to everything.</p>
</td>
</tr>
<tr id="row091912214299"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p1491922112915"><a name="p1491922112915"></a><a name="p1491922112915"></a>resourceVersion</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.4.1.2 "><p id="p1391962152918"><a name="p1391962152918"></a><a name="p1391962152918"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61.22%" headers="mcps1.2.4.1.3 "><p id="p66718106"><a name="p66718106"></a><a name="p66718106"></a>When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it is 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.</p>
</td>
</tr>
<tr id="row2919429292"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p491916272919"><a name="p491916272919"></a><a name="p491916272919"></a>timeoutSeconds</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.4.1.2 "><p id="p491922112914"><a name="p491922112914"></a><a name="p491922112914"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61.22%" headers="mcps1.2.4.1.3 "><p id="p2091912222913"><a name="p2091912222913"></a><a name="p2091912222913"></a>Timeout for the list/watch call.</p>
</td>
</tr>
<tr id="row1091914216297"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p691962102910"><a name="p691962102910"></a><a name="p691962102910"></a>watch</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.4.1.2 "><p id="p4919152142916"><a name="p4919152142916"></a><a name="p4919152142916"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61.22%" headers="mcps1.2.4.1.3 "><p id="p917787"><a name="p917787"></a><a name="p917787"></a>Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section9517004"></a>

N/A

## Response<a name="section18544176"></a>

**Response parameters:**

For the description about response parameters, see  [Table 2](creating-a-secret.md#en-us_topic_0079614900_ref458786458).

**Example response**:

```
{
    "kind": "SecretList",
    "apiVersion": "v1",
    "metadata": {
        "selfLink": "/api/v1/namespaces/delns-12130306/secrets",
        "resourceVersion": "419248"
    },
    "items": [
        {
            "metadata": {
                "name": "default-token-zx6gk",
                "namespace": "delns-12130306",
                "selfLink": "/api/v1/namespaces/delns-12130306/secrets/default-token-zx6gk",
                "uid": "025df020-dfb4-11e7-9c19-fa163e2d897b",
                "resourceVersion": "419149",
                "creationTimestamp": "2017-12-13T03:16:28Z",
                "annotations": {
                    "generator": "JWT",
                    "kubernetes.io/service-account.name": "default",
                    "kubernetes.io/service-account.uid": "025c1f6e-dfb4-11e7-9c19-fa163e2d897b"
                },
                "enable": true
            },
            "data": {
                "ca.crt": "",
                "namespace": "ZGVsbnMtMTIxMzAzMDY=",
                "token": ""
            },
            "type": "kubernetes.io/service-account-token"
        },
        {
            "metadata": {
                "name": "st-del-12130306",
                "namespace": "delns-12130306",
                "selfLink": "/api/v1/namespaces/delns-12130306/secrets/st-del-12130306",
                "uid": "14975399-dfb4-11e7-9c19-fa163e2d897b",
                "resourceVersion": "419248",
                "creationTimestamp": "2017-12-13T03:16:59Z",
                "enable": true
            },
            "data": {
                ".dockerconfigjson": ""
            },
            "type": "kubernetes.io/dockerconfigjson"
        }
    ]
}
```

## Status Code<a name="section32679856"></a>

[Table 2](#d0e14569)  describes the status code of this API.

**Table  2**  Status code

<a name="d0e14569"></a>
<table><thead align="left"><tr id="row25575097"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p58316938"><a name="p58316938"></a><a name="p58316938"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p26051532"><a name="p26051532"></a><a name="p26051532"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row29799334"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p64935873"><a name="p64935873"></a><a name="p64935873"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p25314373"><a name="p25314373"></a><a name="p25314373"></a>Batch deletion of secrets succeeded.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Code](status-code.md).


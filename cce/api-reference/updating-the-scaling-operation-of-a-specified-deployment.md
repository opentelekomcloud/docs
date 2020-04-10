# Updating the Scaling Operation of a Specified Deployment<a name="cce_02_0131"></a>

## Function<a name="section62265761"></a>

This API is used to partially update scale of the specified Scale.

The following fields can be updated:

-   metadata.resourceVersion
-   metadata.creationTimestamp
-   spec.replicas

## URI<a name="section23520938"></a>

PATCH /apis/apps/v1/namespaces/\{namespace\}/deployments/\{name\}/scale \(Supports only1.9\)

PATCH /apis/extensions/v1beta1/namespaces/\{namespace\}/deployments/\{name\}/scale \(Compatible\)

PATCH /apis/apps/v1beta1/namespaces/\{namespace\}/deployments/\{name\}/scale \(Supports only1.7\)

[Table 1](#d0e37306)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="d0e37306"></a>
<table><thead align="left"><tr id="row41369621"><th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.4.1.1"><p id="p65652297517"><a name="p65652297517"></a><a name="p65652297517"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.4.1.2"><p id="p165661629135114"><a name="p165661629135114"></a><a name="p165661629135114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.32336766323368%" id="mcps1.2.4.1.3"><p id="p14567629115114"><a name="p14567629115114"></a><a name="p14567629115114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row33508240"><td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.1 "><p id="p29812883"><a name="p29812883"></a><a name="p29812883"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.4.1.2 "><p id="p66033360"><a name="p66033360"></a><a name="p66033360"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.32336766323368%" headers="mcps1.2.4.1.3 "><p id="p47101933"><a name="p47101933"></a><a name="p47101933"></a>Name of the Scale.</p>
</td>
</tr>
<tr id="row21264215"><td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.1 "><p id="p44679848"><a name="p44679848"></a><a name="p44679848"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.4.1.2 "><p id="p62297901"><a name="p62297901"></a><a name="p62297901"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.32336766323368%" headers="mcps1.2.4.1.3 "><p id="p12965198"><a name="p12965198"></a><a name="p12965198"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="row49577925"><td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.1 "><p id="p56389021"><a name="p56389021"></a><a name="p56389021"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.4.1.2 "><p id="p4107973"><a name="p4107973"></a><a name="p4107973"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="66.32336766323368%" headers="mcps1.2.4.1.3 "><p id="p64310373"><a name="p64310373"></a><a name="p64310373"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section10361851"></a>

**Request parameters:**

For the description about the  **Content-Type**  field, see  [Patch Request Method Operation Description](patch-request-method-operation-description.md).

**Example request:**

```
Content-Type: application/json-patch+json
[
    {
        "op": "add",
        "path": "/spec/replicas",
        "value": 2
    }
]
```

## Response<a name="section26147797"></a>

**Response parameters:**

For the description about response parameters, see  [Table 2](creating-a-deployment.md#table12862324102610).

**Example response:**

```
{
    "kind": "Scale",
    "apiVersion": "extensions/v1beta1",
    "metadata": {
        "name": "deploy-ex-12130306",
        "namespace": "ns-12130306-s",
        "selfLink": "/apis/extensions/v1beta1/namespaces/ns-12130306-s/deployments/deploy-ex-12130306/scale",
        "uid": "934db57d-dfb3-11e7-9c19-fa163e2d897b",
        "resourceVersion": "418857",
        "creationTimestamp": "2017-12-13T03:13:22Z"
    },
    "spec": {
        "replicas": 2
    },
    "status": {
        "replicas": 1,
        "selector": {
            "cce/appgroup": "deploy-ex-test"
        },
        "targetSelector": "cce/appgroup=deploy-ex-test"
    }
}
```

## Status Code<a name="section34003585"></a>

[Table 2](#d0e37399)  describes the status code of this API.

**Table  2**  Status code

<a name="d0e37399"></a>
<table><thead align="left"><tr id="row19360173"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p24670187"><a name="p24670187"></a><a name="p24670187"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p52128170"><a name="p52128170"></a><a name="p52128170"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row61632274"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p26158282"><a name="p26158282"></a><a name="p26158282"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p38446074"><a name="p38446074"></a><a name="p38446074"></a>This operation succeeds, and a Deployment resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Code](status-code.md).


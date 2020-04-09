# Replacing the Scaling Operation of a Specified Deployment<a name="cce_02_0126"></a>

## Function<a name="section29254118"></a>

This API is used to replace scale of the specified Scale.

The following fields can be updated:

-   metadata.resourceVersion
-   metadata.creationTimestamp
-   spec.replicas

## URI<a name="section61960472"></a>

PUT /apis/apps/v1/namespaces/\{namespace\}/deployments/\{name\}/scale \(Supports only1.9\)

PUT /apis/extensions/v1beta1/namespaces/\{namespace\}/deployments/\{name\}/scale \(Compatible\)

PUT /apis/apps/v1beta1/namespaces/\{namespace\}/deployments/\{name\}/scale \(Supports only1.7\)

[Table 1](#d0e36373)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="d0e36373"></a>
<table><thead align="left"><tr id="row30327279"><th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.4.1.1"><p id="p65652297517"><a name="p65652297517"></a><a name="p65652297517"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.4.1.2"><p id="p165661629135114"><a name="p165661629135114"></a><a name="p165661629135114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.32336766323368%" id="mcps1.2.4.1.3"><p id="p14567629115114"><a name="p14567629115114"></a><a name="p14567629115114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row20449511"><td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.1 "><p id="p45797700"><a name="p45797700"></a><a name="p45797700"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.4.1.2 "><p id="p18626238"><a name="p18626238"></a><a name="p18626238"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.32336766323368%" headers="mcps1.2.4.1.3 "><p id="p32330300"><a name="p32330300"></a><a name="p32330300"></a>Name of the Scale.</p>
</td>
</tr>
<tr id="row22537248"><td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.1 "><p id="p13577824"><a name="p13577824"></a><a name="p13577824"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.4.1.2 "><p id="p26061977"><a name="p26061977"></a><a name="p26061977"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.32336766323368%" headers="mcps1.2.4.1.3 "><p id="p30645362"><a name="p30645362"></a><a name="p30645362"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="row7372802"><td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.1 "><p id="p60326062"><a name="p60326062"></a><a name="p60326062"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.4.1.2 "><p id="p54572879"><a name="p54572879"></a><a name="p54572879"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="66.32336766323368%" headers="mcps1.2.4.1.3 "><p id="p58327117"><a name="p58327117"></a><a name="p58327117"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section20773339"></a>

**Request parameters:**

For the description about request parameters, see  [Table 2](creating-a-deployment.md#table12862324102610).

**Example request:**

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>If the first URI /apis/apps/v1/namespaces/\{namespace\}/deployments/\{name\}/scale\(Supports only1.9\) is used, change the value of  **apiVersion**  to  **autoscaling/v1**.  

```
{
    "kind": "Scale",
    "apiVersion": "extensions/v1beta1",
    "metadata": {
        "name": "deploy-ex-12130306",
        "namespace": "ns-12130306-s",
        "selfLink": "/apis/extensions/v1beta1/namespaces/ns-12130306-s/deployments/deploy-ex-12130306/scale",
        "uid": "934db57d-dfb3-11e7-9c19-fa163e2d897b",
        "resourceVersion": "418871",
        "creationTimestamp": "2017-12-13T03:13:22Z"
    },
    "spec": {
        "replicas": 1
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

## Response<a name="section52742329"></a>

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
        "resourceVersion": "418903",
        "creationTimestamp": "2017-12-13T03:13:22Z"
    },
    "spec": {
        "replicas": 1
    },
    "status": {
        "replicas": 2,
        "selector": {
            "cce/appgroup": "deploy-ex-test"
        },
        "targetSelector": "cce/appgroup=deploy-ex-test"
    }
}
```

## Status Code<a name="section4918913"></a>

[Table 2](#d0e36462)  describes the status code of this API.

**Table  2**  Status code

<a name="d0e36462"></a>
<table><thead align="left"><tr id="row53733915"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p57479854"><a name="p57479854"></a><a name="p57479854"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p25356606"><a name="p25356606"></a><a name="p25356606"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row40619186"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p1819763"><a name="p1819763"></a><a name="p1819763"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p13183080"><a name="p13183080"></a><a name="p13183080"></a>This operation succeeds, and a Deployment resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Code](status-code.md).


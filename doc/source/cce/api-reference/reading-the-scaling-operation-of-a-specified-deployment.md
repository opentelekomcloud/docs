# Reading the Scaling Operation of a Specified Deployment<a name="cce_02_0124"></a>

## Function<a name="section47779875"></a>

This API is used to read scale of the specified Scale.

## URI<a name="section27365698"></a>

GET /apis/apps/v1/namespaces/\{namespace\}/deployments/\{name\}/scale \(Supports only1.9\)

GET /apis/extensions/v1beta1/namespaces/\{namespace\}/deployments/\{name\}/scale \(Compatible\)

GET /apis/apps/v1beta1/namespaces/\{namespace\}/deployments/\{name\}/scale \(Supports only1.7\)

[Table 1](#d0e35851)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="d0e35851"></a>
<table><thead align="left"><tr id="row23454267"><th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.4.1.1"><p id="p65652297517"><a name="p65652297517"></a><a name="p65652297517"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.4.1.2"><p id="p165661629135114"><a name="p165661629135114"></a><a name="p165661629135114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.32336766323368%" id="mcps1.2.4.1.3"><p id="p14567629115114"><a name="p14567629115114"></a><a name="p14567629115114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8437627"><td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.4.1.1 "><p id="p12359162"><a name="p12359162"></a><a name="p12359162"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p61568054"><a name="p61568054"></a><a name="p61568054"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.32336766323368%" headers="mcps1.2.4.1.3 "><p id="p20956438"><a name="p20956438"></a><a name="p20956438"></a>Name of the Scale.</p>
</td>
</tr>
<tr id="row54390215"><td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.4.1.1 "><p id="p43531289"><a name="p43531289"></a><a name="p43531289"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p36373507"><a name="p36373507"></a><a name="p36373507"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.32336766323368%" headers="mcps1.2.4.1.3 "><p id="p60572974"><a name="p60572974"></a><a name="p60572974"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="row8285859"><td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.4.1.1 "><p id="p66002"><a name="p66002"></a><a name="p66002"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.4.1.2 "><p id="p5346197"><a name="p5346197"></a><a name="p5346197"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="66.32336766323368%" headers="mcps1.2.4.1.3 "><p id="p30388821"><a name="p30388821"></a><a name="p30388821"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section44964695"></a>

N/A

## Response<a name="section2029075"></a>

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
        "resourceVersion": "418871",
        "creationTimestamp": "2017-12-13T03:13:22Z"
    },
    "spec": {
        "replicas": 2
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

## Status Code<a name="section18261679"></a>

[Table 2](#d0e35928)  describes the status code of this API.

**Table  2**  Status code

<a name="d0e35928"></a>
<table><thead align="left"><tr id="row52906506"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p57568585"><a name="p57568585"></a><a name="p57568585"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p32543833"><a name="p32543833"></a><a name="p32543833"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18804834"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p46796555"><a name="p46796555"></a><a name="p46796555"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p32424572"><a name="p32424572"></a><a name="p32424572"></a>This operation succeeds, and a Deployment resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Code](status-code.md).


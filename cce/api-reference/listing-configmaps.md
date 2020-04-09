# Listing ConfigMaps<a name="cce_02_0175"></a>

## Function<a name="section13111539"></a>

This API is used to obtain a ConfigMap list.

## URI<a name="section50894989"></a>

GET /api/v1/configmaps

[Table 1](#d0e44223)  describes the parameters of this API.

**Table  1**  Description

<a name="d0e44223"></a>
<table><thead align="left"><tr id="row29971"><th class="cellrowborder" valign="top" width="33%" id="mcps1.2.4.1.1"><p id="p65652297517"><a name="p65652297517"></a><a name="p65652297517"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="27%" id="mcps1.2.4.1.2"><p id="p165661629135114"><a name="p165661629135114"></a><a name="p165661629135114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="40%" id="mcps1.2.4.1.3"><p id="p14567629115114"><a name="p14567629115114"></a><a name="p14567629115114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row57265865"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p8023508"><a name="p8023508"></a><a name="p8023508"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p45924424"><a name="p45924424"></a><a name="p45924424"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p28890827"><a name="p28890827"></a><a name="p28890827"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="row58690859"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p56339147"><a name="p56339147"></a><a name="p56339147"></a>labelSelector</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p68175"><a name="p68175"></a><a name="p68175"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p5522208"><a name="p5522208"></a><a name="p5522208"></a>A selector to restrict the list of returned objects by their labels. Defaults to everything.</p>
</td>
</tr>
<tr id="row49699872"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p66266702"><a name="p66266702"></a><a name="p66266702"></a>includeUninitialized</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p66002685"><a name="p66002685"></a><a name="p66002685"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p66011391"><a name="p66011391"></a><a name="p66011391"></a>If true, partially initialized resources are included in the response.</p>
</td>
</tr>
<tr id="row57231613"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p5249053"><a name="p5249053"></a><a name="p5249053"></a>fieldSelector</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p22520158"><a name="p22520158"></a><a name="p22520158"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p12193511"><a name="p12193511"></a><a name="p12193511"></a>A selector to restrict the list of returned objects by their fields. Defaults to everything.</p>
</td>
</tr>
<tr id="row42632743"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p30700144"><a name="p30700144"></a><a name="p30700144"></a>watch</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p3683734"><a name="p3683734"></a><a name="p3683734"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p29947008"><a name="p29947008"></a><a name="p29947008"></a>Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.</p>
</td>
</tr>
<tr id="row1087618"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p20988238"><a name="p20988238"></a><a name="p20988238"></a>resourceVersion</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p22325714"><a name="p22325714"></a><a name="p22325714"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p63552439"><a name="p63552439"></a><a name="p63552439"></a>When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history.</p>
</td>
</tr>
<tr id="row35101045"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="p24612430"><a name="p24612430"></a><a name="p24612430"></a>timeoutSeconds</p>
</td>
<td class="cellrowborder" valign="top" width="27%" headers="mcps1.2.4.1.2 "><p id="p47449819"><a name="p47449819"></a><a name="p47449819"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p18230149"><a name="p18230149"></a><a name="p18230149"></a>Timeout for the list/watch call.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section55401721"></a>

N/A

## Response<a name="section28853449"></a>

**Response parameters:**

For the description about response parameters, see  [Table 4](data-structure-of-response-parameters.md#en-us_topic_0079614930_table6622802).

**Example response:**

```
{
    "kind": "ConfigMapList",
    "apiVersion": "v1",
    "metadata": {
        "selfLink": "/api/v1/configmaps",
        "resourceVersion": "419140"
    },
    "items": [
        {
            "metadata": {
                "name": "cluster-versions",
                "namespace": "kube-system",
                "selfLink": "/api/v1/namespaces/kube-system/configmaps/cluster-versions",
                "uid": "89dff34e-dc8e-11e7-9c19-fa163e2d897b",
                "resourceVersion": "19743",
                "creationTimestamp": "2017-12-09T03:10:41Z",
                "enable": true
            },
            "data": {
                "192.168.0.197": "v1.13.10-r0",
                "192.168.0.200": "v1.13.10-r0",
                "master": "v1.13.10-r0"
            }
        },
        {
            "metadata": {
                "name": "extension-apiserver-authentication",
                "namespace": "kube-system",
                "selfLink": "/api/v1/namespaces/kube-system/configmaps/extension-apiserver-authentication",
                "uid": "842ce75c-dc8e-11e7-9c19-fa163e2d897b",
                "resourceVersion": "69",
                "creationTimestamp": "2017-12-09T03:10:31Z",
                "enable": true
            },
            "data": {
                "client-ca-file": ""
            }
        },
        {
            "metadata": {
                "name": "kube-dns",
                "namespace": "kube-system",
                "selfLink": "/api/v1/namespaces/kube-system/configmaps/kube-dns",
                "uid": "86f45cfb-dc8e-11e7-9c19-fa163e2d897b",
                "resourceVersion": "80",
                "creationTimestamp": "2017-12-09T03:10:36Z",
                "labels": {
                    "addonmanager.kubernetes.io/mode": "EnsureExists"
                },
                "enable": true
            }
        },
        {
            "metadata": {
                "name": "cm-12130306",
                "namespace": "ns-12130306-s",
                "selfLink": "/api/v1/namespaces/ns-12130306-s/configmaps/cm-12130306",
                "uid": "efd6d9e0-dfb3-11e7-9c19-fa163e2d897b",
                "resourceVersion": "419081",
                "creationTimestamp": "2017-12-13T03:15:57Z",
                "enable": true
            },
            "data": {
                "property_1": "cm-test"
            }
        }
    ]
}
```

## Status Code<a name="section58354453"></a>

[Table 2](#d0e44344)  describes the status code of this API.

**Table  2**  Status code

<a name="d0e44344"></a>
<table><thead align="left"><tr id="row34522802"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p44883567"><a name="p44883567"></a><a name="p44883567"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p11690292"><a name="p11690292"></a><a name="p11690292"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row7389610"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p61687544"><a name="p61687544"></a><a name="p61687544"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p30635207"><a name="p30635207"></a><a name="p30635207"></a>This operation succeeds, and the JSONs of a group of ConfigMap objects are returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Code](status-code.md).


# Updating a Specified ConfigMap<a name="cce_02_0176"></a>

## Function<a name="section62552745"></a>

This API is used to update a specified ConfigMap resource object.

The following fields can be updated:

-   metadata.selfLink
-   metadata.resourceVersion
-   metadata.generation
-   metadata.creationTimestamp
-   metadata.deletionTimestamp
-   metadata.labels
-   metadata.clusterName
-   metadata.generateName
-   metadata.annotations
-   spec.replicas
-   spec.restartPolicy
-   spec.activeDeadlineSeconds

## URI<a name="section26103793"></a>

PATCH /api/v1/namespaces/\{namespace\}/configmaps/\{name\}

[Table 1](#d0e44438)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="d0e44438"></a>
<table><thead align="left"><tr id="row33489305"><th class="cellrowborder" valign="top" width="22.220000000000002%" id="mcps1.2.4.1.1"><p id="p65652297517"><a name="p65652297517"></a><a name="p65652297517"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.4.1.2"><p id="p165661629135114"><a name="p165661629135114"></a><a name="p165661629135114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="60.61%" id="mcps1.2.4.1.3"><p id="p14567629115114"><a name="p14567629115114"></a><a name="p14567629115114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row14067825"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p65752073"><a name="p65752073"></a><a name="p65752073"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p24317681"><a name="p24317681"></a><a name="p24317681"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p23575121"><a name="p23575121"></a><a name="p23575121"></a>name of the Job</p>
</td>
</tr>
<tr id="row10849502"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p6394470"><a name="p6394470"></a><a name="p6394470"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p48190075"><a name="p48190075"></a><a name="p48190075"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p11081988"><a name="p11081988"></a><a name="p11081988"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="row32629032"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p25705915"><a name="p25705915"></a><a name="p25705915"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p1804342"><a name="p1804342"></a><a name="p1804342"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p11934018"><a name="p11934018"></a><a name="p11934018"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section33607552"></a>

**Request parameters**:

For the description about the  **Content-Type**  message header, see section  [Patch Request Method Operation Description](patch-request-method-operation-description.md).

**Example request**:

```
Content-Type: application/merge-patch+json
```

```
{
    "data": {
        "property_1": "new"
    }
}
```

## Response<a name="section34032518"></a>

**Response parameters:**

For the description about response parameters, see the parameter description in  [Table 2](creating-a-configmap.md#d0e42951).

**Example response:**

```
{
    "kind": "ConfigMap",
    "apiVersion": "v1",
    "metadata": {
        "name": "test-12130306",
        "namespace": "ns-12130306-s",
        "selfLink": "/api/v1/namespaces/ns-12130306-s/configmaps/test-12130306",
        "uid": "efd6d9e0-dfb3-11e7-9c19-fa163e2d897b",
        "resourceVersion": "419141",
        "creationTimestamp": "2017-12-13T03:15:57Z",
        "enable": true
    },
    "data": {
        "property_1": "new"
    }
}
```

## Status Code<a name="section37857212"></a>

[Table 2](#d0e44533)  describes the status code of this API.

**Table  2**  Status code

<a name="d0e44533"></a>
<table><thead align="left"><tr id="row14217584"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p10773671"><a name="p10773671"></a><a name="p10773671"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p252187"><a name="p252187"></a><a name="p252187"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row20427187"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p43989464"><a name="p43989464"></a><a name="p43989464"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p6376817"><a name="p6376817"></a><a name="p6376817"></a>This operation succeeds, and a ConfigMap resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see  [Status Code](status-code.md).


# Deleting a StatefulSet<a name="cce_02_0146"></a>

## Function<a name="section31372179"></a>

This API is used to delete a StatefulSet resource object.

## URI<a name="section13914160"></a>

DELETE /apis/apps/v1/namespaces/\{namespace\}/statefulsets/\{name\} \(Supports only1.9\)

DELETE /apis/apps/v1beta1/namespaces/\{namespace\}/statefulsets/\{name\} \(Compatible\)

[Table 1](#d0e38270)  describes the parameters of this API.

**Table  1**  Description

<a name="d0e38270"></a>
<table><thead align="left"><tr id="row14143522"><th class="cellrowborder" valign="top" width="21.21%" id="mcps1.2.4.1.1"><p id="p65652297517"><a name="p65652297517"></a><a name="p65652297517"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.16%" id="mcps1.2.4.1.2"><p id="p165661629135114"><a name="p165661629135114"></a><a name="p165661629135114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="62.629999999999995%" id="mcps1.2.4.1.3"><p id="p14567629115114"><a name="p14567629115114"></a><a name="p14567629115114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row49796945"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p7020714"><a name="p7020714"></a><a name="p7020714"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.4.1.2 "><p id="p31806923"><a name="p31806923"></a><a name="p31806923"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p26223965"><a name="p26223965"></a><a name="p26223965"></a>Name of the StatefulSet.</p>
</td>
</tr>
<tr id="row34689095"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p58353349"><a name="p58353349"></a><a name="p58353349"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.4.1.2 "><p id="p29000839"><a name="p29000839"></a><a name="p29000839"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p257782"><a name="p257782"></a><a name="p257782"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="row2320041"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p53705670"><a name="p53705670"></a><a name="p53705670"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.4.1.2 "><p id="p55192003"><a name="p55192003"></a><a name="p55192003"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p41367240"><a name="p41367240"></a><a name="p41367240"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="row36760846"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p24838515"><a name="p24838515"></a><a name="p24838515"></a>gracePeriodSeconds</p>
</td>
<td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.4.1.2 "><p id="p65762676"><a name="p65762676"></a><a name="p65762676"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p25176571"><a name="p25176571"></a><a name="p25176571"></a>The duration in seconds before the object should be deleted. Value must be a non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.</p>
</td>
</tr>
<tr id="row25262547"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p33000411"><a name="p33000411"></a><a name="p33000411"></a>orphanDependents</p>
</td>
<td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.4.1.2 "><p id="p55787611"><a name="p55787611"></a><a name="p55787611"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p22502652"><a name="p22502652"></a><a name="p22502652"></a>Deprecated: Use the PropagationPolicy. This field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the "orphan" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both.</p>
</td>
</tr>
<tr id="row1197280"><td class="cellrowborder" valign="top" width="21.21%" headers="mcps1.2.4.1.1 "><p id="p29870869"><a name="p29870869"></a><a name="p29870869"></a>propagationPolicy</p>
</td>
<td class="cellrowborder" valign="top" width="16.16%" headers="mcps1.2.4.1.2 "><p id="p3621310"><a name="p3621310"></a><a name="p3621310"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p2044017414610"><a name="p2044017414610"></a><a name="p2044017414610"></a>Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section58118584"></a>

**Request parameters:**

For the description about request parameters, see  [Table 2](deleting-a-daemonset.md#table191461259175715).

**Example request:**

-   Deleting only the StatefulSet \(the pod is not deleted\):

    ```
    {
        "Kind": "DeleteOptions",
        "apiVersion": "v1",
        "propagationPolicy": "Orphan"
    }
    ```

-   Deleting the pod and then the StatefulSet:

    ```
    {
        "kind": "DeleteOptions",
        "apiVersion": "v1",
        "propagationPolicy": "Foreground"
    }
    ```

-   Deleting the StatefulSet and then the pod:

    ```
    {
        "kind": "DeleteOptions",
        "apiVersion": "v1",
        "propagationPolicy": "Background"
    }
    ```


## Response<a name="section53305210"></a>

**Response parameters:**

For the description about response parameters, see  [Table 2](deleting-a-secret.md#table13766144711235).

**Example response:**

```
{
    "kind": "Status",
    "apiVersion": "v1",
    "metadata": {},
    "status": "Success",
    "code": 200
}
```

## Status Code<a name="section9984849"></a>

[Table 2](#d0e38393)  describes the status code of this API.

**Table  2**  Status code

<a name="d0e38393"></a>
<table><thead align="left"><tr id="row39018542"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p6385371"><a name="p6385371"></a><a name="p6385371"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p47453032"><a name="p47453032"></a><a name="p47453032"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18490365"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p21324611"><a name="p21324611"></a><a name="p21324611"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p49571937"><a name="p49571937"></a><a name="p49571937"></a>Delete a StatefulSet resource object successfully.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Code](status-code.md).


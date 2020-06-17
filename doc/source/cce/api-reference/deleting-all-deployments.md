# Deleting All Deployments<a name="cce_02_0122"></a>

## Function<a name="section58759520"></a>

This API is used to delete collection of Deployment.

## URI<a name="section59073635"></a>

DELETE /apis/apps/v1/namespaces/\{namespace\}/deployments \(Supports only1.9\)

DELETE /apis/apps/v1beta1/namespaces/\{namespace\}/deployments \(Supports only1.7\)

DELETE /apis/extensions/v1beta1/namespaces/\{namespace\}/deployments \(Compatible\)

[Table 1](#d0e35322)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="d0e35322"></a>
<table><thead align="left"><tr id="row32289194"><th class="cellrowborder" valign="top" width="22.45%" id="mcps1.2.4.1.1"><p id="p65652297517"><a name="p65652297517"></a><a name="p65652297517"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.33%" id="mcps1.2.4.1.2"><p id="p165661629135114"><a name="p165661629135114"></a><a name="p165661629135114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="61.22%" id="mcps1.2.4.1.3"><p id="p14567629115114"><a name="p14567629115114"></a><a name="p14567629115114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row60766168"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p23112558"><a name="p23112558"></a><a name="p23112558"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.4.1.2 "><p id="p60177946"><a name="p60177946"></a><a name="p60177946"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="61.22%" headers="mcps1.2.4.1.3 "><p id="p42575425"><a name="p42575425"></a><a name="p42575425"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="row47634511"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p33190205"><a name="p33190205"></a><a name="p33190205"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.4.1.2 "><p id="p4052059"><a name="p4052059"></a><a name="p4052059"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61.22%" headers="mcps1.2.4.1.3 "><p id="p59781329"><a name="p59781329"></a><a name="p59781329"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="row1161053"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p26936459"><a name="p26936459"></a><a name="p26936459"></a>fieldSelector</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.4.1.2 "><p id="p34369574"><a name="p34369574"></a><a name="p34369574"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61.22%" headers="mcps1.2.4.1.3 "><p id="p32472085"><a name="p32472085"></a><a name="p32472085"></a>A selector to restrict the list of returned objects by their fields. Defaults to everything.</p>
</td>
</tr>
<tr id="row23813312"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p49830089"><a name="p49830089"></a><a name="p49830089"></a>includeUninitialized</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.4.1.2 "><p id="p9705370"><a name="p9705370"></a><a name="p9705370"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61.22%" headers="mcps1.2.4.1.3 "><p id="p28784318"><a name="p28784318"></a><a name="p28784318"></a>If true, partially initialized resources are included in the response.</p>
</td>
</tr>
<tr id="row57732278"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p45802961"><a name="p45802961"></a><a name="p45802961"></a>labelSelector</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.4.1.2 "><p id="p19052373"><a name="p19052373"></a><a name="p19052373"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61.22%" headers="mcps1.2.4.1.3 "><p id="p66847208"><a name="p66847208"></a><a name="p66847208"></a>A selector to restrict the list of returned objects by their labels. Defaults to everything.</p>
</td>
</tr>
<tr id="row64753968"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p10580064"><a name="p10580064"></a><a name="p10580064"></a>resourceVersion</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.4.1.2 "><p id="p51678836"><a name="p51678836"></a><a name="p51678836"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61.22%" headers="mcps1.2.4.1.3 "><p id="p25236181"><a name="p25236181"></a><a name="p25236181"></a>When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.</p>
</td>
</tr>
<tr id="row25799037"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p9347259"><a name="p9347259"></a><a name="p9347259"></a>timeoutSeconds</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.4.1.2 "><p id="p18930554"><a name="p18930554"></a><a name="p18930554"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61.22%" headers="mcps1.2.4.1.3 "><p id="p56979938"><a name="p56979938"></a><a name="p56979938"></a>Timeout for the list/watch call.</p>
</td>
</tr>
<tr id="row43057396"><td class="cellrowborder" valign="top" width="22.45%" headers="mcps1.2.4.1.1 "><p id="p65097067"><a name="p65097067"></a><a name="p65097067"></a>watch</p>
</td>
<td class="cellrowborder" valign="top" width="16.33%" headers="mcps1.2.4.1.2 "><p id="p38371103"><a name="p38371103"></a><a name="p38371103"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="61.22%" headers="mcps1.2.4.1.3 "><p id="p21051639"><a name="p21051639"></a><a name="p21051639"></a>Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section61900675"></a>

**Request parameters:**

For the description about request parameters, see  [Table 2](deleting-a-daemonset.md#table191461259175715).

**Example request:**

-   Deleting only the Deployment \(the ReplicaSet and pod are not deleted\):

    ```
    {
        "Kind": "DeleteOptions",
        "apiVersion": "v1",
        "propagationPolicy": "Orphan"
    }
    ```

-   Deleting the pod, ReplicaSet and then the Deployment:

    ```
    {
        "kind": "DeleteOptions",
        "apiVersion": "v1",
        "propagationPolicy": "Foreground"
    }
    ```

-   Deleting the Deployment, ReplicaSet and then the pod:

    ```
    {
        "kind": "DeleteOptions",
        "apiVersion": "v1",
        "propagationPolicy": "Background"
    }
    ```


## Response<a name="section20235168"></a>

**Response parameters:**

For the description about response parameters, see  [Table 2](creating-a-deployment.md#table12862324102610).

**Example response:**

```
{
    "kind": "DeploymentList",
    "apiVersion": "apps/v1beta1",
    "metadata": {
        "selfLink": "/apis/apps/v1beta1/namespaces/ns-12130306-s/deployments",
        "resourceVersion": "418745"
    },
    "items": null
}
```

## Status Code<a name="section47898787"></a>

[Table 2](#d0e35450)  describes the status code of this API.

**Table  2**  Status code

<a name="d0e35450"></a>
<table><thead align="left"><tr id="row7535426"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p6389758"><a name="p6389758"></a><a name="p6389758"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p47808350"><a name="p47808350"></a><a name="p47808350"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row47271114"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p3755051"><a name="p3755051"></a><a name="p3755051"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p35723753"><a name="p35723753"></a><a name="p35723753"></a>Delete a Deployment resource object successfully.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Code](status-code.md).


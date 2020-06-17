# Reading a Specified ConfigMap<a name="cce_02_0172"></a>

## Function<a name="section55356496"></a>

This API is used to read a specified ConfigMap resource object.

## URI<a name="section28446419"></a>

GET /api/v1/namespaces/\{namespace\}/configmaps/\{name\}

[Table 1](#d0e43679)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="d0e43679"></a>
<table><thead align="left"><tr id="row18163667"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p65652297517"><a name="p65652297517"></a><a name="p65652297517"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="30.303030303030305%" id="mcps1.2.4.1.2"><p id="p165661629135114"><a name="p165661629135114"></a><a name="p165661629135114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="36.36363636363636%" id="mcps1.2.4.1.3"><p id="p14567629115114"><a name="p14567629115114"></a><a name="p14567629115114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row32810792"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p40428502"><a name="p40428502"></a><a name="p40428502"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.2 "><p id="p53483269"><a name="p53483269"></a><a name="p53483269"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.4.1.3 "><p id="p37177565"><a name="p37177565"></a><a name="p37177565"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="row66162631"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p57572910"><a name="p57572910"></a><a name="p57572910"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.2 "><p id="p32894162"><a name="p32894162"></a><a name="p32894162"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.4.1.3 "><p id="p47181466"><a name="p47181466"></a><a name="p47181466"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="row21980015"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p35550825"><a name="p35550825"></a><a name="p35550825"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.2 "><p id="p61044604"><a name="p61044604"></a><a name="p61044604"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.4.1.3 "><p id="p45665871"><a name="p45665871"></a><a name="p45665871"></a>Name of the Pod.</p>
</td>
</tr>
<tr id="row8339656"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p4423518"><a name="p4423518"></a><a name="p4423518"></a>exact</p>
</td>
<td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.2 "><p id="p22760714"><a name="p22760714"></a><a name="p22760714"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.4.1.3 "><p id="p31678513"><a name="p31678513"></a><a name="p31678513"></a>Should the export be exact. Exact export maintains cluster-specific fields like 'Namespace'.</p>
</td>
</tr>
<tr id="row16671167"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p8187309"><a name="p8187309"></a><a name="p8187309"></a>export</p>
</td>
<td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.2 "><p id="p59192267"><a name="p59192267"></a><a name="p59192267"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="36.36363636363636%" headers="mcps1.2.4.1.3 "><p id="p29844289"><a name="p29844289"></a><a name="p29844289"></a>Should this value be exported. Export strips fields that a user cannot specify.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section54691182"></a>

N/A

## Response<a name="section22458594"></a>

**Response parameters**:

For the description about response parameters, see  [Table 3](data-structure-of-response-parameters.md#en-us_topic_0079614930_table52931650).

**Example response**:

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

## Status Code<a name="section800761"></a>

[Table 2](#d0e43778)  describes the status code of this API.

**Table  2**  Status code

<a name="d0e43778"></a>
<table><thead align="left"><tr id="row4687938"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p44178660"><a name="p44178660"></a><a name="p44178660"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p21701723"><a name="p21701723"></a><a name="p21701723"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13009167"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p47109607"><a name="p47109607"></a><a name="p47109607"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p57781836"><a name="p57781836"></a><a name="p57781836"></a>This operation succeeds, and a ConfigMap resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see section  [Status Code](status-code.md).


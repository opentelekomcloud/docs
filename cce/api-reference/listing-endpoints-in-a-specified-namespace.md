# Listing Endpoints in a Specified Namespace<a name="cce_02_0064"></a>

## Function<a name="s929c7f68195e496187ed769a50539e04"></a>

This API is used to obtain all endpoints in a specified namespace.

## URI<a name="s3de16f9dad264ecd9bc63f9ea6344f66"></a>

GET /api/v1/namespaces/\{namespace\}/endpoints

[Table 1](#en-us_topic_0079615068_table59737867)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="en-us_topic_0079615068_table59737867"></a>
<table><thead align="left"><tr id="en-us_topic_0079615068_row56122452"><th class="cellrowborder" valign="top" width="33%" id="mcps1.2.4.1.1"><p id="en-us_topic_0079615068_p49624734"><a name="en-us_topic_0079615068_p49624734"></a><a name="en-us_topic_0079615068_p49624734"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p20000134201651"><a name="p20000134201651"></a><a name="p20000134201651"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="42%" id="mcps1.2.4.1.3"><p id="p9398121201651"><a name="p9398121201651"></a><a name="p9398121201651"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079615068_row42819751"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615068_p45847827"><a name="en-us_topic_0079615068_p45847827"></a><a name="en-us_topic_0079615068_p45847827"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615068_p22686540"><a name="en-us_topic_0079615068_p22686540"></a><a name="en-us_topic_0079615068_p22686540"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079615068_p25670457"><a name="en-us_topic_0079615068_p25670457"></a><a name="en-us_topic_0079615068_p25670457"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="en-us_topic_0079615068_row29707527"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615068_p57499486"><a name="en-us_topic_0079615068_p57499486"></a><a name="en-us_topic_0079615068_p57499486"></a>labelSelector</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615068_p26946781"><a name="en-us_topic_0079615068_p26946781"></a><a name="en-us_topic_0079615068_p26946781"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079615068_p35205677"><a name="en-us_topic_0079615068_p35205677"></a><a name="en-us_topic_0079615068_p35205677"></a>A selector to restrict the list of returned objects by their labels. Defaults to everything.</p>
</td>
</tr>
<tr id="en-us_topic_0079615068_row48415643"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615068_p29352999"><a name="en-us_topic_0079615068_p29352999"></a><a name="en-us_topic_0079615068_p29352999"></a>fieldSelector</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615068_p28782679"><a name="en-us_topic_0079615068_p28782679"></a><a name="en-us_topic_0079615068_p28782679"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079615068_p49695635"><a name="en-us_topic_0079615068_p49695635"></a><a name="en-us_topic_0079615068_p49695635"></a>A selector to restrict the list of returned objects by their fields. Defaults to everything.</p>
</td>
</tr>
<tr id="rf157bc9241714a0baab6571a8293ed96"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615068_p195946478489"><a name="en-us_topic_0079615068_p195946478489"></a><a name="en-us_topic_0079615068_p195946478489"></a>includeUninitialized</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="a11962462ff4f440c914e2e1dbff49096"><a name="a11962462ff4f440c914e2e1dbff49096"></a><a name="a11962462ff4f440c914e2e1dbff49096"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p id="af7a03c50244f4d06a1b3cfe72137392d"><a name="af7a03c50244f4d06a1b3cfe72137392d"></a><a name="af7a03c50244f4d06a1b3cfe72137392d"></a>If true, partially initialized resources are included in the response.</p>
</td>
</tr>
<tr id="en-us_topic_0079615068_row44607538"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615068_p56440812"><a name="en-us_topic_0079615068_p56440812"></a><a name="en-us_topic_0079615068_p56440812"></a>watch</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615068_p8303079"><a name="en-us_topic_0079615068_p8303079"></a><a name="en-us_topic_0079615068_p8303079"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079615068_p1460811"><a name="en-us_topic_0079615068_p1460811"></a><a name="en-us_topic_0079615068_p1460811"></a>Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.</p>
</td>
</tr>
<tr id="en-us_topic_0079615068_row13147299"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615068_p58298294"><a name="en-us_topic_0079615068_p58298294"></a><a name="en-us_topic_0079615068_p58298294"></a>resourceVersion</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615068_p24541382"><a name="en-us_topic_0079615068_p24541382"></a><a name="en-us_topic_0079615068_p24541382"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079615068_p41694906"><a name="en-us_topic_0079615068_p41694906"></a><a name="en-us_topic_0079615068_p41694906"></a>When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history.</p>
</td>
</tr>
<tr id="en-us_topic_0079615068_row39709837"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615068_p62380243"><a name="en-us_topic_0079615068_p62380243"></a><a name="en-us_topic_0079615068_p62380243"></a>timeoutSeconds</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615068_p19634929"><a name="en-us_topic_0079615068_p19634929"></a><a name="en-us_topic_0079615068_p19634929"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079615068_p46925456"><a name="en-us_topic_0079615068_p46925456"></a><a name="en-us_topic_0079615068_p46925456"></a>Timeout for the list/watch call.</p>
</td>
</tr>
<tr id="en-us_topic_0079615068_row19675928"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615068_p50246298"><a name="en-us_topic_0079615068_p50246298"></a><a name="en-us_topic_0079615068_p50246298"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615068_p43418353"><a name="en-us_topic_0079615068_p43418353"></a><a name="en-us_topic_0079615068_p43418353"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079615068_p27225733"><a name="en-us_topic_0079615068_p27225733"></a><a name="en-us_topic_0079615068_p27225733"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="sef5c2e860abe4851bf5e58fb868633d9"></a>

N/A

## Response<a name="sd91f7b136258433a922cbc821ade2d1f"></a>

**Response parameters:**

For the description about response parameters, see  [Table 2](listing-endpoints.md#en-us_topic_0079614910_ref458760085).

**Example response:**

```
{
    "kind": "EndpointsList",
    "apiVersion": "v1",
    "metadata": {
        "selfLink": "/api/v1/namespaces/default/endpoints",
        "resourceVersion": "598704"
    },
    "items": [
        {
            "metadata": {
                "name": "kubernetes",
                "namespace": "default",
                "selfLink": "/api/v1/namespaces/default/endpoints/kubernetes",
                "uid": "64593b5d-f83d-11e7-9c3c-fa163eb8ad1a",
                "resourceVersion": "49",
                "creationTimestamp": "2018-01-13T08:40:21Z",
                "enable": true
            },
            "subsets": [
                {
                    "addresses": [
                        {
                            "ip": "192.168.0.64"
                        }
                    ],
                    "ports": [
                        {
                            "name": "https",
                            "port": 5444,
                            "protocol": "TCP"
                        }
                    ]
                }
            ]
        }
    ]
}
```

## Status Code<a name="s1736c40a8a6e4e3dab0ee276f7614231"></a>

[Table 2](#en-us_topic_0079615068_table769899)  describes the status code of this API.

**Table  2**  Status code

<a name="en-us_topic_0079615068_table769899"></a>
<table><thead align="left"><tr id="en-us_topic_0079615068_row22998005"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p11007541201651"><a name="p11007541201651"></a><a name="p11007541201651"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p19195629201651"><a name="p19195629201651"></a><a name="p19195629201651"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079615068_row15320653"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0079615068_p33013406"><a name="en-us_topic_0079615068_p33013406"></a><a name="en-us_topic_0079615068_p33013406"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0079615068_p56840268"><a name="en-us_topic_0079615068_p56840268"></a><a name="en-us_topic_0079615068_p56840268"></a>This operation succeeds, and a group of Endpoint resource objects is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Code](status-code.md).


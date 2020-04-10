# Updating a Specified NetworkPolicy<a name="cce_02_0277"></a>

## Function<a name="section195161234135216"></a>

This API is used to partially update a specified NetworkPolicy.

The following fields can be updated:

-   metadata.name
-   metadata.namespace
-   metadata.selfLink
-   metadata.resourceVersion
-   metadata.generation
-   metadata.uid
-   metadata.creationTimestamp
-   metadata.deletionTimestamp
-   metadata.labels
-   metadata.annotations
-   spec.ingress

## URL<a name="section5845143395718"></a>

PATCH /apis/networking.k8s.io/v1/namespaces/\{namespace\}/networkpolicies/\{name\}

[Table 1](#d0e42906)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="d0e42906"></a>
<table><thead align="left"><tr id="row10640301"><th class="cellrowborder" valign="top" width="22.220000000000002%" id="mcps1.2.4.1.1"><p id="p65652297517"><a name="p65652297517"></a><a name="p65652297517"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.4.1.2"><p id="p165661629135114"><a name="p165661629135114"></a><a name="p165661629135114"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="60.61%" id="mcps1.2.4.1.3"><p id="p14567629115114"><a name="p14567629115114"></a><a name="p14567629115114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row10781191719208"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p19781117112019"><a name="p19781117112019"></a><a name="p19781117112019"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p578231710205"><a name="p578231710205"></a><a name="p578231710205"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p978261710207"><a name="p978261710207"></a><a name="p978261710207"></a>Name of the NetworkPolicy.</p>
</td>
</tr>
<tr id="row19095777"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p3254085"><a name="p3254085"></a><a name="p3254085"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p62254326"><a name="p62254326"></a><a name="p62254326"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p9435611"><a name="p9435611"></a><a name="p9435611"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="row17811636"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p33456451"><a name="p33456451"></a><a name="p33456451"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p25618043"><a name="p25618043"></a><a name="p25618043"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p61795587"><a name="p61795587"></a><a name="p61795587"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="row26391471649"><td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.1 "><p id="p14640471145"><a name="p14640471145"></a><a name="p14640471145"></a>body</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p064011716413"><a name="p064011716413"></a><a name="p064011716413"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60.61%" headers="mcps1.2.4.1.3 "><p id="p46408710414"><a name="p46408710414"></a><a name="p46408710414"></a>-</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section1097017235815"></a>

**Request parameters:**

For the description about request parameters, see  [Table 2](creating-a-networkpolicy.md#d0e42951).

For the description about the  **Content-Type**  field, see  [Patch Request Method Operation Description](patch-request-method-operation-description.md).

**Example request:**

```
Content-Type: application/merge-patch+json
{
    "spec": {
        "ingress": [{
            "from": [{
                "podSelector": {
                    "matchLabels": {
			"app": "nginx2"
	            }
                 }
             }]
        }]
     }
}  
```

## Response<a name="section13598181712916"></a>

**Response parameters:**

For the description about response parameters, see  [Table 2](creating-a-networkpolicy.md#d0e42951).

**Example response:**

```
{
    "kind": "NetworkPolicy",
    "apiVersion": "networking.k8s.io/v1",
    "metadata": {
	    "name": "test-network-policy",
		"namespace": "default",
		"selfLink": "/apis/networking.k8s.io/v1/namespaces/default/networkpolicies/test-network-policy",
		"uid": "be347ddd-e8af-11e8-b187-fa163e3cca63",
		"resourceVersion": "213982",
		"generation": 1,
		"creationTimestamp": "2018-11-15T08:23:34Z",
            "labels": {
		"app": "nginx"
			}
	},
    "spec": {
	    "podSelector": {
		"matchLabels": {
		    "app": "nginx"
		    }
	    },
	    "ingress": [{
		"from": [{
		    "podSelector": {
		        "matchLabels": {
			    "app": "nginx2"
				    }
			    }
		}],
	    "ports": [{
	        "protocol": "TCP",
		"port": 6379
		}]
	    }],
	    "policyTypes":[
		"Ingress"
        ]
    }
}
```

## Status Code<a name="section14947131610112"></a>

[Table 2](#d0e43055)  describes the status code of this API.

**Table  2**  Status Code

<a name="d0e43055"></a>
<table><thead align="left"><tr id="row20813512"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p8172937"><a name="p8172937"></a><a name="p8172937"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p58028199"><a name="p58028199"></a><a name="p58028199"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2663689"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p14432280"><a name="p14432280"></a><a name="p14432280"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p13489144118012"><a name="p13489144118012"></a><a name="p13489144118012"></a>OK</p>
</td>
</tr>
</tbody>
</table>


# Updating a Specified ReplicationController<a name="cce_02_0023"></a>

## Function<a name="s615bc0b56fbf44b6a8f921b400a80a30"></a>

This API is used to update a ReplicationController object under a specified Namespace.

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
-   template.contaions
-   spec.restartPolicy
-   spec.activeDeadlineSeconds

## URI<a name="s1fa3f000cd23422083df6d59217fcd93"></a>

PATCH /api/v1/namespaces/\{namespace\}/replicationcontrollers/\{name\}

[Table 1](#table065881717820)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="table065881717820"></a>
<table><thead align="left"><tr id="row1765915171683"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p196590171983"><a name="p196590171983"></a><a name="p196590171983"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p13659117782"><a name="p13659117782"></a><a name="p13659117782"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p116591617686"><a name="p116591617686"></a><a name="p116591617686"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6659517586"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p36595174813"><a name="p36595174813"></a><a name="p36595174813"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p365911713818"><a name="p365911713818"></a><a name="p365911713818"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p865914177813"><a name="p865914177813"></a><a name="p865914177813"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="row196598171889"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p765915171488"><a name="p765915171488"></a><a name="p765915171488"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p46601017882"><a name="p46601017882"></a><a name="p46601017882"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p7660161719818"><a name="p7660161719818"></a><a name="p7660161719818"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="row206606170811"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p7660191717818"><a name="p7660191717818"></a><a name="p7660191717818"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p126602017181"><a name="p126602017181"></a><a name="p126602017181"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p16660191711815"><a name="p16660191711815"></a><a name="p16660191711815"></a>Name of the ReplicationController.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="scb1fe2c0ceef4190939652221c118528"></a>

**Request parameters:**

For the description about the  **Content-Type**  message header, see section  [Patch Request Method Operation Description](patch-request-method-operation-description.md).

For the description about request parameters, see  [Table 1](data-structure-of-request-parameters.md#en-us_topic_0079614925_table51284307).

**Example request:**

```
Content-Type: application/strategic-merge-patch+json
```

```
 { 
   "spec": { 
         "template": { 
             "spec": { 
                 "containers": [ 
                     { 
                         "name": "hello-world", 
                         "image": "busybox:latest" 
                     }, 
                     { 
                         "name": "hello", 
                         "image": "busybox:latest" 
                     } 
                 ] 
             } 
         } 
     } 
 }
```

## Response<a name="en-us_topic_0079615044_section988213"></a>

**Response parameters:**

For the description about response parameters, see  [Table 1](data-structure-of-response-parameters.md#en-us_topic_0079614930_table30479638).

**Example response:**

```
{ 
   "kind": "ReplicationController", 
   "apiVersion": "v1", 
   "metadata": { 
     "name": "frontend-controller", 
     "namespace": "default", 
     "selfLink": "/api/v1/namespaces/default/replicationcontrollers/frontend-controller", 
     "uid": "cd4594b6-5d0b-11e6-aeb9-286ed488fafe", 
     "resourceVersion": "1658", 
     "generation": 2, 
     "creationTimestamp": "2016-08-08T01:59:55Z", 
     "labels": { 
       "app": "nginx" 
     } 
   }, 
   "spec": { 
     "replicas": 2, 
     "selector": { 
       "app": "nginx" 
     }, 
     "template": { 
       "metadata": { 
         "creationTimestamp": null, 
         "labels": { 
       "app": "nginx" 
     } 
   }, 
       "spec": { 
         "containers": [ 
         { 
             "name": "hello-world", 
             "image": "busybox:latest", 
             "resources": {}, 
             "terminationMessagePath": "/dev/termination-log", 
             "imagePullPolicy": "Always" 
           }, 
           { 
             "name": "hello", 
             "image": "busybox:latest", 
             "resources": {}, 
             "terminationMessagePath": "/dev/termination-log", 
             "imagePullPolicy": "Always" 
           } 
         ], 
         "restartPolicy": "Always", 
         "terminationGracePeriodSeconds": 30, 
         "dnsPolicy": "ClusterFirst", 
         "securityContext": {} 
       } 
     } 
   }, 
   "status": { 
     "replicas": 2, 
     "fullyLabeledReplicas": 2, 
     "observedGeneration": 1 
   } 
 }
```

## Status Code<a name="s6211e732eeb946dcb43c007e90829a94"></a>

[Table 2](#en-us_topic_0079615044_table29947515)  describes the status code of this API.

**Table  2**  Status code

<a name="en-us_topic_0079615044_table29947515"></a>
<table><thead align="left"><tr id="en-us_topic_0079615044_row41083762"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p64069331195026"><a name="p64069331195026"></a><a name="p64069331195026"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p22233337195026"><a name="p22233337195026"></a><a name="p22233337195026"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079615044_row62212303"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0079615044_p6031802"><a name="en-us_topic_0079615044_p6031802"></a><a name="en-us_topic_0079615044_p6031802"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p97444480817"><a name="p97444480817"></a><a name="p97444480817"></a>This operation succeeds, and a ReplicationController resource object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about status codes, see section  [Status Code](status-code.md).


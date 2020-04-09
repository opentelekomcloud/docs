# Replacing the Status of a Specified Pod<a name="cce_02_0038"></a>

## Function<a name="s14b3085e84f44f248c15900b7a9ae75e"></a>

This API is used to replace the status of a pod in a specified namespace, that is, to change the status value of the pod.

## URI<a name="s2146020c33a84ca5aa9bc6e54586edc9"></a>

PUT /api/v1/namespaces/\{namespace\}/pods/\{name\}/status

[Table 1](#en-us_topic_0079614908_table13708463)  describes the parameters of this API.

**Table  1**  Parameter description

<a name="en-us_topic_0079614908_table13708463"></a>
<table><thead align="left"><tr id="en-us_topic_0079614908_row53056665"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0079614908_p2622637"><a name="en-us_topic_0079614908_p2622637"></a><a name="en-us_topic_0079614908_p2622637"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p25672384203057"><a name="p25672384203057"></a><a name="p25672384203057"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p66197242203057"><a name="p66197242203057"></a><a name="p66197242203057"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079614908_row60209123"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079614908_p45100793"><a name="en-us_topic_0079614908_p45100793"></a><a name="en-us_topic_0079614908_p45100793"></a>pretty</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079614908_p29285587"><a name="en-us_topic_0079614908_p29285587"></a><a name="en-us_topic_0079614908_p29285587"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079614908_p23322329"><a name="en-us_topic_0079614908_p23322329"></a><a name="en-us_topic_0079614908_p23322329"></a>If 'true', then the output is pretty printed.</p>
</td>
</tr>
<tr id="en-us_topic_0079614908_row16574033"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079614908_p319438"><a name="en-us_topic_0079614908_p319438"></a><a name="en-us_topic_0079614908_p319438"></a>namespace</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079614908_p25874536"><a name="en-us_topic_0079614908_p25874536"></a><a name="en-us_topic_0079614908_p25874536"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079614908_p15462662"><a name="en-us_topic_0079614908_p15462662"></a><a name="en-us_topic_0079614908_p15462662"></a>Object name and auth scope, such as for teams and projects.</p>
</td>
</tr>
<tr id="en-us_topic_0079614908_row4946234"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079614908_p65100698"><a name="en-us_topic_0079614908_p65100698"></a><a name="en-us_topic_0079614908_p65100698"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079614908_p38665203"><a name="en-us_topic_0079614908_p38665203"></a><a name="en-us_topic_0079614908_p38665203"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0079614908_p44873708"><a name="en-us_topic_0079614908_p44873708"></a><a name="en-us_topic_0079614908_p44873708"></a>Name of the Pod.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0079614908_ref458608140"></a>

**Request parameters:**

For the description about request parameters, see  [Table 3](data-structure-of-response-parameters.md#en-us_topic_0079614930_table52931650).

**Example request:**

```
{ 
     "kind": "Pod", 
     "apiVersion": "v1", 
     "metadata": { 
         "name": "hello-world", 
         "namespace": "default", 
         "selfLink": "/api/v1/namespaces/default/pods/hello-world", 
         "uid": "84973056-5d3b-11e6-aeb9-286ed488fafe", 
         "resourceVersion": "3636", 
         "creationTimestamp": "2016-08-08T07:41:29Z", 
         "labels": { 
             "name": "brace" 
         } 
     }, 
     "status": { 
         "phase": "Running", 
         "conditions": [ 
             { 
                 "type": "Ready", 
                 "status": "True", 
                 "lastProbeTime": null, 
                 "lastTransitionTime": "2016-08-08T07:41:29Z" 
             } 
         ], 
         "hostIP": "127.0.0.1", 
         "podIP": "172.16.0.4", 
         "startTime": "2016-08-08T07:41:29Z" 
   } 
 }
```

## Response<a name="s279a234cda4443f0afa7d8de9b799a5a"></a>

**Response parameters:**

For the description about response parameters, see  [Request](#en-us_topic_0079614908_ref458608140).

**Example response:**

```
{ 
   "kind": "Pod", 
   "apiVersion": "v1", 
   "metadata": { 
     "name": "hello-world", 
     "namespace": "default", 
     "selfLink": "/api/v1/namespaces/default/pods/hello-world/status", 
     "uid": "84973056-5d3b-11e6-aeb9-286ed488fafe", 
     "resourceVersion": "3641", 
     "creationTimestamp": "2016-08-08T07:41:29Z", 
   "labels": { 
       "name": "brace" 
     } 
   }, 
   "spec": { 
     "volumes": [ 
       { 
         "name": "test", 
         "emptyDir": {} 
       }, 
       { 
         "name": "default-token-test2", 
         "secret": { 
           "secretName": "default-token-test2" 
         } 
       } 
     ], 
     "containers": [ 
       { 
         "name": "hello-world", 
         "image": "beego:v1", 
         "env": [ 
           { 
             "name": "cy", 
             "value": "cy" 
           } 
         ], 
         "resources": {}, 
         "volumeMounts": [ 
           { 
             "name": "test", 
             "mountPath": "/tmp/foo" 
           }, 
           { 
             "name": "default-token-test2", 
             "readOnly": true, 
             "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount" 
           } 
         ], 
         "terminationMessagePath": "/dev/termination-log", 
         "imagePullPolicy": "IfNotPresent" 
       } 
     ], 
     "restartPolicy": "Always", 
     "terminationGracePeriodSeconds": 30, 
     "dnsPolicy": "ClusterFirst", 
     "serviceAccountName": "default", 
     "serviceAccount": "default", 
     "nodeName": "127.0.0.1", 
     "securityContext": {} 
   }, 
   "status": { 
     "phase": "Running", 
     "conditions": [ 
       { 
         "type": "Ready", 
         "status": "True", 
         "lastProbeTime": null, 
         "lastTransitionTime": "2016-08-08T07:41:29Z" 
       } 
     ], 
     "hostIP": "127.0.0.1", 
     "podIP": "172.16.0.4", 
     "startTime": "2016-08-08T07:41:29Z" 
   } 
 }
```

## Status Code<a name="s8a2da3e1bb8a49d2af7cf2027ab3fea0"></a>

[Table 2](#en-us_topic_0079614908_table56267310)  describes the status code of this API.

**Table  2**  Status code

<a name="en-us_topic_0079614908_table56267310"></a>
<table><thead align="left"><tr id="en-us_topic_0079614908_row31065142"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p26385296203057"><a name="p26385296203057"></a><a name="p26385296203057"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p56834228203057"><a name="p56834228203057"></a><a name="p56834228203057"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0079614908_row39832915"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0079614908_p5240702"><a name="en-us_topic_0079614908_p5240702"></a><a name="en-us_topic_0079614908_p5240702"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0079614908_p21843730"><a name="en-us_topic_0079614908_p21843730"></a><a name="en-us_topic_0079614908_p21843730"></a>This operation succeeds, and the JSON of a Pod object is returned.</p>
</td>
</tr>
</tbody>
</table>

For the description about error status codes, see  [Status Code](status-code.md).


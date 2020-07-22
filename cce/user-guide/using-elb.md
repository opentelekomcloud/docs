# Using ELB<a name="cce_01_0148"></a>

Charts support the ELB service. The definition method is the same as that of the Kubernetes community.

To display the ELB information on the CCE console, add the annotation to the chart of the corresponding resource type.

```
apiVersion: apps/v1beta1
kind: StatefulSet
metadata:
  name: {{ .Release.Name }}-master
  annotations:
    "service.protal.kubernetes.io/access-ip": "10.4.4.14:8888"
    "service.protal.kubernetes.io/type": LoadBalancer
spec:
......
```

**Table  1**  Key parameters

<a name="t4057e0d2c18e4bcdad29f13997228056"></a>
<table><thead align="left"><tr id="r8d0a4897353048709c4aa962889bc538"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.3.1.1"><p id="ae2df68d587514cf696be05ad07ea8935"><a name="ae2df68d587514cf696be05ad07ea8935"></a><a name="ae2df68d587514cf696be05ad07ea8935"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="78%" id="mcps1.2.3.1.2"><p id="aa32ca93b099b452abcb87874d30dbea0"><a name="aa32ca93b099b452abcb87874d30dbea0"></a><a name="aa32ca93b099b452abcb87874d30dbea0"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r4b6a2afe1b5f461baed2d98d90e0d076"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.3.1.1 "><p id="addf873143dc44d089a15afc6bc713139"><a name="addf873143dc44d089a15afc6bc713139"></a><a name="addf873143dc44d089a15afc6bc713139"></a>*annotations</p>
</td>
<td class="cellrowborder" valign="top" width="78%" headers="mcps1.2.3.1.2 "><p id="a243aba01af4940cea5e913682f0cb550"><a name="a243aba01af4940cea5e913682f0cb550"></a><a name="a243aba01af4940cea5e913682f0cb550"></a>Used for console display. <strong id="b873370172154646"><a name="b873370172154646"></a><a name="b873370172154646"></a>service.protal.kubernetes.io/access-ip</strong> indicates the IP address and exposed port number of the load balancer. The value of <strong id="b13879724154652"><a name="b13879724154652"></a><a name="b13879724154652"></a>service.protal.kubernetes.io/type</strong> is fixed at <strong id="b1253319477154652"><a name="b1253319477154652"></a><a name="b1253319477154652"></a>LoadBalancer</strong>.</p>
</td>
</tr>
</tbody>
</table>


# OS::Heat::CloudConfig<a name="EN-US_TOPIC_0088407213"></a>

A configuration resource for representing cloud-init cloud-config.

This resource allows cloud-config YAML to be defined and stored by the config API. Any intrinsic functions called in the config will be resolved before storing the result.

This resource will generally be referenced by OS::Nova::Server user\_data, or OS::Heat::MultipartMime parts config. Since cloud-config is boot-only configuration, any changes to the definition will result in the replacement of all servers which reference it.

## Optional Properties<a name="section6598152618415"></a>

<a name="table14260243133815"></a>
<table><thead align="left"><tr id="row10424104375912"><th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.1.3.1.1"><p id="p92611043163811"><a name="p92611043163811"></a><a name="p92611043163811"></a><strong id="b11777116014"><a name="b11777116014"></a><a name="b11777116014"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.1.3.1.2"><p id="p8261184310386"><a name="p8261184310386"></a><a name="p8261184310386"></a><strong id="b41781017011"><a name="b41781017011"></a><a name="b41781017011"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1642454315910"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p3261543173812"><a name="p3261543173812"></a><a name="p3261543173812"></a>cloud_config</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p61320792"><a name="p61320792"></a><a name="p61320792"></a>Map representing the cloud-config data structure which will be formatted as YAML.</p>
<p id="p15016217"><a name="p15016217"></a><a name="p15016217"></a>Map value expected.</p>
<p id="p928228"><a name="p928228"></a><a name="p928228"></a>Updates cause replacement.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section62627172424"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Heat::CloudConfig
    properties:
      cloud_config: {...}
```


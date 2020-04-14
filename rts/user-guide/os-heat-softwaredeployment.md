# OS::Heat::SoftwareDeployment<a name="EN-US_TOPIC_0088407125"></a>

This resource associates a server with some configuration.

The configuration is to be deployed to that server.

A deployment allows input values to be specified which map to the inputs schema defined in the config resource. These input values are interpreted by the configuration tool in a tool-specific manner.

Whenever this resource goes to an IN\_PROGRESS state, it creates an ephemeral config that includes the inputs values plus a number of extra inputs which have names prefixed with  [deploy\_](http://docs.openstack.org/developer/heat/template_guide/openstack.html#id1). The extra inputs relate to the current state of the stack, along with the information and credentials required to signal back the deployment results.

Unless signal\_transport=NO\_SIGNAL, this resource will remain in an IN\_PROGRESS state until the server signals it with the output values for that deployment. Those output values are then available as resource attributes, along with the default attributes deploy\_stdout, deploy\_stderr and deploy\_status\_code.

Specifying actions other than the default CREATE and UPDATE will result in the deployment being triggered in those actions. For example this would allow cleanup configuration to be performed during action DELETE. A config could be designed to only work with some specific actions, or a config can read the value of the deploy\_action input to allow conditional logic to perform different configuration for different actions.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If the software deployment function is used, the cloud-init, heat-config, os-collect-config, os-refresh-config, os-apply-config, and heat-config-script tools must be installed on images.  

## Optional Properties<a name="section99570357293"></a>

<a name="table7994151543015"></a>
<table><thead align="left"><tr id="row7625104145315"><th class="cellrowborder" valign="top" width="33%" id="mcps1.1.3.1.1"><p id="p1599491513010"><a name="p1599491513010"></a><a name="p1599491513010"></a><strong id="b87191421125318"><a name="b87191421125318"></a><a name="b87191421125318"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.3.1.2"><p id="p17994171503014"><a name="p17994171503014"></a><a name="p17994171503014"></a><strong id="b1172082119533"><a name="b1172082119533"></a><a name="b1172082119533"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2625543538"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p7825164755916"><a name="p7825164755916"></a><a name="p7825164755916"></a>actions</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p44563818"><a name="p44563818"></a><a name="p44563818"></a>Which lifecycle actions of the deployment resource will result in this deployment being triggered.</p>
<p id="p65530045"><a name="p65530045"></a><a name="p65530045"></a>List value expected.</p>
<p id="p52899501"><a name="p52899501"></a><a name="p52899501"></a>Can be updated without replacement.</p>
<p id="p6333466"><a name="p6333466"></a><a name="p6333466"></a>Defaults to "[CREATE, UPDATE]".</p>
<p id="p299416152302"><a name="p299416152302"></a><a name="p299416152302"></a>Allowed values: CREATE, UPDATE, DELETE</p>
</td>
</tr>
<tr id="row162517405317"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p43248727"><a name="p43248727"></a><a name="p43248727"></a>config</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p53694225"><a name="p53694225"></a><a name="p53694225"></a>ID of software configuration resource to execute when applying to the server.</p>
<p id="p13485980"><a name="p13485980"></a><a name="p13485980"></a>String value expected.</p>
<p id="p699421517304"><a name="p699421517304"></a><a name="p699421517304"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row1462512411537"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p18622610"><a name="p18622610"></a><a name="p18622610"></a>input_values</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p33385767"><a name="p33385767"></a><a name="p33385767"></a>Input values to apply to the software configuration on this server.</p>
<p id="p32036448"><a name="p32036448"></a><a name="p32036448"></a>Map value expected.</p>
<p id="p7994161515300"><a name="p7994161515300"></a><a name="p7994161515300"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row46250416534"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p44815535"><a name="p44815535"></a><a name="p44815535"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p686639"><a name="p686639"></a><a name="p686639"></a>ID of resource to apply configuration to. Normally this should be a Nova server ID.</p>
<p id="p6179751"><a name="p6179751"></a><a name="p6179751"></a>String value expected.</p>
<p id="p4994141583014"><a name="p4994141583014"></a><a name="p4994141583014"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row262554205313"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p168524251975"><a name="p168524251975"></a><a name="p168524251975"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p8744808"><a name="p8744808"></a><a name="p8744808"></a>Name of the derived config associated with this deployment. This is used to apply a sort order to the list of configurations currently deployed to a server.</p>
<p id="p11594415"><a name="p11594415"></a><a name="p11594415"></a>String value expected.</p>
<p id="p3380114316315"><a name="p3380114316315"></a><a name="p3380114316315"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row96257418539"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p66732432"><a name="p66732432"></a><a name="p66732432"></a>signal_transport</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p66571835111517"><a name="p66571835111517"></a><a name="p66571835111517"></a>How the server should signal to heat with the deployment output values.</p>
<a name="ul10531133410159"></a><a name="ul10531133410159"></a><ul id="ul10531133410159"><li>TEMP_URL_SIGNAL will create a Swift TempURL to be signaled via HTTP PUT.</li><li>NO_SIGNAL will result in the resource going to the COMPLETE state without waiting for any signal.</li></ul>
<p id="p63720980"><a name="p63720980"></a><a name="p63720980"></a>String value expected.</p>
<p id="p36617913"><a name="p36617913"></a><a name="p36617913"></a>Updates cause replacement.</p>
<p id="p19460165512158"><a name="p19460165512158"></a><a name="p19460165512158"></a>Defaults to "TEMP_URL_SIGNAL".</p>
<p id="p13261011"><a name="p13261011"></a><a name="p13261011"></a>Allowed values: TEMP_URL_SIGNAL, NO_SIGNAL</p>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section92841445102911"></a>

<a name="table14613114183216"></a>
<table><thead align="left"><tr id="row514019445711"><th class="cellrowborder" valign="top" width="33%" id="mcps1.1.3.1.1"><p id="p1615131413218"><a name="p1615131413218"></a><a name="p1615131413218"></a><strong id="b330816222579"><a name="b330816222579"></a><a name="b330816222579"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.3.1.2"><p id="p761581493219"><a name="p761581493219"></a><a name="p761581493219"></a><strong id="b2309152225710"><a name="b2309152225710"></a><a name="b2309152225710"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row101409412577"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p66161014153215"><a name="p66161014153215"></a><a name="p66161014153215"></a>deploy_status_code</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p176181314103220"><a name="p176181314103220"></a><a name="p176181314103220"></a>Returned status code from the configuration execution.</p>
</td>
</tr>
<tr id="row1014014195714"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p17619111412322"><a name="p17619111412322"></a><a name="p17619111412322"></a>deploy_stderr</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p66212014113210"><a name="p66212014113210"></a><a name="p66212014113210"></a>Captured stderr from the configuration execution.</p>
</td>
</tr>
<tr id="row20140154115714"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p1962214147324"><a name="p1962214147324"></a><a name="p1962214147324"></a>deploy_stdout</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p862351453216"><a name="p862351453216"></a><a name="p862351453216"></a>Captured stdout from the configuration execution.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section663216542299"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Heat::SoftwareDeployment
    properties:
      actions: [Value, Value, ...]
      config: String
      input_values: {...}
      name: String
      server: String
      signal_transport: String
```


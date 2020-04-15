# OS::Heat::MultipartMime<a name="EN-US_TOPIC_0088407131"></a>

Assembles a collection of software configurations as a multi-part mime.

Parts in the message can be populated with inline configuration or references to other config resources. If the referenced resource is itself a valid multi-part mime message, that will be broken into parts and those parts appended to this message.

The resulting multi-part mime message will be stored by the configs API and can be referenced in properties such as OS::Nova::Server user\_data.

This resource is generally used to build a list of cloud-init configuration elements including scripts and cloud-config. Since cloud-init is boot-only configuration, any changes to the definition will result in the replacement of all servers which reference it.

## Optional Properties<a name="section14814122218499"></a>

<a name="table14260243133815"></a>
<table><thead align="left"><tr id="row10424104375912"><th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.1.3.1.1"><p id="p92611043163811"><a name="p92611043163811"></a><a name="p92611043163811"></a><strong id="b11777116014"><a name="b11777116014"></a><a name="b11777116014"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.1.3.1.2"><p id="p8261184310386"><a name="p8261184310386"></a><a name="p8261184310386"></a><strong id="b41781017011"><a name="b41781017011"></a><a name="b41781017011"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1642454315910"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.1.3.1.1 "><p id="p3261543173812"><a name="p3261543173812"></a><a name="p3261543173812"></a>parts</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.1.3.1.2 "><p id="p27601094"><a name="p27601094"></a><a name="p27601094"></a>Parts belonging to this message.</p>
<p id="p47083259"><a name="p47083259"></a><a name="p47083259"></a>List value expected.</p>
<p id="p21096148"><a name="p21096148"></a><a name="p21096148"></a>Updates cause replacement.</p>
<p id="p55647612"><a name="p55647612"></a><a name="p55647612"></a>Defaults to "[]".</p>
<p id="p11162755"><a name="p11162755"></a><a name="p11162755"></a>List contents:</p>
<a name="ul33355931"></a><a name="ul33355931"></a><ul id="ul33355931"><li>*<p id="p54741650456"><a name="p54741650456"></a><a name="p54741650456"></a>Map value expected.</p>
<p id="p69483519513"><a name="p69483519513"></a><a name="p69483519513"></a>Updates cause replacement.</p>
<p id="p193677582051"><a name="p193677582051"></a><a name="p193677582051"></a>Map properties:</p>
<a name="ul1715818511063"></a><a name="ul1715818511063"></a><ul id="ul1715818511063"><li>config<p id="p119271911876"><a name="p119271911876"></a><a name="p119271911876"></a>Content of part to attach, either inline or by referencing the ID of another software config resource.</p>
<p id="p1892917111712"><a name="p1892917111712"></a><a name="p1892917111712"></a>String value expected.</p>
<p id="p392916115712"><a name="p392916115712"></a><a name="p392916115712"></a>Updates cause replacement.</p>
</li><li>filename<p id="p85366291875"><a name="p85366291875"></a><a name="p85366291875"></a>Optional filename to associate with part.</p>
<p id="p85364298715"><a name="p85364298715"></a><a name="p85364298715"></a>String value expected.</p>
<p id="p105371429272"><a name="p105371429272"></a><a name="p105371429272"></a>Updates cause replacement.</p>
</li><li>subtype<p id="p614744512718"><a name="p614744512718"></a><a name="p614744512718"></a>Optional subtype to specify with the type.\</p>
<p id="p81471845170"><a name="p81471845170"></a><a name="p81471845170"></a>String value expected.</p>
<p id="p17148345377"><a name="p17148345377"></a><a name="p17148345377"></a>Updates cause replacement.</p>
</li><li>Type<p id="p286517017816"><a name="p286517017816"></a><a name="p286517017816"></a>Whether the part content is text or multipart.</p>
<p id="p1386530784"><a name="p1386530784"></a><a name="p1386530784"></a>String value expected.</p>
<p id="p7866901089"><a name="p7866901089"></a><a name="p7866901089"></a>Updates cause replacement.</p>
<p id="p48662015815"><a name="p48662015815"></a><a name="p48662015815"></a>Defaults to "text".</p>
<p id="p28671106819"><a name="p28671106819"></a><a name="p28671106819"></a>Allowed values: text, multipart</p>
</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section3949643125910"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Heat::MultipartMime
    properties:
      parts: [{"filename": String, "subtype": String, "config": String, "type": String}, {"filename": String, "subtype": String, "config": String, "type": String}, ...]
```


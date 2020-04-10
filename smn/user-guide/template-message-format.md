# Template Message Format<a name="smn_ug_a2000"></a>

Message templates are used to publish messages with fixed content and use variables as placeholders to represent content that you can change.

The size of template content cannot exceed 256 KB. The following is an example of how to format a template when you manually type the template message content:

```
"message_template_name":"confirm_message",
"tags":{
    "topic_urn":"urn:smn:regionId:xxxx:SMN_01"
     }
```

<a name="table205138417137"></a>
<table><thead align="left"><tr id="row69932217137"><th class="cellrowborder" valign="top" width="34.589999999999996%" id="mcps1.1.3.1.1"><p id="p5664513217137"><a name="p5664513217137"></a><a name="p5664513217137"></a><strong id="b842352706161143"><a name="b842352706161143"></a><a name="b842352706161143"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="65.41%" id="mcps1.1.3.1.2"><p id="p2485300317137"><a name="p2485300317137"></a><a name="p2485300317137"></a><strong id="b842352706193020"><a name="b842352706193020"></a><a name="b842352706193020"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2235043817137"><td class="cellrowborder" valign="top" width="34.589999999999996%" headers="mcps1.1.3.1.1 "><p id="p6555509117137"><a name="p6555509117137"></a><a name="p6555509117137"></a>message_template_name</p>
</td>
<td class="cellrowborder" valign="top" width="65.41%" headers="mcps1.1.3.1.2 "><p id="p836214417137"><a name="p836214417137"></a><a name="p836214417137"></a>Template name, which cannot be left blank. You can query the template name in the template list. You must create a template of the default protocol so that SMN can send messages using the default template once it fails to match a specified protocol.</p>
</td>
</tr>
<tr id="row815043417137"><td class="cellrowborder" valign="top" width="34.589999999999996%" headers="mcps1.1.3.1.1 "><p id="p5620541117137"><a name="p5620541117137"></a><a name="p5620541117137"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="65.41%" headers="mcps1.1.3.1.2 "><p id="p5634440817137"><a name="p5634440817137"></a><a name="p5634440817137"></a>Variables in the template, which are presented as JSON mappings. You can create templates for different protocols using the same template name and configure different variables in each template.</p>
</td>
</tr>
</tbody>
</table>


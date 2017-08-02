## Template Message Format


A message template is used to push messages of a fixed format. You can use tags as placeholders to represent the changeable content.

The template content cannot exceed 256 KB. The following is the template format required when you manually type the template message content:

    "message\_template\_name":"confirm\_message",
    "tags":{
		     "topic\_urn":"urn:smn:regionId:xxxx:SMN\_01"
		     }

<table>
<tr>
<th>Parameter</th>
<th>Description</th>
</tr>
<tr>
<td>message_template_name </td>
<td>Specifies the template name, which cannot be empty. You can query the template name in the template list. You must create a template of the default protocol so that SMN can send messages using the default template once it fails to match a specified protocol. </td>
</tr>
<tr>
<td> tags</td>
<td>Specifies the placeholder in the template, which is presented as a JSON mapping. You can create templates of different protocols using the same template name and configure different tags in each template. </td>
</tr>
</table> 

                                                   
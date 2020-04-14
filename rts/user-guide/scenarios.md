# Scenarios<a name="EN-US_TOPIC_0076468617"></a>

-   To perform operations on a stack using the Heat client, you only need to compile a template file.
-   To perform operations on a stack using the RTS console, you need to not only compile a template file, but also package the file in the required format if you create a stack by uploading a template. However, packaging the template file is not required if you choose to compile a template online. Compiling a template online is suitable if only one template is required. Uploading a template fits a wider range of templates: a single template or nested templates.

**Table  1**  Scenario description

<a name="table1048032513413"></a>
<table><thead align="left"><tr id="row54808259412"><th class="cellrowborder" colspan="2" valign="top" id="mcps1.2.4.1.1"><p id="p19480102544113"><a name="p19480102544113"></a><a name="p19480102544113"></a><strong id="b1943192182217"><a name="b1943192182217"></a><a name="b1943192182217"></a>Method</strong></p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.2.4.1.2"><p id="p11480142514118"><a name="p11480142514118"></a><a name="p11480142514118"></a>How to Prepare a Template</p>
</th>
</tr>
</thead>
<tbody><tr id="row164801525124114"><td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.4.1.1 "><p id="p14480192554114"><a name="p14480192554114"></a><a name="p14480192554114"></a>Heat client</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p248020255412"><a name="p248020255412"></a><a name="p248020255412"></a>Use a text editor (like Notepad++) to compile a template and save it in the YAML format.</p>
</td>
</tr>
<tr id="row3480625174115"><td class="cellrowborder" rowspan="2" valign="top" width="18.13%" headers="mcps1.2.4.1.1 "><p id="p15480172515414"><a name="p15480172515414"></a><a name="p15480172515414"></a>Management console</p>
</td>
<td class="cellrowborder" valign="top" width="15.68%" headers="mcps1.2.4.1.1 "><p id="p54317674810"><a name="p54317674810"></a><a name="p54317674810"></a>Entering template content</p>
</td>
<td class="cellrowborder" valign="top" width="66.19%" headers="mcps1.2.4.1.2 "><p id="p174801925104113"><a name="p174801925104113"></a><a name="p174801925104113"></a>Compile a template using a text editor and copy template content to the text box when creating a stack.</p>
</td>
</tr>
<tr id="row6691192414813"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p6692024124813"><a name="p6692024124813"></a><a name="p6692024124813"></a>Uploading a file</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1969210241485"><a name="p1969210241485"></a><a name="p1969210241485"></a>Compile a template using a text editor and then pack it in the format provided in <a href="template-package-structure.md">Template Package Structure</a>. <a href="example-template-packages.md">Example Template Packages</a> provides examples for your reference.</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Template files can be in the YAML or JSON format.  
>You can compile a template by following instructions in  [Template Syntax](template-syntax.md). If you are not familiar with how to compile a template, you can refer to our examples.  


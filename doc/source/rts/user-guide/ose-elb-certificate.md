# OSE::ELB::Certificate<a name="EN-US_TOPIC_0088407137"></a>

A resource for certificate.

## Required Properties<a name="section68221571095"></a>

<a name="table129051653171018"></a>
<table><thead align="left"><tr id="row1633018229616"><th class="cellrowborder" valign="top" width="33%" id="mcps1.1.3.1.1"><p id="p109064533102"><a name="p109064533102"></a><a name="p109064533102"></a><strong id="b1849833520414"><a name="b1849833520414"></a><a name="b1849833520414"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.3.1.2"><p id="p6906153151016"><a name="p6906153151016"></a><a name="p6906153151016"></a><strong id="b149923516410"><a name="b149923516410"></a><a name="b149923516410"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row17330192210610"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p7906125314101"><a name="p7906125314101"></a><a name="p7906125314101"></a>certificate</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p63783314"><a name="p63783314"></a><a name="p63783314"></a>PEM-formatted certificate chain.</p>
<p id="p37178915"><a name="p37178915"></a><a name="p37178915"></a>String value expected.</p>
<p id="p66174781"><a name="p66174781"></a><a name="p66174781"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row9331102216612"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p890625351018"><a name="p890625351018"></a><a name="p890625351018"></a>private_key</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p58557049"><a name="p58557049"></a><a name="p58557049"></a>PEM-formatted private_key chain.</p>
<p id="p57251397"><a name="p57251397"></a><a name="p57251397"></a>String value expected.</p>
<p id="p45500525"><a name="p45500525"></a><a name="p45500525"></a>Updates cause replacement.</p>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section0215610141010"></a>

<a name="table16396174451114"></a>
<table><thead align="left"><tr id="row73652313715"><th class="cellrowborder" valign="top" width="33%" id="mcps1.1.3.1.1"><p id="p1039774441110"><a name="p1039774441110"></a><a name="p1039774441110"></a><strong id="b8366113113719"><a name="b8366113113719"></a><a name="b8366113113719"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.3.1.2"><p id="p183972441114"><a name="p183972441114"></a><a name="p183972441114"></a><strong id="b103672031673"><a name="b103672031673"></a><a name="b103672031673"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row143671831171"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p173982446119"><a name="p173982446119"></a><a name="p173982446119"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p23191453"><a name="p23191453"></a><a name="p23191453"></a>The description of the certificate.</p>
<p id="p7396486"><a name="p7396486"></a><a name="p7396486"></a>String value expected.</p>
<p id="p66568381"><a name="p66568381"></a><a name="p66568381"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row10368153117710"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p83994447112"><a name="p83994447112"></a><a name="p83994447112"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p23329790"><a name="p23329790"></a><a name="p23329790"></a>The name of the certificate.</p>
<p id="p8641522"><a name="p8641522"></a><a name="p8641522"></a>String value expected.</p>
<p id="p10664839"><a name="p10664839"></a><a name="p10664839"></a>Can be updated without replacement.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section24189217108"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OSE::ELB::Certificate
    properties:
      certificate: String
      description: String
      name: String
      private_key: String
```


# OS::Nova::KeyPair<a name="EN-US_TOPIC_0088407151"></a>

A resource for creating Nova key pairs.

A keypair is an SSH key that can be injected into a server on launch.

**Note** that if a new key is generated setting _save\_private\_key_ to _True_ results in the system saving the private key which can then be retrieved via the _private\_key_  attribute of this resource.

Setting the  _public\_key_ property means that the _private\_key_ attribute of this resource will always return an empty string regardless of the _save\_private\_key_  setting since there will be no private key data to save.

>![](/images/icon-note.gif) **NOTE:**   
>The Server template does not support key pair update. If the key pair is updated, Servers will be rebuilt.  

## Required Properties<a name="section187062051133615"></a>

<a name="table6130171418399"></a>
<table><thead align="left"><tr id="row11453710617"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p713110142397"><a name="p713110142397"></a><a name="p713110142397"></a><strong id="b040713209313"><a name="b040713209313"></a><a name="b040713209313"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p513117141393"><a name="p513117141393"></a><a name="p513117141393"></a><strong id="b6409142013317"><a name="b6409142013317"></a><a name="b6409142013317"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row8416374616"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p4131614103920"><a name="p4131614103920"></a><a name="p4131614103920"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p55603624"><a name="p55603624"></a><a name="p55603624"></a>The name of the key pair.</p>
<p id="p30670568"><a name="p30670568"></a><a name="p30670568"></a>String value expected.</p>
<p id="p7599661"><a name="p7599661"></a><a name="p7599661"></a>Updates cause replacement.</p>
<p id="p1288086"><a name="p1288086"></a><a name="p1288086"></a>The length must be in the range 1 to 255, include 1 and 255.</p>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section11977018372"></a>

<a name="table1378645133917"></a>
<table><thead align="left"><tr id="row163546244718"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p3380345133919"><a name="p3380345133919"></a><a name="p3380345133919"></a><strong id="b163551424372"><a name="b163551424372"></a><a name="b163551424372"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p1438024523911"><a name="p1438024523911"></a><a name="p1438024523911"></a><strong id="b035618246718"><a name="b035618246718"></a><a name="b035618246718"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row53567248720"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p5381945123917"><a name="p5381945123917"></a><a name="p5381945123917"></a>public_key</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p58659836"><a name="p58659836"></a><a name="p58659836"></a>The optional public key. This allows users to supply the public key from a pre-existing key pair. If not supplied, a new key pair will be generated.</p>
<p id="p58176478"><a name="p58176478"></a><a name="p58176478"></a>String value expected.</p>
<p id="p53826262"><a name="p53826262"></a><a name="p53826262"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row78967468716"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p52846724016"><a name="p52846724016"></a><a name="p52846724016"></a>save_private_key</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p64959985"><a name="p64959985"></a><a name="p64959985"></a>True if the system should remember a generated private key; False otherwise.</p>
<p id="p47768958"><a name="p47768958"></a><a name="p47768958"></a>Boolean value expected.</p>
<p id="p27267445"><a name="p27267445"></a><a name="p27267445"></a>Updates cause replacement.</p>
<p id="p44080413"><a name="p44080413"></a><a name="p44080413"></a>Defaults to "False".</p>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section912313712373"></a>

<a name="table107871529124018"></a>
<table><thead align="left"><tr id="row340615234815"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p1078942910403"><a name="p1078942910403"></a><a name="p1078942910403"></a><strong id="b1407102315819"><a name="b1407102315819"></a><a name="b1407102315819"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p778912915400"><a name="p778912915400"></a><a name="p778912915400"></a><strong id="b64082023685"><a name="b64082023685"></a><a name="b64082023685"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row12408723189"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p2790192919406"><a name="p2790192919406"></a><a name="p2790192919406"></a>private_key</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p13792102919407"><a name="p13792102919407"></a><a name="p13792102919407"></a>The private key if it has been saved.</p>
</td>
</tr>
<tr id="row114109233811"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p18793192917404"><a name="p18793192917404"></a><a name="p18793192917404"></a>public_key</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1079472934010"><a name="p1079472934010"></a><a name="p1079472934010"></a>The public key.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section761441693712"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Nova::KeyPair
    properties:
      name: String
      public_key: String
      save_private_key: Boolean
```


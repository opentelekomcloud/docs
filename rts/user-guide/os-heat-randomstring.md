# OS::Heat::RandomString<a name="EN-US_TOPIC_0088407060"></a>

A resource which generates a random string.

This is useful for configuring passwords and secrets on services. Random string can be generated from specified character sequences, which means that all characters will be randomly chosen from specified sequences, or with some classes, e.g. letterdigits, which means that all character will be randomly chosen from union of ascii letters and digits. Output string will be randomly generated string with specified length \(or with length of 32, if length property doesnt specified\).

## Optional Properties<a name="section094343614233"></a>

<a name="table14260243133815"></a>
<table><thead align="left"><tr id="row1255615271868"><th class="cellrowborder" valign="top" width="33%" id="mcps1.1.3.1.1"><p id="p92611043163811"><a name="p92611043163811"></a><a name="p92611043163811"></a><strong id="b3117752560"><a name="b3117752560"></a><a name="b3117752560"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.3.1.2"><p id="p8261184310386"><a name="p8261184310386"></a><a name="p8261184310386"></a><strong id="b4157352965"><a name="b4157352965"></a><a name="b4157352965"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row185568271163"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p3261543173812"><a name="p3261543173812"></a><a name="p3261543173812"></a>character_classes</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p27236870"><a name="p27236870"></a><a name="p27236870"></a>A list of character class and their constraints to generate the random string from.</p>
<p id="p43805245"><a name="p43805245"></a><a name="p43805245"></a>List value expected.</p>
<p id="p58702885"><a name="p58702885"></a><a name="p58702885"></a>Updates cause replacement.</p>
<p id="p58563920"><a name="p58563920"></a><a name="p58563920"></a>Defaults to "[{class: lettersdigits, min: 1}]".</p>
<p id="p57313240"><a name="p57313240"></a><a name="p57313240"></a>List contents:</p>
<a name="ul46057117"></a><a name="ul46057117"></a><ul id="ul46057117"><li>*<p id="p1191092461013"><a name="p1191092461013"></a><a name="p1191092461013"></a>Map value expected.</p>
<p id="p9869152591019"><a name="p9869152591019"></a><a name="p9869152591019"></a>Updates cause replacement.</p>
<p id="p547883018109"><a name="p547883018109"></a><a name="p547883018109"></a>Map properties:</p>
<a name="ul4183195811103"></a><a name="ul4183195811103"></a><ul id="ul4183195811103"><li>class<p id="p19541522"><a name="p19541522"></a><a name="p19541522"></a>A character class and its corresponding min constraint to generate the random string from.</p>
<p id="p41655971"><a name="p41655971"></a><a name="p41655971"></a>String value expected.</p>
<p id="p39359427"><a name="p39359427"></a><a name="p39359427"></a>Updates cause replacement.</p>
<p id="p18690530"><a name="p18690530"></a><a name="p18690530"></a>Defaults to "lettersdigits".</p>
<p id="p1520412225112"><a name="p1520412225112"></a><a name="p1520412225112"></a>Allowed values: lettersdigits, letters, lowercase, uppercase, digits, hexdigits, octdigits</p>
</li><li>min<p id="p20678658"><a name="p20678658"></a><a name="p20678658"></a>The minimum number of characters from this character class that will be in the generated string.</p>
<p id="p51890195"><a name="p51890195"></a><a name="p51890195"></a>Integer value expected.</p>
<p id="p64358578"><a name="p64358578"></a><a name="p64358578"></a>Updates cause replacement.</p>
<p id="p42356295"><a name="p42356295"></a><a name="p42356295"></a>Defaults to "1".</p>
<p id="p2080253151114"><a name="p2080253151114"></a><a name="p2080253151114"></a>The value must be in the range 1 to 512, include 1 and 512.</p>
</li></ul>
</li></ul>
</td>
</tr>
<tr id="row25563272063"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p4941174862418"><a name="p4941174862418"></a><a name="p4941174862418"></a>character_sequences</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p7661980"><a name="p7661980"></a><a name="p7661980"></a>A list of character sequences and their constraints to generate the random string from.</p>
<p id="p1848964"><a name="p1848964"></a><a name="p1848964"></a>List value expected.</p>
<p id="p16640678"><a name="p16640678"></a><a name="p16640678"></a>Updates cause replacement.</p>
<p id="p15548381"><a name="p15548381"></a><a name="p15548381"></a>List contents:</p>
<a name="ul5717705"></a><a name="ul5717705"></a><ul id="ul5717705"><li>*<p id="p9217851216"><a name="p9217851216"></a><a name="p9217851216"></a>Map value expected.</p>
<p id="p119831186128"><a name="p119831186128"></a><a name="p119831186128"></a>Updates cause replacement.</p>
<p id="p177611013201220"><a name="p177611013201220"></a><a name="p177611013201220"></a>Map properties:</p>
<a name="ul1293816228124"></a><a name="ul1293816228124"></a><ul id="ul1293816228124"><li>min<p id="p7760184318128"><a name="p7760184318128"></a><a name="p7760184318128"></a>The minimum number of characters from this sequence that will be in the generated string.</p>
<p id="p157611743101213"><a name="p157611743101213"></a><a name="p157611743101213"></a>Integer value expected.</p>
<p id="p1762164381220"><a name="p1762164381220"></a><a name="p1762164381220"></a>Updates cause replacement.</p>
<p id="p3762164321211"><a name="p3762164321211"></a><a name="p3762164321211"></a>Defaults to "1".</p>
<p id="p776394316124"><a name="p776394316124"></a><a name="p776394316124"></a>The value must be in the range 1 to 512, include 1 and 512.</p>
</li><li>sequence<p id="p76173535129"><a name="p76173535129"></a><a name="p76173535129"></a>A character sequence and its corresponding min constraint to generate the random string from.</p>
<p id="p2618135371217"><a name="p2618135371217"></a><a name="p2618135371217"></a>String value expected.</p>
<p id="p76191353111216"><a name="p76191353111216"></a><a name="p76191353111216"></a>Updates cause replacement.</p>
</li></ul>
</li></ul>
</td>
</tr>
<tr id="row755610277617"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p13455101262513"><a name="p13455101262513"></a><a name="p13455101262513"></a>length</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p10398613"><a name="p10398613"></a><a name="p10398613"></a>Length of the string to generate.</p>
<p id="p26478656"><a name="p26478656"></a><a name="p26478656"></a>Integer value expected.</p>
<p id="p36981316"><a name="p36981316"></a><a name="p36981316"></a>Updates cause replacement.</p>
<p id="p64396395"><a name="p64396395"></a><a name="p64396395"></a>Defaults to "32".</p>
<p id="p42696644"><a name="p42696644"></a><a name="p42696644"></a>The value must be in the range 1 to 512, include 1 and 512.</p>
</td>
</tr>
<tr id="row1655615277611"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p876572592514"><a name="p876572592514"></a><a name="p876572592514"></a>salt</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p35876157"><a name="p35876157"></a><a name="p35876157"></a>Value which can be set or changed on stack update to trigger the resource for replacement with a new random string. The salt value itself is ignored by the random generator.</p>
<p id="p54449958"><a name="p54449958"></a><a name="p54449958"></a>String value expected.</p>
<p id="p20287574"><a name="p20287574"></a><a name="p20287574"></a>Updates cause replacement.</p>
</td>
</tr>
<tr id="row75561527567"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p71671294254"><a name="p71671294254"></a><a name="p71671294254"></a>sequence</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p19312529473"><a name="p19312529473"></a><a name="p19312529473"></a>Sequence of characters to build the random string from.</p>
<p id="p25691378"><a name="p25691378"></a><a name="p25691378"></a>String value expected.</p>
<p id="p29895817"><a name="p29895817"></a><a name="p29895817"></a>Updates cause replacement.</p>
<p id="p626899"><a name="p626899"></a><a name="p626899"></a>Allowed values: lettersdigits, letters, lowercase, uppercase, digits, hexdigits, octdigits</p>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section335814465414"></a>

<a name="table15629533105412"></a>
<table><thead align="left"><tr id="row6430469230"><th class="cellrowborder" valign="top" width="33%" id="mcps1.1.3.1.1"><p id="p116331433185410"><a name="p116331433185410"></a><a name="p116331433185410"></a><strong id="b1863716229239"><a name="b1863716229239"></a><a name="b1863716229239"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.3.1.2"><p id="p16634203385415"><a name="p16634203385415"></a><a name="p16634203385415"></a><strong id="b1463812224236"><a name="b1463812224236"></a><a name="b1463812224236"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row94301863232"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p186361331549"><a name="p186361331549"></a><a name="p186361331549"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p27601094"><a name="p27601094"></a><a name="p27601094"></a>The random string generated by this resource. This value is also available by referencing the resource.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section6421182018553"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Heat::RandomString
    properties:
      character_classes: [{"class": String, "min": Integer}, {"class": String, "min": Integer}, ...]
      character_sequences: [{"min": Integer, "sequence": String}, {"min": Integer, "sequence": String}, ...]
      length: Integer
      salt: String
      sequence: String
```


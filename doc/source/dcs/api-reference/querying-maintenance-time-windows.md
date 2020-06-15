# Querying Maintenance Time Windows<a name="EN-US_TOPIC_0237964380"></a>

## Function<a name="section62992947"></a>

This API is used to query maintenance time windows.

## URI<a name="section30065613"></a>

-   URI format:

    GET /v1.0/instances/maintain-windows


## Request<a name="section2155065"></a>

None.

## Response<a name="section19395593"></a>

-   Status code:

    If status code "200 OK" is returned, this request is fulfilled. For description of other status codes, see  [API Usage Guidelines](api-usage-guidelines.md).

-   Response parameter:

    [Table 1](#table7815975)  describes the response parameter.


**Table  1**  Parameter description

<a name="table7815975"></a>
<table><thead align="left"><tr id="row51020375"><th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.4.1.1"><p id="p39009721"><a name="p39009721"></a><a name="p39009721"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p5670856"><a name="p5670856"></a><a name="p5670856"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.515151515151516%" id="mcps1.2.4.1.3"><p id="p56686187"><a name="p56686187"></a><a name="p56686187"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row28178443"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.4.1.1 "><p id="p752527"><a name="p752527"></a><a name="p752527"></a>maintain_windows</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p60954720"><a name="p60954720"></a><a name="p60954720"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.2.4.1.3 "><p id="p38385253"><a name="p38385253"></a><a name="p38385253"></a>List of supported maintenance time windows.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Parameter description of the maintain\_windows array

<a name="table9922958"></a>
<table><thead align="left"><tr id="row4659750"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.1"><p id="p41895498"><a name="p41895498"></a><a name="p41895498"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.2.4.1.2"><p id="p38092178"><a name="p38092178"></a><a name="p38092178"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52%" id="mcps1.2.4.1.3"><p id="p65567591"><a name="p65567591"></a><a name="p65567591"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9374640"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p21148374"><a name="p21148374"></a><a name="p21148374"></a>seq</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.4.1.2 "><p id="p35296704"><a name="p35296704"></a><a name="p35296704"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p40460758"><a name="p40460758"></a><a name="p40460758"></a>Sequence number of the maintenance time window.</p>
</td>
</tr>
<tr id="row28602510"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p35101970"><a name="p35101970"></a><a name="p35101970"></a>begin</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.4.1.2 "><p id="p24687351"><a name="p24687351"></a><a name="p24687351"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p53518437"><a name="p53518437"></a><a name="p53518437"></a>Start time of the maintenance time window.</p>
</td>
</tr>
<tr id="row11903886"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p24690715"><a name="p24690715"></a><a name="p24690715"></a>end</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.4.1.2 "><p id="p53790917"><a name="p53790917"></a><a name="p53790917"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p62097011"><a name="p62097011"></a><a name="p62097011"></a>End time of the maintenance time window.</p>
</td>
</tr>
<tr id="row22002191"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p37347071"><a name="p37347071"></a><a name="p37347071"></a>default</p>
</td>
<td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.4.1.2 "><p id="p5213928"><a name="p5213928"></a><a name="p5213928"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.4.1.3 "><p id="p19674993"><a name="p19674993"></a><a name="p19674993"></a>An indicator of whether the maintenance time window is set to the default time segment.</p>
</td>
</tr>
</tbody>
</table>

-   Example response:

    ```
    { 
     "maintain_windows": [ 
            { 
             "seq": 1, 
                "begin": "22", 
                "end": "02", 
                "default": false 
            }, 
            { 
                "seq": 2, 
                "begin": "02", 
                "end": "06", 
                "default": true 
            }, 
            { 
                "seq": 3, 
                "begin": "06", 
                "end": "10", 
                "default": false 
            }, 
            { 
                "seq": 4, 
                "begin": "10", 
                "end": "14", 
                "default": false 
            }, 
            { 
                "seq": 5, 
                "begin": "14", 
                "end": "18", 
                "default": false 
            }, 
            { 
                "seq": 6, 
                "begin": "18", 
                "end": "22", 
                "default": false 
            } 
     ] 
    }
    ```



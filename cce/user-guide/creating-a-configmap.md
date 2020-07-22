# Creating a ConfigMap<a name="cce_01_0152"></a>

A  ConfigMap  is a type of resource that stores configuration information required by a workload. Its content is user-defined. After creating ConfigMaps, you can use them as files or environment variables in a containerized workload.

ConfigMaps allow you to decouple configuration files from  container images  to enhance the portability of containerized workloads.

Benefits of ConfigMaps:

-   Manage configurations of different environments and services.
-   Deploy workloads in different environments. Multiple versions are supported for configuration files so that you can update and roll back workloads easily.
-   Quickly import your configurations files to containers.

## Prerequisites<a name="section19209149103913"></a>

Cluster  and  node  resources have been created. For more information, see  [Creating a Hybrid Cluster](creating-a-hybrid-cluster.md). If you have available clusters and node resources, skip this operation.

## Creating a ConfigMap<a name="section18512531861"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Configuration Center**  \>  **ConfigMaps**. Click  **Create ConfigMap**.
2.  You can create a ConfigMap directly or based on YAML. If you create a ConfigMap based on YAML, go to  [4](#li2731182712159).
3.  Method 1: Create a ConfigMap directly.

    Set the parameters by referring to  [Table 1](#table16321825732).

    **Table  1**  Parameters for creating a ConfigMap

    <a name="table16321825732"></a>
    <table><thead align="left"><tr id="row173212251235"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.3.1.1"><p id="p43211725338"><a name="p43211725338"></a><a name="p43211725338"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="72%" id="mcps1.2.3.1.2"><p id="p0322102516320"><a name="p0322102516320"></a><a name="p0322102516320"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row163229255313"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p1232219251339"><a name="p1232219251339"></a><a name="p1232219251339"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p173227259312"><a name="p173227259312"></a><a name="p173227259312"></a>Name of a ConfigMap, which must be unique in a namespace.</p>
    </td>
    </tr>
    <tr id="row6334727910"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p233592498"><a name="p233592498"></a><a name="p233592498"></a>Cluster</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p2020234461913"><a name="p2020234461913"></a><a name="p2020234461913"></a>Cluster that will use the ConfigMap you create.</p>
    </td>
    </tr>
    <tr id="row111551253912"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p51551451293"><a name="p51551451293"></a><a name="p51551451293"></a>Namespace</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p216414418190"><a name="p216414418190"></a><a name="p216414418190"></a>Namespace to which the ConfigMap belongs. If you do not specify this parameter, the value <strong id="b28378323103254"><a name="b28378323103254"></a><a name="b28378323103254"></a>default</strong> is used by default.</p>
    </td>
    </tr>
    <tr id="row1535723154615"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p83591731124620"><a name="p83591731124620"></a><a name="p83591731124620"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p1736012314462"><a name="p1736012314462"></a><a name="p1736012314462"></a>Description of the ConfigMap.</p>
    </td>
    </tr>
    <tr id="row133224252315"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p23228259314"><a name="p23228259314"></a><a name="p23228259314"></a>Data</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p133223251335"><a name="p133223251335"></a><a name="p133223251335"></a>The workload configuration data can be used in a <span class="keyword" id="keyword1376453106113514"><a name="keyword1376453106113514"></a><a name="keyword1376453106113514"></a>container</span> or used to store the configuration data. <strong id="b24207722105458"><a name="b24207722105458"></a><a name="b24207722105458"></a>Key</strong> indicates a file name. <strong id="b16542913105458"><a name="b16542913105458"></a><a name="b16542913105458"></a>Value</strong> indicates the content in the file.</p>
    <a name="ol10322425232"></a><a name="ol10322425232"></a><ol id="ol10322425232"><li>Click <strong id="b946239950103318"><a name="b946239950103318"></a><a name="b946239950103318"></a>Add Data</strong>.</li><li>Set <strong id="b1714902967103320"><a name="b1714902967103320"></a><a name="b1714902967103320"></a>Key</strong> and <strong id="b1769765316103320"><a name="b1769765316103320"></a><a name="b1769765316103320"></a>Value</strong>.</li></ol>
    </td>
    </tr>
    <tr id="row123142814330"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p17322225134"><a name="p17322225134"></a><a name="p17322225134"></a>Labels</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p1932211253312"><a name="p1932211253312"></a><a name="p1932211253312"></a>Labels are attached to objects such as workloads, nodes, and services in key-value pairs.</p>
    <p id="p1932220252316"><a name="p1932220252316"></a><a name="p1932220252316"></a>Labels define the identifiable attributes of these objects and are used to manage and select the objects.</p>
    <a name="ol11394016509"></a><a name="ol11394016509"></a><ol id="ol11394016509"><li>Click <strong id="b811138571103421"><a name="b811138571103421"></a><a name="b811138571103421"></a>Add Label</strong>.</li><li>Set <strong id="b4941748105458"><a name="b4941748105458"></a><a name="b4941748105458"></a>Key</strong> and <strong id="b44475740105458"><a name="b44475740105458"></a><a name="b44475740105458"></a>Value</strong>.</li></ol>
    </td>
    </tr>
    </tbody>
    </table>

4.  <a name="li2731182712159"></a>Method 2: Create a ConfigMap based on YAML.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >To create configuration items by uploading a file, ensure that the resource description file has been created. CCE supports files in JSON or yaml format. For more information, see  [ConfigMap Requirements for ConfigMap](#section66903416102).  

    Click  **Create** **YAML **on the right of the page.

    -   Method 1: Import the orchestration file.

        Click  **Add File**  to import the file in YAML or JSON format. The orchestration content can be directly displayed.

    -   Method 2: Directly orchestrate the content.

        In the orchestration content area, enter the content of the YAML or JSON file.

5.  After the configuration is complete, click  **Create**.

    The new ConfigMap is displayed in the ConfigMap list.


## ConfigMap Requirements for ConfigMap<a name="section66903416102"></a>

A ConfigMap resource file can be in JSON or YAML format, and the file size cannot exceed 2 MB.

-   JSON format

    The file name is  **configmap.json**  and the following shows a configuration example.

    ```
    {
      "kind": "ConfigMap",
      "apiVersion": "v1",
      "metadata": {
        "name": "paas-broker-app-017",
        "namespace": "test",
       "enable": true
      },
      "data": {
        "context": "{\"applicationComponent\":{\"properties\":{\"custom_spec\":{}},\"node_name\":\"paas-broker-app\",\"stack_id\":\"0177eae1-89d3-cb8a-1f94-c0feb7e91d7b\"},\"softwareComponents\":[{\"properties\":{\"custom_spec\":{}},\"node_name\":\"paas-broker\",\"stack_id\":\"0177eae1-89d3-cb8a-1f94-c0feb7e91d7b\"}]}"
     }
    }
    ```

-   YAML format

    The file name is  **configmap.yaml**  and the following shows a configuration example.

    ```
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: test-configmap
    data:
      data-1: value-1
      data-2: value-2
    ```


## Creating a ConfigMap Using kubectl<a name="section639712716372"></a>

1.  Configure the  **kubectl**  command to connect an ECS to the cluster. For details, see  [Connecting to a Kubernetes Cluster Using kubectl](connecting-to-a-kubernetes-cluster-using-kubectl.md).
2.  Create and edit the  **cce-configmap.yaml**  file.

    **vi cce-configmap.yaml**

    ```
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: cce-configmap
    data:
      SPECIAL_LEVEL: Hello
      SPECIAL_TYPE: CCE
    ```

3.  Run the following commands to create a ConfigMap.

    **kubectl create -f cce-configmap.yaml**

    **kubectl get cm**

    ```
    NAME               DATA            AGE
    cce-configmap      3               3h
    cce-configmap1     3               7m
    ```


## Related Operations<a name="section359413445405"></a>

After creating a configuration item, you can update or delete it as described in  [Table 2](#table1619535674020).

**Table  2**  Related operations

<a name="table1619535674020"></a>
<table><thead align="left"><tr id="row16740630125918"><th class="cellrowborder" valign="top" width="32%" id="mcps1.2.3.1.1"><p id="p17740730115914"><a name="p17740730115914"></a><a name="p17740730115914"></a>Operation</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.2.3.1.2"><p id="p1574018303592"><a name="p1574018303592"></a><a name="p1574018303592"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row133318512019"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p163331851201"><a name="p163331851201"></a><a name="p163331851201"></a>Viewing a YAML file</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p1633314512016"><a name="p1633314512016"></a><a name="p1633314512016"></a>Click <strong id="b84235270611425"><a name="b84235270611425"></a><a name="b84235270611425"></a>View YAML</strong> next to the ConfigMap name to view the YAML file corresponding to the current ConfigMap.</p>
</td>
</tr>
<tr id="row12740103016592"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p4740153012590"><a name="p4740153012590"></a><a name="p4740153012590"></a>Updating a ConfigMap</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><a name="ol187401330145919"></a><a name="ol187401330145919"></a><ol id="ol187401330145919"><li>Select the name of the ConfigMap to be updated and click <strong id="b842352706114220"><a name="b842352706114220"></a><a name="b842352706114220"></a>Update</strong>.</li><li>Modify the secret data. For more information, see <a href="#table16321825732">Table 1</a>.</li><li>Click <strong id="b84235270613114"><a name="b84235270613114"></a><a name="b84235270613114"></a>Update</strong>.</li></ol>
</td>
</tr>
<tr id="row874013304597"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p17740330175915"><a name="p17740330175915"></a><a name="p17740330175915"></a>Deleting a ConfigMap</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><p id="p13740630165914"><a name="p13740630165914"></a><a name="p13740630165914"></a>Select the configuration you want to delete and click <strong id="b84235270613133"><a name="b84235270613133"></a><a name="b84235270613133"></a>Delete</strong>.</p>
<p id="p1574020307590"><a name="p1574020307590"></a><a name="p1574020307590"></a>Follow the prompts to delete the ConfigMap.</p>
</td>
</tr>
</tbody>
</table>


# Preparing a Chart<a name="cce_01_0144"></a>

You can prepare a chart using one of the following methods:

-   [Customizing a Chart](#s84a75de063eb4fb29387e64d133b0da6)
-   [Using a Kubernetes Official Chart](#s5f9699b10586401d81cfebd947cf416f)

>![](/images/icon-notice.gif) **NOTICE:**   
>If the created workload requires the  EVS disk  and  ELB  functions, you need to modify the chart. For details, see  [Using an EVS Disk](using-an-evs-disk.md)  and  [Using ELB](using-elb.md).  

## Customizing a Chart<a name="s84a75de063eb4fb29387e64d133b0da6"></a>

1.  Customize the content of a chart as required.

    For details about how to create a chart, see  [https://github.com/helm/helm/blob/master/cmd/helm/chart.go](https://github.com/helm/helm/blob/master/cmd/helm/chart.go).

2.  Set the chart directory structure and name the chart based on the requirements defined in  [Chart Specifications](#s8af9336c49a44399865c7a0f3149d789).

## Using a  Kubernetes Official Chart<a name="s5f9699b10586401d81cfebd947cf416f"></a>

1.  <a name="l6d35ccf85da74660b802f524cc9e3095"></a>Access  [https://github.com/kubernetes/charts](https://github.com/helm/charts)  to obtain the required chart.
2.  Log in to a Linux host.
3.  Upload the chart obtained in  [1](#l6d35ccf85da74660b802f524cc9e3095).
4.  Run the following command to compress the chart.
    -   If the Helm client is not installed on the  Linux  host, run the following command:

        **tar pzcf \{name\}-\{version\}.tgz \{name\}/**

        In the preceding command,

        **\{name\}**  indicates the actual chart name.

        **\{version\}**  indicates the actual chart version.

        >![](/images/icon-notice.gif) **NOTICE:**   
        >The values of \{name\} and \{version\} must be the same as the values of name and version in the  **Chart.yaml**  file in the chart.  

    -   If the Helm client is installed on the Linux host, run the following command:

        **helm package \{name\}/**

        In the preceding command, replace  **\{name\}**  with the actual chart name.

5.  Set the chart directory structure and name the chart based on the requirements defined in  [Chart Specifications](#s8af9336c49a44399865c7a0f3149d789).

## Chart Specifications<a name="s8af9336c49a44399865c7a0f3149d789"></a>

This section uses the  Redis  workload as an example to illustrate the chart specifications.

-   **Naming Requirement**

    A chart is named in the format of  _Workload name-Main version number.Minor version number.Revision number.tgz_, for example,  **redis-0.4.2.tgz**,  **redis-0.4.2-beta.tgz**, and  **redis-0.4.2-alpha.1.tgz**.

    >![](/images/icon-note.gif) **NOTE:**   
    >The version number of the chart must comply with the  [semantic versioning](https://semver.org/)  rules.  
    >-   The main and minor version numbers are mandatory, and the revision number is optional.  
    >-   The version number contains a maximum of 64 characters.  
    >-   The values of the main and minor version numbers are integers. They must be ≥0 and ≤99.  
    >-   The revision number consists of digits \(0-9\), uppercase letters \(A-Z\), lowercase letters \(a-z\), and hyphens \(-\).  

-   **Directory Structure**

    The directory structure of a chart is as follows:

    ```
    redis/
      templates/
      values.yaml
      README.md
      Chart.yaml
      .helmignore
    ```

    As listed in  [Table 1](#tb7d789a3467e4fe9b4385a51f3460321), the parameters marked with \* are mandatory.

    **Table  1**  Parameters in the directory structure of a chart

    <a name="tb7d789a3467e4fe9b4385a51f3460321"></a>
    <table><thead align="left"><tr id="row6784152135012"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.3.1.1"><p id="p278413212502"><a name="p278413212502"></a><a name="p278413212502"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="78%" id="mcps1.2.3.1.2"><p id="p20784621115018"><a name="p20784621115018"></a><a name="p20784621115018"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37842210500"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.3.1.1 "><p id="p1278432119504"><a name="p1278432119504"></a><a name="p1278432119504"></a>* templates</p>
    </td>
    <td class="cellrowborder" valign="top" width="78%" headers="mcps1.2.3.1.2 "><p id="p478412213502"><a name="p478412213502"></a><a name="p478412213502"></a>Stores all templates.</p>
    </td>
    </tr>
    <tr id="row147841721185017"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.3.1.1 "><p id="p14784172119501"><a name="p14784172119501"></a><a name="p14784172119501"></a>* values.yaml</p>
    </td>
    <td class="cellrowborder" valign="top" width="78%" headers="mcps1.2.3.1.2 "><p id="p1678472115013"><a name="p1678472115013"></a><a name="p1678472115013"></a>Describes configuration parameters required by templates.</p>
    <div class="notice" id="note11415171194911"><a name="note11415171194911"></a><a name="note11415171194911"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p394216481648"><a name="p394216481648"></a><a name="p394216481648"></a>Make sure that the image address set in the <strong id="b84245074610"><a name="b84245074610"></a><a name="b84245074610"></a>values.yaml</strong> file is the same as the image address in the container image repository. Otherwise, an exception occurs when you create a workload, and the system displays a message indicating that the image fails to be pulled.</p>
    <p id="p04177113498"><a name="p04177113498"></a><a name="p04177113498"></a>To obtain the image address, perform the following operations: Log in to the CCE console. In the navigation pane, choose <strong id="b842352706112344"><a name="b842352706112344"></a><a name="b842352706112344"></a>Image Repository</strong> to access the SWR console. On the SWR console, choose <strong id="b84235270611204"><a name="b84235270611204"></a><a name="b84235270611204"></a>My Images</strong>. On the <strong id="b842352706112549"><a name="b842352706112549"></a><a name="b842352706112549"></a>Private Images</strong> tab page, click the name of an uploaded image. On the <strong id="b842352706112621"><a name="b842352706112621"></a><a name="b842352706112621"></a>Image Version</strong> tab page, you can view the image address in the <strong id="b842352706112829"><a name="b842352706112829"></a><a name="b842352706112829"></a>Intranet Image Address</strong> column.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row1078472120505"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.3.1.1 "><p id="p1278411218502"><a name="p1278411218502"></a><a name="p1278411218502"></a>README.md</p>
    </td>
    <td class="cellrowborder" valign="top" width="78%" headers="mcps1.2.3.1.2 "><p id="p10784102115505"><a name="p10784102115505"></a><a name="p10784102115505"></a>A markdown file, including:</p>
    <a name="ul778411210502"></a><a name="ul778411210502"></a><ul id="ul778411210502"><li>The workload or services provided by the chart.</li><li>Prerequisites for running the chart.</li><li>Configurations in the <strong id="b1630612311263"><a name="b1630612311263"></a><a name="b1630612311263"></a>values.yaml</strong> file.</li><li>Information about chart installation and configuration.</li></ul>
    </td>
    </tr>
    <tr id="row1678672116506"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.3.1.1 "><p id="p6786162113504"><a name="p6786162113504"></a><a name="p6786162113504"></a>* Chart.yaml</p>
    </td>
    <td class="cellrowborder" valign="top" width="78%" headers="mcps1.2.3.1.2 "><p id="p278615212501"><a name="p278615212501"></a><a name="p278615212501"></a>Basic information about the chart.</p>
    </td>
    </tr>
    <tr id="row97861621175015"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.3.1.1 "><p id="p6786921165010"><a name="p6786921165010"></a><a name="p6786921165010"></a>.helmignore</p>
    </td>
    <td class="cellrowborder" valign="top" width="78%" headers="mcps1.2.3.1.2 "><p id="p07861721145013"><a name="p07861721145013"></a><a name="p07861721145013"></a>Files or data that does not need to read templates during workload installation.</p>
    </td>
    </tr>
    </tbody>
    </table>



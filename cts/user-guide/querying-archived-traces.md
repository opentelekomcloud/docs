# Querying Archived Traces<a name="en-us_topic_0030598636"></a>

## **Scenarios**<a name="section1534311495828"></a>

CTS periodically compresses the recorded traces into trace files and delivers them to OBS buckets. Trace files are collections of traces that CTS automatically generates by service and dump interval. CTS adjusts the number of traces contained in a trace file as the service load changes.

This section describes how to obtain historical operation records from trace files downloaded from the OBS bucket.

## **Procedure**<a name="section4763421295828"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner to select the desired region and project. 
3.  Click  **Service List**  and choose  **Management & Deployment**  \>  **Cloud Trace Service**.
4.  Click  **Tracker**  in the left pane.
5.  Click the specified bucket in the  **OBS Bucket**  column.

    **Figure  1**  Selecting the OBS bucket<a name="fig25931383105014"></a>  
    ![](figures/selecting-the-obs-bucket.png "selecting-the-obs-bucket")

6.  Select the target trace. Choose  _OBS bucket name_  \>  **CloudTraces**  \>  _Region_  \>  _Year_  \>  _Month_  \>  _Day_  \>  _Tracker name_  \>  _Service type directory_. Click  **Download**  in the  **Operation**  column to download the trace file to the default path. To download the trace file to a customized path, click  **Download As**.

    -   The trace file storage path is as follows:

        _OBS bucket name_  \>  **CloudTraces**  \>  _Region_  \>  _Year_  \>  _Month_  \>  _Day_  \>  _Tracker name_  \>  _Service type directory_

        An example is  _User Define\>CloudTraces\>region\>2016\>5\>19\>system\>ECS_.

    -   The trace file naming format is as follows:

        _Operation trace file prefix_\_CloudTrace\__Region_\__/Region-project__Time when the log was uploaded to OBS__: year-__month-__day_T_hour-minute-second_Z\__Character randomly generated_.json.gz

        An example is  _**File Prefix**_**\_CloudTrace\_region\_2016-05-30T16-20-56Z\_21d36ced8c8af71e.json.gz**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The OBS bucket name and trace file prefix are user-defined, and other parameters are automatically generated.  

    For details about key fields in the trace structure, see  [Trace Structure](trace-structure.md)  and  [Example Traces](example-traces.md).

    **Figure  2**  Viewing trace file content<a name="fig3440489620918"></a>  
    ![](figures/viewing-trace-file-content.png "viewing-trace-file-content")

7.  Extract a JSON file with the same name as the downloaded trace file and open the JSON file using a text file editor to view trace logs.


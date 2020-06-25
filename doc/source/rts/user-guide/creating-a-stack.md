# Creating a stack<a name="EN-US_TOPIC_0076468623"></a>

With RTS, you can create a collection of cloud resources using a template. These resources are defined as a stack. This section uses creating a random string as an example to describe how to create a stack on the RTS console.

## Prerequisite<a name="section698911138323"></a>

You have prepared a stack template.

## Procedure<a name="section16219936205317"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner to select the desired region and project.
3.  Under  **Management & Deployment**, click  **Resource Template Service**.
4.  Click  **Create Stack**  in the upper right corner.

    The process of creating a stack is displayed.

5.  Upload a template.
    -   For a single template, you can create a stack by entering template content online.
        1.  **Template Source**: Select  **Manually specify**.
        2.  **Template Content**: Enter template content online or copy content of an existing template to the text box.

            >![](/images/icon-note.gif) **NOTE:**   
            >The template must comply with the JSON or YAML format and uses the UTF-8 encoding format.  

        3.  Click  **Next**  to check syntax.

            If the syntax check succeeds, the  **Specify Details**  page is displayed. If the syntax check fails, modify the template as prompted.

    -   For a single or nested template, you can create a stack by uploading a template package.

        **Figure  1**  Uploading a template file<a name="fig753215101111"></a>  
        ![](figures/uploading-a-template-file.png "uploading-a-template-file")

        1.  **Template Source**: Select  **Upload template**.
        2.  **Stack Template**: Click  ![](figures/icon-vertexs.png), select the prepared template package, and click  **Upload**.
        3.  **Main File**: Select a template file as the main file based on the resources you want to create. A template package may contain multiple template files.
        4.  After selecting a main file, click  **Next**  to check the syntax.

            If the syntax check succeeds, the  **Specify Details**  page is displayed. If the syntax check fails, modify the template as prompted.


6.  On the  **Specify Details**  page, enter a stack name, set parameters based on the required resource information, and click  **Next**.

    >![](/images/icon-note.gif) **NOTE:**   
    >The stack name:  
    >-   Contains 1 to 255 characters.  
    >-   Starts with a letter.  
    >-   Can contain digits, hyphens \(-\), dots \(.\), and underlines \(\_\).  

7.  Confirm that stack configurations are correct and click  **Submit**.

    It takes some time to complete the creation.


## Result<a name="section771635719379"></a>

You can view the stack creation result in the stack list or details or query events.

You can click  **Events**  on the  **Specify Details**  page to view each operation occurring during stack creation. All operations are displayed in the time sequence, and the latest operation is in the first row.


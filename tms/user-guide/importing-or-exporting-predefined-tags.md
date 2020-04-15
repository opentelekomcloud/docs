# Importing or Exporting Predefined Tags<a name="EN-US_TOPIC_0141727065"></a>

## Importing Tags<a name="section18567105115413"></a>

If you have inventory tags, you can quickly import them to the TMS predefined tags to facilitate subsequent resource association.

The predefined tag import function allows you to import the .csv file exported from a third party to TMS. The encoding format of the .csv file must be UTF-8.

If duplicate content exists between the current environment and the imported file, the content of the current environment will be overwritten after the import.

When editing tags to be imported, pay attention to the following restrictions:

-   Each user can create up to 500 predefined tags.
-   You can enter a maximum of 36 and 43 characters for  **Key**  and  **Value**, respectively. Both  **Key**  and  **Value**  can contain only digits, letters, hyphens \(-\), at signs \(@\), and underscores \(\_\).

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>Predefined tag importation does not support .csv files that have been modified in Excel. Attempting to import such files will produce garbled characters and result in an importation failure. To edit a .csv file, open it with notepad.  

To import tags, perform the following steps:

1.  Log in to the management console.
2.  Under  **Management & Deployment**, select  **Tag Management Service**.
3.  Choose  **Predefined Tags**.
4.  Click  **Download template \(CSV file\)**.
5.  Fill in the template as prompted.
6.  Click  **Import**  and select the target file.
7.  Click  **OK**.

    The predefined tags are imported successfully and displayed in the predefined tag list.


## Exporting Tags<a name="section27504973115735"></a>

Tag files or templates downloaded with Internet Explorer 9 cannot be imported into other browsers. Those downloaded with other browsers cannot be imported into Internet Explorer 9.

To export predefined tags for editing, perform the following steps:

1.  Log in to the management console.
2.  Under  **Management & Deployment**, select  **Tag Management Service**.
3.  Choose  **Predefined Tags**.
4.  Select the predefined tag that you want to export.
5.  Click  **Export**.

    The system saves the exported .csv file and the predefined tag is exported successfully.



# Managing Tags<a name="rds_pg_tag"></a>

## Scenarios<a name="rds_tag_section7898787175059"></a>

Tag Management Service \(TMS\)  enables you to use tags on the management console to manage resources. TMS works with other cloud services to manage tags. TMS manages tags globally, and other cloud services manage their own tags.

-   You are advised to set predefined tags on the TMS console.
-   A tag consists of a key and value. You can add only one value for each key.
-   A maximum of 20 tags can be added for each DB instance.

## Adding a Tag<a name="rds_tag_section57172399175119"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target DB instance.
5.  On the  **Tags**  page, click  **Add Tag**. In the displayed dialog box, enter a tag key and a tag value, and click  **OK**.
    -   The tag key must be unique and must consist of 1 to 36 characters. Only letters, digits, hyphens \(-\), underscores \(\_\), and at signs \(@\) are allowed.
    -   The tag value can be empty or consist of 1 to 43 characters. Only letters, digits, hyphens \(-\), underscores \(\_\), and at signs \(@\) are allowed.

6.  After a tag has been added, you can view and manage it on the  **Tags**  page.

## Editing a Tag<a name="rds_tag_section38640924175719"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target DB instance.
5.  On the  **Tags**  page, locate the tag to be edited and click  **Edit**  in the  **Operation**  column. In the displayed dialog box, change the tag value and click  **OK**.
    -   Only the tag value can be edited.
    -   The tag value can be empty or consist of 1 to 43 characters. Only letters, digits, hyphens \(-\), underscores \(\_\), and at signs \(@\) are allowed.

6.  After a tag has been edited, you can view and manage it on the  **Tags**  page.

## Deleting a Tag<a name="rds_tag_section51403672175725"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target DB instance.
5.  On the  **Tags**  page, locate the tag to be deleted and click  **Delete**  in the  **Operation**  column. In the displayed dialog box, click  **Yes**.
6.  After a tag has been deleted, it will no longer be displayed on the  **Tags**  page.


# Managing a Project<a name="en-us_topic_0066738518"></a>

Projects are used to group and isolate OpenStack resources, including computing, storage, and network resources. Resources in your account must be mounted under projects. A project can be a department or a project team. Access IAM with a security administrator to create projects in a region and perform isolated management of resources.

## Procedure<a name="section51118979101057"></a>

1.  In the navigation pane, choose  **Projects**.
2.  On the  **Projects**  page, click  **Create Project**.
3.  On the  **Create Project**  page, select a region from the  **Region**  drop-down list.
4.  Set  **Project Name**.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   The project name format is  _Region Name_\__Project Name_.  _Region Name_  cannot be modified.  
    >-   Only letters, digits, underscores \(\_\), and hyphens \(-\) are allowed in the project name. The maximum length of  _Region Name_\__Project Name_  is 64 characters.  

5.  \(Optional\) Set  **Description**.
6.  Click  **OK**.

    Return to the project list. Check that  **Status**  of the newly created project is displayed as  **Normal**.


## Follow-up Procedure<a name="section13675102471011"></a>

Authorizing projects

In the  **User Group Permissions**  area on the  **Modify User Group**  page, locate the row that contains the target project, and click  **Modify**. In the displayed dialog box, select the required permission sets for the project. For details, see section  [Creating a User Group](creating-a-user-group.md).

## Related Operations<a name="section645408871296"></a>

-   Viewing project details
    1.  View the projects in the corresponding region in the project list.
    2.  Click  **View**  in the  **Operation**  column of the row that contains the target project.

        View project details and the users bound to the project.

        >![](/images/icon-note.gif) **NOTE:**   
        >After the permissions on a project are granted to a user group and a user is added to the user group, the user has the permissions of the user group and is bound to the project. The user can switch projects to access different resources.  

    3.  Click  **View**  in the  **Operation**  column in the user permission list.

        View the permissions of the users bound to the project.



-   Modifying project data

    1.  In the project list, expand the region where the target project resides.
    2.  Click  **Modify**  in the  **Operation**  column of the row that contains the target project. In the displayed  **Modify Project**  dialog box, modify  **Project Name**  and  **Description**.

    >![](/images/icon-note.gif) **NOTE:**   
    >The project name format is  _Region Name_\__Project Name_.  _Region Name_  cannot be modified.  

-   Deleting a project

    >![](/images/icon-notice.gif) **NOTICE:**   
    >After a project is deleted successfully, the resources in the project are also deleted.  

    1.  Click  **Delete**  on the right of the project to be deleted.

        >![](/images/icon-note.gif) **NOTE:**   
        >Only the projects created in a region can be deleted. The project named after the region name cannot be deleted.  

    2.  Enter  **Login Password**  and  **Verification Code**.
    3.  Click  **OK**.

        Return to the project list. Check that  **Status**  of the project to be deleted is displayed as  **Deleting**.

        >![](/images/icon-note.gif) **NOTE:**   
        >After the resources in a project are deleted, the project is deleted completely.  


-   For details about how to switch between projects, see section  [Switching Projects or Regions](switching-projects-or-regions.md).


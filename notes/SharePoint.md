


# MS Graph Operations

Id format (https://stackoverflow.com/a/45424133/5932184):

{hostname},{spsite.id},{spweb.id}


The Site collection has a root Site. web.ID represents ID for the root site.


List subsites:
GET /sites/{site-id}/sites

Document libraries
https://graph.microsoft.com/v1.0/sites/root/drives


# OD Open Link

## View Storage Size Usage SharePoint

Add the following to the end of the base URL of the site:

`_layouts/15/storman.aspx`

## Versioning Settings

`_layouts/15/LstSetng.aspx?List=%7B73B91133%2DA627%2D4F69%2D9847%2D2AF85ABB878D%7D`


[List vs Doc Library](https://sharepointmaven.com/lists-vs-libraries-in-sharepoint-online/)

Doc library is special subset of lists.

## Report MS Graph

<https://learn.microsoft.com/en-us/graph/api/reportroot-getsharepointsiteusagestorage?view=graph-rest-1.0&tabs=http>

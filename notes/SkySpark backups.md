# SkySpark Backups

References:
 - <https://skyfoundry.com/doc/docAppNotes/ITOperationsAndMaintenance#backups>

Recommendation is to do normal file style backup for everything under `var` directory,
*except* the `db` sub directory.
That backup should be done using the UI or the `folioBackup()` axon method.

- Tools -> Backup
- Host -> Host App -> Projects -> *Click on project, and then 'Backup'*

Backups are then saved to: `var/proj/<proj_name>/backup`

# Configuration

3.128. folder
Type: mailbox
Default: `~/Mail`

Specifies the default location of your mailboxes.
A "+" or "=" at the beginning of a pathname will be expanded to the value of this variable.
Note that if you change this variable (from the default) value you need to make sure that the assignment occurs before you use "+" or "=" for any other variables since expansion takes place when handling the " mailboxes" command.

In a Maildir setup, I believe this should be the same directory that is the root Maildir mailbox.

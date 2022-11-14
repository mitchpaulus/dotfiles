# Understanding Redirection

References:

- <https://devconnected.com/input-output-redirection-on-linux-explained>
- <http://books.gigatux.nl/mirror/kerneldevelopment/0672327201/ch12lev1sec10.html>

[Visual explanation](https://wiki.bash-hackers.org/howto/redirection_tutorial)

From [here](http://www.sichong.site/linux/2021/11/06/dev-stdout-vs-2-a-dive-into-linux-stdio.html),
You should pretty much always use >& instead of /dev/stderr or /dev/stdout when manipulating STDIO streams.


When process is created, gets `task_struct`. Has two things, `fs` and `files`. `fs` has umask info,
and `files` has the file descriptor table.

```c
struct task_struct {
  fs_struct fs
  files_struct files
}

struct files_struct {
        atomic_t    count;              /* structure's usage count */
        spinlock_t  file_lock;          /* lock protecting this structure */
        int         max_fds;            /* maximum number of file objects */
        int         max_fdset;          /* maximum number of file descriptors */
        int         next_fd;            /* next file descriptor number */
        struct file **fd;               /* array of all file objects */
        fd_set      *close_on_exec;     /* file descriptors to close on exec() */
        fd_set      *open_fds;           /* pointer to open file descriptors */
        fd_set      close_on_exec_init; /* initial files to close on exec() */
        fd_set      open_fds_init;      /* initial set of file descriptors */
        struct file *fd_array[NR_OPEN_DEFAULT]; /* default array of file objects */
};

struct fs_struct {
        atomic_t        count;       /* structure usage count */
        rwlock_t        lock;        /* lock protecting structure */
        int             umask;       /* default file permissions*/
        struct dentry   *root;       /* dentry of the root directory */
        struct dentry   *pwd;        /* dentry of the current directory */
        struct dentry   *altroot;    /* dentry of the alternative root */
        struct vfsmount *rootmnt;    /* mount object of the root directory */
        struct vfsmount *pwdmnt;     /* mount object of the current directory */
        struct vfsmount *altrootmnt; /* mount object of the alternative root */
};
```

##
Duplicating file descriptors

```
[digit1]><word> :: Opens file <word> for writing and puts it in file descriptor digit1.

[digit1]>&<digit2> :: file descriptor digit2 is copied to file descriptor digit1

[digit]>&- :: Closes the file descriptor for digit

// Moving
[digit1]<&<digit2>- Takes file pointed by digit2 and puts it to file descriptor digit1, then closes digit2

```

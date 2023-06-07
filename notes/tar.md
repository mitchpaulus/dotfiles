# `tar`

 - t, --list  list the contents of an archive
 -x, --extract, --get extract files from an archive
 -v, --verbose verbosely list files processed
 -f ARCHIVE, --file=ARCHIVE use archive file or device ARCHIVE


- GNU tar automatically deals with compression on extraction. Quote from
  the manual (https://www.gnu.org/software/tar/manual/tar.html#gzip):

  > You can also let GNU tar select the compression program based on the
  > suffix of the archive file name. This is done using ‘--auto-compress’
  > (‘-a’) command line option. For example, the following invocation will
  > use bzip2 for compression:
  >
  > ```
  > $ tar caf archive.tar.bz2 .
  > ```
  >
  > whereas the following one will use lzma:
  >
  > ```
  > $ tar caf archive.tar.lzma .
  > ```
  >
  > For a complete list of file name suffixes recognized by GNU tar, see
  > auto-compress.
  >
  > Reading compressed archive is even simpler: you don’t need to specify
  > any additional options as GNU tar recognizes its format automatically.
  > Thus, the following commands will list and extract the archive created
  > in previous example:
  >
  > ```
  > # List the compressed archive
  > $ tar tf archive.tar.gz
  > # Extract the compressed archive
  > $ tar xf archive.tar.gz
  > ```
  >
  > The format recognition algorithm is based on signatures, a special
  > byte sequences in the beginning of file, that are specific for certain
  > compression formats. If this approach fails, tar falls back to using
  > archive name suffix to determine its format (see auto-compress, for a
  > list of recognized suffixes).

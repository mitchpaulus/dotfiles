# RIS file format

Tag  	Meaning
TY 	Type of reference (must be the first tag)
A1 	Primary Authors (each author on its own line preceded by the A1 tag)
A2 	Secondary Authors (each author on its own line preceded by the A2 tag)
A3 	Tertiary Authors (each author on its own line preceded by the A3 tag)
A4 	Subsidiary Authors (each author on its own line preceded by the A4 tag)
AB 	Abstract
AD 	Author Address
AN 	Accession Number
AU 	Author (each author on its own line preceded by the AU tag)
AV 	Location in Archives
BT 	This field maps to T2 for all reference types except for Whole Book and Unpublished Work references. It can contain alphanumeric characters. There is no practical limit to the length of this field.
C1 	Custom 1
C2 	Custom 2
C3 	Custom 3
C4 	Custom 4
C5 	Custom 5
C6 	Custom 6
C7 	Custom 7
C8 	Custom 8
CA 	Caption
CN 	Call Number
CP 	This field can contain alphanumeric characters. There is no practical limit to the length of this field.
CT 	Title of unpublished reference
CY 	Place Published
DA 	Date
DB 	Name of Database
DO 	DOI
DP 	Database Provider
ED 	Editor
EP 	End Page
ET 	Edition
ID 	Reference ID
IS 	Issue number
J1 	Periodical name: user abbreviation 1. This is an alphanumeric field of up to 255 characters.
J2 	Alternate Title (this field is used for the abbreviated title of a book or journal name, the latter mapped to T2)
JA 	Periodical name: standard abbreviation. This is the periodical in which the article was (or is to be, in the case of in-press references) published. This is an alphanumeric field of up to 255 characters.
JF 	Journal/Periodical name: full format. This is an alphanumeric field of up to 255 characters.
JO 	Journal/Periodical name: full format. This is an alphanumeric field of up to 255 characters.
KW 	Keywords (keywords should be entered each on its own line preceded by the tag)
L1 	Link to PDF. There is no practical limit to the length of this field. URL addresses can be entered individually, one per tag or multiple addresses can be entered on one line using a semi-colon as a separator. These links should end with a file name, and not simply a landing page. Use the UR tag for URL links.
L2 	Link to Full-text. There is no practical limit to the length of this field. URL addresses can be entered individually, one per tag or multiple addresses can be entered on one line using a semi-colon as a separator.
L3 	Related Records. There is no practical limit to the length of this field.
L4 	Image(s). There is no practical limit to the length of this field.
LA 	Language
LB 	Label
LK 	Website Link
M1 	Number
M2 	Miscellaneous 2. This is an alphanumeric field and there is no practical limit to the length of this field.
M3 	Type of Work
N1 	Notes
N2 	Abstract. This is a free text field and can contain alphanumeric characters. There is no practical length limit to this field.
NV 	Number of Volumes
OP 	Original Publication
PB 	Publisher
PP 	Publishing Place
PY 	Publication year (YYYY)
RI 	Reviewed Item
RN 	Research Notes
RP 	Reprint Edition
SE 	Section
SN 	ISBN/ISSN
SP 	Start Page
ST 	Short Title
T1 	Primary Title
T2 	Secondary Title (journal title, if applicable)
T3 	Tertiary Title
TA 	Translated Author
TI 	Title
TT 	Translated Title
U1 	User definable 1. This is an alphanumeric field and there is no practical limit to the length of this field.
U2 	User definable 2. This is an alphanumeric field and there is no practical limit to the length of this field.
U3 	User definable 3. This is an alphanumeric field and there is no practical limit to the length of this field.
U4 	User definable 4. This is an alphanumeric field and there is no practical limit to the length of this field.
U5 	User definable 5. This is an alphanumeric field and there is no practical limit to the length of this field.
UR 	URL
VL 	Volume number
VO 	Published Standard number
Y1 	Primary Date
Y2 	Access Date
ER 	End of Reference (must be empty and the last tag)

Abbreviation 	Type
ABST 	Abstract
ADVS 	Audiovisual material
AGGR 	Aggregated Database
ANCIENT 	Ancient Text
ART 	Art Work
BILL 	Bill
BLOG 	Blog
BOOK 	Whole book
CASE 	Case
CHAP 	Book chapter
CHART 	Chart
CLSWK 	Classical Work
COMP 	Computer program
CONF 	Conference proceeding
CPAPER 	Conference paper
CTLG 	Catalog
DATA 	Data file
DBASE 	Online Database
DICT 	Dictionary
EBOOK 	Electronic Book
ECHAP 	Electronic Book Section
EDBOOK 	Edited Book
EJOUR 	Electronic Article
WEB 	Web Page
ENCYC 	Encyclopedia
EQUA 	Equation
FIGURE 	Figure
GEN 	Generic
GOVDOC 	Government Document
GRANT 	Grant
HEAR 	Hearing
ICOMM 	Internet Communication
INPR 	In Press
JFULL 	Journal (full)
JOUR 	Journal
LEGAL 	Legal Rule or Regulation
MANSCPT 	Manuscript
MAP 	Map
MGZN 	Magazine article
MPCT 	Motion picture
MULTI 	Online Multimedia
MUSIC 	Music score
NEWS 	Newspaper
PAMP 	Pamphlet
PAT 	Patent
PCOMM 	Personal communication
RPRT 	Report
SER 	Serial publication
SLIDE 	Slide
SOUND 	Sound recording
STAND 	Standard
STAT 	Statute
THES 	Thesis/Dissertation
UNBILL 	Unenacted Bill
UNPB 	Unpublished work
VIDEO 	Video recording

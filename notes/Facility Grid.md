Can't edit equipment parameters in checklists
  - Change 'Installed As Submitted' to blank
  - Save checklist


# File uploads

Reverse engineering, appears that `plupload` is used for file uploads (<https://www.plupload.com/>).
<https://github.com/moxiecode/plupload/>.

Found the code for the GUID id at `js/moxie.js` line 525 in the source code:

```javascript
	var guid = (function() {
		var counter = 0;

		return function(prefix) {
			var guid = new Date().getTime().toString(32), i;

			for (i = 0; i < 5; i++) {
				guid += Math.floor(Math.random() * 65535).toString(32);
			}

			return (prefix || 'o_') + guid + (counter++).toString(32);
		};
	}());

```

#!/bin/sh
redo-ifchange rss.tsv

printf "#!/bin/sh\n"
printf "sfeedpath=\"\$HOME\"/.local/share/sfeed/feeds\n"

printf "# fetch a feed via HTTP/HTTPS etc.
# fetch(name, url, feedfile)
fetch() {
	# fail on redirects, hide User-Agent, timeout is 15 seconds.
	curl -L --max-redirs 10 -H \"User-Agent:\" -f -s -m 15 \"\$2\" 2>/dev/null
}
"

printf "feeds() {\n"

awk 'BEGIN {FS="\t" } { printf "    feed \"%s\" \"%s\"\n", $2, $1 }' rss.tsv

printf "}\n"

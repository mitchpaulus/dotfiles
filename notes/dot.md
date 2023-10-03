# `dot`

Super useful tool for producing graphs, like graph theory.

```
dot -Tpng input.dot > output.png
```

Typical file looks like

```
strict digraph graphname {
  node1 [label="label with spaces"]
  node1 -> node2 [label="edge label"]
  ...
}
```

```
digraph {
  abc [color = red]
}
```

Other formats:
- `canon`
- `cmap`
- `cmapx`
- `cmapx_np`
- `dot`
- `dot_json`
- `eps`
- `fig`
- `gd`
- `gd2`
- `gif`
- `gv`
- `imap`
- `imap_np`
- `ismap`
- `jpe`
- `jpeg`
- `jpg`
- `json`
- `json0`
- `mp`
- `pdf`
- `pic`
- `plain`
- `plain-ext`
- `png`
- `pov`
- `ps`
- `ps2`
- `svg`
- `svgz`
- `tk`
- `vdx`
- `vml`
- `vmlz`
- `vrml`
- `wbmp`
- `webp`
- `x11`
- `xdot`
- `xdot1.2`
- `xdot1.4`
- `xdot_json`
- `xlib`

```grammar
graph	:	[ strict ] (graph | digraph) [ ID ] '{' stmt_list '}'
stmt_list	:	[ stmt [ ';' ] stmt_list ]
stmt	:	node_stmt
      |	edge_stmt
      |	attr_stmt
      |	ID '=' ID
      |	subgraph

attr_stmt	:	(graph | node | edge) attr_list

attr_list	:	'[' [ a_list ] ']' [ attr_list ]

a_list	:	ID '=' ID [ (';' | ',') ] [ a_list ]
edge_stmt	:	(node_id | subgraph) edgeRHS [ attr_list ]
edgeRHS	:	edgeop (node_id | subgraph) [ edgeRHS ]
node_stmt	:	node_id [ attr_list ]
node_id	:	ID [ port ]
port	:	':' ID [ ':' compass_pt ]
|	':' compass_pt
subgraph	:	[ subgraph [ ID ] ] '{' stmt_list '}'
compass_pt	:	(n | ne | e | se | s | sw | w | nw | c | _)
```

# Shapes

<https://graphviz.org/doc/info/shapes.html#polygon>

`box`, `rect`, `rectangle`
`square`
`diamond`
`point`
`circle`
`triangle`

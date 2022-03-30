# HTML

## Form submission algorithm

https://html.spec.whatwg.org/#constructing-form-data-set

Elements:
- button
- input
- select
- textarea
- form-associated custom elements


## Link to internal headings

```html
<a href="#id">Link</a>
<h1 id="id">Header</h1>
```

Valid id:

From <https://www.leonieclaire.com/the-best-writing-tips/what-characters-are-allowed-in-html-id/>:

The HTML 4.01 spec states that ID tokens must begin with a letter (
[A-Za-z] ) and may be followed by any number of letters, digits (
[0-9]), hyphens ( – ), underscores ( _ ), colons ( : ), and periods ( .
). Classnames can contain any character, and they don’t have to start
with a letter to be valid.

## Tables

In this order:
1. an optional `<caption>` element,
2. zero or more `<colgroup>` elements,
3. an optional `<thead>` element,
4. either one of the following:
   - zero or more `<tbody>` elements
   - one or more `<tr>` elements
5. an optional `<tfoot>` element

<thead> or <tbody> Must contain 0 or more <tr> elements
<tr> contains either <td> or <th> elements

`colspan="2" rowspan="2"` - used on `<td>` or `<th>` elements.

## Flow Elements

- `<a>`
- `<abbr>`
- `<address>`
- `<article>`
- `<aside>`
- `<audio>`
- `<b>`
- `<bdo>`
- `<bdi>`
- `<blockquote>`
- `<br>`
- `<button>`
- `<canvas>`
- `<cite>`
- `<code>`
- `<command>`
- `<data>`
- `<datalist>`
- `<del>`
- `<details>`
- `<dfn>`
- `<div>`
- `<dl>`
- `<em>`
- `<embed>`
- `<fieldset>`
- `<figure>`
- `<footer>`
- `<form>`
- `<h1>`
- `<h2>`
- `<h3>`
- `<h4>`
- `<h5>`
- `<h6>`
- `<header>`
- `<hgroup>`
- `<hr>`
- `<i>`
- `<iframe>`
- `<img>`
- `<input>`
- `<ins>`
- `<kbd>`
- `<keygen>`
- `<label>`
- `<main>`
- `<map>`
- `<mark>`
- `<math>`
- `<menu>`
- `<meter>`
- `<nav>`
- `<noscript>`
- `<object>`
- `<ol>`
- `<output>`
- `<p>`
- `<picture>`
- `<pre>`
- `<progress>`
- `<q>`
- `<ruby>`
- `<s>`
- `<samp>`
- `<script>`
- `<section>`
- `<select>`
- `<small>`
- `<span>`
- `<strong>`
- `<sub>`
- `<sup>`
- `<svg>`
- `<table>`
- `<template>`
- `<textarea>`
- `<time>`
- `<u>`
- `<ul>`
- `<var>`
- `<video>`
- `<wbr>`

## Progress Element

[Cool builtin element for progress.](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress)


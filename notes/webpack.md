# Webpack

Came across its use while trying to implement the JavaScript target in
Antlr (See
[here](https://github.com/antlr/antlr4/blob/master/doc/javascript-target.md).
The runtime code is written for a node environment, which makes it
harder to integrate into the browser code that I'd like to use it for.

`webpack` can be used to turn this code into something the browser
understands. We typically don't `webpack` any of our code, plus we use
TypeScript for the most part, so what I wanted is to have the final
output of the `webpack` code simply add what I needed to the global
scope under some variable name.

Could accomplish this by having a `.js` file like:

```js
window.antlr4 = require('./index.js');

// ... Add other things to the object if required

window.antlr4.CompassLexer = require('./CompassLexer.js');
```

then using:

```sh
npx webpack mycode.js
```

## Installing `webpack`

Will need to have `node` and `npm`.

```
mkdir webpack-demo
cd webpack-demo
npm init -y
npm install webpack webpack-cli --save-dev
```

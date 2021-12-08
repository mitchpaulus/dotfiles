# siunitx package

- [Options for spacing between number and unit](https://tex.stackexchange.com/questions/597855/special-rule-in-siunitx-for-percentages).
- Used to be `number-unit-prodcut`, now is `quantity-product`.

From siunitx user manual on custom pre-defined unit list.

There are many units which sit outside of those defined in the (current)
si Brochure which are of use to many people. Most obvious are those
which have been detailed in previous editions of the Brochure, as
described in Section 6, but there are many others. It is often
convenient to have a pre-defined set of useful units available without
needing to copy the full set of definitions into each source file. At
the same time, it is important that such sources do show that they are
using units not defined by the core part of siunitx. The most
straight-forward way to achieve this is to create a separate file, for
example siunitx-local-units.tex, and place it in your local TEX tree
(usually ~/texmf/tex/latex/ on Linux, ~/Library/texmf/tex/latex/ on
macOS or C:\Users\<name>\texmf\tex\latex on Windows). This can then be
loaded in the preamble using

```tex
% Load useful ’local’ units
\input{siunitx-local-units}
```

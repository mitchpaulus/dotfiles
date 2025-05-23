Setting up trending.

1. Go to controller -> Properties -> Trend Sources
2. Open Developer Tools
3. In Console, run

   ```
   copy(actionContent.contentDocument.documentElement.outerHTML)
   ```

4. Paste into local HTML file
5. Run

   ```
  ./trendRefs.msh < input.html
  ./trendNames.msh < input.html
   ````

6. Get controller Id

   1. Do a sample CSV export for one trend, note the DBID in the request.

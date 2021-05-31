{-# LANGUAGE OverloadedStrings #-}
import System.Environment
import qualified Data.Text as T

main = do
    args <- getArgs
    putStrLn $ T.unpack $ underscore $ head args

underscore :: String -> T.Text
underscore commandline = let splitCommandLine = splitLine commandline
                         in T.concat [head splitCommandLine, " ",  T.intercalate "_" (tail splitCommandLine)]

splitLine :: String -> [T.Text]
splitLine line = T.words $ T.pack $ line

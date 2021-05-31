{-# LANGUAGE OverloadedStrings #-}
import System.Environment
import qualified Data.Text as T
import qualified Data.Text.IO as TIO

main = do
    args <- getArgs
    handleArgs args

underscore :: String -> T.Text
underscore commandline = let splitCommandLine = splitLine commandline
                         in T.concat $ [head splitCommandLine,
                           " ",
                           T.intercalate " " (map joinUnderscore (splitOnExtensions $ tail splitCommandLine))]

joinUnderscore tokens = T.intercalate "_" tokens

splitLine :: String -> [T.Text]
splitLine line = T.words $ T.pack $ line

handleArgs :: [String] -> IO ()
handleArgs args
    | null args        = putStr helpText
    | length args == 1 = TIO.putStr $ underscore $ head args
    | otherwise        = putStrLn "underscore_files expects only a single argument."

helpText = unlines [
    "underscore_files",
    "",
    "USAGE: underscore_files commandline",
    "",
    "This function attempts to add underscores between words on the command line.",
    "The first word is assumed to be the command."
    ]

type Token = T.Text

-- Splits a list of tokens into a tuple: first value is the list of tokens til first extension (including extension token)
-- second value is remaining tokens.
takeTillExt :: [Token] -> ([Token], [Token])
takeTillExt []  = ([], [])
takeTillExt (x:xs)
    | isExtension x = ([x], xs)
    | otherwise     = let (ys, zs) = takeTillExt xs in (x:ys, zs)

splitOnExtensions :: [Token] -> [[Token]]
splitOnExtensions [] = [[]]
splitOnExtensions tokens
    | snd takeTilExtResult == [] = [fst takeTilExtResult]
    | fst takeTilExtResult == [] = [snd takeTilExtResult]
    | otherwise = (fst takeTilExtResult) : (splitOnExtensions (snd takeTilExtResult))
    where takeTilExtResult = takeTillExt tokens

-- Considering any token with a period to be an extension.
isExtension text =
    case findResult of
        Nothing -> False
        Just _  -> True
    where findResult = T.find (== '.') text

import System.Environment

main = do
    args <- getArgs
    let options = parseArgs args defaultOptions
    putStrLn $ printExcelReset (inputCell options) (coords options !! 0) (coords options !! 1) (coords options !! 2) (coords options !! 3)

data Options = Options {
    absolute :: Bool,
    orientation :: Orientation,
    startCell :: String,
    inputCell :: String,
    helpWanted :: Bool,
    coords :: [String]
    } deriving Show

data Orientation = Vertical | Horizontal deriving Show

defaultOptions = Options {
    absolute = True,
    orientation = Vertical,
    startCell = "$A$1",
    helpWanted = False,
    inputCell = "B1",
    coords = ["A1", "A2", "A3", "A4"]
}

parseArgs ("-r" : xs) options = parseArgs xs (options { absolute = False })
parseArgs ("-h" : xs) options = parseArgs xs (options { orientation = Horizontal })
parseArgs ("-v" : xs) options = parseArgs xs (options { orientation = Vertical })
parseArgs ("--help" : xs) options = parseArgs xs (options { helpWanted = True })
parseArgs [] options = options

parsePositional (input:coords) options =
    options { inputCell = (input), coords = coords }

printExcelReset input x1 y1 x2 y2 =
        "IF(" ++ input ++ " < " ++ x1 ++ ", " ++ y1 ++ ", IF(" ++ input ++ " > " ++ x2 ++ ", " ++ y2 ++ ", "

helpText = unlines [
    "linear_reset_excel",
    "",
    "USAGE:",
    "linear_reset_excel "
    ]

import System.Environment
import System.Process
import System.Exit
import System.IO

main = do
    args <- getArgs
    let options = parseArgs args defaultPrintMathOptions
    if helpRequested options then putStrLn helpText else processEquation options

processEquation :: PrintMathOptions -> IO ()
processEquation options = do
    myText <- equationToPrint options
    -- Using equation, write a self-contained tex template file
    writeFile (texFileName options) (template myText)
    -- Open a handle to send output to /dev/null
    nullHandle <- openFile "/dev/null" WriteMode
    -- Run lualatex on template file
    let process =  proc "lualatex" [(texFileName options)]
    (_, _, _, processHandle) <- createProcess process { std_out = UseHandle nullHandle }
    exitCode <- waitForProcess processHandle
    if exitCode == ExitSuccess then putStrLn "Success" else putStrLn "Fail"
    hClose nullHandle

equationToPrint :: PrintMathOptions -> IO String
equationToPrint options = if inputFile options == "" then return $ equation options else readFile $ inputFile options

template :: String -> String
template equationText = unlines
    [
        "\\documentclass[border=1pt]{standalone}",
        "\\begin{document}",
        "\\( \\displaystyle " ++ equationText ++ " \\)",
        "\\end{document}"
    ]

parseArgs :: [String] -> PrintMathOptions -> PrintMathOptions
parseArgs (arg:args) options
    | arg == "-h" || arg == "--help" = parseArgs args (options { helpRequested = True })
    | arg == "-f"                    = parseArgs (tail args) (options { inputFile = head args })
    | arg == "-o"                    = parseArgs (tail args) (options { outputFileName = head args })
    | otherwise                      = parseArgs args (options { equation = arg })

parseArgs [] options = options


data PrintMathOptions = PrintMathOptions
    {
        inputFile      :: String,
        outputFileName :: String,
        helpRequested  :: Bool,
        equation       :: String
    }


defaultPrintMathOptions = PrintMathOptions {
    inputFile = "",
    outputFileName = "math",
    helpRequested = False,
    equation = ""
}

texFileName :: PrintMathOptions -> String
texFileName options = outputFileName options ++ ".tex"

helpText :: String
helpText = unlines
    [
        "printmath - command line program to generate Tex equations",
        "",
        "USAGE:",
        "printmath [options] equation",
        "",
        "OPTIONS",
        "  -f         Input file that contains Tex equation",
        "  -o         Set output file name. Don't include extension",
        "  -h, --help Show this help and exit"
    ]


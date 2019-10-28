import System.Environment

main = do
    args <- getArgs
    let numArgs = length args
    let result =
                if any (== "-h") args then helpText
                else if numArgs /= 3 then "3 arguments required. Received " ++ (show numArgs) ++ "."
                else
                    do
                        let value = read (args !! 0)
                        let originalUnit = args !! 1
                        let newUnit = args !! 2

                        case convertUnit value originalUnit newUnit of
                                        Just convertedValue -> show convertedValue
                                        Nothing             -> "No conversion from " ++ originalUnit ++ " to " ++ newUnit
    putStrLn result

convertUnit :: Double -> String -> String -> Maybe Double
convertUnit val "C" "F" = Just (val * 9 / 5 + 32)
convertUnit val "F" "C" = Just ((val - 32) * 5 / 9)
convertUnit val "m2" "ft2" = Just (val * 1562500 / 145161)
convertUnit val "ft2" "m2" = Just (val * 145161 / 1562500)
convertUnit val "W/ft2" "W/m2" = Just (val * 1562500 / 145161)
convertUnit val "W/m2" "W/ft2" = Just (val * 145161 / 1562500)
convertUnit _ _ _ = Nothing


helpText = unlines [
                "uc - unit converter",
                "",
                "USAGE:",
                "  uc val fromUnit toUnit",
                "",
                "Examples:",
                "",
                "70°F to °C",
                " uc 70 F C"
            ]

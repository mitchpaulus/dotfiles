span :: (a -> Bool) -> [a] -> ([a], [a])
span _ [] = ([], [])
span p (x:xs)
  | p x       = (x:ys, zs)
  | otherwise = ([], x:xs)
  where
    (ys, zs) = span p xs

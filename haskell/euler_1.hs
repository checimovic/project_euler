solution :: Int
solution = foldl1 (+) [x | x <- [3..999], x `mod` 3 == 0 || x `mod` 5 == 0]


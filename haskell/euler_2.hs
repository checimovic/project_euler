fibs :: [Int]
fibs = 1 : 2 : zipWith (+) fibs (tail fibs)

solution :: Int
solution = sum $ filter even $ takeWhile (<= 4000000) fibs

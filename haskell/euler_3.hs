-- Project Euler problem 3

{- The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ? -}

get_largest_factor :: Int -> Int
get_largest_factor n = get_largest_factor' n 2 

get_largest_factor' :: Int -> Int -> Int
get_largest_factor' n divisor 
    | n == divisor = divisor 
    | n `mod` divisor == 0 = get_largest_factor' (n `div` divisor) divisor
    | otherwise = get_largest_factor' n (succ divisor)  
    
solution = get_largest_factor 600851475143

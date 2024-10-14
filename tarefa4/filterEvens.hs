module FilterEvens where

-- Função que retorna apenas os números pares de uma lista
filterEvens :: [Int] -> [Int]
filterEvens xs = filter even xs

-- Teste para filterEvens
testFilterEvens :: Bool
testFilterEvens = filterEvens [1, 2, 3, 4, 5, 6] == [2, 4, 6]

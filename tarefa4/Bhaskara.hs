module Bhaskara where

bhaskara :: Double -> Double -> Double -> (Double, Double)
bhaskara a b c
  | delta < 0 = error "raizes complexas nao sao calculadas"
  | otherwise = ((-b + sqrt delta) / (2 * a), (-b - sqrt delta) / (2 * a))
  where
    delta = b^2 - 4 * a * c

-- Teste para bhaskara
testBhaskara :: Bool
testBhaskara = bhaskara 1 (-3) 2 == (2.0, 1.0)

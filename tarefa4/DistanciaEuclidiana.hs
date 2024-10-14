module DistanciaEuclidiana where

import Data.List (zipWith)

distanciaEuclidiana :: [Double] -> [Double] -> Double
distanciaEuclidiana xs ys = sqrt $ sum $ zipWith (\x y -> (x - y) ^ 2) xs ys

-- teste para distanciaEuclidiana
testDistanciaEuclidiana :: Bool
testDistanciaEuclidiana = distanciaEuclidiana [1.0, 2.0, 3.0] [4.0, 5.0, 6.0] == sqrt 27

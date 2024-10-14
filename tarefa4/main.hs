-- importando os arquivos necessários
import SomaQuadrados
import DistanciaEuclidiana
import Bhaskara
import FilterEvens

-- função principal para rodar os testes básicos das funções
main :: IO ()
main = do
    putStrLn "Teste de somaQuadrados (3, 4):"
    print (somaQuadrados 3 4)  -- Deve retornar 25

    putStrLn "Teste de distanciaEuclidiana ([1.0, 2.0, 3.0], [4.0, 5.0, 6.0]):"
    print (distanciaEuclidiana [1.0, 2.0, 3.0] [4.0, 5.0, 6.0])  -- Deve retornar 5.19615242270663

    putStrLn "Teste de bhaskara (1, -3, 2):"
    print (bhaskara 1 (-3) 2)  -- Deve retornar (2.0, 1.0)

    putStrLn "Teste de filterEvens [1, 2, 3, 4, 5, 6]:"
    print (filterEvens [1, 2, 3, 4, 5, 6])  -- Deve retornar [2, 4, 6]

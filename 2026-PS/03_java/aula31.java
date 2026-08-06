public class aula31 {
    public static void main(String[] args) {
        int[] valores = {8, 3, 10, 5, 12};
        System.out.println(calculaSoma(valores));
        System.out.println(calculaMedia(valores));
        System.out.println(menorValor(valores));
        System.out.println(maiorValor(valores));
        System.out.println(contarAcima(valores, 6));
    }

    static int calculaSoma(int[] numeros) {
        int soma = 0;
        for (int n : numeros) {
            soma += n;
        }
        return soma;
    }

    static int calculaMedia(int[] numeros) {
        int soma = 0;
        for (int i=0; i < numeros.length; i++) {
            soma += numeros[i];
        }
        return soma / numeros.length;
    }

    static int menorValor(int[] numeros) {
        int menor = numeros[0];
        int it = 1;
        while (it < numeros.length) {
            if (numeros[it] < menor) {
                menor = numeros[it];
            }
            it++;
        }
        return menor;
    }

    static int maiorValor(int[] numeros) {
        int maior = numeros[0];
        for (int n : numeros) {
            if (n > maior) {
                maior = n;
            }
        }
        return maior;
    }

    static int contarAcima(int[] numeros, int limite) {
        int quantidade = 0;
        for (int i=0; i < numeros.length; i++) {
            if (numeros[i] > limite) {
                quantidade++;
            }
        }
        return quantidade;
    }

}

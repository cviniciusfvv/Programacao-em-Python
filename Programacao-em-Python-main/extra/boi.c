#include <stdio.h>

int main() {
    float valor;
    int parcelas, quantidade;
    float resultado;
    printf("Digite o valor da parcela leião: ");
    scanf("%f", &valor);
    printf("Digite a quantidade de parcelas: ");
    scanf("%d", &parcelas);
    printf("Quantidade de cabeças: ");
    scanf("%d", &quantidade);
    resultado = (valor * parcelas) * quantidade;
    printf("Valor da parcela: %.2f\n", valor);
    printf("Quantidade de parcelas: %d\n", parcelas);
    printf("Quantidade de cabeças: %d\n", quantidade);
    printf("Valor total: %.2f\n", resultado);
    return 0;
}
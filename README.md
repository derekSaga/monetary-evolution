# Monetary Evolution
Sistema que guarda as cotações do dólar versus real, euro e iene(JPY) e que as exibe em um gráfico, respeitando as seguintes especificações:

* Deve ser possível informar uma data de início e de fim para consultar qualquer período de tempo, contanto que o período informado seja de no máximo 5 dias úteis.
* Deve ser possível variar as moedas (real, euro e iene).

Existem algumas restrições que devem ser seguidas:
* Os dados das cotações devem ser coletados utilizando a api do https://www.vatcomply.com/documentation (Você vai precisar usar Dólar como base).
* O código deve ser desenvolvido utilizando um repositório git no seu perfil do Github ou BitBucket;
* Backend: deve ser implementado em python utilizando o framework django.
* Frontend: o único requisito é usar o highcharts para apresentação dos dados.

### Pré-Requisitos
* Docker em sua versão 22.3.1 ou superior

## Uso


Você deve usar o comando abaixo em seu terminal:
```bash
docker-compose up app --build
```
A aplicação será exposta na url http://localhost:8000/


# Asgard API SDK

Nesse projeto encontramos código comum que pode ser usado em plugins escritos para a API.



# Funções disponíveis

## asgard.sdk.options.get_option()

Permite ler múltiplas variaveis de ambiente e retorna os valores em uma lista, ex:

dados = get_option("MESOS", "ADDRESS")

Nesse caso a variável `dados` seria uma lista com todos os valores das envs:

 * HOLLOWMAN_MESOS_ADDRESS_0
 * HOLLOWMAN_MESOS_ADDRESS_1
 * HOLLOWMAN_MESOS_ADDRESS_2
 * HOLLOWMAN_MESOS_ADDRESS_<N>

 Onde `N` é um inteiro

## mesos.sdk.mesos.get_mesos_leader_address()

Retorna o endereço do mesos que atualmente é o lider do cluster. Essa função depende
da `get_option`. Faz a chamada `get_option("MESOS", "ADDRESS")`

## mesos.sdk.is_master_healthy()

Dada uma URL de um master, acessa `<URL>/health` e retorna True em caso de HTTP 200 OK, False caso contrário.
Essa função usa timeout de 2s


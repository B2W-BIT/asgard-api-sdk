
# Asgard API SDK

Nesse projeto encontramos código comum que pode ser usado em plugins escritos para a API.



# Funções disponíveis

asgard.sdk.options.get_option()

Permite ler múltiplas variaveis de ambiente e retorna os valores em uma lista, ex:

dados = get_option("MESOS", "ADDRESS")

Nesse caso a variável `dados` seria uma lista com todos os valores das envs:

 * HOLLOWMAN_MESOS_ADDRESS_0
 * HOLLOWMAN_MESOS_ADDRESS_1
 * HOLLOWMAN_MESOS_ADDRESS_2
 * HOLLOWMAN_MESOS_ADDRESS_<N>

 Onde `N` é um inteiro


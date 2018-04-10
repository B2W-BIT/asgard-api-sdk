#encoding: utf-8

import os

ENV_NAME_PATTERN = "HOLLOWMAN_{namespace}_{option_name}"


def get_option(namespace, option_name):
    """
    Gets an options based on an namespace and an option name.
    All option are read from Environ variables. The formation name is:
    HOLLOWMAN_<NAMESPACE>_<OPTIONNAME>
    If OPTIONNAME is a multi-value (list) option a numver suffix can be used, eg:
        HOLLOWMAN_<NAMESPACE>_<OPTIONNAME>_<INDEX>


    :name: Name of the filter who owns this option
    :option_name: Name of the option
    :returns: The option value, **always** as a list of values

    """
    envvalue = _get_env_value(namespace, option_name)

    idx = 0
    final_value = []

    if envvalue:
        final_value.append(envvalue)

    while _get_env_value(namespace, option_name, idx):
        final_value.append(_get_env_value(namespace, option_name, idx))
        idx += 1

    return final_value

def _get_env_value(namespace, option_name, idx=None):
    base_envname = ENV_NAME_PATTERN.format(namespace=namespace.upper(), option_name=option_name.upper())
    if idx is None:
        return os.getenv(base_envname)
    return os.getenv("{}_{}".format(base_envname, idx))

{% if proxy_auth is defined and proxy_auth -%}
export proxy={{proxy_proto}}://{{proxy_user}}:{{proxy_pass}}@{{proxy_address}}:{{proxy_port}}
{% else -%}
export proxy={{proxy_proto}}://{{proxy_address}}:{{proxy_port}}
{%- endif %}

export http_proxy=$proxy \
       https_proxy=$proxy \
       PROXY=$proxy \
       HTTP_PROXY=$proxy \
       HTTPS_PROXY=$proxy

# -*- coding: UTF-8 -*-
# descontos.py
class Desconto_por_cinco_itens(object):

  def calcular(self, orcamento):

    if(orcamento.total_itens > 5):
        return orcamento.valor * 0.1
    else: 
      # se não segue a regra, o desconto é zero!
      return 0

class Desconto_por_mais_de_quinhentos_reais(object):

  def calcular(self, orcamento):

    if(orcamento.valor > 500):
      return orcamento.valor * 0.07
    else:
      # se não segue a regra, o desconto é zero
      return 0
# -*- coding: utf-8 -*-
import scrapy
import json
from locations.hourstudy import inputoutput


class VeaSpider(scrapy.Spider):

    name = "vea"
    allowed_domains = ["www.supermercadosvea.com"]
    start_urls = (
        'http://www.supermercadosvea.com.ar/sucursales-obtener.html',
    )

    def parse(self, response):

        store_list = json.loads(response.body_as_unicode())
        for store in store_list:
            properties = {
                'name': store['descripcion'],
                'addr_full': store['direccion'],
                'city': store['vea_localidades_desc'],
                'opening_hours': store['horarios'],
                'phone': store['telefonos'],
                'ref': str(store['codigo']).replace('SM ', ''),
            }
            # yield inputoutput(**properties)

            raw = store['horarios']
            formatted = sstore['horarios']
            yield inputoutput(raw,formatted)


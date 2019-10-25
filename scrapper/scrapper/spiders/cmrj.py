# -*- coding: utf-8 -*-
import scrapy

class CMRJSpider(scrapy.Spider):
   name = "cmrj"
   start_urls = [
       "http://www.camara.rj.gov.br/vereadores_atuais.php"
   ]

   def parse(self, response):
       line_count = 0
       for item in response.css("table#listaver tr"):
            if line_count == 0:
               line_count += 1
            else:
                obj = {
                    "nome": item.css("tr td a img::attr(alt)").extract()[0].upper(),
                    "img_url": item.css("tr td a img::attr(src)").extract()[0],
                    "telefone": item.css("tr td")[4].css("h6::text")[0].extract(),
                    "partido": item.css("tr td a img::attr(alt)").extract()[1].replace(" ", "")
                }

                if len(item.css("tr td")[5].css("a::text").extract()) > 0:
                    obj["email"] = item.css("tr td")[5].css("a::text").extract()[0]

                yield obj
                
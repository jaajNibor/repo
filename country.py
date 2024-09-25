import pycountry
import pycountry_convert
import unittest

def pays(country_alpha_2):
    #for country in pycountry.countries:
    try:
        continent_code = pycountry_convert.country_alpha2_to_continent_code(country_alpha_2)
        continent_name = pycountry_convert.convert_continent_code_to_continent_name(continent_code)
    except KeyError:
        continent_name = 'Unknown'
    return(continent_name)
    #print(f'{country.name}({continent_name})'.rstrip())

if __name__=='__main__':
    unittest.main()
    assert pays('FR') == 'Europe'
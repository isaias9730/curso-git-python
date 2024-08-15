import csv
import charts
import utils

def run():
    with open('data.csv', mode='r') as file:
        # Lee el archivo CSV correctamente
        data = list(csv.DictReader(file))
        
        # Verifica si hay filas sin la clave 'Continent'
        missing_continent = [item for item in data if 'Continent' not in item]
        if missing_continent:
            print(f"Advertencia: {len(missing_continent)} filas no tienen la clave 'Continent'.")

        # Filtra los datos para obtener solo los países de Sudamérica
        filtered_data = list(filter(lambda item: item.get('Continent') == 'South America', data))

        # Mapea los países y los porcentajes de población
        countries = list(map(lambda x: x['Country'], filtered_data))
        percentages = list(map(lambda x: x['World Population Percentage'], filtered_data))
        
        # Genera un gráfico de torta (pie chart) usando los datos filtrados
        charts.generate_pie_chart(countries, percentages)
        
        # Pide al usuario que ingrese un país
        country = input('Type Country => ')
        print(country)
        
        # Busca la población por país utilizando utils
        result = utils.population_by_country(data, country)
        
        if len(result) > 0:
            country_data = result[0]
            labels, values = utils.get_population(country_data)
            charts.generate_bar_chart(country['country'], labels, values)
        else:
            print(f'No se encontraron datos para el país:{country}')

if __name__ == '__main__':
    run()
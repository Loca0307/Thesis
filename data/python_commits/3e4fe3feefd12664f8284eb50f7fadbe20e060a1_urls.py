

def trip_analysis(request, country_name):
    top_city_counter = get_top_city(country_name, 5)
    labels = [i[0] for i in top_city_counter]
    data = [i[1] for i in top_city_counter]

    info = CountryInfo.objects.get(country_name=country_name)

    return render(request, 'analysis.html', {
        'country_name': country_name,
        'country_name_ch': info.country_name_ch,
        'analysis': info.analysis,
        "labels": labels,
        "data": data,
    })
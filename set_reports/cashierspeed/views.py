from operator import itemgetter

from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime, timedelta
from .analyzer import DataAnalyzer
from .excel import ExcelExporter
from .forms import DateForm


# def put_to_excel(current_date, shop_num, exporter):
#     """
#     Выгрузка в Excel.
#     :param current_date: дата анализа, будет еще именем вкладки.
#     :param shop_num: номер магазина, если нужен фильтр по магазину.
#     :param exporter: Класс экспорта из модуля excel.
#     :return: None.
#     """
#     analyzer = DataAnalyzer(datetime.strftime(current_date, '%Y-%m-%d'))
#     analyzer.get_results(shop_num)
#     analyzer.calculate_cashier_data()
#     analyzer.generate_summary_data()
#     analyzer.export_summary_to_excel(exporter)


def render_to_main(current_date, shop_num):
    analyzer = DataAnalyzer(datetime.strftime(current_date, '%Y-%m-%d'))
    analyzer.get_results(shop_num)
    analyzer.calculate_cashier_data()
    analyzer.generate_summary_data()
    summary_data = analyzer.summary_data
    # analyzer.export_summary_to_excel(exporter)
    summary_data_sorted = sorted(summary_data, key=itemgetter(1, 0))

    return summary_data_sorted


def analyze(operation_day, all_week=None, all_month=None, shop_num=None):
    """
    Основная функция для выборки и передачи данных для выгрузки excel.
    :param operation_day: день или начальный день для выгрузки
    :param all_week: выгружать ли неделю.
    :param all_month: выгружать ли месяц
    :param shop_num: номер магазина, если нужен фильтр по магазину.
    :return: None.
    """
    if all_week:
        day_count = 7
        exporter = ExcelExporter(f'{operation_day.month}-{operation_day.year}.xlsx')
        exporter.create_workbook()
        for single_date in (operation_day + timedelta(n) for n in range(day_count)):
            # put_to_excel(single_date, shop_num, exporter)
            res = render_to_main(single_date, shop_num)
            print(f'Analyze for day {datetime.strftime(single_date, "%Y-%m-%d")} is done')
            return res

    else:
        exporter = ExcelExporter(f'{datetime.strftime(operation_day, "%Y-%m-%d")}.xlsx')
        exporter.create_workbook()
        # put_to_excel(operation_day, shop_num, exporter)
        res = render_to_main(operation_day, shop_num)
        # exporter.save_workbook()
        print(2, res)
        return res


def main_page(request):
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            # Получение введенной пользователем даты из формы
            analyze_day = form.cleaned_data['analyze_day']
            filter_shop = form.cleaned_data['filter_shop']
            shop_num = form.cleaned_data['shop_num'] if filter_shop else None
            # фильтр по магазину
            table_data = analyze(analyze_day, all_week=True, shop_num=shop_num)
            return render(request, 'index.html', {'form': form, 'analyze_day': analyze_day, 'table_data': table_data})
    else:
        form = DateForm()
    return render(request, 'index.html', {'form': form})


# analyze_day = '2023-05-01'

# if __name__ == '__main__':
#     analyze(datetime.strptime(analyze_day, '%Y-%m-%d'), all_week=True, shop_num=1)
#     print(f'Analyze period complete')

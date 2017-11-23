# -*- coding: utf-8 -*-
import xlrd
import xlwt


def read_from_xls(fp, sheet=None):
    workbook = xlrd.open_workbook(fp)
    if isinstance(sheet, int):
        tables = [workbook.sheet_by_index(sheet)]
    elif isinstance(sheet, str):
        tables = [workbook.sheet_by_name(sheet)]
    else:
        tables = [workbook.sheet_by_name(sn) for sn in workbook.sheet_names()]
    data = []
    for table in tables:
        _table = []
        keys = table.row_values(0)
        for i in range(1, table.nrows):
            vals = table.row_values(i)
            _table.append(dict(zip(keys, vals)))
        if _table:
            data.append(_table)
    return data


def write_xls(fp, data, keys_single_sheet=None, pure_data=False, encoding='GBK'):
    workbook = xlwt.Workbook(encoding=encoding or 'utf-8')
    if isinstance(data, list):
        data = {'sheet': data}
    for sheet_name, items in data.items():
        sheet = workbook.add_sheet(sheet_name)
        keys = keys_single_sheet or items[0].keys()

        head_line_numer = 0
        if not pure_data:
            for idx, k in enumerate(keys):
                sheet.write(0, idx, k)
            head_line_numer = 1

        for ldx, item in enumerate(items):
            for idx, key in enumerate(keys):
                sheet.write(ldx + head_line_numer, idx, item[key])
    workbook.save(fp)


def write_xls_beta(fp, data, pure_data=False, encoding='GBK'):
    pass


if __name__ == '__main__':
    data = {
        'sheet1': [
            {
                'name': 'dick',
                'age': 23
            },
            {
                'name': 'dick',
                'age': 22
            },
            {
                'name': 'dick',
                'age': 21
            }
        ],
        'sheet2': [
            {
                'name': 'dick1',
                'age': 231
            },
            {
                'name': 'dick2',
                'age': 232
            },
            {
                'name': 'dick3',
                'age': 233
            }
        ]
    }

    write_xls(fp='test.xlsx', data=data)


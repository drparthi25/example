from xlrd import open_workbook as wb
op = wb("mn_details.xlsx").sheet_by_index(0)
mn_dict = {}
#self.print_output(op.nrows)
for i in range(1,op.nrows):
    if op.cell_value(i, 0):
        mn_dict[op.cell_value(i, 0)] = [op.cell_value(i, 1).strip(),op.cell_value(i, 2).strip(),op.cell_value(i, 3).strip()]
print mn_dict

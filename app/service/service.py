import numpy as np

from app.service.service_abc import WorkGraphBase
from app.service.service_abc import mat_evel, SAFE_FUNCS
from app.service.DRY import draw_graph

class WorkGraph(WorkGraphBase):
    def add_graph(self, sl):
        try:
            x_min = float(sl.x_min_input.text())
            x_max = float(sl.x_max_input.text())

            if x_min >= x_max:
                raise ValueError("x_min must be less than x_max")
            
        except ValueError as e:
            print(f"x range error: {e}")
            return

        x = np.linspace(x_min, x_max, 400)
        expr = sl.mat.text()
        mat_evel.append(f"{expr}\n")

        try:
            y = eval(expr, {"x": x, **SAFE_FUNCS, "__builtins__": {}})

            if np.isscalar(y):
                y = np.full_like(x, y)

            if y.shape != x.shape:
                raise ValueError("The expression must return an array of the same length as x.")

            draw_graph(self=sl, dr=True, x=x, y=y, expr=expr)

            res = ''

            for i in range(len(mat_evel)):
                res += mat_evel[i]

            sl.mat_exp.setText(res)
        except Exception as e:
            print(f"Error in expression: {e}")
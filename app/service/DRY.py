def draw_graph(self, dr : bool, x=None, y=None, expr=None):
    if dr:
        self.ax.plot(x, y, label=expr)
    else:
        self.ax.cla()
        
    self.ax.set_title("Graph")
    self.ax.set_xlabel("X")
    self.ax.set_ylabel("Y")
    self.ax.grid(True)
    self.ax.legend()
    self.canvas.draw()
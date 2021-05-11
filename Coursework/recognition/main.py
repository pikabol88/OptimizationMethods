from recognition.launcher import launch

def main():
    method = 'SMO'
    convert_classes = False
    verbose = True
    graphical = True
    plot_rows = 3
    plot_cols = 4

    launch(method, convert_classes, verbose, graphical, plot_rows, plot_cols)

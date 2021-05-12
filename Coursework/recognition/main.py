from tabulate import tabulate

from recognition.launcher import launch

def main():
    exp_count = 5

    verbose = True
    graphical = False
    plot_rows = 3
    plot_cols = 4

    scores_table = dict()
    scores_table['SMO'] = list()
    scores_table['IP'] = list()
    scores_table['SLSQP'] = list()

    for method in ('SMO', 'IP', 'SLSQP'):
        for convert_classes in (False, True):
            av_score = 0
            for exp in range(exp_count):
                av_score += launch(method, convert_classes, verbose, graphical, plot_rows, plot_cols)
            av_score /= exp_count
            scores_table[method].append(av_score)
    
    headers = ['', '10 classes', '2 classes']
    rows = [['SMO', scores_table['SMO'][0], scores_table['SMO'][1]],
            ['IP', scores_table['IP'][0], scores_table['IP'][1]],
            ['SLSQP', scores_table['SLSQP'][0], scores_table['SLSQP'][1]]]
    
    print("Average scores table:")    
    print(tabulate(rows, headers))

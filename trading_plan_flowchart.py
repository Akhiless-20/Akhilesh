from graphviz import Digraph

def create_flowchart():
    # Initialize the flowchart
    flowchart = Digraph(format='png', name='Trading Plan Flowchart')

    # Add nodes
    flowchart.node('A', 'Account: $5000 (Avinash Sir)', shape='box', style='filled', color='lightblue')
    flowchart.node('B', 'Risk Management: 5% per trade ($250)', shape='box', style='filled', color='lightgreen')
    flowchart.node('C', 'Daily Target: 3.3% ($165)', shape='box', style='filled', color='lightyellow')
    flowchart.node('D', 'Assets: Gold (XAU/USD) and BTC/USD', shape='ellipse', style='filled', color='lightcoral')
    flowchart.node('E', 'Example Trade 1: Gold', shape='ellipse', style='dotted', color='grey')
    flowchart.node('F', 'Buy at 1900
SL: 1898, TP: 1904', shape='plaintext')
    flowchart.node('G', 'Example Trade 2: BTC/USD', shape='ellipse', style='dotted', color='grey')
    flowchart.node('H', 'Buy at 18,500
SL: 18,300, TP: 18,900', shape='plaintext')
    flowchart.node('I', 'Expected Outcome: $10,000 (100% Return)', shape='box', style='filled', color='lightblue')

    # Connect nodes
    flowchart.edges([
        ('A', 'B'),
        ('B', 'C'),
        ('C', 'D'),
        ('D', 'E'),
        ('D', 'G'),
        ('E', 'F'),
        ('G', 'H'),
        ('C', 'I')
    ])

    # Save and render the flowchart
    flowchart.render(filename='/mnt/data/Trading_Plan_Flowchart', cleanup=True)

create_flowchart()

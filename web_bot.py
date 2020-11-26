import PySimpleGUI as sg
from webutils import get_html_using_content, parse_html_using_tag
from utils import get_statistics

layout = [
    [sg.Text("Web Page Analyzer",font=("Arial",18))],
    [sg.Text("Enter URL", font=("Arial",14)), sg.InputText("",font=("Arial",14),key='url'),
     sg.Button("Get Data", font=("Arial",14),key='get')],
    [sg.Multiline("",font=("Arial",14), size=(60,15),key = 'output')]
]


def get_details(url):
    html_content = get_html_using_content(url)
    data = parse_html_using_tag(html_content,'p')
    statistics = get_statistics(data)
    display(statistics)

def display(statistics):
    window['output'].print('The web page consists of the following information\n')
    window['output'].print(statistics['Line_count'],"sentences")
    window['output'].print(statistics['word_count'], "words")
    window['output'].print(statistics['unique_words'], "unique words\n")
    window['output'].print('The top words are\n')
    for i in statistics['top_words']:
        window['output'].print(i)



if __name__ == '__main__':
    window = sg.Window("WebPageAnalyser",layout)
    while True:
        event ,values = window.Read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'get':
            get_details(values['url'])
    window.Close()

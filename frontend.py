import PySimpleGUI as sg
from backend import download_audio, download_playlist

sg.theme('Reddit') 
layout = [  
    [sg.Text('URL do video:')],
    [sg.Input(key='url', size=(60,1))],
    [sg.Radio('Audio', 'group', default=True, key='audio'), sg.Radio('Playlist', 'group', key='playlist')],
    [sg.Text(key='result')],
    [sg.Button('Baixar'), sg.Button('Fechar')]
]

window = sg.Window('Donwload Youtube Video', layout=layout)

while True:
    event, values = window.read()

    match event:
        case 'Baixar':
            if values['audio']:
                try:
                    title = download_audio(values['url'])
                    window['url'].update('')
                    window['result'].update(f'Musica {title} baixada com sucesso!')
                    sg.Popup('Download realizado com sucesso!')
                except:
                    sg.Popup('Insira uma URL valida!')
            elif values['playlist']:
                try:
                    download_playlist(values['url'])
                    window['url'].update('')
                    sg.Popup('Download realizado com sucesso!')
                except:
                    sg.Popup('Insira uma URL valida!')


        case sg.WIN_CLOSED | 'Fechar':
            break
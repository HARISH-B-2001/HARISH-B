import PySimpleGUI as sg

tasks = []
priority = []
deadline = []

layout = [
    [sg.Text('Enter Your task'),
     sg.InputText("", key='todo_item'),
     sg.Button(button_text='Add', key="add_save")],
    [sg.Text('Priority'),sg.Combo(['High','Low'],key='pri'),
     sg.Text('Deadline'),sg.InputText("", key='_CALENDAR_'),
     sg.CalendarButton('DD Month,YYYY', target='_CALENDAR_', pad=None, key='_CALENDAR_', format=('%d %B, %Y'))],
    [sg.Listbox(values=tasks, size=(40, 10), key="items1"),
     sg.Listbox(values=tasks, size=(5, 10), key="items2"),
     sg.Listbox(values=tasks, size=(20, 10), key="items3"),
     sg.Button('Delete'), sg.Button('Edit')],
    [sg.Text('If use Edit or Delete botton,select Task , Priority & Deadline')]
          ]

window = sg.Window('ToDo App', layout)
while True:

    event, values = window.Read()
    if event == "add_save":
        tasks.append(values['todo_item'])
        priority.append(values['pri'])
        deadline.append(values['_CALENDAR_'])
        window.FindElement('items1').Update(values=tasks)
        window.FindElement('items2').Update(values=priority)
        window.FindElement('items3').Update(values=deadline)
        window.FindElement('add_save').Update("Add")
    elif event == "Delete":
        print(values)
        tasks.remove(values["items1"][0])
        priority.remove(values["items2"][0])
        deadline.remove(values["items3"][0])
        window.FindElement('items1').Update(values=tasks)
        window.FindElement('items2').Update(values=priority)
        window.FindElement('items3').Update(values=deadline)
    elif event == "Edit":
        print(values)
        edit_val1 = values["items1"][0]
        edit_val2 = values["items2"][0]
        edit_val3 = values["items3"][0]
        tasks.remove(values["items1"][0])
        priority.remove(values["items2"][0])
        deadline.remove(values["items3"][0])
        window.FindElement('items1').Update(values=tasks)
        window.FindElement('items2').Update(values=priority)
        window.FindElement('items3').Update(values=deadline)
        window.FindElement('todo_item').Update(value=edit_val1)
        window.FindElement('pri').Update(value=edit_val2)
        window.FindElement('_CALENDAR_').Update(value=edit_val3)
        window.FindElement('add_save').Update("Save")
    elif event == None:
        break

window.Close()

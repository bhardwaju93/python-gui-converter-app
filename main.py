import PySimpleGUI as sg
import converter



sg.theme("Black")

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input(key="inches")

button = sg.Button("Convert")
output_label = sg.Text("", key="output")
exit_button = sg.Button("Exit")

pop_up = sg.Text("Please provide two numbers first")

window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button, exit_button, output_label]])

while True:
    event, values = window.read()
    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

    try:
        feet = float(values["feet"])
        inches = float(values["inches"])

        result = convert(feet, inches)
        window["output"].update(value=f"{result} m", text_color="white")

    except ValueError:
        sg.popup("Please enter the inches and feet first")

window.close()

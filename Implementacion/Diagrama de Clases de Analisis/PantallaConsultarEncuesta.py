import PySimpleGUI as GUI
from datetime import datetime

class PantallaConsultarEncuesta:
    # PySimpleGUI no permite utilizar 2 veces el mismo elemento de layout en dos windows distintos
    # Por lo que definimos un string y luego lo evaluamos para obtener cada vez un nuevo elemento
    def __init__(self,
                 gestorConsultarEncuesta=None,
                 btnConsultarEncuesta = "GUI.Button('Consultar Encuesta')",
                 btnCancelar = "GUI.Button('Cancelar')",
                 txtFechaInicio = "GUI.InputText('Fecha Inicio: {}'.format(self.fechaInicio), disabled=True, key='txtFI')",
                 calendarBtnFechaInicio = "GUI.CalendarButton(button_text='{:^19}'.format( \
                     'Seleccionar Inicio'), key='BtnFI', target='txtFI', format='Fecha Inicio: %d/%m/%Y')",
                 txtFechaFin = "GUI.InputText( \
                     'Fecha Fin: {}'.format(self.fechaFin), disabled=True, key='txtFF')",
                 calendarBtnFechaFin = "GUI.CalendarButton(button_text='{:^19}'.format( \
                     'Seleccionar Fin'), key='BtnFI', target='txtFF', format='Fecha Fin: %d/%m/%Y')",
                 btnBuscar = "GUI.Button('Buscar')"
                 ):
        self.gestor = gestorConsultarEncuesta
        self.btnConsultarEncuesta = btnConsultarEncuesta
        self.btnCancel = btnCancelar
        self.txtFechaInicio = txtFechaInicio
        self.txtFechaFin = txtFechaFin
        self.calendarBtnFechaInicio = calendarBtnFechaInicio
        self.calendarBtnFechaFin = calendarBtnFechaFin
        self.btnBuscar = btnBuscar

        self.fechaInicio = ''
        self.fechaFin = ''

    def opcionConsultarEncuesta(self, gestor):
        self.gestor = gestor
        self.habilitarVentana()

    def habilitarVentana(self):
        layout = [
            [GUI.VPush()],
            [GUI.Push(), eval(self.btnConsultarEncuesta), GUI.Push()],
            [GUI.VPush()],
            [GUI.Push(), eval(self.btnCancel)]
        ]

        window = GUI.Window('Consultar Encuesta', layout,
                            resizable=False, size=(300, 100))

        while True:
            event, values = window.read()

            if event == 'Consultar Encuesta':
                window.close()
                self.gestor.nuevaConsultaEncuesta()

            if event == GUI.WIN_CLOSED or event == 'Cancelar':
                break

        window.close()

    def pedirPeriodo(self):
        col1 = GUI.Column([[eval(self.txtFechaInicio)], [eval(self.txtFechaFin)]])
        col2 = GUI.Column([[eval(self.calendarBtnFechaInicio)],
                          [eval(self.calendarBtnFechaFin)]])
        dateFrame = GUI.Frame('Periodo', [[col1, col2]])
        layout = [
            [dateFrame],
            [GUI.Push(), eval(self.btnBuscar)],
            [GUI.Push(), eval(self.btnCancel)]
        ]

        window = GUI.Window('Consultar Encuesta', layout, resizable=False)

        while True:
            event, values = window.read()

            if event == 'Buscar':
                if values['txtFI'] == 'Fecha Inicio: ' or values['txtFF'] == 'Fecha Fin: ':
                    GUI.popup('Debe seleccionar un periodo', title='Error')
                else:
                    self.fechaInicio = datetime.strptime(values['txtFI'], 'Fecha Inicio: %d/%m/%Y')
                    self.fechaFin = datetime.strptime(values['txtFF'], 'Fecha Fin: %d/%m/%Y').replace(hour=23, minute=59, second=59)
                    if self.fechaInicio > self.fechaFin:
                        GUI.popup('La fecha de inicio debe ser menor a la fecha de fin', title='Error')
                    else:
                        window.close()
                        self.tomarPeriodo()

            if event == GUI.WIN_CLOSED or event == 'Cancelar':
                break

        window.close()

    def tomarPeriodo(self):
        self.gestor.tomarPeriodo(self.fechaInicio, self.fechaFin)
    
    def pedirSeleccionLlamada(self, llamadasAMostrar):
        if type(self.fechaInicio) == datetime:
            self.fechaInicio = self.fechaInicio.strftime('%d/%m/%Y')
        if type(self.fechaFin) == datetime:
            self.fechaFin = self.fechaFin.strftime('%d/%m/%Y')
        col1 = GUI.Column([[eval(self.txtFechaInicio)], [eval(self.txtFechaFin)]])
        col2 = GUI.Column([[eval(self.calendarBtnFechaInicio)],
                          [eval(self.calendarBtnFechaFin)]])
        dateFrame = GUI.Frame('Periodo', [[col1, col2]])

        toprow = ['Fila', 'Fecha Llamada']
        rows = []
        for i in range(len(llamadasAMostrar)):
            # Cambiar '12/12/12' por str(llamdasAMostrar[i]) cuando este implementado
            rows.append([str(i + 1), '12/12/12'])
        
        tbl = GUI.Table(values = rows, headings = toprow,
            key = 'tblLlamadas',
            num_rows = 10,
            expand_x = True,
            auto_size_columns = True,
            display_row_numbers = False,
            justification = 'center',
            enable_events = True,
            enable_click_events = True,
            select_mode = GUI.TABLE_SELECT_MODE_BROWSE
            )

        layout = [
            [dateFrame],
            [GUI.Push(), eval(self.btnBuscar)],
            [tbl],
            [GUI.Push(), eval(self.btnCancel)]
        ]

        window = GUI.Window('Consultar Encuesta', layout, resizable=False)

        while True:
            event, values = window.read()

            if event == 'Buscar':
                if values['txtFI'] == 'Fecha Inicio: ' or values['txtFF'] == 'Fecha Fin: ':
                    GUI.popup('Debe seleccionar un periodo', title='Error')
                else:
                    fechaInicio = datetime.strptime(
                        values['txtFI'], 'Fecha Inicio: %d/%m/%Y')
                    fechaFin = datetime.strptime(
                        values['txtFF'], 'Fecha Fin: %d/%m/%Y').replace(hour=23, minute=59, second=59)
                    if fechaInicio > fechaFin:
                        GUI.popup(
                            'La fecha de inicio debe ser menor a la fecha de fin', title='Error')
                    else:
                        self.tomarPeriodo()
                        window.close()

            if event == GUI.WIN_CLOSED or event == 'Cancelar':
                break

        window.close()

    def tomarSeleccionLlamada(self):
        pass

    def pedirSeleccionSalida(self):
        pass

    def tomarSeleccionSalida(self):
        pass

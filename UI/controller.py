import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model



    def handleCreaGrafo(self, e):
        storeId = self._view._ddStore.value
        if storeId is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Errore. Selezionare uno storeId per procedere.", color='red'))
            self._view.update_page()
            return
        k_giorni_input = self._view._txtIntK.value
        if k_giorni_input is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Errore. Inserire k giorni per procedere.", color='red'))
            self._view.update_page()
            return
        try:
            k_giorni = int(k_giorni_input)
            self._model.buildGraph(storeId, k_giorni)
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Grafo creato.", color='green'))
            self._view.txt_result.controls.append(ft.Text(f"{self._model.printGraph()}", color='green'))
            self._view.update_page()
            self.fillDDNodes()

        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Errore. Inserire un intero per procedere.", color='red'))
            self._view.update_page()
            return



    def handleCerca(self, e):
        if self._source is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Errore. Inserire un nodo iniziale.", color='red'))
            self._view.update_page()
            return
        self._view.txt_result.controls.clear()
        percorso = self._model.trovaPercorsoPiuLungo(self._source.order_id)
        self._view.txt_result.controls.append(ft.Text(f"Il percorso piu lungo che parte da: {self._source}", color='green'))
        for i in range(1,len(percorso)-1):
            self._view.txt_result.controls.append(
                ft.Text(f"{percorso[i]}", color='green'))
        self._view.update_page()




    def handleRicorsione(self, e):
        pass


    def fillDDStore(self):
        storesId = self._model.getAllStroresId()
        for id in storesId:
            self._view._ddStore.options.append(ft.dropdown.Option(id))
        self._view.update_page()


    def fillDDNodes(self):
        nodi = self._model._nodes
        for node in nodi:
            self._view._ddNode.options.append(ft.dropdown.Option(data=node,
                                                                 key = node,
                                                                 on_click=self.handleReadNode))

        self._view.update_page()


    def handleReadNode(self, e):
        self._source = e.control.data
        print(self._source)



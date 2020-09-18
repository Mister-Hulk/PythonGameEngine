
import Model

class ModelLibrary:

    def __init__(self, models_ini="models/models.ini"):
        self.models={}
        self.models_ini=models_ini

        self.models_basepath="models/data/"

        self.load_all()

    def load_all(self):
        for line in open(self.models_ini):
            data=line.split(" ")
            self.models[data[0]]=Model.Model(self.models_basepath+data[1])

    def load(self, id, model):
        self.models[id]=model

    def render_all(self):
        for id, model in self.models.items():
            model.render()
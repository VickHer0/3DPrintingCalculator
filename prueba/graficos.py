from matplotlib import pyplot
from clases import *

def graficoconsumo__(self):
    datos = ('Filamento','Electricidad','Depreciacion de la impresora','Preparacion','Post-procesing','Consumibles')
    slices = (self.cost_filamento(),self.cost_electricidad(),self.depreciacion_impresora(),self.preparacion(),self.post_proces(),self.material_consumido())
    colores = ('red','blue','green','pink','yellow','orange')

    pyplot.pie(slices, colors=colores, autopct="%1.1f%%")
    pyplot.axis("equal")
    pyplot.title("costo de frabricación")
    pyplot.legend(labels=datos)
    pyplot.show()

def graficotendensia__(self):
    datos = ('Tiempo de uso de Impresora','Energia consumida','tiempo de proceso consumido')
    slices = (self.imp_timeImpresion,self.opcion_imp_consumo,self.opcion_imp_timeDepre)

    pyplot.plot(datos,slices)
    pyplot.title("Analisis de tendencias en los servicios")
    pyplot.legend(labels=datos)
    pyplot.show()



import json
from pathlib import Path
import difflib
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, scrolledtext, filedialog

# ---------------------------- utilidades ----------------------------
def norm(s: str) -> str:
    return " ".join(s.strip().upper().split())

# ---------------------------- diccionario base ----------------------------
INITIAL_DICT = {
    # ---- Lista 1 ----
    "APLICACION": "Programa de software diseñado para realizar tareas específicas para el usuario o la empresa.",
    "BPM": "Business Process Management: disciplina para modelar, automatizar y mejorar procesos de negocio.",
    "CLIENTE": "Persona u organización que recibe un producto o servicio.",
    "COMERCIO": "Intercambio de bienes o servicios entre personas o entidades.",
    "COMPETENCIA": "Empresas rivales en un mismo mercado; también capacidad o habilidad.",
    "CONTABILIDAD": "Sistema para registrar y analizar operaciones financieras.",
    "COSTOS": "Recursos económicos empleados para producir bienes o prestar servicios.",
    "CRM": "Customer Relationship Management: estrategia/sistema para gestionar relaciones con clientes.",
    "DATOS": "Representaciones de hechos que pueden procesarse para obtener información.",
    "DISTRIBUCION": "Actividad de llevar productos desde el productor hasta el consumidor.",
    "EFICIENCIA": "Lograr un objetivo usando el mínimo de recursos.",
    "ELECTRONICO": "Que funciona mediante dispositivos eléctricos o digitales.",
    "EMPRESA": "Organización dedicada a actividades económicas con fines determinados.",
    "ERP": "Enterprise Resource Planning: sistema integrado que gestiona procesos clave de la empresa.",
    "FABRICACION": "Proceso de producción de bienes materiales.",
    "FACTURACION": "Emisión y registro de facturas por ventas de bienes o servicios.",
    "FIDELIZACION": "Conjunto de acciones para mantener y aumentar la lealtad de los clientes.",
    "FINANZAS": "Gestión del dinero, inversiones y riesgos económicos.",
    "GESTION": "Administración y coordinación de recursos y actividades.",
    "HIBRIDA": "Combinación de dos o más enfoques/entornos (p. ej., nube híbrida).",
    "HORIZONTAL": "En negocio: soluciones aplicables a múltiples industrias; no específicas de un sector.",
    "INDUSTRIA": "Conjunto de actividades productivas transformadoras de materias primas.",
    "INFORMACION": "Datos procesados y con significado para la toma de decisiones.",
    "INTEGRACION": "Conectar sistemas o datos para que trabajen de forma unificada.",
    "INVENTARIO": "Conjunto y registro de bienes almacenados.",
    "LOGISTICA": "Planificación y gestión del flujo de productos, información y recursos.",
    "MANAGEMENT": "Gestión o administración de una organización.",
    "MARKETING": "Conjunto de estrategias para crear, comunicar y entregar valor al mercado.",
    "MERCADO": "Ámbito donde se intercambian bienes y servicios.",
    "NEGOCIO": "Actividad económica que busca generar valor e ingresos.",
    "ONBOARDING": "Proceso de incorporación y adaptación de usuarios o empleados a un sistema u organización.",
    "PLANIFICACION": "Definir objetivos, recursos y acciones para alcanzarlos.",
    "PROCESOS": "Secuencias de actividades relacionadas que generan un resultado.",
    "PRODUCTIVIDAD": "Relación entre lo producido y los recursos utilizados.",
    "PROVEEDORES": "Personas o empresas que suministran bienes o servicios.",
    "PUBLICIDAD": "Comunicación pagada para promover productos, servicios o marcas.",
    "RECURSOS": "Medios (humanos, financieros, materiales) disponibles para un fin.",
    "RECURSOSHUMANOS": "Área que gestiona al personal y su desarrollo en la organización.",
    "SALUD": "Estado de bienestar físico, mental y social; también sector sanitario.",
    "SCM": "Supply Chain Management: gestión integral de la cadena de suministro.",
    "SECTOR": "Parte de la economía con actividades similares (por ejemplo, sector salud).",
    "SERVICIO": "Actividad intangible que satisface una necesidad del cliente.",
    "SISTEMA": "Conjunto de elementos interrelacionados con un objetivo común.",
    "SOFTWARE": "Conjunto de programas y rutinas que hacen funcionar un sistema informático.",
    "SUPPLYCHAIN": "Cadena de suministro: red de actividades desde insumos hasta el cliente final.",
    "TECNOLOGIA": "Aplicación de conocimientos para resolver problemas o crear productos.",
    "TRAZABILIDAD": "Capacidad de seguir el historial y ubicación de un producto o dato.",
    "USUARIO": "Persona que utiliza un sistema o servicio.",
    "VENTAS": "Transacciones por las que se intercambian bienes o servicios por dinero.",
    "VERTICAL": "En negocio: solución específica para una industria (p. ej., vertical salud).",
    # ---- Lista 2 ----
    "ACCESO": "Posibilidad de entrar o utilizar un recurso, sistema o información.",
    "ACTUALIZACION": "Proceso de poner algo al día con nuevas versiones o datos.",
    "ADAPTACION": "Ajuste de un sistema o proceso a nuevas condiciones.",
    "AGILIDAD": "Capacidad de responder rápidamente a cambios con valor continuo.",
    "ALMACENAMIENTO": "Guardado de datos o bienes en un medio o instalación.",
    "ANALISIS": "Examen detallado para comprender o resolver un problema.",
    "AUTOMATIZACION": "Uso de tecnología para ejecutar tareas con mínima intervención humana.",
    "BASEDEDATOS": "Conjunto organizado de datos accesibles y gestionados por un SGBD.",
    "BENEFICIOS": "Ventajas o ganancias obtenidas.",
    "CLINICAS": "Establecimientos de atención de salud; también soluciones del sector salud.",
    "COLABORACION": "Trabajo coordinado entre personas o sistemas para un objetivo común.",
    "COMPATIBILIDAD": "Capacidad de coexistir o funcionar con otros sistemas sin conflicto.",
    "COMPROMISO": "Acuerdo u obligación; también nivel de involucramiento de usuarios.",
    "COMUNICACION": "Intercambio de información entre partes.",
    "CONSOLIDACION": "Unificación de datos/sistemas para simplificar y ganar eficiencia.",
    "CONSULTORIA": "Servicio profesional que asesora a organizaciones en temas especializados.",
    "COSTE": "Gasto económico de una actividad o recurso.",
    "CRECIMIENTO": "Aumento sostenido en tamaño, ingresos o capacidad.",
    "DECISIONES": "Selección entre alternativas con base en información.",
    "DESARROLLO": "Creación o mejora de software, productos o capacidades.",
    "DIGITAL": "Relacionado con tecnologías de información y comunicación electrónicas.",
    "DOCUMENTACION": "Conjunto de documentos que describen un sistema, proceso o producto.",
    "EFICACIA": "Grado en que se logran los objetivos propuestos.",
    "ESCALABILIDAD": "Capacidad de un sistema para crecer en carga o funcionalidades manteniendo rendimiento.",
    "ESTRATEGIA": "Plan de acciones para alcanzar objetivos a medio/largo plazo.",
    "HISTORIAS": "En ágil: historias de usuario; descripciones breves de necesidades del usuario.",
    "HOJADECALCULO": "Aplicación tipo spreadsheet para cálculo y análisis de datos.",
    "IMPLEMENTACION": "Puesta en marcha de un sistema o solución en producción.",
    "INFORMES": "Documentos que presentan datos y análisis para tomar decisiones.",
    "INNOVACION": "Introducción de mejoras o soluciones nuevas con impacto.",
    "INTEGRADOS": "Componentes o sistemas que funcionan como un todo.",
    "INTERFAZ": "Superficie o medio de interacción entre usuario y sistema o entre sistemas.",
    "MODULOS": "Partes funcionales de un sistema que pueden operar de forma separada.",
    "OBJETIVOS": "Resultados específicos que se desean alcanzar.",
    "OPTIMIZACION": "Mejorar desempeño, costo o calidad de un sistema o proceso.",
    "PARAMETROS": "Valores configurables que alteran el comportamiento de un sistema.",
    "PARTNER": "Socio estratégico de negocio o tecnología.",
    "PERSONALIZACION": "Adaptación de un sistema a preferencias de un usuario o cliente.",
    "PLANES": "Conjunto de acciones programadas para lograr objetivos.",
    "PREDICCION": "Estimación de resultados futuros basada en datos.",
    "PROYECTO": "Esfuerzo temporal para crear un producto, servicio o resultado único.",
    "REDUCCION": "Disminución de costos, tiempos, errores u otros indicadores.",
    "RENTABILIDAD": "Relación entre beneficios obtenidos y la inversión realizada.",
    "REPORTES": "Sinónimo de informes: salidas estructuradas de datos.",
    "RESULTADOS": "Efectos o productos finales de un proceso o proyecto.",
    "SEGUIMIENTO": "Monitoreo continuo del avance o estado de algo.",
    "SEGURIDAD": "Conjunto de medidas para proteger datos, sistemas y personas.",
    "SOCIOS": "Aliados o compañías que colaboran con la organización.",
    "TRANSFORMACION": "Cambio profundo, típicamente digital, en procesos y modelos.",
    # ---- Técnicos del PDF ----
    "MIDDLEWARE": "Capa de software que conecta aplicaciones, datos y servicios para integrarlos.",
    "SOAP": "Protocolo basado en XML para intercambiar mensajes en servicios web.",
    "OBJECT REQUEST BROKER": "Intermediario que gestiona peticiones entre objetos distribuidos (ej. CORBA).",
    "OBJETC REQUEST BROKER": "Forma mal escrita de 'OBJECT REQUEST BROKER'; ver definición correcta.",
    "CORBA": "Common Object Request Broker Architecture: estándar para comunicación entre objetos distribuidos.",
    "IPAAS": "Integration Platform as a Service: plataforma en la nube para integrar aplicaciones y datos.",
    "PAAS": "Platform as a Service: servicio en la nube que provee plataforma para desarrollar y desplegar apps.",
    "SAAS": "Software as a Service: software entregado como servicio en la nube, bajo suscripción.",
    "CSP": "Cloud Service Provider: proveedor de servicios en la nube (p. ej., AWS, Azure, GCP).",    
    "ESB": "Enterprise Service Bus: patrón para integrar aplicaciones mediante un bus de servicios.",
    "KUBERNETES": "Plataforma de orquestación de contenedores para desplegar y escalar aplicaciones.",
    "REST API": "Estilo de servicios web que usan HTTP y recursos representados.",
}

STORE_PATH = Path("diccionario.json")

# Cargar diccionario del usuario si existe
if STORE_PATH.exists():
    try:
        user_data = json.loads(STORE_PATH.read_text(encoding="utf-8"))
        for k, v in user_data.items():
            INITIAL_DICT[norm(k)] = v
    except Exception:
        pass

# ---------------------------- app tk ----------------------------
class DiccionarioApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Formulario de Consulta de Palabras - SII")
        self.geometry("760x520")
        self.minsize(720, 480)

        style = ttk.Style(self)
        try:
            self.tk.call("source", "azure.tcl")  # si el tema existe
            style.theme_use("azure")
        except Exception:
            pass

        self.dict_data = dict(sorted(INITIAL_DICT.items(), key=lambda x: x[0]))

        top = ttk.Frame(self, padding=10)
        top.pack(fill="x")

        ttk.Label(top, text="Palabra:").pack(side="left")
        self.entry = ttk.Entry(top)
        self.entry.pack(side="left", fill="x", expand=True, padx=8)
        self.entry.bind("<Return>", self.buscar_event)

        ttk.Button(top, text="Buscar", command=self.buscar).pack(side="left", padx=4)
        ttk.Button(top, text="Agregar / Editar", command=self.agregar).pack(side="left", padx=4)
        ttk.Button(top, text="Listar todas", command=self.listar).pack(side="left", padx=4)

        self.result = scrolledtext.ScrolledText(self, wrap="word", height=18)
        self.result.pack(fill="both", expand=True, padx=10, pady=8)

        bottom = ttk.Frame(self, padding=10)
        bottom.pack(fill="x")
        ttk.Button(bottom, text="Guardar cambios", command=self.guardar).pack(side="left")
        ttk.Button(bottom, text="Exportar a JSON...", command=self.exportar).pack(side="left", padx=6)
        ttk.Button(bottom, text="Importar JSON...", command=self.importar).pack(side="left", padx=6)
        self.status = ttk.Label(bottom, text="Listo.", anchor="e")
        self.status.pack(side="right", fill="x", expand=True)

        self.entry.focus_set()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def buscar_event(self, *_):
        self.buscar()

    def buscar(self):
        palabra = norm(self.entry.get())
        if not palabra:
            messagebox.showinfo("Aviso", "Escribe una palabra para buscar.")
            return
        if palabra in self.dict_data:
            significado = self.dict_data[palabra]
            self.mostrar(f"📘 {palabra}\n\n{significado}")
            self.status.config(text=f"Encontrado: {palabra}")
        else:
            sugerencias = difflib.get_close_matches(palabra, self.dict_data.keys(), n=5, cutoff=0.6)
            msg = f"❌ No se encontró '{palabra}'.\n"
            if sugerencias:
                msg += "¿Quisiste decir?: " + ", ".join(sugerencias)
            self.mostrar(msg)
            self.status.config(text="No encontrado")

    def agregar(self):
        palabra = simpledialog.askstring("Agregar/Editar", "Palabra:", initialvalue=self.entry.get())
        if not palabra:
            return
        palabra_n = norm(palabra)
        significado = simpledialog.askstring(
            "Definición",
            f"Escribe la definición para '{palabra_n}':",
            initialvalue=self.dict_data.get(palabra_n, ""),
        )
        if significado is None or not significado.strip():
            return
        self.dict_data[palabra_n] = significado.strip()
        self.mostrar(f"✅ Guardado '{palabra_n}'.")
        self.status.config(text=f"Guardado: {palabra_n}")

    def listar(self):
        listado = "\\n".join(f"• {k}" for k in sorted(self.dict_data.keys()))
        self.mostrar("📚 Palabras disponibles:\\n\\n" + listado)
        self.status.config(text=f"{len(self.dict_data)} términos.")

    def mostrar(self, texto: str):
        self.result.delete("1.0", "end")
        self.result.insert("1.0", texto)

    def guardar(self):
        try:
            STORE_PATH.write_text(json.dumps(self.dict_data, ensure_ascii=False, indent=2), encoding="utf-8")
            self.status.config(text=f"Guardado en {STORE_PATH.name}")
            messagebox.showinfo("Éxito", f"Se guardaron los cambios en {STORE_PATH}.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar: {e}")

    def exportar(self):
        fp = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON", "*.json")],
            initialfile="diccionario.json",
            title="Exportar diccionario",
        )
        if not fp:
            return
        try:
            Path(fp).write_text(json.dumps(self.dict_data, ensure_ascii=False, indent=2), encoding="utf-8")
            messagebox.showinfo("Exportado", f"Diccionario exportado en:\\n{fp}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo exportar: {e}")

    def importar(self):
        fp = filedialog.askopenfilename(
            filetypes=[("JSON", "*.json")],
            title="Importar diccionario JSON",
        )
        if not fp:
            return
        try:
            data = json.loads(Path(fp).read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                raise ValueError("El archivo JSON no contiene un objeto diccionario.")
            normed = {norm(k): v for k, v in data.items()}
            self.dict_data.update(normed)
            self.mostrar("✅ Diccionario importado y combinado con el actual.")
            self.status.config(text=f"Importadas {len(normed)} definiciones.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo importar: {e}")

    def on_close(self):
        try:
            STORE_PATH.write_text(json.dumps(self.dict_data, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception:
            pass
        self.destroy()

if __name__ == "__main__":
    app = DiccionarioApp()
    app.mainloop()

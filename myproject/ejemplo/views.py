from django.shortcuts import render, get_object_or_404
from ejemplo.models import (Familiar, Mascota, Empleo)
from ejemplo.forms import (Buscar, FamiliarForm, MascotaForm, EmpleoForm)
from django.views import View

# Create your views here.
def index(request):
    return render(request, 'ejemplo/saludar.html')

def mostrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, 'ejemplo/familiares.html', {'lista_familiares': lista_familiares})

class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {'nombre':''}

    def get(self, request):                 # lo usamos para renderizar el formulario en pagina
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):                # atiende la consulta cuando demos submit en pagina y ejecuta la busqueda
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all()
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form, 'lista_familiares': lista_familiares})
        
        return render(request, self.template_name, {'form': form})

class AltaFamiliar(View):
    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {'nombre': '', 'direccion':'', 'numero_pasaporte': ''}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con exito {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 'msg_exito': msg_exito})
        return render(request, self.template_name, {'form': form})

class ActualizarFamiliar(View):
    form_class = FamiliarForm
    template_name = 'ejemplo/actualizar_familiar.html'
    initial = {'nombre': '', 'direccion':'', 'numero_pasaporte': ''}

    def get(self, request, pk):
        familiar = get_object_or_404(Familiar, pk=pk)
        form = self.form_class(instance=familiar)
        return render(request, self.template_name, {'form': form, 'familiar': familiar})

    def post(self, request, pk):
        familiar = get_object_or_404(Familiar, pk=pk)
        form = self.form_class(request.POST, instance=familiar)
        if form.is_valid():
            form.save()
            msg_exito = f'se actualizo {form.cleaned_data.get("nombre")} con exito!'
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 'familiar': familiar, 'msg_exito': msg_exito})
        return render(request, self.template_name, {'form':form})

class BorrarFamiliar(View):
    template_name = 'ejemplo/familiares.html'

    def get(self, request, pk):
        familiar = get_object_or_404(Familiar, pk=pk)
        familiar.delete()
        familiares = Familiar.objects.all()
        return render(request, self.template_name, {'lista_familiares': familiares})

########################################################################################################################

def mostrar_mascotas(request):
    lista_mascotas = Mascota.objects.all()
    return render(request, 'ejemplo/mascotas.html', {'lista_mascotas': lista_mascotas})

class BuscarMascota(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar_mascota.html'
    initial = {'nombre':''}

    def get(self, request):                 # lo usamos para renderizar el formulario en pagina
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):                # atiende la consulta cuando demos submit en pagina y ejecuta la busqueda
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            lista_mascotas = Mascota.objects.filter(nombre__icontains=nombre).all()
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form, 'lista_mascotas': lista_mascotas})
        
        return render(request, self.template_name, {'form': form})

class AltaMascota(View):
    form_class = MascotaForm
    template_name = 'ejemplo/alta_mascota.html'
    initial = {'nombre': '', 'tipo':'', 'edad': ''}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con exito {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 'msg_exito': msg_exito})
        return render(request, self.template_name, {'form': form})

class ActualizarMascota(View):
    form_class = MascotaForm
    template_name = 'ejemplo/actualizar_mascota.html'
    initial = {'nombre': '', 'tipo':'', 'edad': ''}

    def get(self, request, pk):
        mascota = get_object_or_404(Mascota, pk=pk)
        form = self.form_class(instance=mascota)
        return render(request, self.template_name, {'form': form, 'mascota': mascota})

    def post(self, request, pk):
        mascota = get_object_or_404(Mascota, pk=pk)
        form = self.form_class(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            msg_exito = f'se actualizo {form.cleaned_data.get("nombre")} con exito!'
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 'mascota': mascota, 'msg_exito': msg_exito})
        return render(request, self.template_name, {'form':form})

class BorrarMascota(View):
    template_name = 'ejemplo/mascotas.html'

    def get(self, request, pk):
        mascota = get_object_or_404(Mascota, pk=pk)
        mascota.delete()
        mascotas = Mascota.objects.all()
        return render(request, self.template_name, {'lista_mascotas': mascotas})

#######################################################################################################################################

def mostrar_empleos(request):
    lista_empleos = Empleo.objects.all()
    return render(request, 'ejemplo/empleos.html', {'lista_empleos': lista_empleos})

class BuscarEmpleo(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar_empleo.html'
    initial = {'ocupacion':''}

    def get(self, request):                 # lo usamos para renderizar el formulario en pagina
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):                # atiende la consulta cuando demos submit en pagina y ejecuta la busqueda
        form = self.form_class(request.POST)
        if form.is_valid():
            ocupacion = form.cleaned_data.get('ocupacion')
            lista_empleos = Empleo.objects.filter(ocupacion__icontains=ocupacion).all()
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form, 'lista_empleos': lista_empleos})        
        return render(request, self.template_name, {'form': form})

class AltaEmpleo(View):
    form_class = EmpleoForm
    template_name = 'ejemplo/alta_empleo.html'
    initial = {'ocupacion': '', 'antiguedad':'', 'cargo': '', 'breve_descripcion': ''}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con exito {form.cleaned_data.get('ocupacion')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 'msg_exito': msg_exito})
        return render(request, self.template_name, {'form': form})

class ActualizarEmpleo(View):
    form_class =EmpleoForm
    template_name = 'ejemplo/actualizar_empleo.html'
    initial = {'ocupacion': '', 'antiguedad':'', 'cargo': '', 'breve_descripcion': ''}

    def get(self, request, pk):
        empleo = get_object_or_404(Empleo, pk=pk)
        form = self.form_class(instance=empleo)
        return render(request, self.template_name, {'form': form, 'empleo': empleo})

    def post(self, request, pk):
        empleo = get_object_or_404(Empleo, pk=pk)
        form = self.form_class(request.POST, instance=empleo)
        if form.is_valid():
            form.save()
            msg_exito = f'se actualizo {form.cleaned_data.get("ocupacion")} con exito!'
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 'empleo': empleo, 'msg_exito': msg_exito})
        return render(request, self.template_name, {'form':form})

class BorrarEmpleo(View):
    template_name = 'ejemplo/empleos.html'

    def get(self, request, pk):
        empleo = get_object_or_404(Empleo, pk=pk)
        empleo.delete()
        empleos = Empleo.objects.all()
        return render(request, self.template_name, {'lista_empleos': empleos})
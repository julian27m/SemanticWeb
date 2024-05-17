import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from "@angular/forms";
import { ActivatedRoute, Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { Tarea } from '../tarea';
import { TareaService } from '../tarea.service';

@Component({
  selector: 'app-tarea-editar',
  templateUrl: './tarea-editar.component.html',
  styleUrls: ['./tarea-editar.component.css']
})
export class TareaEditarComponent implements OnInit {

  tarea: Tarea
  tareaForm: FormGroup

  constructor(
    private formBuilder: FormBuilder,
    private router: ActivatedRoute,
    private routerPath: Router,
    private toastr: ToastrService,
    private tareaService: TareaService
  ) { }

  ngOnInit() {
    const idTarea = parseInt(this.router.snapshot.params['id']);
    this.tareaService.darTarea(idTarea).subscribe((tarea) => {
      this.tarea = tarea;
      this.tareaForm = this.formBuilder.group({
        id: [this.tarea.id, []],
        texto: [this.tarea.texto, [Validators.required, Validators.minLength(2)]],
        fechaInicial: [this.tarea.fechaInicial, [Validators.required, Validators.minLength(2)]],
        fechaFinal: [this.tarea.fechaFinal, [Validators.required, Validators.minLength(2)]],
        estado: [this.tarea.estado, [Validators.required, Validators.minLength(2)]]
        });
    });
  }

  editarTarea(tarea: Tarea): void {
    this.tareaService.editarTarea(tarea).subscribe((tarea) => {
      this.toastr.success("Confirmation", "Información editada")
      this.tareaForm.reset();
      this.routerPath.navigate(['/tareas/']);
    },
    error => {
      if (error.statusText === "UNAUTHORIZED") {
        this.toastr.error("Error","Su sesión ha caducado, por favor vuelva a iniciar sesión.")
      }
      else if (error.statusText === "UNPROCESSABLE ENTITY") {
        this.toastr.error("Error","No hemos podido identificarlo, por favor vuelva a iniciar sesión.")
      }
      else {
        this.toastr.error("Error","Ha ocurrido un error. " + error.message)
      }
    })
}

  cancelarTarea(): void {
    this.tareaForm.reset();
    this.routerPath.navigate(['/tareas/']);
  }
  


}

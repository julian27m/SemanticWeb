import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from "@angular/forms";
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { Tarea } from '../tarea';
import { TareaService } from '../tarea.service';

@Component({
  selector: 'app-tarea-crear',
  templateUrl: './tarea-crear.component.html',
  styleUrls: ['./tarea-crear.component.css']
})
export class TareaCrearComponent implements OnInit {

  tareaForm: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private routerPath: Router,
    private toastr: ToastrService,
    private tareaService: TareaService
  ) { }

  ngOnInit() {
    this.tareaForm = this.formBuilder.group({
      texto: ["", [Validators.required, Validators.minLength(2)]],
      fechaInicial: ["", [Validators.required, Validators.minLength(2)]],
      fechaFinal: ["", [Validators.required, Validators.minLength(2)]],
      estado: ["", [Validators.required, Validators.minLength(2)]]
    });
  }

  crearTarea(tarea: Tarea): void {
    this.tareaService.crearTarea(tarea).subscribe((tarea) => {
      this.toastr.success("Confirmation", "Registro creado")
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
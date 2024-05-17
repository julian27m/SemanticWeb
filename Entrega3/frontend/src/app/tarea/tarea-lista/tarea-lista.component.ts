import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';
import { Tarea } from '../tarea';
import { TareaService } from '../tarea.service';

@Component({
  selector: 'app-tarea-lista',
  templateUrl: './tarea-lista.component.html',
  styleUrls: ['./tarea-lista.component.css']
})
export class TareaListaComponent implements OnInit {

  tareas:Array<Tarea> = []

  constructor(
    private routerPath: Router,
    private router: ActivatedRoute,
    private toastr: ToastrService,
    private tareaService: TareaService
  ) { }

  ngOnInit() {
    this.tareaService.darTareas().subscribe((tareas) => {
      this.tareas = tareas;
    })
  }

  crearTarea():void {
    this.routerPath.navigate(['/tarea/crear/']);
  }

  editarTarea(idTarea: number):void {
    this.routerPath.navigate(['/tarea/editar/' + idTarea]);
  }

  borrarTarea(idTarea: number):void {
    this.tareaService.borrarTarea(idTarea).subscribe((tarea) => {
      this.toastr.success("Confirmation", "Registro eliminado de la lista")
      this.ngOnInit();
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
    });
  }
}

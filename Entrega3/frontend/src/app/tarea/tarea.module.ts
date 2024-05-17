import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { EncabezadoAppModule } from '../encabezado-app/encabezado-app.module';
import { TareaListaComponent } from './tarea-lista/tarea-lista.component';
import { TareaCrearComponent } from './tarea-crear/tarea-crear.component';
import { TareaEditarComponent } from './tarea-editar/tarea-editar.component';

@NgModule({
  imports: [
    CommonModule,
    ReactiveFormsModule,
    EncabezadoAppModule
  ],
  declarations: [
    TareaListaComponent,
    TareaCrearComponent,
    TareaEditarComponent
  ],
  exports: [
    TareaListaComponent,
    TareaCrearComponent,
    TareaEditarComponent
  ]
})
export class TareaModule { }

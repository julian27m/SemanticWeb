import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { UsuarioLoginComponent } from './usuario-login/usuario-login.component';
import { UsuarioRegistroComponent } from './usuario-registro/usuario-registro.component';
import { RouterModule } from '@angular/router'; // Asegúrate de importar RouterModule

@NgModule({
  imports: [
    CommonModule,
    ReactiveFormsModule,
    RouterModule // Añadir RouterModule aquí
  ],
  declarations: [
    UsuarioLoginComponent,
    UsuarioRegistroComponent
  ],
  exports: [
    UsuarioLoginComponent,
    UsuarioRegistroComponent
  ]
})
export class UsuarioModule { }

import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UsuarioLoginComponent } from './usuario/usuario-login/usuario-login.component';
import { UsuarioRegistroComponent } from './usuario/usuario-registro/usuario-registro.component';
import { ArticuloListaComponent } from './articulo/articulo-lista/articulo-lista.component';
import { ArticuloCrearComponent } from './articulo/articulo-crear/articulo-crear.component';
import { ArticuloDetalleComponent } from './articulo/articulo-detalle/articulo-detalle.component';

const routes: Routes = [
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  { path: 'login', component: UsuarioLoginComponent },
  { path: 'registro', component: UsuarioRegistroComponent },
  { path: 'articulos', component: ArticuloListaComponent },
  { path: 'crear-articulo', component: ArticuloCrearComponent },
  { path: 'articulo/:id', component: ArticuloDetalleComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

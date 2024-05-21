import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UsuarioLoginComponent } from './usuario/usuario-login/usuario-login.component';
import { UsuarioRegistroComponent } from './usuario/usuario-registro/usuario-registro.component';
import { ArticuloListaComponent } from './articulo/articulo-lista/articulo-lista.component';
import { ArticuloCrearComponent } from './articulo/articulo-crear/articulo-crear.component';
import { ArticuloDetalleComponent } from './articulo/articulo-detalle/articulo-detalle.component';

const routes: Routes = [
  { path: 'login', component: UsuarioLoginComponent },
  { path: 'signin', component: UsuarioRegistroComponent },
  { path: 'articulos', component: ArticuloListaComponent },
  { path: 'articulo/nuevo', component: ArticuloCrearComponent },
  { path: 'articulo/:id', component: ArticuloDetalleComponent },
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  { path: '**', redirectTo: '/login' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

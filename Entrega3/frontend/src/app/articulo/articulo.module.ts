import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormsModule } from '@angular/forms'; 
import { RouterModule } from '@angular/router';
import { EncabezadoAppModule } from '../encabezado-app/encabezado-app.module';
import { ArticuloListaComponent } from './articulo-lista/articulo-lista.component';
import { ArticuloCrearComponent } from './articulo-crear/articulo-crear.component';
import { ArticuloDetalleComponent } from './articulo-detalle/articulo-detalle.component';
import { NgxPaginationModule } from 'ngx-pagination';

@NgModule({
  imports: [
    CommonModule,
    ReactiveFormsModule,
    FormsModule, 
    EncabezadoAppModule,
    NgxPaginationModule,
    RouterModule
  ],
  declarations: [
    ArticuloListaComponent,
    ArticuloCrearComponent,
    ArticuloDetalleComponent
  ],
  exports: [
    ArticuloListaComponent,
    ArticuloCrearComponent,
    ArticuloDetalleComponent
  ]
})
export class ArticuloModule { }

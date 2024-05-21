import { Component, OnInit } from '@angular/core';
import { ArticuloService } from '../articulo.service';
import { Articulo } from '../articulo';

@Component({
  selector: 'app-articulo-lista',
  templateUrl: './articulo-lista.component.html',
  styleUrls: ['./articulo-lista.component.css']
})
export class ArticuloListaComponent implements OnInit {
  articulos: Articulo[] = [];
  page: number = 1;
  pageSize: number = 5; // Número de artículos por página

  constructor(private articuloService: ArticuloService) { }

  ngOnInit(): void {
    this.articuloService.darArticulos().subscribe(
      data => {
        this.articulos = data;
      },
      error => {
        console.error('Error al obtener artículos', error);
      }
    );
  }
}

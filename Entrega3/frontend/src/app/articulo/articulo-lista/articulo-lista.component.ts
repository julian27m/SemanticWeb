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
  articulosFiltrados: Articulo[] = [];
  searchText: string = '';
  page: number = 1;
  pageSize: number = 5; // Número de artículos por página

  constructor(private articuloService: ArticuloService) { }

  ngOnInit(): void {
    this.articuloService.darArticulos().subscribe(
      data => {
        this.articulos = data;
        this.articulosFiltrados = data; // Inicialmente mostrar todos los artículos
      },
      error => {
        console.error('Error al obtener artículos', error);
      }
    );
  }

  buscarArticulos(): void {
    if (this.searchText) {
      this.articulosFiltrados = this.articulos.filter(articulo =>
        articulo.nombre.toLowerCase().includes(this.searchText.toLowerCase()) ||
        articulo.nombre_autor?.toLowerCase().includes(this.searchText.toLowerCase())
      );
    } else {
      this.articulosFiltrados = this.articulos; // Mostrar todos los artículos si no hay búsqueda
    }
    this.page = 1; // Reiniciar a la primera página de resultados
  }
}

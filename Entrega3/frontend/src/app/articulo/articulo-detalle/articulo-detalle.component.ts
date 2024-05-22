import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router, NavigationEnd } from '@angular/router';
import { ArticuloService } from '../articulo.service';
import { environment } from 'src/environments/environment';
import { Articulo } from '../articulo';
import { filter } from 'rxjs/operators';

@Component({
  selector: 'app-articulo-detalle',
  templateUrl: './articulo-detalle.component.html',
  styleUrls: ['./articulo-detalle.component.css']
})
export class ArticuloDetalleComponent implements OnInit {
  articulo: Articulo | undefined;
  referenciasList: Articulo[] = [];

  private apiUrl = environment.apiUrl;

  constructor(
    private route: ActivatedRoute,
    private articuloService: ArticuloService,
    private router: Router
  ) { }

  ngOnInit(): void {
    // Subscribe to router events to reload the component when the URL changes
    this.router.events
      .pipe(filter(event => event instanceof NavigationEnd))
      .subscribe(() => {
        this.loadArticulo();
      });

    this.loadArticulo();
  }

  loadArticulo(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    const token = sessionStorage.getItem('token');

    if (token) {
      this.articuloService.darArticulo(id).subscribe(
        data => {
          this.articulo = data;
          if (this.articulo.referencias) {
            this.obtenerReferencias(this.articulo.referencias);
          }
        },
        error => {
          console.error('Error al obtener el artículo', error);
        }
      );
    }
  }

  obtenerReferencias(referencias: string): void {
    this.articuloService.darArticulos().subscribe(
      articulos => {
        const referenciasNombres = referencias.split(', ');
        this.referenciasList = articulos.filter(articulo => referenciasNombres.includes(articulo.nombre));
      },
      error => {
        console.error('Error al obtener las referencias', error);
      }
    );
  }

  getRutaPdf(rutaPdf: string): string {
    const rutaRelativa = rutaPdf.replace('DescargasPDFs/', '');
    return `${this.apiUrl}/descargar/${encodeURIComponent(rutaRelativa)}`;
  }

  navegarADetalle(id: number): void {
    this.router.navigate(['/articulo', id]);
  }
}
